# list methods
# var = list()
# print(type(var))
# var = []
# print(type(var))

var_list = ["uno", "element", "dos"]
var_list.append("element")  # add a new element
print(var_list)
sub_list = ["r", "fff"]
var_list.extend(sub_list)  # add a new collection
print(var_list)
# var_list.pop(0)               # remove element by index
# var_list.remove("element")    # remove  first element by value
# print(var_list)

# start_index = 0
# end_index = 10
# index = var_list.index("element", start_index, end_index)   # return a first index of the element

# var_list.insert(0, "new element")     # push e new element on the index
# print(var_list.count("element"))      # count the element by value
# var_list.reverse()                    # reverse the list
# var_list.sort(key=len, reverse=False) # sort list by key | default num sort or by alfabet

# var_list[start_index, end_index, step]

# tup_tup = ()
# tup_tup = (1,2,3)
# tup_tup = 1,2,3
# tup_tup = 1,
# tup_tup = tuple("values")
# tup_tup[start_index, end_index, step]

