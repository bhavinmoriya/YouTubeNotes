# Objective: Maximize a^2 * b
# Since OR-Tools doesn't directly support nonlinear objectives, we'll use a workaround:
# We'll iterate over possible values of a and b, compute a^2 * b, and find the maximum.

# This is a workaround since OR-Tools doesn't directly support nonlinear objectives in integer programming
max_value = 0
best_a, best_b = 0, 0

for a_val in range(1, 20):
    b_val = 20 - a_val
    current_value = a_val ** 2 * b_val
    if current_value > max_value:
        max_value = current_value
        best_a, best_b = a_val, b_val

print(f"The maximum value of a^2 * b is {max_value}, achieved when a = {best_a} and b = {best_b}.")
