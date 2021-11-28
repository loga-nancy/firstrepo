"""C program to do ‘Reverse square Reverse Number’ in input range from 1….. 100.
Ex: RSRN means input number satisfy the following condition
Input = 12
then
122= 144
Rev(12) = 21
212 = 441
Rev(441) = 144
So, if Rev(144) = Sqr(212) then output is ‘12 is Reverse square reverse number’. (21 also RSRN)"""


import math
a=int(input("Enter a number:"))
#sqrt of given number
b=round(math.pow(a,2))
print("The sqrt of given number is: {}".format(b))
#reverse a given number
c=str(a)[::-1]
d=int(c)

#sqrt of reverse number
e=round(math.pow(d,2))

#reverse of value e
f=str(e)[::-1]
g=int(f)
print("The reverse value is:{}".format(g))

if b==g:
    print("The number is RSRN")
else:
    print("Not a RSRN number")
























   
      


 

    

