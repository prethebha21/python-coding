a = int(input("ENTER ANY YEAR: "))
if(a%400 == 0 & a%100 == 0):
    print("IT IS A LEAP YEAR")
elif(a%4 == 0 & a%100 != 0):
    print("IT IS A LEAP YEAR")
else:
    print("IT IS NOT A LEAP YEAR")
