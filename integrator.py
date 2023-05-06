import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Get user input for function to integrate
function_str = input("Enter a function in terms of x. (ex. 2*x+1) \nMake sure to use valid Python syntax. Type help for syntax list.\n")
if function_str == "help":
    print('x squared(or to another power) = x**2\nfor trig functions, use the python math library syntax.\n sin(x) = math.sin(x), cos(x) = math.cos(x), etc.')
else:
    # Convert user input function string to a callable function using eval()
    def user_function(x):
        return eval(function_str)

    # Get user input for integration bounds and number of trapezoids
    a = float(input("Enter lower bound: "))
    b = float(input("Enter upper bound: "))
    n = int(input("Enter number of trapezoids: "))

    # Calculate width of each trapezoid
    h = (b - a) / n

    fig, ax = plt.subplots()

    #create simple line plot
    ax.plot([0, 100],[0, 100])


    # Calculate area using trapezoidal rule
    area = 0.5 * (user_function(a) + user_function(b))
    for i in range(1, n):
        x = a + i * h
        area += user_function(x)
    area *= h

    # Print the result
    print("The numerical integration of the function is: {:.6f}".format(area))


#add rectangle to plot
ax.add_patch(Rectangle((1, 1), 2, 6))

#display plot
plt.show()