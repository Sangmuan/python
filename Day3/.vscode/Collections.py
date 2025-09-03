# List

my_list = [1, 3,2,3,3,3,3,3,4,"Tuang",True,3.14]
print("List:", my_list)

for i in range(5):
    print(i,"--",my_list[i])

print(type(my_list))
print(id(my_list))
my_list.append(1000)
print("-------------------")
print("List after append:", my_list)
print(id(my_list))

my_list.insert(2, "Sangmuan")
print("-------------------")
print("List after append:", my_list)
print(id(my_list))

print("-------------------")
print(my_list.count(3))
print(my_list.index("Tuang"))

print("-------------------")
my_list.remove("Tuang")
print(my_list)
print (id(my_list))

# remove the first element
print("-------------------")
my_list.pop(0)
print(my_list)
print (id(my_list))

print("-------------------")
# delete duplicate elements
my_list = list(set(my_list))
print(my_list)