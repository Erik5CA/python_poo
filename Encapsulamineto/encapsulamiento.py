class Auto:
    def __init__(self, marca, modelo, anio):
        # Atribito privados
        self.__marca = marca
        self.__modelo = modelo
        # Atributos no provados
        self.anio = anio
    # Obtener el valor de un atributo privado
    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    # Modificar el valor de un atributo privado
    def set_marca(self, marca):
        self.__marca = marca
    
    # Metodo provados
    def __acelerar(self):
        print('Acelerar')


mi_auto = Auto('Citroen', 'C4', 2016)

print(mi_auto.anio)
# print(mi_auto.__marca)
print(f'La marca del auto es {mi_auto.get_marca()} y el modelo es {mi_auto.get_modelo()}')

mi_auto.set_marca('Audi')
print(f'La marca del auto es {mi_auto.get_marca()} y el modelo es {mi_auto.get_modelo()}')

# mi_auto.__acelerar()

# mi_auto._Auto.__acelerar()