val = int(input("Enter the nth-term to find sum : "))
if val < 0:
  print("Wrong Input")
else:
  sumvalue = 0
  for i in range(1,val+1):
    sumvalue += i
print("The sum is:", sumvalue)