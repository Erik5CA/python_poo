class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print('Estudiando...')
        
nombre = input('Ingrese el nombre: ')
edad = input('Ingrese la edad: ')
grado = input('Ingrese el grado: ')

estudiante = Estudiante(nombre, edad, grado)

print(f"""
      DATOS DEL ESTUDIANTE: \n
      Nombre: {estudiante.nombre}
      Edad: {estudiante.edad} 
      Grado: {estudiante.grado}
      """)

estudiar = input()
if estudiar.lower() == 'estudiar':
    estudiante.estudiar()