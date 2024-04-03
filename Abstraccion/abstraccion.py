class Auto:
    def __init__(self):
        self.estado = 'apagado'
        
    def encender(self):
        self.estado = 'encendido'
        print('Es auto esta encendido.')
        
    def apagar(self):
        self.estado = 'apagado'
        print('Es auto esta apagado.')
        
    def conducir(self):
        if self.estado == 'apagado':
            self.encender()
        print('Cunduciendo el auto.')

auto = Auto()
auto.conducir()