test_str = str(input("Enter the string: "))
print ("The original string is : " + test_str)
new_str = ""
n=int(input("Enter the length of the string: "))
i=int(input("Enter the position: "))
for i in range(len(test_str)):
  if i != 5:
    new_str = new_str + test_str[i]
print ("The string after removal of i'th character : ",i, + new_str)