set_set = {"element1", "element2", "element3", "element4"}
set_set2 = {"element1", "element2", "unique element"}
# set_set = set()
# set_set = {} # not correct | it`s dict

# set_set.add("element5")               # add a new element
# set_set.discard("element5")           # soft delete element
# set_set.remove("element1")            # hard delete element
# set_set.pop()                         # delete random element
# set_set.update({"new element"})       # add a new element | str adds like a list

# print(set_set.intersection(set_set2))             # elements in both sets
# print(set_set.symmetric_difference(set_set2))     # unique elements in sets
# print({"element1"}.issubset(set_set))             # does element or set fully in set
# print(set_set.issuperset({"element1"}))           # does set have element or set
# print(set_set.difference(set_set2))               # set1 - set2
# print(set_set.union(set_set2))                    # set1 + set2

# set_set3 = {"el", "ul", "al"}
# print(set_set.isdisjoint(set_set3))           # return true, then both sets are unique
