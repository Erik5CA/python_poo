class Personda:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    # Accdeder a el valor de un atributo
    def get_nombre(self):
        return self.__nombre
    
    # Modificar el valor del atributo
    def set_nombre(self, nombre):
        self.__nombre = nombre


persona = Personda('Erik', 24)

nombre = persona.get_nombre()
print(nombre)

persona.set_nombre('Juan')
nombre = persona.get_nombre()
print(nombre)