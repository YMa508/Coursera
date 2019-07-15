import scipy.io
import numpy as np
import scipy.optimize
import time

#using scipy.io.loadmat to read the .mat files into Python
mat = scipy.io.loadmat('ex3weights.mat')
Theta1 = mat["Theta1"]
Theta2 = mat["Theta2"]

mat1 = scipy.io.loadmat('ex3data1.mat')
X = mat1["X"]
y = mat1["y"]

# =============================================================================
# Vectorizing the cost function
# =============================================================================

def costfun(theta, X, Y):
    extra_ones = np.ones((len(X), 1))
    X_p = np.hstack((X, extra_ones)) # X_p: 5000 x 401
    XTheta = X_p @ theta # theta: 401 x 1; XTheta: 5000 x 1
    # hypothesis using XTheta through sigmod (logisitc) function
    h = 1/(1 + np.exp(-XTheta))
    cost = np.sum(- Y * np.log(h) - (1 - Y) * np.log(1 - h))/len(X)
    return cost

# =============================================================================
# Vectorizing the gradient
# =============================================================================

def gradient(theta, X, Y):
    extra_ones = np.ones((len(X), 1))
    X_p = np.hstack((X, extra_ones)) # X_p: 5000 x 401
    XTheta = X_p @ theta # theta: 401 x 1; XTheta: 5000 x 1
    # hypothesis using XTheta through sigmod (logisitc) function
    h = 1/(1 + np.exp(-XTheta)).reshape(-1, 1)
    # should use X_p as the gradient for the constant should also be included
    g = 1/len(X) * X_p.T @ (h - Y) 
    #print(h.shape)
    return g

#temp_theta = Theta1[0, :].T
#cost = costfun(temp_theta)
#grad = gradient(temp_theta)
#print(type(cost))
#print(grad.shape)

# =============================================================================
# Vectorizing regularized logistic regression
# =============================================================================
def costfun_reg(theta, lam, X, Y):
    extra_ones = np.ones((len(X), 1))
    X_p = np.hstack((X, extra_ones)) # X_p: 5000 x 401
    XTheta = X_p @ theta # theta: 401 x 1; XTheta: 5000 x 1
    # hypothesis using XTheta through sigmod (logisitc) function
    h = 1/(1 + np.exp(-XTheta))
    cost = np.sum(- Y * np.log(h) - (1 - Y) * np.log(1 - h))/len(X)
    cost += lam / (2 * len(X)) * (theta[1:] ** 2).sum()
    return cost

def gradient_reg(theta, lam, X, Y):
    extra_ones = np.ones((len(X), 1))
    X_p = np.hstack((X, extra_ones)) # X_p: 5000 x 401
    XTheta = X_p @ theta # theta: 401 x 1; XTheta: 5000 x 1
    # hypothesis using XTheta through sigmod (logisitc) function
    h = 1/(1 + np.exp(-XTheta))#.reshape(-1, 1)
    # should use X_p as the gradient for the constant should also be included
    #print((X_p.T @ (h - y.flatten())).shape)
    g = 1/len(X) * X_p.T @ (h - Y.flatten())
    g[1:] += lam/len(X) * theta[1:]
    # make sure the dimension of gradient is 1-d not N by 1.    
    return g

Y = np.where(y == 1, 1, 0)
#temp_theta = Theta1[0, :].T
#cost1 = costfun_reg(temp_theta, 0.1, X, Y)
#grad1 = gradient_reg(temp_theta, 0.1, X, Y)
#print(type(cost1))
#print(grad1.shape)

start_time = time.time()
res = scipy.optimize.minimize(costfun_reg, np.zeros((401, 1)), (0, X, Y))#, method = "BFGS", jac = gradient_reg)
print("--- %s seconds ---" % (time.time() - start_time))