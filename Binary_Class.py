import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2)

N_point = 10
means = [[2,2],[4,2]]
cov =[[0.3,0.2],[0.2,0.3]]
X1 = np.random.multivariate_normal(means[0],cov,N_point).T
X2 = np.random.multivariate_normal(means[1],cov,N_point).T
X = np.concatenate((X1,X2),axis=1)
#Extend the vector X
X_bar = np.concatenate((np.ones((1,2*N_point)),X), axis=0)
y = np.concatenate((np.ones((1,N_point)),-1*np.ones((1,N_point))), axis=1)



def action_func(x,w):
    return np.sign(np.dot(w.T,x))

def terminate_prog(x,y,w):
    return np.array_equal(action_func(x,w),y)

def perceptron(x,y,w_init):
    w = [w_init]
    N = X.shape[1]

    while True:
        mix_id = np.random.permutation(N)

        for i in range(N):
            x_i = x[:, mix_id[i]].reshape(3, 1)
            y_i = y[0, mix_id[i]]
            print(y_i)
            if action_func(x_i,w[-1]) != y_i:

                w_new = w[-1] + y_i*x_i
                w.append(w_new)
        if terminate_prog(x,y,w[-1]):
            break
    return w

def draw_line(w):
    w0, w1, w2 = w[0], w[1], w[2]
    if w2 != 0:
        x11, x12 = 0, 6
        return plt.plot([x11, x12], [-(w1 * x11 + w0) / w2, -(w1 * x12 + w0) / w2], 'k')
    else:
        x10 = -w0 / w1
        return plt.plot([x10, x10], [0, 6], 'k')
fig, ax = plt.subplots(figsize=(5,5))
plt.plot(X1[0, :], X1[1, :], 'b^', markersize=8, alpha=.8)
plt.plot(X2[0, :], X2[1, :], 'ro', markersize=8, alpha=.8)
plt.axis([0, 6, -2, 4])

d = X_bar.shape[0]
w_init = np.random.randn(d, 1)       #R^3x1
w_final = perceptron(X_bar,y,w_init)
draw_line(w_final[-1])
iterative = len(w_final)
print(w_final[-1])
ax.set_xlabel('Iterative: %d' %iterative)
plt.show()

