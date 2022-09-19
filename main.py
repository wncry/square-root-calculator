import cmath
import math
print("Note: For complex numbers the letter 'j' is used instead of 'i'")
x = float(input("""What number would you like to square root, 
""" ))   


def sqrt(x):
      
  

  
  if x < 0:
    crt = cmath.sqrt(x)
    print(crt)
  if x > 0 or x == 0 :
    rt = math.sqrt(x)
    print(rt)
  
  
  

sqrt(x)

  
