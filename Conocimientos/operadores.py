# operadores, tambien suma strings. No puedes sumar diferentes tipos

suma = 1 + 2
resta = 2 - 1
multi = 3 * 2
divi = 4 / 2
resto = 10 % 3 # 10 / 3 = 3, resto = 1
floor_division = 10 // 3 # aproxima al numero entero
exponente = 2 ** 3
print(suma, resta, multi, divi, resto, floor_division, exponente)

# comparativos. Tambien compara strings

mayor = 3 < 4
no_mayor = 3 > 4
no_igual = 3 != 2 + 1
print(no_igual)

# operadores logicos

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or  "Hola" > "Python")
print(not(3 > 4))