class ClaseBase:
    def __init__(self):
        print('Constructor de la clase base')
        
class ClaseSubClase(ClaseBase):
    def __init__(self):
        # Con super el metodo que especifiquemos no cambia el metodo de la clase que se hereda
        super().__init__()
        print('Constructor de la clase subclase')
        
obj = ClaseSubClase()