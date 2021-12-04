

import math
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))

if ((a + b) > c and (b + c) > a and (c + a) > b ):
    S = (a + b + c) / 2
    Area = math.sqrt(S * (S - a) * (S - b) * (S - c))
    
    print("Area of the Triangle is : " , Area)

else:
    print("The Triangle is not possible ")
