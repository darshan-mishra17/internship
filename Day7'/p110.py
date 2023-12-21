my_dict = {
    "a" : [1,8,2,8],
    "b" : [10,11,12,5],
    "c" : [7, 12, 10, 11],
    "d" : [2, 8, 5, 6]
    }

print(my_dict)
my_set = set() # way to declare a set

for x in my_dict.values():
    for i in x:
        my_set.add(i)

sorted = list(sorted(my_set))
print(sorted)       
