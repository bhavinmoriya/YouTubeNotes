import numpy as np
from scipy import stats

# Sample data: volumes of 10 coffee cups (ml)
sample = np.array([248, 251, 244, 255, 249, 247, 252, 243, 250, 246])

# Hypothesized population mean (the shop's claim)
mu0 = 250

# One-sample t-test
t_stat, p_value = stats.ttest_1samp(sample, popmean=mu0)

alpha = 0.05
n = len(sample)
dof = n - 1
critical_value = stats.t.ppf(1 - alpha / 2, dof)  # two-tailed

print(f"Sample mean:        {sample.mean():.2f} ml")
print(f"t-statistic:       {t_stat:.4f}")
print(f"Critical value:    ±{critical_value:.4f} (two-tailed, α = {alpha})")
print(f"p-value:           {p_value:.4f}")

if p_value < alpha:
    print("Decision: Reject H0 — the true mean differs from 250 ml.")
else:
    print("Decision: Fail to reject H0 — no evidence the mean differs from 250 ml.")
