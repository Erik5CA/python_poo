class Persona:
    def __init__(self, nombre, edad, nacionalidad) :
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print('Hablando...')
        

class Empleado(Persona):
    def __init__(self,nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
class Estudiante(Persona):
    def __init__(self,nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.universidad = universidad
        self.notas = notas
        
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return f'Mi habilidad es: {self.habilidad}'
        
class EmpleadoArtista(Empleado, Artista):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario, habilidad):
        Empleado.__init__(self, nombre, edad, nacionalidad, trabajo, salario)
        Artista.__init__(self, habilidad)
    
    def presentarse(self):
        print(f'Hola soy {self.nombre}, {super().mostrar_habilidad()} y soy {self.trabajo}') 
    

artista = EmpleadoArtista('Erik', 45, 'mexicano', 'Ingeniero', 3000, 'Pintar')

artista.presentarse()

herencia = issubclass(EmpleadoArtista, Artista)
print(herencia)

instancia = isinstance(artista, EmpleadoArtista)
print(instancia)