from limparTela import limpar_tela
from abrirMochila import abreMochila
def abrir_Porta(mochila,porta):
    escolha = abreMochila(mochila)
    limpar_tela()
    if porta == 2:
        if escolha=="Chave de coração":
            return True
        else:
            return False
    elif porta == 1:
        if escolha=="Chave Medieval":
            return True
        else:
            input("Chave errada!")
            abrir_Porta(mochila,1)
    elif porta == 3:
        if escolha=="Chave Dourada":
            return True
        else:
            return False
        