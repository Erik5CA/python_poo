# Single Responsability Principle

class Auto:
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque

    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
        else:
            print("No hay combustible suficiente")
            
    def obtener_posicion(self):
        return self.posicion
            
class TanqueCombustible:
    def __init__(self):
        self.combustible = 100
    
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
    
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad
        
tanque = TanqueCombustible()
auto = Auto(tanque)

print(auto.obtener_posicion())
print(auto.mover(10))
print(auto.obtener_posicion())
print(auto.mover(20))
print(auto.obtener_posicion())
print(auto.mover(30))
print(auto.obtener_posicion())
print(auto.mover(50))
print(auto.obtener_posicion())
print(auto.mover(100))
        
        



    
