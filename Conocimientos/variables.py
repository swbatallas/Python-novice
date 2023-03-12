# variables. Son como let, pueden reescribrirse, como veremos en el input.

my_variable = "hey"
print(my_variable)


# funciones del sistema
print(len(my_variable))

# variables en una sola linea
name, surname, age, alias = "Stewart", "Batallas", 25, "batallasDev"
print(name,surname,age,alias)

# inputs. Aparece automaticamente en la terminal
my_variable = input("Indica otro saludo: ")
name = input("Whats your name: ")
print(my_variable)
print(name)

# no podemos forzar el tipo, pero si guiar la variable
address: str = "Calle rs ciudad de cadiz"
address = 32
print(type(address))