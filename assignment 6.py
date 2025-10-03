import numpy as np




A = np.array([10, 20, 30, 40, 50])
B = np.array([5, 4, 3, 2, 1])



print("A + B =", A + B)
print("A - B =", A - B)
print("A * B =", A * B)
print("A / B =", A / B)

print("Mean of A =", np.mean(A))
print("Max of A =", np.max(A))
print("Min of A =", np.min(A))

print("Dot product of A and B =", np.dot(A, B))


print("Reshape A into 5x1 matrix:\n", A.reshape(5, 1))