import matplotlib.pyplot as plt

def linear_regression(X, Y):
    sum_xy = sum([x*y for x,y in zip(X, Y)])
    sum_x = sum(X)
    sum_y = sum(Y)
    sum_x_squared = sum([x*x for x in X])
    n = len(X)
    theta_1 = (n*sum_xy-sum_x*sum_y)/(n*sum_x_squared-sum_x**2)
    theta_2 = (sum_y*sum_y-sum_x*sum_xy)/(n*sum_x_squared-sum_x**2)

    print(theta_1)
    print(theta_2)

X = [1, 2, 3, 4, 5]
Y = [2, 4, 6, 8, 9]

linear_regression(X, Y)
plt.scatter(X, Y)
plt.show()