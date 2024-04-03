
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

roberto = Empleado('Roberto', 25, 'mexicano', 'ingeniero', 3000)

print(roberto.nombre)

roberto.hablar()