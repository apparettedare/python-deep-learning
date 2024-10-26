import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y = 1 / (1 + np.exp(-x))

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('sigmoid')
plt.show()
