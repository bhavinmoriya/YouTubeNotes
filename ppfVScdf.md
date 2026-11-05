```ppf``` and ```cdf``` are mathematical inverses of each other:

> **ppf(cdf(x)) = x** and **cdf(ppf(q)) = q**

```python
from scipy import stats

dof = 9
x = 2.0
q = stats.t.cdf(2.0, dof)     # 0.9617 → P(T ≤ 2.0)
stats.t.ppf(q, dof)          # 2.0 — back to where we started
```

## The two directions

| | cdf | ppf |
|---|---|---|
| Question | "How much probability lies below this value?" | "Which value has this much probability below it?" |
| Input → Output | value → probability | probability → value |
| Math name | CDF, F(x) | Inverse CDF, F⁻¹(q), also called the quantile function |

## Same pairing across distributions

This inverse relationship holds for every distribution in scipy:

```python
stats.norm.cdf(1.96)          # 0.975
stats.norm.ppf(0.975)         # 1.96

stats.chi2.cdf(12.59, dof=6)  # ~0.95
stats.chi2.ppf(0.95, dof=6)   # 12.59
```

One subtlety: the cdf is defined everywhere (any real number in, probability out), but the ppf only accepts probabilities in [0, 1]. So it's technically a partial inverse — but over the meaningful range, they perfectly undo each other.

That's why your chi-square app used `ppf` to get the critical *value* from α (probability → threshold), and `sf`/`cdf` to get a p-*value* from a statistic (threshold → probability): two directions of the same bridge.
