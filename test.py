def logistic_equation(R, x_0, iterations=1000):
    x_values = []
    x = x_0

    for _ in range(iterations):
        x = R * x * (1 - x)
        x_values.append(x)

    return x_values

def find_transition_R(x_0, threshold=1e-6, max_iterations=1000):
    R = 0.0

    while R <= 4.0:
        x_values = logistic_equation(R, x_0)
        last_value = x_values[-1]
        period = 1

        # Check if the sequence is stable (period 1)
        if abs(last_value - x_values[-2]) < threshold:
            period = 1

        # Check if the sequence has switched to period 2
        elif abs(last_value - x_values[-3]) < threshold:
            period = 2
            return R

        R += 0.001

    return None

# Set the initial condition
x_0 = 0.4

# Find R where the logistic equation switches from period 1 to period 2
R_1 = find_transition_R(x_0)

print("R_1:", R_1)