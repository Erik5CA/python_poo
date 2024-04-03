class MiClase:
    def __init__(self):
        # Atributo privado
        self._atributo_privado = 'Valor'
        # Atributo mas privado
        self.__atributo_mas_privado = 'Valor'
        # Atributo publico
        self.atributo_publico = 'Valor'
        
    # Metodo Privado
    def __metodo_privado(self):
        print('Metodo Privado')
        
obj = MiClase()
print(obj.__atributo_mas_privado)