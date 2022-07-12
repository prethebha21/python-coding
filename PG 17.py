def list_swapping(my_list):
   size_of_list = len(my_list)
   temp = my_list[0]
   my_list[0] = my_list[size_of_list - 1]
   my_list[size_of_list - 1] = temp
   return my_list
my_list = [34, 21, 56, 78, 93, 20, 11, 9]
print("The list is :")
print(my_list)
print("The list after swapping the first and last elements is: ")
print(list_swapping(my_list))
