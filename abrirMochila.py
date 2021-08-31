mochila=["clips"]

def abreMochila(mochila) :
    if len(mochila) == 0:
        print('Bolso Vazio!')
    if len(mochila)!= 0:
        print("Itens no bolso:\nDigite o numero correspondente dele para escolher")
        for item in mochila:
            print(mochila.index(item),"-",item)
        escolha=int(input(print("Escolha:")))
    return(escolha)

abreMochila(mochila)