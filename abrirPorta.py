from abrirMochila import abreMochila
def abrir_Porta(mochila,porta):
    escolha = abreMochila(mochila)
    if porta == 2:
        if escolha=="Chave de coração":
            return True
        else:
            return False
    elif porta == 3:
        escolha = abreMochila(mochila)
        if porta == 2:
            if escolha=="Clava":
                return True
            else:
                return False