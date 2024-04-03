class Personda:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    # Accdeder a el valor de un atributo
    # Con el decorador converitimos a la funcion a una propiedad
    @property
    def nombre(self):
        return self.__nombre
    
    # Modificar el valor del atributo
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre


persona = Personda('Erik', 24)

nombre = persona.nombre
print(nombre)

persona.nombre = 'Juan'
nombre = persona.nombre
print(nombre)