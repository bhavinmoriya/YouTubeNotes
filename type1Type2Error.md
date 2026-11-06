Let's make it precise using the standard terminology.

## Type I and Type II Errors

| Reality | Reject \(H_0\) | Fail to reject \(H_0\) |
|---|---|---|
| \(H_0\) is true | **Type I error (\(\alpha\))** | Correct decision |
| \(H_0\) is false | Correct decision (Power) | **Type II error (\(\beta\))** |

### Type I Error — False Positive

You reject the null hypothesis even though it is true.

\[
\boxed{P(\text{Type I error})=\alpha}
\]

Example: A medicine actually has no effect, but your test concludes that it works.

### Type II Error — False Negative

You fail to reject the null hypothesis even though it is false.

\[
\boxed{P(\text{Type II error})=\beta}
\]

Example: A medicine actually reduces recovery time, but your test fails to detect the effect.

### Statistical Power

The probability of correctly rejecting a false null hypothesis is called power.

\[
\boxed{\text{Power}=1-\beta}
\]

It measures the ability of a statistical test to detect a genuine effect.

---

## A subtle but important point

We say **"fail to reject \(H_0\)"**, not "accept \(H_0\)."

Why?

Because a nonsignificant result does not prove that the null hypothesis is true.

Perhaps the effect is genuinely absent. Or perhaps the sample size is too small to detect the effect.

For example:

A medicine reduces recovery time by 1 day, but your sample contains only 5 patients.

Your test might fail to reject \(H_0\), even though the medicine genuinely works.

This could be a Type II error.

### Remember this simple analogy

Imagine a criminal trial:

- \(H_0\): The defendant is innocent.
- \(H_1\): The defendant is guilty.

| Statistical error | Criminal trial analogy |
|---|---|
| Type I error | Innocent person convicted |
| Type II error | Guilty person acquitted |

One final statistical insight:

**There is often a trade-off between Type I and Type II errors.**

For a fixed sample size, reducing \(\alpha\) often increases \(\beta\), unless we change other factors such as sample size or the test design.
