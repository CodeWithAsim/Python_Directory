from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import math


def predict_using_sklearn(x, y):
    x = x.reshape(len(x), 1)
    reg = LinearRegression()
    reg.fit(x, y)
    return reg.coef_, reg.intercept_


def gradient_descent(x, y):

    m_current = b_current = 0
    n = len(x)
    iterations = 10000
    learning_rate = 0.08

    cost_prev = 0

    for i in range(iterations):

        y_predict = m_current*x + b_current
        m_d = -(2/n)*sum(x*(y-y_predict))
        b_d = -(2/n)*sum(y-y_predict)
        m_current = m_current - learning_rate*m_d
        b_current = b_current - learning_rate*b_d
        cost_function = (1/n)*sum([val**2 for val in (y - y_predict)])

        if math.isclose(cost_function, cost_prev, rel_tol=1e-29):
            break

        cost_prev = cost_function

        print("m : {} b : {} cost : {} iteration : {} ".format(m_current, b_current, cost_function, i))

    return m_current, b_current


if __name__ == "__main__":

    x_arr = np.array([1, 2, 3, 4, 5])
    y_arr = np.array([6, 7, 8, 9, 10])
    m, b = gradient_descent(x_arr, y_arr)
    print("Coefficient : {} Intercept : {} using Gradient Descent ".format(m, b))

    s_m, s_b = predict_using_sklearn(x_arr, y_arr)
    print("Coefficient : {} Intercept : {} using sklearn ".format(s_m,s_b))
