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
