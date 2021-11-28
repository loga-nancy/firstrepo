import math

a = input("Please Enter a Number : ")
sqrt = lambda x: round(math.pow(int(x), 2))
orig = sqrt(a)
print("The square of the given number {}".format(sqrt(a)))
rev = sqrt(a[::-1])
print("The Square of the reverse number {}".format(rev))
if str(orig) == str(rev)[::-1]:
    print("reversed")
else:
    print("Non Reversable")
