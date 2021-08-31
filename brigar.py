import random
from abrirMochila import abreMochila
from inicioEfim import perder
def briga(mochila):
    vidasLoki = 5
    vidasAdversario = 3
    while vidasAdversario > 0 or vidasLoki > 0:
        acao = int(input("Parece que você se meteu em uma briga! O que deseja fazer?:\n1-Usar arma\n2-Dar Soco\n3-Fugir\n4-Trapacear!\n"))
        if acao == 1: #quando tiver arma, estar na posição 1
            usar = abreMochila(mochila)
            if usar == "podador":
                vidasAdversario = 0
                input("Era uma vez um guarda...")
            elif usar == "clava":
                input("Quase um home run...")
                vidasAdversario -= 2
            else:
                input(f"Isso não é bem uma arma, tá mais pra um {usar}")
                vidasLoki -= 1        
        elif acao == 2:
            soco = random.randrange(1, 101)
            if soco % 3 == 0:
                input("Depois de tanto apanhar, parece que você aprendeu a lutar.")
                vidasAdversario -= 1
            else:
                vidasLoki -= 1
                input("Esse você errou. Vai continuar tentando?")
        elif acao == 3:
            fugir = int(input("Deseja realmente fugir?\nPressione 1 para confirmar ou outra tecla para negar\n"))
            if fugir == 1:
                perder("Você foi pego. Parece que voce vai ter que pensar em outro plano fugir.")
            else:
                vidasLoki -= 1
                input("Você se distraiu querendo fugir e acabou levando um soco!")              
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
    if vidasLoki <= 0 :
        perder("Você acabou desmaiando e sendo levado de volta para a cela...É o fim")
    else:
        input("Nada como uma briga para se sentir mais vivo")
    