import numpy as np
from scipy.stats import chisquare, chi2

observed = [50,10,5,20,10,55,50]
expected = [60,10,8,10,6,26,80]
# expected = [60,10,8,19,8,56,70]

# observed = [30,14,34,45,57,20]
# expected = [20,20,30,40,60,30]

# expected = [30,14,34,45,57,20]
# observed = [20,20,30,40,60,30]

# Input data
obs = np.array(observed)
exp = np.array(expected)

# Perform Chi-Square goodness-of-fit test without checking equal sums
chi2_stat, p_value = chisquare(f_obs=obs, f_exp=exp, sum_check=False)

# Degrees of freedom (k - 1)
dof = len(obs) - 1

# Critical value at 5% significance level
alpha = 0.05
critical_value = chi2.ppf(1 - alpha, dof)

print(f"Chi-Square Statistic: {chi2_stat:.4f}")
print(f"Critical Value (alpha=0.05): {critical_value:.4f}")
print(f"p-value: {p_value:.6e}")

if chi2_stat > critical_value:
    print("Decision: Reject the null hypothesis (critical value < chi-square statistic).")
else:
    print("Decision: Fail to reject the null hypothesis (critical value >= chi-square statistic).")

# Chi-Square Statistic: 59.0545
# Critical Value (alpha=0.05): 12.5916
# p-value: 7.003127e-11
# Decision: Reject the null hypothesis (critical value < chi-square statistic).
￼
