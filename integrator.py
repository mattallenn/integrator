

n = 0.01#Number of trapezoids to integrate aka base
n1 = 0 
n2 = n 
upper_bound = 2
lower_bount = 0
func = "2x+1"
area = 0

while n2 <= upper_bound:
    area += 0.5((2(n1)+1) + (2(n2)+1))
    n1 += n
    n2 += n

print(area) 

