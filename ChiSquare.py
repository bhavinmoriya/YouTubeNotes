from scipy.stats import chi2, chi2_contingency

observed = [[30, 10],
            [20, 40]]

chi2_stat, p_value, dof, expected = chi2_contingency(observed)

print(f"χ² statistic : {chi2_stat:.2f}")   # 16.67
print(f"p-value      : {p_value:.6f}")      # 4.5e-05
print(f"df           : {dof}")              # 1
print(f"expected    : {expected}")
# [[20. 20.]
#  [30. 30.]]

critical = chi2.ppf(0.95, dof)
print(f"critical value: {critical:.2f}")   # 3.84

if chi2_stat > critical:
    print("Reject H0 → variables are related")
