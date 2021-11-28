n1=int(input("Enter a value:"))
l=str(n1)

for i in list(l):
    d=1
    m=1
    while d!=len(l):
        
        print("No of #{}s is {}".format(m,i))
        m=m*10
        d=d+1
***************        
        
import itertools 
  
num = [1, 10, 100, 1000]
n=int(input("Enter a value:"))
n1=str(n)
  
# iterates over 3 lists and executes 
# 2 times as len(value)= 2 which is the
# minimum among all the three 
for (a, b) in zip(num, list(n1)):
     print ("No of {}s is :{}".format(a, b))    
       

         
