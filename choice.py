import time
menuchoice=0
print("*******menu*******")
print(" ")
print("1.Display my name")  
print("2:Display my age")
print("3:Display my address")
print(" ")

while True:
    try:
        while (menuchoice<1) or (menuchoice>3):
            menuchoice=int(input("What is your menu option?"))
        break
    except ValueError:
        print("Please Enter number!")
if menuchoice==1:
    print("Nancyloga")
elif menuchoice==2:
    print("25 years old")
elif menuchoice==3:
    print("Salem TN")

time.sleep(2)