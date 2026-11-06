# One-Sided (One-Tailed) t-Test

A **one-sided t-test** is used when we want to test whether a population mean is specifically greater than or specifically less than a hypothesized value.

The key difference from a two-sided t-test is the direction of the alternative hypothesis.

Let's understand this with intuition, mathematical formulas, and Python.

## 1\. Intuition: Why one-sided?

Suppose a company claims that its employees work an average of 40 hours per week.

You suspect that employees are actually working **more than 40 hours**\.

You are not interested in whether they work less than 40 hours. Your research question is specifically\:

"Is the population mean working time greater than 40 hours?"

Therefore, we use a right-tailed one-sample t-test.

### The hypotheses

\[
H_0:\mu=40
\]

\[
H_1:\mu>40
\]

Here\:

- \(H_0\)\: The population mean is 40 hours.
- \(H_1\)\: The population mean is greater than 40 hours.

The alternative hypothesis determines which tail of the t-distribution we examine.

## 2\. Right-tailed vs left-tailed t-test

There are two possible one-sided tests.



| Test | Null hypothesis | Alternative hypothesis |
|--------|--------|--------|
| Right-tailed | \(H_0:\mu=40\) | \(H_1:\mu>40\) |
| Left-tailed | \(H_0:\mu=40\) | \(H_1:\mu<40\) |

### Right-tailed test

We are interested in whether the mean is greater than 40.

\[
H_1:\mu>40
\]

The rejection region is in the right tail.

### Left-tailed test

Suppose instead we suspect that employees work less than 40 hours.

\[
H_1:\mu<40
\]

The rejection region is in the left tail.

**Important\:** The direction must be decided before examining the data. We should not choose whichever tail gives a smaller p-value.

---

## 3\. Mathematical formula

The one-sample t-statistic is the same as in a two-sided test\:

\[
\boxed{t=\frac{\bar{x}-\mu_0}{s/\sqrt n}}
\]

The degrees of freedom are\:

\[
df=n-1
\]

The formula does not change. Only the rejection region and p-value calculation change.

### Example: Right-tailed test

Suppose\:

- Hypothesized mean: \(\mu_0=40\)
- Sample size: \(n=10\)
- Sample mean: \(\bar{x}=42\)
- Sample standard deviation: \(s=3\)
- Significance level: \(\alpha=0.05\)

We test\:

\[
H_0:\mu=40
\]

\[
H_1:\mu>40
\]

Calculate\:

\[
t=\frac{42-40}{3/\sqrt{10}}
\]

\[
t\approx2.108
\]

Degrees of freedom\:

\[
df=9
\]

For a right-tailed test at 5% significance\:

\[
t_{\text{critical}}\approx1.833
\]

Since\:

\[
2.108>1.833
\]

we reject \(H_0\)\.

There is statistically significant evidence that the population mean is greater than 40 hours.

## 4\. Python implementation

SciPy's `ttest_1samp()` supports one-sided tests using the `alternative` parameter.

```
import numpy as npfrom scipy import stats# Sample observationsdata = np.array([45, 41, 42, 38, 44,                 43, 40, 46, 39, 42])mu_0 = 40alpha = 0.05# Right-tailed test: H1: mu > 40result = stats.ttest_1samp(    data,    popmean=mu_0,    alternative="greater")print("Sample mean:", data.mean())print("t-statistic:", result.statistic)print("One-sided p-value:", result.pvalue)if result.pvalue < alpha:    print("Reject H0")else:    print("Fail to reject H0")
```



The three possible values of `alternative` are\:

| Parameter | Hypothesis being tested |
|--------|--------|
| `"greater"` | \(H_1:\mu>\mu_0\) |
| `"less"` | \(H_1:\mu<\mu_0\) |
| `"two-sided"` | \(H_1:\mu\neq\mu_0\) |

For the same sample, we can compare all three\:

```

for alternative in ["greater", "less", "two-sided"]:
    result = stats.ttest_1samp(
        data,
        popmean=40,
        alternative=alternative
    )

    print(
        f"{alternative:>10}: "
        f"t = {result.statistic:.4f}, "
        f"p = {result.pvalue:.4f}"
    )

```

iframe



## 5\. The statistical intuition behind the p-value

This is the most important part to understand.

Under the null hypothesis\:

\[
T\sim t_{n-1}
\]

For our example, \(df=9\)\.

We obtained\:

\[
t_{\text{observed}}=2.108
\]

### Right-tailed test

We calculate\:

\[
p=P(T\geq2.108)
\]

This is the probability of obtaining a t-statistic at least as large as the observed one, assuming \(H_0\) is true.

### Left-tailed test

We calculate\:

\[
p=P(T\leq2.108)
\]

Because the observed t-statistic is positive, this probability is very large.

### Two-sided test

We calculate\:

\[
p=P(|T|\geq2.108)
\]

That means we consider extreme values in either direction.

Illustrative p-values

For t = 2.108 with 9 degrees of freedom, comparing one-sided and two-sided alternatives.

Test	P
Right-tailed	0.032
Left-tailed	0.968
Two-sided	0.064

For a positive t-statistic, the two-sided p-value is twice the right-tailed p-value\:

\[
p_{\text{two-sided}}=2p_{\text{right}}
\]

This relationship holds when the test statistic is positive. For a negative t-statistic, the analogous relationship uses the left tail.

## 6\. One-sided vs two-sided: a crucial distinction

Suppose the right-tailed test gives\:

\[
p=0.032
\]

At significance level\:

\[
\alpha=0.05
\]

We reject \(H_0\)\.

But the two-sided test gives approximately\:

\[
p=0.064
\]

We fail to reject \(H_0\)\.

Why?

Because the two-sided test reserves 2.5% of the probability for each tail, while the right-tailed test reserves the entire 5% for the right tail.

This gives a one-sided test more statistical power in its specified direction, but it cannot detect a significant effect in the opposite direction.

**A one-sided test is not simply a trick to obtain a smaller p-value.** It is appropriate only when the scientific or practical question genuinely concerns one direction.

---

## 7\. Your understanding check

A pharmaceutical company wants to show that its new medicine reduces the average recovery time below 10 days.

Which alternative hypothesis should be used?

A. \(H_1:\mu<10\)

B. \(H_1:\mu>10\)

C. \(H_1:\mu\neq10\)

[Check answer]

The next natural topic is the **relationship between one-sided t-tests, two-sided t-tests, and confidence intervals**—particularly why a 95% one-sided confidence bound corresponds to a 90% two-sided confidence interval.
