from limparTela import limpar_tela
from salas import camara
from salas import sala_h
from salas import sala_ultima
from abrirPorta import abrir_Porta
def salao(mochila):
    porta = int(input("Você entra na sala com 3 portas, o que fazer?\n1-Porta da esquerda\n2-Porta do Centro\n3-Porta da direita\n"))
    saiuSala = False
    esquerda = True
    centro = True
    while True:
        if porta == 1:
            if esquerda:
                resp = int(input('A porta está aberta, deseja entrar?\n1-Sim\n2-Não\n'))
                if resp == 1:
                    camara(mochila)
                    esquerda = False
                elif resp == 2:
                    input('Voltamos pra busca...')
                else:
                    input("Opção inválida!")
            else:
                input("Porta Bloqueada!")
        elif porta == 2:
            input("Essa porta tá trancada, tem um simbolo de coração na maçaneta, deve ter algum jeito de abri-la em algum lugar...")
            abriu = abrir_Porta(mochila,2)
            if abriu:
                if centro:
                    sala_h(mochila)
                    centro = False
                else:
                    input('Você já vasculhou essa sala, procure a saída!')
            else:
                input('Essa não era a chave!')
        elif porta == 3:
            if centro == False:
                sala_ultima(mochila)
            else:
                input("É uma porta de madeira bem pesada, não deve ser fácil de abrir...trancada")
        else:
            input("Opção inválida!")
        limpar_tela()
        porta = int(input("Você volta pro centro da sala, o que fazer?\n1-Porta da esquerda\n2-Porta do Centro\n3-Porta da direita\n"))    
        

        