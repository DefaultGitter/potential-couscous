# users1 = {"Tom", "Bob", "Maks"}  # set
# users2 = {"Mark", "Nake", "Bob", "Tom", "Maks"}
# users2 = {"Mark", "Nake", "Bob"}
# users1 = {}  # dict
# users.discard("Tom")
# users.discard("AAA")
# users.remove("AAA")
# res1 = users1.union(users2)
# res2 = users1.intersection(users2)
# users1.intersection_update(users2)
# res1 = users1.difference(users2)
# res2 = users1 & users2
# print(res1)
# print(f"{users1}\n{users2}")
# res1 = users1.symmetric_difference(users2)
# res1 = users1 ^ users2
# print(res1)
# print(users2.issuperset(users1))
# print(users1.issubset(users2))
# users1 = frozenset({"Tom", "Bob", "Maks"})  # set | like tuple | no add
# print(type(users1))

city_set_1 = {"Lviv", "Kyiv", "Kharkiv"}
city_set_2 = {"Kharkiv"}
res = city_set_1.intersection(city_set_2)
print(res)
