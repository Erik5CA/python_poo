class Personaje:
    def __init__(self, nombre, poder, velocidad):
        self.nombre = nombre
        self.poder = poder
        self.velocidad = velocidad
        
    def __repr__(self) -> str:
        return f'Personaje(nombre={self.nombre}, poder={self.poder}, velocidad={self.velocidad})'
    
    def __add__(self, otro_pj):
        nuevo_nombre = f'{self.nombre}-{otro_pj.nombre}'
        nuevo_poder = round((self.poder + otro_pj.poder/2)**1.3)
        nuevo_velocidad = round(((self.velocidad + otro_pj.velocidad)/2)**1.3)
        return Personaje(nuevo_nombre, nuevo_poder, nuevo_velocidad)
    
goku = Personaje('Goku', 100, 100)
vegeta = Personaje('Vegeta', 99, 99)
jiren = Personaje('Jiren', 130, 140)
gogeta = goku + vegeta
print(gogeta)
jigeta = gogeta + jiren
print(jigeta)