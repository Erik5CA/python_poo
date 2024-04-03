# Liskov´s Subtitution Principle

class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return 'Voy volando'
    
class AveNoVoladora(Ave):
    pass

class Pinguino(AveNoVoladora):
    pass