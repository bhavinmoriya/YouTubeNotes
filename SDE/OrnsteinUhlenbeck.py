import numpy as np
import matplotlib.pyplot as plt
from typing import Callable

# Type aliases
DriftFn = Callable[[float, np.ndarray], np.ndarray]
DiffusionFn = Callable[[float, np.ndarray], np.ndarray]

# Euler-Maruyama solver
def euler_maruyama(
    drift: DriftFn,
    diffusion: DiffusionFn,
    x0: np.ndarray,
    t0: float,
    t_max: float,
    n_steps: int,
    rng: np.random.Generator = np.random.default_rng(),
) -> tuple[np.ndarray, np.ndarray]:
    dt = (t_max - t0) / n_steps
    time_points = np.linspace(t0, t_max, n_steps + 1)
    trajectories = np.zeros((n_steps + 1, *x0.shape))
    trajectories[0] = x0

    for i in range(n_steps):
        t = time_points[i]
        x = trajectories[i]
        mu = drift(t, x)
        sigma = diffusion(t, x)
        dW = rng.normal(0, np.sqrt(dt), size=x.shape)
        trajectories[i + 1] = x + mu * dt + sigma * dW

    return time_points, trajectories

# Ornstein-Uhlenbeck drift and diffusion
def ou_drift(t: float, x: np.ndarray, theta: float = 1.0, mu: float = 0.0) -> np.ndarray:
    return theta * (mu - x)

def ou_diffusion(t: float, x: np.ndarray, sigma: float = 0.1) -> np.ndarray:
    return sigma * np.ones_like(x)

# Parameters
x0 = np.array([1.0])  # Initial state
t0, t_max = 0.0, 10.0
n_steps = 1000
theta, mu, sigma = 1.0, 0.0, 0.1
n_simulations = 5  # Number of trajectories to simulate

# Simulate multiple trajectories
rng = np.random.default_rng(seed=42)
plt.figure(figsize=(10, 6))

for _ in range(n_simulations):
    time, trajectories = euler_maruyama(
        drift=lambda t, x: ou_drift(t, x, theta, mu),
        diffusion=lambda t, x: ou_diffusion(t, x, sigma),
        x0=x0,
        t0=t0,
        t_max=t_max,
        n_steps=n_steps,
        rng=rng,
    )
    plt.plot(time, trajectories, label=f"Trajectory {_ + 1}", alpha=0.7)

# Add mean-reverting line (theoretical mean)
plt.axhline(y=mu, color="red", linestyle="--", label="Long-term mean (μ)")

# Customize plot
plt.title("Ornstein-Uhlenbeck Process (Euler-Maruyama Simulation)")
plt.xlabel("Time (t)")
plt.ylabel("X(t)")
plt.legend()
plt.grid(True)
plt.savefig("OrnsteinUhlenbeck.png")
plt.show()
