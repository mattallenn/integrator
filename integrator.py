import math

n = 0.01#Number of trapezoids to integrate aka base
n1 = 0 
n2 = n 
upper_bound = 2
lower_bount = 0
area = 0

''' while n2 <= upper_bound:
    area += 0.5((2(n1)+1) + (2(n2)+1))
    n1 += n
    n2 += n

print(area) 
'''

try:
    function_str = input("Enter a function in terms of x. (ex. 2*x+1) \nMake sure to use valid Python syntax. Type help for syntax list.\n")
    if function_str == "help":
        print('x squared(or to another power) = x**2\nfor trig functions, use the python math library syntax.\n sin(x) = math.sin(x), cos(x) = math.cos(x), etc.')
except:
    print("Invalid syntax or equation.")
def function(x):
    return eval(function_str)

x = 2
print(function(x))
