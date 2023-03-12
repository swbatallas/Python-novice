# functions

def my_function () :
    print("esto es una funcion")

my_function ()

def sum_two_values(a: int,b: int) : # el tipado es debil, solo sirve como guia
    print(a + b)

sum_two_values(2,3)
sum_two_values("stw", "batallas")

def return_rest_values (a,b) :
    return a - b

resta = return_rest_values(4,2)

print(resta)

def print_name(name, surname, alias = "sin alias") :
    nombre = str()
    nombre = name
    apellido = str()
    apellido = surname
    print(f"{nombre} {apellido}")

print_name(surname = "batallas", name= "stewart")

def print_all(*text) :
    print(text)

print_all("hola","pa ti mi cola","con crayola","de gramola")