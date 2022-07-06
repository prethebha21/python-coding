n=str(input("Enter the string: "))
s=n.split(" ")
for i in s:
 if len(i)%2==0:
  print(i)