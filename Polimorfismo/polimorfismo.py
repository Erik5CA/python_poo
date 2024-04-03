class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        print('Se llamo al metodo hablar')
        
class Perro(Animal):
    def  hablar(self):
        return 'Guau Guau'
        
class Gato(Animal):
    def  hablar(self):
        # super().hablar()
        return 'Miau Miau'
    
def escuchar_animal(animal : Animal):
    print(animal.hablar())
        
perro = Perro('Boddie')
gato = Gato('Luna')

escuchar_animal(perro)
escuchar_animal(gato)

