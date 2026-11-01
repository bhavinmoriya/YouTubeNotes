from scipy.stats import binom

n = 10      # number of flips
p = 0.5     # probability of heads under H0 (fair coin)
k = 9       # observed heads

# Method 1: P(X >= 9) = P(9) + P(10)
p_value = binom.sf(k - 1, n, p)   # sf = "survival function" = 1 - CDF
print(f"p-value = {p_value:.4f}")  # p-value = 0.0107

# Method 2: calculate it manually, head by head
p9  = binom.pmf(9,  n, p)   # exactly 9 heads
p10 = binom.pmf(10, n, p)   # exactly 10 heads
print(f"p-value = {p9 + p10:.4f}")

# Method 3: from the formula, no scipy needed
from math import comb
p_manual = (comb(n, 9) + comb(n, 10)) / 2**n
print(f"p-value = {p_manual:.4f}")   # 11/1024 = 0.0107
