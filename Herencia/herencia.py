class ClaseBase:
    def __init__(self) :
        print('Constructor de la ClaseBase')
        
    def metodo_clase(self):
        print('Metodo de la ClaseBase')

class ClaseDerivada(ClaseBase):
    def __init__(self) :
        print('Constructor de la ClaseDerivada')
        

obj = ClaseDerivada()
obj.metodo_clase()