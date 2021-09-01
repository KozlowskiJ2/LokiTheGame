from limparTela import limpar_tela
from inicioEfim import perder
from abrirPorta import abrir_Porta
def camara(mochila):
    limpar_tela()
    acao = int(input("Voce entrou em uma camara com 2 portas\nEscolha uma:\n1-Esquerda\n2-Direita\n"))#Escolha de alguns dos lados
    if acao==1:
        acao = int(input("Faca silencio, ha um guarda dormindo...\nTem uma chave em forma de coração, deve ser para a próxima porta...\n Deseja pega-la?\n1-Sim\n2-Não\n"))
        if acao ==1:
            mochila.append("Chave de coração")
            podador = int(input("O guarda deixou um item parecido com uma arma no chão, deseja pegar?\n1-Sim\n2-Não"))
            if podador == 1:
                mochila.append("arma estranha")
                input("Nao ha mais nada nessa sala alem de um guarda dormindo e uma porta trancada, voltaremos para a camara")
            elif podador == 2:
                input("Nao ha mais nada nessa sala alem de um guarda dormindo e uma porta trancada, voltaremos para a camara")
                escolha = int(input("Você voltou para a câmara. A sua frente tem um corredor que te levará ao salão e uma porta a sua direita.\nO que você deseja fazer?\n1- Entrar no corredor\n2- Passar pela porta\n"))
                if escolha == 1:
                    salao(mochila)
                elif escolha == 2:
                    input("Ops...\nVoce entrou em uma sala com 5 guardas. Parece que voce está em uma fria...")
                    porta_dir = int(input("Você deseja lutar ou sair correndo para o salão?\n1-Lutar\n2-Ir para o salão!"))
                    if porta_dir == 1:
                        perder("Parece que você não bate muito bem da cabeça. Você quis lutar e acabou morrendo.")
                    elif porta_dir == 2:  
                        trancar = int(input("Os guardas estão quase te alcançando, deseja trancar a porta?\n1-Sim\n2-Não"))
                        if trancar == 1:
                            input("Você pega a chave dourada do primeiro guarda e tranca a porta, parece que esses guardas não tem acesso a essas chaves, você vai ganhar algum tempo.")
                        else:
                            perder("Você demorou muito tempo para fechar a porta, mais sorte da próxima vez!")
        elif acao==2:
            print("Nao ha mais nada de interessante aqui, voltaremos para a camara e tambem deixaremos os itens aqui...")
            camara() # será que é funcao camara mesmo?
        elif acao==2:
            print("Nao ha mais nada nessa sala alem de um guarda dormindo e uma porta trancada, voltaremos para a camara")
            camara() # será que é funcao camara mesmo?

    elif acao==2:
        input("Ops...\nVoce entrou em uma sala com 5 guardas. Parece que voce está em uma fria...\nSaia correndo daí o mais depressa possível")        
        perder("Você estava sem a chave necessária para abrir a porta que te ajudaria a fugir. Depois de tanto correr, você ficou preso e acabou sendo morto pelos guardas.")
    else:
        input("Selecione uma opção válida!")
        camara()



def sala_h(mochila):
    acao = int(input("Você abre a porta lentamente e dá de cara com um Hulk raivoso...Espero que tenha algo util na mochila. Abrir mochila?\n1-Sim\n2-Nao\n"))
    if acao==1:
        escolha=abreMochila(mochila)
        if escolha=="arma estranha":
            limpar_tela()
            print("Esse item era um podador, um item usado para acabar com a existência de alguém de modo definitivo no espaço-tempo...\nResumidamente, não existe mais Hulk...eu acho")
            print("Olha, há uma escrivaninha cheia de armas aqui.\nPor que tem isso aqui? Nao me pergunte, sou apenas um narrador.\nMas que tal pegar uma delas? Pode ser util...")
            sala_ultima()
        else:
            mensagem="Voce escolheu o item errado e acabou apanhando feio do Hulk :|\nTao feio que morreu ;("
            perder(mensagem)
    elif acao==2:
        mensagem="Voce apanhou tanto que morreu ;("
        perder(mensagem)
    else:
        input("Selecione uma opção válida!")
        sala_h()

def sala_ultima():
    opcao=["Adaga","Espada de uma mao","Clava","Faca de cortar pao","Cimitarra","Lança"]
    acao = int(input("Escolha uma\n1-Adaga\n2-Espada de uma mao\n3-Clava\n4-Faca de cortar pao\n5-Cimitarra\n6-Lanca\n"))
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
    else:
        print("Acho que com essa arma voce nao vai conseguir, acho melhor escolher outra")
        sala_ultima()
camara([])