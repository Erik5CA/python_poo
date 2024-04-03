# Open/Close Principle

class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificar(self):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def notificar(self):
        print(f'Enviando mensaje a {self.usuario.email}')
        
class NotificadorTelefono(Notificador):
    def notificar(self):
        print(f'Enviando mensaje SMS a {self.usuario.telefono}')

class NotificadorWhatApp(Notificador):
    def notificar(self):
        print(f'Enviando mensaje WhatsApp a {self.usuario.whatsapp}')
    


