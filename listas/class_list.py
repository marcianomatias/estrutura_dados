#Métodos da classe list
list = [1, "Python", [40, 30, 20]]
print(list)
l2 = list.copy()
print(list)
print(id(l2), id(list))
list.clear()
