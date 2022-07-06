myList = [6, 2, 5 ,1, 4]
tupleList = [(val, (val*val*val)) for val in myList]
print("The list of Tuples is " , str(tupleList))