mochila = []
import random
import os

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
        print("Item no bolso.")
        mochila.append("clips")
        print("Acho que da para abrir essa porta com isso e com um pouco de furtilidade...\nPegue no bolso o clips")
        # puxar abrir mochila
        print("Aperte ENTER para tentar com ",mochila[0])
        input()
        #vai para uma função que tenta abrir gerando números aleatorios de 1 ou 0, tendo no maximo 3 tentativas falhas, apos isso vai sozinho
        # if escolha==0:
        #     abrir_cela(i=0)
        # else:
        #     print("Não é possível realizar essa ação com esse item...\nEscolha outro")
        #     # puxar abrir mochila

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
    acao = int(input(print("Voce entrou em uma camera com 2 portas\nEscolha uma:\n1-Esquerda\n2-Direita")))#Esolha de alguns dos lados
    if acao==1:
        acao = int(input(print("Faca silencio ha um guarda dormindo...\nOlha uma chave, deve ser para a próxima porta\nE um item misterioso, deve ser util. Deseja pega-los?\n1-Sim\n2-Não")))#Pega de itens ou não
        if acao ==1:
            mochila.append("Chaves")
            mochila.append("Item misterioso")
            acao = int(input(print("Destrancar a porta com as chaves do guarda?\n1-Sim\n2-Não")))
            if acao==1 and mochila[1]=="Chaves":#trocar se precisar de algum item depois do clips
                print("Porta destrancada")
                sala_h()
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

def sala_h():
    acao = int(input(print("Eita, o Hulk ta aqui, acho que seria uma boa usar o Item misterioso.\nSim\nNao")))
    if acao==1 and mochila[2]=="Item misterioso":#trocar se precisar de algum item depois de chaves
        print("Olha, esse item deve ser um podador, um item usado para cortar acabar com sua existencia de modo definitivo no espaco tempo...\nResumidamente, nao existe mais Hulk")
        print("Olha, ha uma escrivaninha cheia de armas aqui.\nPor que tem isso aqui? Nao me pergunte, sou apenas um narrador.\nMas que tal pegar uma delas? Pode ser util...")
        sala_ultima()
    elif acao==2:
        print("Voce apanhou tanto que morreu ;(")
        #def perder()
    elif mochila[2]!="Item misterioso":#trocar se precisar de algum item depois de chaves
        print("Voce nao pegou o item misterioso e nao teve nenhuma chance contra o Hulk desarmado ;(")
        #def perder()

def sala_ultima():
    escolha = int(input("1-Adaga\n2-Espada de uma mao\n3-Clava\n4-Faca de cortar pao\n5-Cortador de grama(nunca deixe elas crescerem, ou o pior pode acontecer\n6-Lanca\nEscolha: )"))
    #Continuar fazendo desse ponto

cela()
#puxar brigar

camara()