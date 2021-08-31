mochila = []
import abrirMochila
import random
import os
import inicioEfim

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cela():
    print("Voce esta preso...\nAperte ENTER para continuar")
    input()
    acao = int(input(print("Acho que seria uma boa ideia tentar achar algo para fugir...\n1-Para procurar\n2-Esperar")))
    limpar_tela()#limpa a saída do usuário
    if acao==1:
        procura()
    elif acao==2:
        espera(i=0)#vai para uma função que pergunta para o usuario se ele quer procurar até ele falar que sim ou juntar 5 tentativas, ai perde

def espera(i):
    i=i+1
    limpar_tela()
    acao = int(input(print("Ja passou um bom tempo, quer tentar procurar algo agora?\n1-Sim\n2-Não")))
    if acao==1:
        procura()
    elif i>=5:
        print("Voce esperou tanto tempo que acabou morrendo de velhice ;(")
        #def perder()
    elif acao==2:
        espera(i)
    
def procura():
    opcao=int(input(print("Parece que você achou um clips...\nColocar no bolso?\n1-Sim\n2-Não")))
    if opcao==1:
        limpar_tela()
        print("Item no bolso.")
        mochila.append("clips")
        print("Acho que da para abrir essa porta com isso e com um pouco de furtilidade...\nPegue no bolso o clips")
        escolha=abrirMochila.abreMochila(mochila)
        print("Aperte ENTER para tentar com ",mochila[0])
        input()
        # vai para uma função que tenta abrir gerando números aleatorios de 1 ou 0, tendo no maximo 3 tentativas falhas, apos isso vai sozinho
        if escolha=="clips":
            abrir_cela(i=0)
        else:
            print("Não é possível realizar essa ação com esse item...\nEscolha outro")
            # puxar abrir mochila

    elif opcao==2:
        opcao=int(input(print("Tem certeza?\nIsso pode ser a única de chance de sair desse lugar\n1-Sim\n2-Pegar o clips")))
        if opcao==1:
            print("Devido a sua escolha voce ficou o resto da sua vida na prisão e morreu ;(")
            #def perder()
        elif opcao==2:
            abrir_cela(i=0)

def abrir_cela(i):
    tentativa=random.randint(0,1)
    if tentativa==0 or i==3:
        print("Voce conseguiu abrir a cela!!!\nEntretanto...um guarda te viu e está vindo, se prepare...\n")
    elif tentativa==1:
        print("Ops, voce não conseguiu...\nAperte ENTER para tentar de novo")
        input()
        i=i+1
        abrir_cela(i)

def camara():
    limpar_tela()
    acao = int(input(print("Voce entrou em uma camera com 2 portas\nEscolha uma:\n1-Esquerda\n2-Direita")))#Esolha de alguns dos lados
    if acao==1:
        acao = int(input(print("Faca silencio ha um guarda dormindo...\nOlha uma chave, deve ser para a próxima porta\nE um item misterioso, deve ser util. Deseja pega-los?\n1-Sim\n2-Não")))#Pega de itens ou não
        if acao ==1:
            mochila.append("Chaves")
            mochila.append("Item misterioso")
            acao = int(input(print("Destrancar a porta com as chaves do guarda?\n1-Sim\n2-Não")))
            if acao==1:
                abrir_Porta()

            elif acao==2:
                print("Nao ha mais nada de interessante aqui, voltaremos para a camara e tambem deixaremos os itens aqui...")
                camara()
        elif acao==2:
            print("Nao ha mais nada nessa sala então alem de um guarda dormindo e uma porta trancada, voltaremos para a camera")
            camara()

    elif acao==2:
        print("Ops...\nVoce entrou em uma sala com 5 guardas, voce acabou de entrar em uma fria...")
        limpar_tela()
        cela()

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
            print("Olha, esse item deve ser um podador, um item usado para cortar acabar com sua existencia de modo definitivo no espaco tempo...\nResumidamente, nao existe mais Hulk")
            print("Olha, ha uma escrivaninha cheia de armas aqui.\nPor que tem isso aqui? Nao me pergunte, sou apenas um narrador.\nMas que tal pegar uma delas? Pode ser util...")
            sala_ultima()
        else:
            mensagem="Voce escolheu o item errado e acabou apanhando feio do HUlk :|\nTao feio que morreu ;("
            inicioEfim.perder(mensagem)
    elif acao==2:
        mensagem="Voce apanhou tanto que morreu ;("
        inicioEfim.perder(mensagem)

def sala_ultima():
    opcao=["Adaga","Espada de uma mao","Clava","Faca de cortar pao","Cimitarra","Lanca"]
    acao = int(input(print("Escolha uma\n1-Adaga\n2-Espada de uma mao\n3-Clava\n4-Faca de cortar pao\n5-Cimitarra\n6-Lanca")))
    for i in range(7):
        if i==acao:
            mochila.append(opcao[i-1])
    print("Ops...\nTem uma porta, não temos chaves mas pelo estado dela conseguimos abrir ela com algum objeto\nVamos dar uma olhada no bolso")
    escolha=abrirMochila.abreMochila(mochila)
    if escolha=="clava":
        acao=int(input(print("Usar a ",escolha," para abrir a porta?\n1-Sim\n2-Nao")))
        if acao ==1:
            print("Voce acabou com a porta, agora so falta acabar com guarda que esta dentro da sala e coincidentemente te prendeu")
            #puxar brigar
            #se venceu END GAME




cela()
#puxar brigar

camara()