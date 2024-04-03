from textblob import TextBlob

class AnalizadorDeSentimientos:
    def anailizar_sentimientos(self, texto):
        analisis = TextBlob(texto)
        print(analisis.sentiment.polarity)
        if analisis.sentiment.polarity > 0:
            return "\x1b[1;32m" + 'Sentimiento positivo'
        elif analisis.sentiment.polarity < 0:
            return "\x1b[1;30m" + 'Sentimiento negativo'
        else:
            return "\x1b[1;33m" + 'Sentimiento neutro'
        
analizador = AnalizadorDeSentimientos()
# resultado = analizador.anailizar_sentimientos('Hello, Im bad')
# print(resultado)

while True:
    user_promt = input("\x1b[1;33m" + '\nEscribe algo: ' + "\x1b[0;37m" )
    resultado = analizador.anailizar_sentimientos(user_promt)
    print(resultado)