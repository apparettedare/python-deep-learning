import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y = relu(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('ReLU')
plt.show()
