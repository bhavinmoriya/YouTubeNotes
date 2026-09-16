import numpy as np
import matplotlib.pyplot as plt

# Parameters
mu = 0.1       # Drift coefficient
sigma = 0.2    # Diffusion coefficient
X0 = 1.0       # Initial condition
T = 1.0        # Total time
N = 1000       # Number of time steps
dt = T / N     # Time step size

# Define the drift and diffusion functions
def drift(t, X):
    return mu * X

def diffusion(t, X):
    return sigma * X

# Define the derivative of the diffusion function
def diffusion_derivative(t, X):
    return sigma  # Since sigma * X, the derivative is sigma

# Milstein method
def milstein_method(X0, T, N, drift, diffusion, diffusion_derivative):
    dt = T / N
    X = np.zeros(N + 1)
    X[0] = X0
    t = np.linspace(0, T, N + 1)

    for k in range(N):
        dW = np.random.normal(0, np.sqrt(dt))  # Increment of Brownian motion
        Xk = X[k]
        X[k + 1] = (
            Xk
            + drift(t[k], Xk) * dt
            + diffusion(t[k], Xk) * dW
            + 0.5 * diffusion(t[k], Xk) * diffusion_derivative(t[k], Xk) * (dW**2 - dt)
        )

    return t, X

# Simulate the SDE
t, X = milstein_method(X0, T, N, drift, diffusion, diffusion_derivative)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t, X, label="Milstein Method")
plt.title("Simulation of SDE using Milstein Method")
plt.xlabel("Time (t)")
plt.ylabel("X_t")
plt.legend()
plt.grid(True)
plt.show()import numpy as np
import matplotlib.pyplot as plt

# Parameters
mu = 0.1       # Drift coefficient
sigma = 0.2    # Diffusion coefficient
X0 = 1.0       # Initial condition
T = 1.0        # Total time
N = 1000       # Number of time steps
dt = T / N     # Time step size

# Define the drift and diffusion functions
def drift(t, X):
    return mu * X

def diffusion(t, X):
    return sigma * X

# Define the derivative of the diffusion function
def diffusion_derivative(t, X):
    return sigma  # Since sigma * X, the derivative is sigma

# Milstein method
def milstein_method(X0, T, N, drift, diffusion, diffusion_derivative):
    dt = T / N
    X = np.zeros(N + 1)
    X[0] = X0
    t = np.linspace(0, T, N + 1)

    for k in range(N):
        dW = np.random.normal(0, np.sqrt(dt))  # Increment of Brownian motion
        Xk = X[k]
        X[k + 1] = (
            Xk
            + drift(t[k], Xk) * dt
            + diffusion(t[k], Xk) * dW
            + 0.5 * diffusion(t[k], Xk) * diffusion_derivative(t[k], Xk) * (dW**2 - dt)
        )

    return t, X

# Simulate the SDE
t, X = milstein_method(X0, T, N, drift, diffusion, diffusion_derivative)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t, X, label="Milstein Method")
plt.title("Simulation of SDE using Milstein Method")
plt.xlabel("Time (t)")
plt.ylabel("X_t")
plt.legend()
plt.grid(True)
plt.show()
