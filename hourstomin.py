#convert hours to minutes
#ValueError: will throw error when issue with datatypes
#TypeError:can only concatenate str (not "int") to str
#ZeroDivisionError: division by zero
#NameError: name is not defined


import time

h=0
m=0
print(" ")
print("*******Give inputs*******")
print(" ")

while True:
    try:
        h=int(input("enter hours?"))
        m=int(input("Enterminutes? "))
        while (h<=0) or (m<=0):
            raise Exception("Both hours and minutes should not be zero or less!")
        break
    except ValueError:
        print("Please type number!")

if h>0 and m>0:
    print("*****Result****")
    print(h*60+30)

time.sleep(2)
        


    





    
    
        
        
        

        
        
        
    
       
