class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        print('Se llamo al metodo hablar')
        
class Perro(Animal):
    def  hablar(self):
        print('Guau Guau')
        
class Gato(Animal):
    def  hablar(self):
        super().hablar()
        print('Miau Miau')
        
perro = Perro('Boddie')
gato = Gato('Luna')

perro.hablar()
gato.hablar()

print(perro.nombre)
print(gato.nombre)