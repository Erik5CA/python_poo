class Animal:
    def comer(self):
        print("Comiendo...")

class Ave(Animal):
    def volar(self):
        print("Volando...")

class Mamifero(Animal):
    def amamantar(self):
        print('Amamantando...')
        
class Murcialago(Ave, Mamifero):
    pass

muricelago = Murcialago()

muricelago.comer()
muricelago.volar()
muricelago.amamantar()

print(Murcialago.mro())