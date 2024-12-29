import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3]
y = [4, 5, 6]

plt.plot(x, y, marker='o', linestyle='-', color='b', label='Line 1')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.legend()
plt.grid(True)
plt.show()
arr = np.array([1, 2, 3])
print(arr.sum())
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
