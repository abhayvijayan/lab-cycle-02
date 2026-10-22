import numpy as np

# Equations:
# x + y = 2200
# 1.5x + 4y = 5050

A = np.array([[1, 1],
              [1.5, 4]])

B = np.array([2200, 5050])

# Solve the linear equations
solution = np.linalg.solve(A, B)

children = int(solution[0])
adults = int(solution[1])

print("Number of children:", children)
print("Number of adults:", adults)