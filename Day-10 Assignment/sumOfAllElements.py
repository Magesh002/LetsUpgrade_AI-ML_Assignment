import numpy as np

ele = np.array([[2, 4], [3, 8]])
print("Given array:\n", ele)
print("Sum of all ele:\n", np.sum(ele))
print("Sum of row:\n", np.sum(ele, axis=1))
print("Sum of column:\n", np.sum(ele, axis=0))
