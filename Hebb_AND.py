# تمرین 1)
# یک شبکه هب برای تابع 
# AND را با در نظر گرفتن حالت دو قطبی پیاده سازی نمائید

import numpy as np
import matplotlib.pyplot as plt

X = np.array([[-1,-1,1], [-1,1,1], [1,-1,1], [1,1,1]]) # input vectors + bias
T = np.array([-1, -1, -1, 1]) # targets
w = np.array([0, 0, 0]) # weights

for i in range(len(X)):
    x = X[i]
    t = T[i]

    w = w + x * t # update the weights

    plt.figure(figsize=(8,6))
    plt.title(f'iteration {i+1}, weights: {w}')
    colors = ['red' if t == -1 else 'blue' for t in T]
    plt.scatter(X[:,0], X[:,1], c=colors, s=100)


    if w[1] != 0:
        x1 = np.array([-2, 2])
        x2 = (-w[0] * x1 - w[2]) / w[1] # x2 = (-w1 * x1 - w3) / w2
        plt.plot(x1, x2, label="Decision Boundary", color='green')
    
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.grid(True)
    plt.legend()
    plt.show()

print("Final Weights:", w)
