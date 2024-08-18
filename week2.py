my_list = [10, 20, 30, 40]

print(my_list)
my_list[1] = 15

print(my_list)
 
my_list2 = [50, 60, 70]

my_list.extend(my_list2)

print(my_list)
del my_list[-1]
print(my_list)
my_list.sort()