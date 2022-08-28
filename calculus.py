import math
import matplotlib.pyplot as plt
import numpy as np

def calculusator():
    print("*****WELCOME TO THE CALCULUS CALCULATOR******")
    def f(x):
        return (x**2)

    bgn1 = int(input("Enter the lower bound of the graph: "))
    end1 = int(input("Enter the upper bound of the graph: "))
    f2 = np.vectorize(f)
    arr1 = np.arange(bgn1,end1, 0.001)

    plt.plot(arr1,f2(arr1))
    plt.xlabel('X-AXIS')
    plt.ylabel('Y-AXIS')


    entrance = int(input("Please enter 1 to integrate, 2 to differentiate: "))
    value = 0

    if (entrance == 1):
        bgn = int(input("Enter the lower bound of the integral: "))
        end = int(input("Enter the upper bound of the integral: "))
        Sum = 0
        stepSize = 0.000001
        currentX = bgn
        Ran = int((end-bgn)/stepSize)
        for t in range(Ran):
            Sum += stepSize * (f(currentX))
            currentX += t*stepSize
        xIntegrated = np.arange(bgn, end, 0.001)
        yIntegrated = f2(xIntegrated)
        plt.fill_between(xIntegrated, yIntegrated)

        print("THE INTEGRAL FOR F(X) FROM "+ str(bgn)+ " TO "+ str(end)+ " IS "+str(Sum))

    elif (entrance == 2):
        xVal = int(input("Enter the x_value for the derivative: "))
        epsilon = 0.00001
        derivative = (f(xVal+epsilon) - f(xVal-epsilon))/(2*epsilon)
        print("THE DERIVATIVE OF F(X) AT X = "+ str(xVal)+ " IS EQUAL TO "+  str(derivative))
        xDerivated = np.arange(bgn1, end1, 0.001)
        def tangent(xVal,derivative, xDerivated, yVal = f(xVal)):
            y = derivative*(xDerivated-xVal)+yVal
            return y
        y = tangent(xVal, derivative, xDerivated)
        plt.plot(xDerivated, y, color = "red")
        plt.plot(xVal, f(xVal), marker = "o", markeredgecolor="yellow")


    else:
        print("INVALID NUMBER")
        calculusator()

    plt.show()
calculusator()
