def abreMochila(mochila) :
    if len(mochila) == 0:
        print('Bolso Vazio!')
        return False
    if len(mochila)!= 0:
        print("Itens no bolso:\nDigite o numero correspondente dele para escolher")
        for item in mochila:
            print(mochila.index(item)+1,"-",item)
        i=input("Escolha:",)
        escolha=mochila[int(i)-1]
    return(escolha)