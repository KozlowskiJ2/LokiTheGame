def camara():
    limpar_tela()
    acao = int(input(print("Voce entrou em uma camera com 2 portas\nEscolha uma:\n1-Esquerda\n2-Direita")))#Esolha de alguns dos lados
    if acao==1:
        acao = int(input(print("Faca silencio ha um guarda dormindo...\nTem uma chave em forma de coração, deve ser para a próxima porta...\nE um item misterioso, deve ser util. Deseja pega-los?\n1-Sim\n2-Não")))#Pega de itens ou não
        if acao ==1:
            mochila.append("coracao")
            mochila.append("Item misterioso")
            acao = int(input(print("Destrancar a porta com as chaves do guarda?\n1-Sim\n2-Não")))
            if acao==1:
                abrir_Porta()

            elif acao==2:
                print("Nao ha mais nada de interessante aqui, voltaremos para a camara e tambem deixaremos os itens aqui...")
                camara()
        elif acao==2:
            print("Nao ha mais nada nessa sala então alem de um guarda dormindo e uma porta trancada, voltaremos para a camara")
            camara()

    elif acao==2:
        perder("Ops...\nVoce entrou em uma sala com 5 guardas, voce acabou de entrar em uma fria...")

def abrir_Porta():
    escolha=abrirMochila.abreMochila(mochila)
    if escolha=="Chaves":
        print("Porta destrancada")
        sala_h()
    else:
        print("Voce escolhe o item errado.")
        abrir_Porta()

def sala_h():
    acao = int(input(print("Eita, o Hulk ta aqui, acho que seria uma boa usar o Item misterioso.\n1-Sim\n2-Nao")))
    if acao==1:
        escolha=abrirMochila.abreMochila(mochila)
        if escolha=="Item misterioso":
            limpar_tela()
            print("Esse item era um podador, um item usado para cortar acabar com sua existência de modo definitivo no espaço-tempo...\nResumidamente, não existe mais Hulk...eu acho")
            print("Olha, ha uma escrivaninha cheia de armas aqui.\nPor que tem isso aqui? Nao me pergunte, sou apenas um narrador.\nMas que tal pegar uma delas? Pode ser util...")
            sala_ultima()
        else:
            mensagem="Voce escolheu o item errado e acabou apanhando feio do HUlk :|\nTao feio que morreu ;("
            perder(mensagem)
    elif acao==2:
        mensagem="Voce apanhou tanto que morreu ;("
        perder(mensagem)

def sala_ultima():
    opcao=["Adaga","Espada de uma mao","Clava","Faca de cortar pao","Cimitarra","Lança"]
    acao = int(input("Escolha uma\n1-Adaga\n2-Espada de uma mao\n3-Clava\n4-Faca de cortar pao\n5-Cimitarra\n6-Lanca"))
    for i in range(7):
        if i==acao:
            mochila.append(opcao[i-1])
    input("Não tem nada nessa sala, vamos voltar pro salão principal!")
    input("Tem apenas mais uma porta para abrir... Será que alguma coisa na mochila que abre essa porta com jeitinho?")
    escolha=abrirMochila.abreMochila(mochila)
    if escolha=="clava":
        acao=int(input("Usar a ",escolha," para abrir a porta?\n1-Sim\n2-Nao"))
        if acao ==1:
            print("Voce acabou com a porta, agora so falta acabar com guarda que esta dentro da sala e coincidentemente te prendeu")
            brigar()