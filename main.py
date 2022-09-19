import cmath
import math
x = float(input("""What number would you like to square root, 
""" ))   


def sqrt(x):
      
  

  
  if x < 0:
    crt = cmath.sqrt(x)
    print(crt, """

('j' is used instead of 'i')""")
  if x > 0 or x == 0 :
    rt = math.sqrt(x)
    print(rt)
  
  
  

sqrt(x)

  
