# excepciones, manejo de errores

number_one = 5
number_two = 3
number_one = '2'

# try except
try:
    print(number_one + number_two)
except:
    print("no se cumplio")

#try except else
try:
    print(number_one + number_two)
except:
    print("no se cumplio")
else:
    print("la ejecucion continua correctamente")

# try except else finally
try:
    print(number_one + number_two)
except:
    print("no se cumple el try")
else:
    print("se ejecuta si se cumple el try, soy opcional")
finally:
    print("se ejecuta siempre, soy opcional")

#excepciones por tipos
try:
    print(number_one + number_two)
except TypeError:
    print("no se cumplio")