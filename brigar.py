from limparTela import limpar_tela
import random
from abrirMochila import abreMochila
from inicioEfim import perder
def briga(mochila):

    vidasLoki = 5
    vidasAdversario = 3
    while True:
        if vidasAdversario <= 0 or vidasLoki <= 0:
            break
        acao = input("Parece que você se meteu em uma briga! O que deseja fazer?:\n1-Usar arma\n2-Dar Soco\n3-Fugir\n4-Trapacear!\n")
        limpar_tela()
        if acao == "1":
            usar = abreMochila(mochila)
            if usar == "Podador":
                vidasAdversario = 0
                input("Era uma vez um guarda...")
            elif usar == "Clava":
                input("Quase um home run...")
                vidasAdversario -= 2
            else:
                input(f"Isso não é bem uma arma, tá mais pra um {usar}")
                limpar_tela()
                vidasLoki -= 1        
        elif acao == "2":
            soco = random.randrange(1, 101)
            if soco % 3 == 0:
                input("Depois de tanto apanhar, parece que você aprendeu a lutar.")
                limpar_tela()
                vidasAdversario -= 1
            else:
                vidasLoki -= 1
                input("Esse você errou. Deveria tentar outra coisa, eu acho...")
                limpar_tela()
        elif acao == "3":
            fugir = input("Deseja realmente fugir?\nPressione 1 para confirmar ou outra tecla para negar\n")
            limpar_tela()
            if fugir == "1":
                perder("Você foi pego. Parece que voce vai ter que pensar em outro plano fugir.")
            else:
                vidasLoki -= 1
                input("Você se distraiu querendo fugir e acabou levando um soco!")              
                limpar_tela()
        elif acao == "4":
            input("Pressione Enter para usar os poderes de trapaça!")
            poder = random.randrange(1, 101)
            if poder % 2 == 0:
                input("Você é o deus da trapaça, enganar ele foi fácil.")
                limpar_tela()
                vidasAdversario = 0
            else:
                input("Parece que perceberam que você estava querendo trapacear, o inimigo é mais forte do que eu pensava!")
                limpar_tela()
                vidasLoki -=1
        else:
            input("Selecione uma opção válida!")
            limpar_tela()
        limpar_tela()
    if vidasLoki <= 0 :
        perder("Você acabou desmaiando e sendo levado de volta para a cela...É o fim")
    else:
        input("Nada como uma briga para se sentir mais vivo")
        limpar_tela()

    
