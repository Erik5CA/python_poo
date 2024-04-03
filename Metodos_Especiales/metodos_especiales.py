class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f'Persona[ Nombre: {self.nombre} - Edad: {self.edad} ]'
    
    def __repr__(self):
        return f'Persona({self.nombre},{self.edad})'
    
    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre , nuevo_valor)
    
persona = Persona('erik', 25)
print(persona)

rep = repr(persona)
print(rep)

persona2 = Persona('juan', 24)

resultado = persona + persona2
print(resultado)

