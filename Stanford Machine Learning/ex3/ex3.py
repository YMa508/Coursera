import scipy.io
import numpy as np
import scipy.optimize
import time
import pandas as pd

#using scipy.io.loadmat to read the .mat files into Python
mat = scipy.io.loadmat('ex3weights.mat')
Theta1 = mat["Theta1"]
Theta2 = mat["Theta2"]

mat1 = scipy.io.loadmat('ex3data1.mat')
Xs = mat1["X"]
ys = mat1["y"].flatten()#.ravel()
ys[ys == 10] = 0

# test values for the parameters theta
theta_t = np.array([-2, -1, 1, 2], dtype=float)

# test values for the inputs
X_t = np.concatenate([np.ones((5, 1)), np.arange(1, 16).reshape(5, 3, order='F')/10.0], axis=1)

# test values for the labels
y_t = np.array([1, 0, 1, 0, 1])

# test value for the regularization parameter
lambda_t = 3

X_t
# =============================================================================
# Vectorizing the cost function
# =============================================================================
def sigmoid(z):
    """
    Computes the sigmoid of z.
    """
    return 1.0 / (1.0 + np.exp(-z))

def lrCostFunction(theta, X, Y, lam):
    if Y.dtype == bool:
        Y = Y.astype(int)
    m = len(Y)
    #extra_ones = np.ones((m, 1))
    #X_p = np.hstack((extra_ones, X)) # X_p: 5000 x 401
    XTheta = X @ theta # theta: 401 x 1; XTheta: 5000 x 1
    # hypothesis using XTheta through sigmod (logisitc) function
    h = sigmoid(XTheta)#1.0/(1.0 + np.exp(-XTheta))
    # if not flatten the Y vector but keep it as (M, 1) then Y * np.log(X) generate M by M matrix
    cost = np.sum(- Y * np.log(h) - (1 - Y) * np.log(1 - h))/m
    cost += lam / (2 * m) * (theta[1:] ** 2).sum()
    
    g = (X.T @ (h - Y.flatten()))/m
    g[1:] += lam/m * theta[1:]
    return cost, g

J, grad = lrCostFunction(theta_t, X_t, y_t, lambda_t)

print('Cost         : {:.6f}'.format(J))
print('Expected cost: 2.534819')
print('-----------------------')
print('Gradients:')
print(' [{:.6f}, {:.6f}, {:.6f}, {:.6f}]'.format(*grad))
print('Expected gradients:')
print(' [0.146561, -0.548558, 0.724722, 1.398003]')


# =============================================================================
# Vectorizing the gradient
# =============================================================================

#def gradient(theta, X, Y, lam):
#    if Y.dtype == bool:
#        Y = Y.astype(int)
#    m = len(Y)
##    extra_ones = np.ones((m, 1))
##    X_p = np.hstack((extra_ones, X)) # X_p: 5000 x 401
#    XTheta = X @ theta # theta: 401 x 1; XTheta: 5000 x 1
#    # hypothesis using XTheta through sigmod (logisitc) function
#    h = 1/(1 + np.exp(-XTheta))#.reshape(-1, 1)
#    # should use X_p as the gradient for the constant should also be included
#    g = (X.T @ (h - Y.flatten()))/m
#    g[1:] += lam/len(X) * theta[1:]
#    return g

#def predict(theta, X):
#    m = len(X)
#    extra_ones = np.ones((m, 1))
#    X_p = np.hstack((extra_ones, X)) # X_p: 5000 x 401
#    XTheta = X_p @ theta # theta: 401 x 1; XTheta: 5000 x 1
#    # hypothesis using XTheta through sigmod (logisitc) function
#    h = 1/(1 + np.exp(-XTheta))
#    return h >= 0.5
#temp_theta = Theta1[0, :].T
#cost = costfun(temp_theta)
#grad = gradient(temp_theta)
#print(type(cost))
#print(grad.shape)
m = len(ys)

def oneVsAll(X, y, num, lam):
    m, n = X.shape
    thetas = np.zeros((num, n + 1))
    X = np.concatenate([np.ones((m, 1)), X], axis=1)
    #np.hstack((np.ones((m, 1)), X))
    guess = np.zeros(n + 1)#np.random.rand(401) * 2  - 1
    options = {'maxiter':50}
    for c in range(num):
        print('optimization for ', c)
        #Y = np.where(ys == i , 1, 0)
        start_time = time.time()
        #guess = np.zeros(401)
        res = scipy.optimize.minimize(lrCostFunction, guess, (X, (y == c), lam), jac = True, \
                                  method = "CG", options = options)
        thetas[c, :] = res.x
        print("--- %s seconds ---" % (time.time() - start_time))
        #print(res.success)
        print(res.message)
    return thetas

lambda_ = 0.2
all_theta = oneVsAll(Xs, ys, 10, lambda_)
    
def predict_mul(thetas, X):
    m = X.shape[0]
    X = np.concatenate([np.ones((m, 1)), X], axis=1)
    XThetas = X @ thetas.T # theta: 401 x 1; XTheta: 5000 x 1
    # hypothesis using XTheta through sigmod (logisitc) function
    h = sigmoid(XThetas)#1.0/(1.0 + np.exp(-XThetas))
    #pd.DataFrame(h).to_csv("dump.csv")
    p = np.argmax(h, axis = 1)
    return p

pred = predict_mul(all_theta, Xs)
print(np.mean(pred == ys.flatten()))

