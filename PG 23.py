string = str(input("Enter any string: "))
words = string.split()
words = list(reversed(words))
print(" ".join(words))