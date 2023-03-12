# clases

class MyPerson:
    def __init__(self, name, surname, alias = "Sin alias") -> None:
        self.name = name
        self.surname = surname
    
    def walk (self) :
        print(f'{self.name} esta caminando')

person = MyPerson("stewart", "batallas")
second_person = MyPerson("stewart", "batallas", "uly")

print(person.name) # no se puede acceder a la clase entera, solo a partes especificas

person.walk()