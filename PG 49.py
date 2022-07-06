def get_my_key(obj):
  return obj['size']
my_list = [{'name': "foo", 'size': 5}, {'name': "bar", 'size': 3}, {'name': "baz", 'size': 7}]
my_list.sort(key=get_my_key)
print(my_list)