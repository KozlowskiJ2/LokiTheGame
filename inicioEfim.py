import sys
def iniciar():
    input("Bem vindo a Loki: The Game, aperte ENTER para começar!")

def perder(mensagem) :
    input(mensagem)
    sys.exit()

def ganhar() :
    input("Esse guarda tinha um timepad, teletransportador que te permite viajar pelo espaço-tempo, resumindo: VOCÊ ESTÁ LIVRE")
    input('Esse foi nosso game, aperte enter para sair.')
    sys.exit()
