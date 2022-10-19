import math
import matplotlib.pyplot as plt
import numpy as np
import math 

def calculusator():
    print("*****WELCOME TO THE CALCULUS CALCULATOR******")

    #This is the mathemetical function
    def f(x):
        return ( (32)**(1/2) / math.sqrt((1-x**4))  )

    #Creates t
    bgn1 = float(input("Enter the lower bound of the graph: "))
    end1 = float(input("Enter the upper bound of the graph: "))
    f2 = np.vectorize(f)
    arr1 = np.arange(bgn1,end1, 0.001)

    #Creates the x and y points in the graph range
    plt.plot(arr1,f2(arr1))
    plt.xlabel('X-AXIS')
    plt.ylabel('Y-AXIS')


    entrance = int(input("Please enter 1 to integrate, 2 to differentiate: "))
    value = 0

    if (entrance == 1):
        #INTEGRATING

        #Beginning
        bgn = float(input("Enter the lower bound of the integral: "))

        #Ending
        end = float(input("Enter the upper bound of the integral: "))
        Sum = 0
        stepSize = 0.000000001
        currentX = bgn
        Ran = int((end-bgn)/stepSize)
        #Loops over for riemann summation
        for t in range(Ran):
                Sum += stepSize * (f(currentX))
                currentX = bgn+ t*stepSize
        xIntegrated = np.arange(bgn, end, 0.0000001)
        txt = "THE INTEGRAL FOR F(X) FROM "+ str(bgn)+ " TO "+ str(end)+ " IS "+str(round(Sum,3))
        #Returns the sum
        plt.title(txt)
        yIntegrated = f2(xIntegrated)
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')

        plt.fill_between(xIntegrated, yIntegrated)

        print("THE INTEGRAL FOR F(X) FROM "+ str(bgn)+ " TO "+ str(end)+ " IS "+str(Sum))

    elif (entrance == 2):
        #Takes the derivative

        xVal = float(input("Enter the x_value for the derivative: "))
        epsilon = 0.00001
        derivative = (f(xVal+epsilon) - f(xVal-epsilon))/(2*epsilon)
        #Derivative Estimation
        print("THE DERIVATIVE OF F(X) AT X = "+ str(xVal)+ " IS EQUAL TO "+  str(derivative))
        xDerivated = np.arange(bgn1, end1, 0.001)

        #Calculates the tangent line
        def tangent(xVal,derivative, xDerivated, yVal = f(xVal)):
            y = derivative*(xDerivated-xVal)+yVal
            return y

        y = tangent(xVal, derivative, xDerivated)
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')

        #Plots the derivative and the tangent liine
        plt.plot(xDerivated, y, color = "red")
        plt.plot(xVal, f(xVal), marker = "o", markeredgecolor="yellow")


    else:
        print("INVALID NUMBER")
        calculusator()

    plt.show()
calculusator()
