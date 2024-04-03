from textblob import TextBlob

class Sentimiento:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
    
    def __str__(self):
        return f"\x1b[1;{self.color}m{self.nombre}\x1b[0;37m"

class AnalizadorDeSentimientos:
    def __init__(self, rangos):
        self.rangos = rangos
    def anailizar_sentimientos(self, texto):
        polaridad = TextBlob(texto)
        # print(polaridad.sentiment.polarity)
        if polaridad.sentiment.polarity > 0:
            return Sentimiento('Sentimiento positivo', '32')
        elif polaridad.sentiment.polarity < 0:
            return Sentimiento('Sentimiento negativo', '30')
        else:
            return Sentimiento('Sentimiento neutral', '33')

rangos = [
    ((-0.6,-0.3), Sentimiento('Neagtivo', '30')),
    ((-0.3,-0.1), Sentimiento('Algo Neagtivo', '30')),
    ((-0.1,0.1), Sentimiento('Neutral', '33')),
    ((0.1,0.4), Sentimiento('Algo Positivo', '32')),
    ((0.4,0.6), Sentimiento('Positivo', '32')),
    ((0.6,1), Sentimiento('Muy Positivo', '32')),
]
        
analizador = AnalizadorDeSentimientos(rangos)
# resultado = analizador.anailizar_sentimientos('Hello, Im bad')
# print(resultado)

while True:
    user_promt = input("\x1b[1;33m" + '\nEscribe algo: ' + "\x1b[0;37m" )
    resultado =  analizador.anailizar_sentimientos(user_promt)
    print(resultado)