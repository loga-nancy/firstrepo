def is_leap(year):
    if year%4==0 and year%400:
        return True
    else:
        return False
    
year = int(input())
print(is_leap(year))