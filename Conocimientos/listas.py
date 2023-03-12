# listas

my_list = list()
my_other_list = [22, 34, 33, 22, 1]
string_list = ["stw", "eeee"]
var_list = [22, 1, "stw"]
personal_list = ["stewart", 25, "perros"]
print(my_other_list.count(22))
print(var_list.count("stw"))

nombre, edad, animales = personal_list # es necesario nombrar todas las var, no de forma aleatoria
print(nombre)

# incluir elementos a una lista
novacia_list = ["no esta vacio"]
novacia_list.append("claro que no") # incluye un elemento al final de la lista
novacia_list.insert(0, "vacio")
print(novacia_list)

# eliminar elementos de una lista

novacia_list.remove("vacio") # indicar el elemento a borrar
print(novacia_list)

pop_list = [0,1,2,3]
pop_list.pop() # elimina el ultimo elemento
print(pop_list)

pop = pop_list.pop(2) # elimina el elemento indicado
print(pop) # el elemento eliminado se guarda en el pop

numbers_list = [0,11,22,33,44]
del numbers_list[2] # elimina el elemento con la posicion indicada
print(numbers_list)

numbers_list.clear() # elimina todos los elementos dentro de la lista
print(numbers_list)

copi_list = my_other_list.copy() # copia la lista