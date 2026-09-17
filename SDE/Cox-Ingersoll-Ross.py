import numpy as np
import matplotlib.pyplot as plt

# Parameters for the CIR process
kappa = 2.0    # Speed of mean reversion
theta = 1.0    # Long-term mean
xi = 0.3       # Volatility
X0 = 0.1       # Initial interest rate (start far from theta)
T = 20.0       # Long time horizon
N = 100000     # Number of time steps
dt = T / N     # Time step size

# Define the drift and diffusion functions for the CIR process
def drift(t, X):
    return kappa * (theta - X)

def diffusion(t, X):
    return xi * np.sqrt(X)

# Define the derivative of the diffusion function
def diffusion_derivative(t, X):
    return xi / (2 * np.sqrt(X))

# Milstein method for the CIR process
def milstein_method_cir(X0, T, N, drift, diffusion, diffusion_derivative):
    dt = T / N
    X = np.zeros(N + 1)
    X[0] = X0
    t = np.linspace(0, T, N + 1)

    for k in range(N):
        dW = np.random.normal(0, np.sqrt(dt))  # Increment of Brownian motion
        Xk = X[k]
        if Xk <= 0:  # Ensure Xk is positive to avoid numerical issues
            Xk = abs(Xk)

        # Milstein update
        X[k + 1] = (
            Xk
            + drift(t[k], Xk) * dt
            + diffusion(t[k], Xk) * dW
            + 0.5 * diffusion(t[k], Xk) * diffusion_derivative(t[k], Xk) * (dW**2 - dt)
        )

        # Ensure the next value is non-negative
        X[k + 1] = max(X[k + 1], 0)

    return t, X

# Simulate the CIR process
t, X = milstein_method_cir(X0, T, N, drift, diffusion, diffusion_derivative)

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(t, X, label=f"CIR Process (X_t)", color="blue")
plt.axhline(y=theta, color="red", linestyle="--", label=f"Long-Term Mean ($\\theta = {theta}$)")
plt.title(f"CIR Process: Convergence to Long-Term Mean ($\\theta = {theta}$)")
plt.xlabel("Time (t)")
plt.ylabel("X_t")
plt.legend()
plt.grid(True)
plt.savefig("Cox-Ingersoll-Ross.png")
plt.show()
