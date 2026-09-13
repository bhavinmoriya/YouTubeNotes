# Lotka-Volterra Model: The Dance of Predator and Prey
# Imagine a world where foxes and rabbits are locked in an eternal chase.
# The rabbits multiply, the foxes feast, and the cycle of life unfolds.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Mechanism: The rules of the game
# alpha: How fast rabbits multiply when foxes aren't looking
# beta: How often a fox and rabbit meet (and the rabbit's fate is sealed)
# delta: How much a fox benefits from a rabbit feast
# gamma: How fast foxes starve without rabbits
alpha, beta, delta, gamma = 0.1, 0.02, 0.3, 0.1
alpha, beta, delta, gamma = 0.1, 0.01, 0.02, 0.1

# The equations: The cause and effect
# dx/dt = alpha * x - beta * x * y  (Rabbits: born or eaten)
# dy/dt = delta * x * y - gamma * y  (Foxes: feast or famine)
def model(state, t):
    x, y = state  # x = rabbits, y = foxes
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return [dxdt, dydt]

# Initial conditions: A few rabbits, a couple of foxes
x0, y0 = 40, 9
state0 = [x0, y0]

# Time: Let's watch for a year (365 days)
t = np.linspace(0, 365, 1000)

# Solve the equations
states = odeint(model, state0, t)
rabbits, foxes = states.T

# Plot the chase
plt.figure(figsize=(10, 6))
plt.plot(t, rabbits, label='Rabbits (Prey)', color='orange')
plt.plot(t, foxes, label='Foxes (Predator)', color='blue')
# plt.axhline(rabbits[0], color='orange', linestyle='--', label='Initial Rabbit Population')
# plt.axhline(foxes[0], color='blue', linestyle='--', label='Initial Fox Population')
# plt.axhline(rabbits[-1], color='orange', linestyle='--', label='Final Rabbit Population')
# plt.axhline(foxes[-1], color='blue', linestyle='--', label='Final Fox Population')
plt.xlabel('Time (days)')
plt.ylabel('Population')
plt.title('The Eternal Chase: Lotka-Volterra Model')
plt.legend()
plt.grid(True)
plt.savefig('lotka_volterra.png', dpi=200, bbox_inches='tight')
plt.show()
plt.close()

# The satisfying click: The cycle of life in numbers
print("Initial rabbits:", x0)
print("Initial foxes:", y0)
print("After a year:")
print("Rabbits:", int(rabbits[-1]))
print("Foxes:", int(foxes[-1]))

# End with a joke
print("\nWhy did the rabbit break up with the fox?")
print("It was tired of being *prey*-ed on!")

# Hashtags for the curious
# #LotkaVolterra #PredatorPrey #MathInNature #EternalChase #PopulationDynamics
