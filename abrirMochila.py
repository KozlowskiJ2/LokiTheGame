mochila=["clips"]

def abreMochila(mochila) :
    if len(mochila) == 0:
        print('Mochila Vazia!')
    if len(mochila)!= 0:
        print("Itens na mochila:\nDigite o numero correspondente dele")
        for item in mochila:
            print(mochila.index(item),"-",item)
        escolha=int(input(print("Escolha:")))

abreMochila(mochila)