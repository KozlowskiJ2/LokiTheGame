from limparTela import limpar_tela
from salas import camara
from salas import sala_h
from salas import sala_ultima
from abrirPorta import abrir_Porta
from salvar import salvar
def salao(mochila,save = False):
    porta = int(input("Você entra na sala com 3 portas, o que fazer?\n1-Porta da esquerda\n2-Porta do Centro\n3-Porta da direita\n"))
    limpar_tela()
    saiuSala = False
    esquerda = True
    if save == True : esquerda = False
    centro = True
    while True:
        if porta == 1:
            if esquerda:
                input("Essa porta parece ser feita de ouro maciço, com certeza não dá pra arrombar, mas parece que existe uma chave pra ela!")
                abriu = abrir_Porta(mochila,3)
                limpar_tela()
                if abriu:
                    camara(mochila)
                    salvar(2)
                    esquerda = False
                else:
                    input("Essa não era a chave, quem sabe outra?")
                    limpar_tela()
            else:
                input("Porta Bloqueada!")
                limpar_tela()
        elif porta == 2:
            input("Essa porta tá trancada, tem um simbolo de coração na maçaneta, deve ter algum jeito de abri-la em algum lugar...")
            abriu = abrir_Porta(mochila,2)
            if abriu:
                if centro:
                    sala_h(mochila)
                    limpar_tela()
                    centro = False
                else:
                    input('Você já vasculhou essa sala, procure a saída!')
                    limpar_tela()
            else:
                input('Essa não era a chave!')
                limpar_tela()
        elif porta == 3:
            if centro == False:
                sala_ultima(mochila)
            else:
                input("É uma porta de madeira bem pesada, não deve ser fácil de abrir...trancada")
                limpar_tela()
        else:
            input("Opção inválida!")
        limpar_tela()
        porta = int(input("Você volta pro centro da sala, o que fazer?\n1-Porta da esquerda\n2-Porta do Centro\n3-Porta da direita\n"))
        limpar_tela()   
        

        