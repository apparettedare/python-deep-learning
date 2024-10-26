import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
    return np.array(x > 0, dtype=int)

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y1 = step_function(x)
y2 = 1 / (1 + np.exp(-x))

plt.plot(x, y1, label='step func')
plt.plot(x, y2, label='sigmoid', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('step & sigmoid')
plt.legend()
plt.show()
