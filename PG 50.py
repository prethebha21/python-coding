def printValues(**kwargs):
  for key, value in kwargs.items():
    print("The value of {} is {}".format(key, value))
if __name__ == '__main__':
  printValues(abbreviation="CP", full_name="Computer Programming")