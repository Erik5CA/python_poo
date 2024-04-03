# Interface Segregation Principle

from abc import ABC, abstractclassmethod

class Trabajador(ABC):
    @abstractclassmethod
    def trabajar(self):
        pass
    
class Comedor(ABC):
    @abstractclassmethod
    def comer(self):
        pass

class Durmiente(ABC):
    @abstractclassmethod
    def dormir(self):
        pass
    

class Humano(Trabajador, Comedor, Durmiente):
    def comer(self):
        print('Comiendo')
    
    def dormir(self):
        print('Dormiendo')
    
    def trabajar(self):
        print('Trabajando')
        
        
class Robot(Trabajador):
    def trabajar(self):
        print('Trabajando Robot')

robot = Robot()
humano = Humano()

robot.trabajar()
humano.trabajar()
