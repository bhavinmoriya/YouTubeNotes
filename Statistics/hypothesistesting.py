import numpy as np

def simulate_coin_pvalue(k=8, n=10, trials=100_000):
    flips = np.random.binomial(n, 0.5, trials)
    return np.mean(flips >= k)

print(simulate_coin_pvalue())
