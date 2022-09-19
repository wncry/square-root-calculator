import cmath
import math
x = float(input("Input number to find it's square root: " ))

def sqrt(x):
  if x < 0:
    crt = cmath.sqrt(x)
    print(crt)


  if x >= 0:
    rt = math.sqrt(x)
    print(rt)   

sqrt(x)
  
