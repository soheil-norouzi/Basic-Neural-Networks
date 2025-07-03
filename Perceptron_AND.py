# تمرین ۳)
# یک شبکه پرسپترون یک لایه برای تابع AND 
# با ورودی های باینری و هدف دوقطبی را با در نظر گرفتن
# 1 = α و 0.2 = θ پیاده سازی نمائید.

import numpy as np
import matplotlib.pyplot as plt

X = np.array([[-1,-1,1], [-1,1,1], [1,-1,1], [1,1,1]]) # input vectors + bias
T = np.array([-1, -1, -1, 1]) # targets
w = np.array([0.1, -0.1, 0.05]) # weights
theta = 0.2 # learning rate
alpha = 1 # threshold

for i in range(len(X)):
    x = X[i]
    t = T[i]

    net = np.dot(w,x)

    # activation function
    if net>= theta:
        y = 1
    else:
        y = -1

    # update the weights
    if y != t:
        w = w + alpha * (t - y) * x

    plt.figure(figsize=(8,6))# plot the decision boundary
    plt.title(f'iteration {i+1}, weights: {w}')
    colors = ['red' if t == -1 else 'blue' for t in T] # plot data points
    plt.scatter(X[:,0], X[:,1], c=colors, s=100)


    if w[1] != 0:
        x1_vals = np.array([-2, 2])
        x2_vals = (-w[0] * x1_vals - w[2]) / w[1]
        plt.plot(x1_vals, x2_vals, label="Decision Boundary", color='green')
    
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.grid(True)
    plt.legend()
    plt.show()

print("Final Weights:", w)
