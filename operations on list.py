my_lst = ['apple', 'guava', 'mango', 'kivi']

print("length of the list :", len(my_lst))
print("First element :", my_lst[0])
print("last element :", my_lst[-1])

my_lst.append('papaya')
print("updated list :", my_lst)

my_lst.remove('guava')
print("updated list :", my_lst)

my_lst.sort()
print("sorted list :", my_lst)

my_lst.pop(1)
print("updated list :", my_lst)
