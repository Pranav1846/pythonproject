import math 
a=float(input())
b=float(input())
c=float(input())
if (a+b< c or b+c<a or a+c<b):
    print("Invalid Triangle")
else:

     s=float((a+b+c)/2)
     area=float(math.sqrt(s*(s-a)*(s-b)*(s-c)))
     print("The area of the triangle is: {:.2f}".format(area))
