# Dependecy Inversion Principle

# class Diccionario:
#     def verificar_palabras(self, palabra):
#         # Logica para verificar las palabras
#         pass
    
# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario
    
#     def corregir_texto(self, texto):
#         # Logica para corregir el texto
#         pass

from abc import ABC, abstractclassmethod

class VerificadorOrtografico:
    @abstractclassmethod()
    def verificar_palabra(self, texto):
        # Logica para verificar las palabra
        pass
    
class Diccionario(VerificadorOrtografico):
    def verificar_palabras(self, palabra):
        # Logica para verificar las palabras si esta en el diccionario
        pass
    
class CorrectorOrtografico(VerificadorOrtografico):
    def __init__(self, verificador):
        self.verificador = verificador
    
    def corregir_texto(self, texto):
        # Logica para corregir el texto
        pass