""" la diferencia entre listas y duplas son
- los elementos de una lista se pueden mutar y los de una dupla no se pueden mutar
 """
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (23, 1, "stw")
print(my_tuple[0], my_tuple[2])
print(my_tuple.index("stw"))

# reasignar tipo
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple = tuple(my_tuple)
#my_tuple.clear() no se pueden limpiar
print(my_tuple)