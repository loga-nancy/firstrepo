#Calculate volume of sphere

import math
r=int(input("Enter value :"))
def sphere(r):
    return (4//3)*math.pi*math.pow(r,3)
print(sphere(r))
