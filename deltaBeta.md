These two ideas are closely connected, and understanding them makes sample-size planning much easier.

# 1. Statistical power: “Will my study notice a real effect?”

Imagine you are testing whether a new teaching method improves students' exam scores.

- Old method: average score is 70.
- New method: perhaps the average score is really 75.
- You collect a sample and perform a hypothesis test.

**Statistical power is the probability that your test detects a real effect of a specified size.**

For example, power \(=0.80\) means:

> If the new method really improves the population mean by 5 points, then in repeated studies using this design, about 80% would reject the null hypothesis.

The other 20% might fail to detect that real effect.

That failure is called a **Type II error**.

\[
\boxed{\text{Power}=1-\beta}
\]

where \(\beta\) is the probability of a Type II error.

-4-3-2-112340.10.20.30.4\\(z\\)\\(f(z)\\)z = 1.96

Two-sided: both shaded tails combine to p ≈ 0.0500

\\(z\\)

Sides

12

Give feedback

The graphic above is about p-values, not power directly—but it helps distinguish the two: a p-value describes the evidence from the data you observed; power describes how likely a testing procedure is to detect a particular effect *before* you collect the data.

## An intuitive example

Suppose a smoke detector is designed to detect smoke.

- If there is a real fire and it alarms, that's a successful detection.
- If there is a real fire and it doesn't alarm, that's a miss.
- The detector's power is the probability it alarms when a fire is present.

A statistical test is similar: it is designed to detect a real effect.

**Higher power means a lower chance of missing a real effect of the size you planned to detect.**

# 2. Minimum meaningful difference \(\delta\): “How much of an effect would actually matter?”

Suppose you are studying whether a new teaching method improves exam scores.

The old method gives an average score of 70.

The new method might raise the average by:
- 0.2 points
- 1 point
- 5 points
- 10 points

A difference can be statistically detectable but still be too small to matter in practice.

The **minimum meaningful difference** \(\delta\) is the smallest effect that you consider important enough to detect.

For example, you might decide:

\[
\boxed{\delta=5\text{ points}}
\]

This means:

> If the new method improves the population average by at least 5 points, I want my study to have a good chance of detecting it.

It does **not** mean that you believe the effect is exactly 5. It is the threshold you choose for a worthwhile effect.

## Three examples

### Example A: Teaching method

Old method average: 70.

You decide that an improvement of at least 5 points would justify changing the teaching method.

\[
\delta=5.
\]

An improvement of 1 point might be real, but you may not consider it worthwhile.

### Example B: A medication

Suppose a medication lowers a measurement by some amount.

You and the clinical experts decide that a reduction of at least 3 units would be meaningful.

\[
\delta=3.
\]

The value should come from clinical or practical reasoning—not simply from whatever number makes the sample-size calculation convenient.

### Example C: A business change

A new website design might improve the conversion rate.

If the current conversion rate is 10%, perhaps you decide that an increase to 12% is worth implementing.

The meaningful difference is:

\[
\delta=12\%-10\%=2\text{ percentage points}.
\]

Be careful: 2 percentage points is a 20% relative increase from 10%, not a 2% relative increase.

---

# 3. How power and \(\delta\) work together

Imagine you are trying to detect a signal in noise.

- \(\delta\) tells you how big the signal is that you care about.
- \(\sigma\) tells you how noisy the observations are.
- \(n\) tells you how much data you collect.
- Power tells you how likely your test is to detect that signal.

The standardized effect size for a one-sample mean test is:

\[
\boxed{d=\frac{\delta}{\sigma}}
\]

For example, if \(\delta=5\) and \(\sigma=10\):

\[
d=\frac{5}{10}=0.5.
\]

A smaller \(\delta\) relative to \(\sigma\) means the effect is harder to distinguish from random variation. You need a larger sample.

**The practical consequence:**

| Situation | Required sample size |
|---|---|
| Large meaningful effect | Smaller |
| Small meaningful effect | Larger |
| Low population variability | Smaller |
| High population variability | Larger |
| Desired power 80% | Smaller than at 90% |
| Desired power 90% | Larger than at 80% |

For a fixed design, increasing sample size generally increases power.

# 4. Python: see how \(\delta\) changes sample size

Let's use a one-sample, two-sided t-test with:
- Significance level \(\alpha=0.05\)
- Desired power \(=0.80\)
- Estimated standard deviation \(\sigma=10\)

We'll vary the minimum meaningful difference.

```python
import numpy as np
from statsmodels.stats.power import TTestPower

planner = TTestPower()

sigma = 10
alpha = 0.05
desired_power = 0.80

for delta in [2, 3, 5, 8]:
    effect_size = delta / sigma

    n = planner.solve_power(
        effect_size=effect_size,
        alpha=alpha,
        power=desired_power,
        alternative="two-sided",
    )

    print(
        f"delta={delta:>2} | "
        f"effect size={effect_size:.2f} | "
        f"required n={np.ceil(n):.0f}"
    )
```

Install and run it with `uv`:

```bash
uv add statsmodels numpy
uv run python main.py
```

You should see the required sample size increase as \(\delta\) becomes smaller.

Why? Because detecting a 2-point effect is harder than detecting an 8-point effect when the data have the same amount of variability.

---

## 5. The most important distinction

There are two different questions:

**Minimum meaningful difference \(\delta\):**

> What is the smallest effect that would matter in the real world?

**Statistical power:**

> If that effect really exists, how likely is my study to detect it?

For example, you might choose:
- \(\delta=5\) points because 5 points matters practically.
- Power \(=80\%\) because you want an 80% chance of detecting that 5-point effect.
- \(\alpha=5\%\) to control the false-positive rate.
- An estimate of \(\sigma\) from previous data or a pilot study.

Then the sample-size calculation tells you how many observations to plan for.

One key caution: **don't choose \(\delta\) merely to obtain a convenient sample size.** Choose it based on what would matter scientifically, clinically, or economically. Otherwise, the calculation may be mathematically correct but answer the wrong question.
