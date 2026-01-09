We now enter **LEVEL 1: THE FOUR PILLARS OF HYPOTHESIS TESTING**
This is the *core* — if you master this, everything else is mechanics.

---

# 🧱 PILLAR 1 — NULL HYPOTHESIS (H₀)

## Abstract idea

**H₀ = the boring world**

It represents:

* no effect
* no difference
* randomness only

You **assume H₀ is true** at the start.

Examples (abstract):

* Coin is fair
* Mean equals a specific value
* Two distributions are identical

---

## Concrete examples

### Data Science / A/B testing

> “New website layout increases conversion”

**H₀**:
[
\text{conversion}*{new} = \text{conversion}*{old}
]

---

### Finance

> “This trading strategy has positive alpha”

**H₀**:
[
\mathbb{E}[\text{return}] = 0
]

---

### Medicine

> “Drug lowers blood pressure”

**H₀**:
[
\mu_{\text{drug}} = \mu_{\text{placebo}}
]

---

## Important expert rule

⚠️ **H₀ always has an equality** (=, ≤, ≥)

If you see a null hypothesis without equality, it’s wrong.

---

# 🧱 PILLAR 2 — ALTERNATIVE HYPOTHESIS (H₁)

## Abstract idea

**H₁ = the interesting world**

It is what you’d like to believe *might* be true.

Three forms:

| Type      | Mathematical form | Meaning        |
| --------- | ----------------- | -------------- |
| Two-sided | ≠                 | Any difference |
| One-sided | >                 | Increase       |
| One-sided | <                 | Decrease       |

---

## Concrete examples

### Data Science

* Two-sided: new layout is **different**
* One-sided: new layout is **better**

### Finance

* One-sided: strategy has **positive** mean return

### Medicine

* One-sided: drug **reduces** blood pressure

⚠️ Direction must be chosen **before** seeing data.

---

# 🧱 PILLAR 3 — TEST STATISTIC

## Abstract idea

A **test statistic** compresses data into **one number** that measures how far reality is from H₀.

Generic form:
[
\text{signal} / \text{noise}
]

Examples:

* z-score
* t-statistic
* χ² statistic

---

## Example (mean test)

[
t = \frac{\bar X - \mu_0}{s / \sqrt{n}}
]

Interpretation:

* numerator = deviation from null
* denominator = uncertainty

Large |t| ⇒ data far from H₀

---

## Python intuition experiment

```python
import numpy as np

np.random.seed(0)

# pretend H0 is true
mu0 = 0
sigma = 1
n = 30

sample = np.random.normal(mu0, sigma, n)
t_stat = (sample.mean() - mu0) / (sample.std(ddof=1) / np.sqrt(n))

sample.mean(), t_stat
```

🔍 Insight:

* Even when H₀ is true, test statistics fluctuate
* Hypothesis testing accounts for this randomness

---

# 🧱 PILLAR 4 — p-VALUE (MOST MISUNDERSTOOD)

## Correct definition (memorize this)

> **p-value = Probability of observing data at least this extreme, assuming H₀ is true**

[
p = P(\text{statistic ≥ observed} \mid H₀)
]

❌ NOT “probability H₀ is false”
❌ NOT “probability result is due to chance”

---

## Intuition

* Large p → data is normal under H₀
* Small p → data is surprising under H₀

---

## Example (coin flip)

* H₀: coin is fair
* Observed: 8 heads out of 10
* p ≈ 0.11

Interpretation:

> “If the coin were fair, seeing 8+ heads happens ~11% of the time.”

Not rare enough → don’t reject H₀

---

## Python simulation of p-value

```python
import numpy as np

def simulate_coin_pvalue(k=8, n=10, trials=100_000):
    flips = np.random.binomial(n, 0.5, trials)
    return np.mean(flips >= k)

simulate_coin_pvalue()
```

🧠 Statistical insight:

* p-values are **tail probabilities**
* Simulation builds intuition better than formulas

---

# 🧱 SIGNIFICANCE LEVEL α

## Abstract

α = **maximum risk you're willing to take** of falsely rejecting H₀

Common choices:

* 0.05 (standard)
* 0.01 (strict)
* 0.10 (exploratory)

---

## Decision rule

| Condition | Action            |
| --------- | ----------------- |
| p ≤ α     | Reject H₀         |
| p > α     | Fail to reject H₀ |

⚠️ We never “accept” H₀.

---

## Risk interpretation

* α = 0.05 → 5% false positive rate **in the long run**

This is a **frequentist guarantee**.

---

# 🧠 BIG PICTURE (EXPERT LEVEL SUMMARY)

Hypothesis testing =

1. Assume H₀
2. Measure deviation (statistic)
3. Compute surprise (p-value)
4. Control risk (α)
5. Decide

---

# 🔥 Common expert pitfalls (early warning)

* p ≠ effect size
* statistical significance ≠ practical importance
* multiple tests inflate false positives
* p-hacking destroys validity

We’ll tackle all of these later **formally**.

---

# NEXT LEVEL OPTIONS

Next I can:

1️⃣ Go **deep mathematically** (distributions of test statistics)
2️⃣ Start **core tests** (z, t, χ²)
3️⃣ Jump to **A/B testing with power analysis**
4️⃣ Show **Bayesian alternative**


