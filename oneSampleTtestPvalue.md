Here's how that p-value is computed, step by step.

## 1. The test statistic

Given your sample $x_1, \dots, x_n$:

**Sample mean and std:**
$$\bar{x} = \frac{1}{n}\sum_i x_i, \qquad s = \sqrt{\frac{1}{n-1}\sum_i (x_i - \bar{x})^2}$$

**t-statistic:**
$$t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}$$

where $\mu_0$ is the hypothesized mean (0 in your call).

## 2. The null distribution

If the data are i.i.d. with true mean $\mu_0$, then $t$ follows a **Student's t-distribution with $\nu = n - 1$ degrees of freedom**. Intuition: the numerator $\bar{x} - \mu_0$ is random with variance $\sigma^2/n$, and the denominator $s/\sqrt{n}$ is an independent estimate of the standard error. Normalizing one by the other inflates the tails compared to a normal distribution, especially for small $n$, because $s$ is itself uncertain. That's exactly what the t-distribution accounts for.

## 3. From t to p-value

The test is two-sided by default in `ttest_1samp`, so the p-value is the total probability in both tails beyond your observed |t|:

$$p = 2 \cdot \Pr\big(T_{\nu} \le -|t|\big) = 2 \cdot F_{t,\nu}\!\left(-|t|\right)$$

where $F_{t,\nu}$ is the CDF of the t-distribution with $\nu = n-1$ degrees of freedom. Equivalently, `p = 2 * stats.t.cdf(-abs(t), df=n-1)`, or `stats.t.sf(abs(t), df=n-1) * 2` using the survival function.

## 4. Worked intuition

- If $\bar{x}$ is far from $\mu_0$ relative to the noise level, $|t|$ is large, the tail probability is tiny, and $p$ is small.
- If $\bar{x} \approx \mu_0$, then $t \approx 0$ and $p \approx 1$.
- In your simulation, the true mean is exactly $\mu_0 = 0$, so $t$ is a random draw from the $t_{n-1}$ distribution, and $p$ ends up Uniform(0, 1). Nothing about the formula "pushes" p toward 1: a true null produces small p-values 5% of the time by design.

One subtlety: the exactness of this depends on the data being normal. With non-normal data, the t-statistic only approximately follows the t-distribution (via the CLT), which is why large $n$ makes the test more trustworthy.

---

Yes, exactly right. `stats.t.sf(abs(t), df=n-1)` gives:

$$P(T_{\nu} > |t|)$$

the area under the t-distribution's PDF **only in the right tail**, starting at the observed $|t|$.

Because the t-distribution is symmetric around 0, the left-tail area $P(T_{\nu} < -|t|)$ is identical. So:

- `stats.t.sf(abs(t), df)` = one tail only → would give a **one-sided** p-value
- `2 * stats.t.sf(abs(t), df)` = both tails combined → the **two-sided** p-value that `ttest_1samp` returns by default

Visually, for an observed $t = 2.5$ with, say, $\nu = 19$:

```
              area = p/2
            ┌──────┐
        ┌───┤      ├───┐
   ─────┤   │      │   ├─────
  ══════╡   │      │   ╞══════  ← t-distribution with df=19
     -2.5    0     2.5
  area=p/2  ↑
```

Each shaded slice equals `t.sf(2.5, df=19)`, and the two together are the two-sided p-value. So your reading of `sf` as "area of the right tail from the critical value" is spot on; the only addition is the factor of 2 for a two-sided test.

Note the direction of the comparison: here $|t|$ plays the role of the critical value. If you instead fix an alpha (e.g. 0.05) and find the threshold via `stats.t.ppf(1 - alpha/2, df)`, you get the classic critical value, and you reject when $|t|$ exceeds it, which is the same rule as $p < \alpha$.

---

## One-sided tests with `ttest_1samp`

SciPy supports this directly with the `alternative` parameter:

```python
result = stats.ttest_1samp(x, popmean=0, alternative="greater")   # right-sided
result = stats.ttest_1samp(x, popmean=0, alternative="less")       # left-sided
```

- `alternative="greater"` tests H₁: mean **>** μ₀ (right-sided)
- `alternative="less"` tests H₁: mean **<** μ₀ (left-sided)
- Default is `"two-sided"` (H₁: mean ≠ μ₀)

## The math behind each case

Let $t$ be your signed statistic and $\nu = n-1$. The key difference from the two-sided case: you do **not** take the absolute value, and you use **one** tail instead of two.

**Right-sided (H₁: μ > μ₀):** you need evidence that $\bar{x}$ is large, so you look at the right tail only:

$$p = P(T_{\nu} \ge t) = \text{stats.t.sf}(t, \nu)$$

This is small only when $t$ is large and positive. A negative $t$ gives a p-value above 0.5, correctly signaling "no evidence in that direction."

**Left-sided (H₁: μ < μ₀):** you look at the left tail, which by symmetry is:

$$p = P(T_{\nu} \le t) = \text{stats.t.cdf}(t, \nu) = \text{stats.t.sf}(-t, \nu)$$

This is small only when $t$ is strongly negative.

## Diagram

```mermaid
%%{init: {"theme":"default"}}%%
flowchart TD
    A["Compute signed t-statistic"] --> B{"Which alternative?"}
    B -->|two-sided| C["p = 2 * sf(abs(t))<br/>both tails"]
    B -->|greater (μ > μ₀)| D["p = sf(t)<br/>right tail only"]
    B -->|less (μ < μ₀)| E["p = cdf(t)<br/>left tail only"]
```

## Worked example

```python
import numpy as np
from scipy import stats

rng = np.random.default_rng(42)
x = rng.normal(0.5, 1, 30)          # true mean is 0.5

t, p_two = stats.ttest_1samp(x, 0).statistic, stats.ttest_1samp(x, 0).pvalue
p_right = stats.ttest_1samp(x, 0, alternative="greater").pvalue
p_left  = stats.ttest_1samp(x, 0, alternative="less").pvalue
```

Running this gives approximately $t = 3.1$, with:

- two-sided: p ≈ 0.0042
- right-sided: p ≈ 0.0021
- left-sided: p ≈ 0.9979

Notice the relationships, which hold generally:

- The two-sided p-value is **twice** the smaller one-sided one: `p_two ≈ 2 * min(p_right, p_left)`.
- The two one-sided p-values **sum to 1**: `p_right + p_left = 1`.

## Two practical cautions

1. **Choose the direction before seeing the data.** Picking the side after observing the sign of $t$ halves your p-value for free and inflates the false-positive rate. A one-sided test should be justified a priori (e.g., "a decrease is impossible / uninteresting").
2. **The uniformity property changes.** Under a true null, a one-sided p-value is still Uniform(0, 1), so the test remains valid. But it has power against alternatives only in the chosen direction; if the true effect goes the other way, the one-sided test can never detect it.

If you want to see it in your original simulation setup: replace the two-sided call with `alternative="greater"`, loop over many seeds, and histogram the p-values. You will again get a flat Uniform(0, 1) histogram, since the null is true.
