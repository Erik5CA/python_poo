from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, acividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = acividad
        
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f'Hola soy {self.nombre}')
        print(f'Tengo {self.edad} años')
        print(f'Sexo: {self.sexo}')

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, acividad):
        super().__init__(nombre, edad, sexo, acividad)
        
    def hacer_actividad(self):
        print(f'Estoy aprendiendo {self.actividad}')
        
class Trabajdor(Persona):
    def __init__(self, nombre, edad, sexo, acividad):
        super().__init__(nombre, edad, sexo, acividad)
        
    def hacer_actividad(self):
        print(f'Ejerzo la profesion de {self.actividad}')
        
estudiante = Estudiante('Erik', 25, 'Masculino', 'programador')
trabajador = Trabajdor('Juan', 46, 'Masculino', 'Abogado')

estudiante.presentarse()
estudiante.hacer_actividad()

trabajador.presentarse()
trabajador.hacer_actividad()
