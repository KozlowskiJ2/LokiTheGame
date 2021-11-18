import speech_recognition as sr

def escutar():
    r = sr.Recognizer()
    texto = ''
    try:
        with sr.Microphone() as fonte:
            print('Estou te escutando!', end='\n')
            audio = r.listen(fonte)


            texto = r.recognize_google(audio,language='pt-BR')

            texto = texto.capitalize()

    except:
        print('Error')
    return texto