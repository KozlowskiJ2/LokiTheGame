import random
from inicioEfim import perder
def briga():
    vidasLoki = 5
    vidasAdversario = 3
    while vidasAdversario != 0 or vidasLoki != 0:
        acao = input("Parece que você se meteu em uma briga! O que deseja fazer?:\n1-Usar arma\n2-Dar Soco\n3-Fugir\n4-Trapacear!
        ")
        if acao == 1:
            #usa arma
        elif acao == 2:
            #dá soco
            c
        elif acao == 3:
            fugir input("Deseja realmente fugir?\nPressione 1 para confirmar ou outra tecla para negar")
            if fugir == 1:
                perder()
            else:
                vidasLoki -= 1
                print("Você se distraiu querendo fugir e acabou levando um soco!")
        elif acao == 4:
            input("Pressione Enter para usar os poderes de trapaça!")
            poder = random.randrange(1, 101)
            if poder % 2 == 0:
                input("Você é o deus da trapaça, enganar ele foi fácil.")
                vidasAdversario = 0
            else:
                input("Parece que perceberam que você estava querendo trapacear, o inimigo é mais forte do que eu pensava!")
                vidasLoki -=1
        else:
            input("Selecione uma opção válida!")
    if vidasLoki == 0 :
        perder("Você acabou desmaiando e sendo levado de volta para a cela...É o fim")
    else:
        input("Nada como uma briga para se sentir mais vivo")