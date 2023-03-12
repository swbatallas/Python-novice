# strings

my_string = "Esto es un string"
sec_string = 'Con comillas simples'
string_con_salto = "string\ncon salto de linea "
string_con_tab = '\tstring con tabulacion'
print(string_con_salto) # longitud del string

# formateo
name, surname,age = "Stew" , "Batallas", 20

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age} ")

# desempaquetado de caracteres
language = "python"
a,b, c, d, e, f = language
print(a,c,d)

# division 

language_slice = language[1:3] #caracteres del 1 al 3, sin contar la 3
language_slice = language[1:] # caracteres del 1 al final
language_slice = language[-2] # caracter contando desde el final - x

print(language_slice)


# reverse
reversed_language = language[::-1]
print(reversed_language)

# funciones

print(language.capitalize()) # capitaliza la palabra
print(language.upper())
print(language.count("t"))
print(language.lower())
print(language.upper().isupper())

