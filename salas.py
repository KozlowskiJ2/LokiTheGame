from limparTela import limpar_tela
from inicioEfim import perder
from abrirMochila import abreMochila
from abrirPorta import abrir_Porta
from inicioEfim import ganhar
from brigar import briga
def camara(mochila):
    limpar_tela()
    acao = input("Voce entrou em uma camara com 2 portas\nEscolha uma:\n1-Esquerda\n2-Direita\n")
    limpar_tela()
    if acao=="1":
        acao = input("Faca silencio, ha um guarda dormindo...\nTem uma chave em forma de coração, deve ser para a próxima porta...\n Deseja pega-la?\n1-Sim\n2-Não\n")
        limpar_tela()
        if acao =="1":
            mochila.append("Chave de coração")
            podador = input("O guarda deixou um item parecido com uma arma no chão, deseja pegar?\n1-Sim\n2-Não\n")
            limpar_tela()
            if podador == "1":
                mochila.append("arma estranha")
                input("Nao ha mais nada nessa sala alem de um guarda dormindo e uma porta trancada, voltaremos para a camara")
                limpar_tela()
            elif podador == "2":
                input("Nao ha mais nada nessa sala alem de um guarda dormindo e uma porta trancada, voltaremos para a camara")
                limpar_tela()
            escolha = input("Você voltou para a câmara. A sua frente tem um corredor que te levará ao salão e uma porta a sua direita.\nO que você deseja fazer?\n1- Entrar no corredor\n2- Passar pela porta\n")
            limpar_tela()
            if escolha == "1":
                input("Ao fechar a porta ela travou, acho que nem a força de um deus é capaz de abrir...")
                limpar_tela()
            elif escolha == "2":
                input("Ops...\nVoce entrou em uma sala com 5 guardas. Parece que voce está em uma fria...")
                porta_dir = input("Você deseja lutar ou sair correndo para o salão?\n1-Lutar\n2-Ir para o salão!\n")
                if porta_dir == "1":
                    perder("Parece que você não bate muito bem da cabeça. Você quis lutar e acabou morrendo.")
                elif porta_dir == "2":  
                    limpar_tela()
                    trancar = input("Os guardas estão quase te alcançando, deseja trancar a porta?\n1-Sim\n2-Não\n")
                    if trancar == "1":
                        input("Você pega a chave dourada do primeiro guarda e tranca a porta, parece que esses guardas não tem acesso a essas chaves, você vai ganhar algum tempo.")
                        limpar_tela()
                    else:
                        perder("Você demorou muito tempo para fechar a porta, mais sorte da próxima vez!")
        elif acao=="2":
            input("Nao ha mais nada de interessante aqui, voltaremos para a camara e tambem deixaremos os itens aqui...")
            limpar_tela()
            camara(mochila) 

    elif acao=="2":
        input("Ops...\nVoce entrou em uma sala com 5 guardas. Parece que voce está em uma fria...\nSaia correndo daí o mais depressa possível")        
        perder("Você estava sem a chave necessária para abrir a porta que te ajudaria a fugir. Depois de tanto correr, você ficou preso e acabou sendo morto pelos guardas.")
    else:
        input("Selecione uma opção válida!")
        camara(mochila)


def sala_h(mochila):
    acao = input("Você abre a porta lentamente e dá de cara com um Hulk raivoso...Espero que tenha algo util na mochila. Abrir mochila?\n1-Sim\n2-Nao\n")
    if acao=="1":
        escolha=abreMochila(mochila)
        if escolha=="arma estranha":
            limpar_tela()
            input("Esse item era um podador, um item usado para acabar com a existência de alguém de modo definitivo no espaço-tempo...\nResumidamente, não existe mais Hulk...eu acho")
            limpar_tela()
            input("Olha, há uma escrivaninha deve ter alguma coisa util alí.\nPor que tem isso aqui? Nao me pergunte, sou apenas um narrador.\nMas que tal pegar uma delas? Pode ser util...")
            mochila[mochila.index('arma estranha')] = "Podador"
            opcao=["Joia da Mente","Caneta Bic","Clava","Livro de LP","Borracha verde","Notebook da Xuxa"]
            acao = int(input("Escolha uma\n1-Joia da Mente\n2-Caneta Bic\n3-Clava\n4-Livro de LP\n5-Borracha Verde\n6-Notebook da Xuxa\n"))           
            for i in range(1, 7):
                if i==acao:
                    mochila.append(opcao[i-1])
            limpar_tela()
            input("Não tem nada nessa sala, vamos voltar pro salão principal!")            
        else:
            mensagem="Voce escolheu o item errado e acabou apanhando feio do Hulk :|\nTao feio que morreu ;("
            perder(mensagem)
    elif acao=="2":
        mensagem="Voce apanhou tanto que morreu ;("
        perder(mensagem)
    else:
        input("Selecione uma opção válida!")
        sala_h(mochila)

def sala_ultima(mochila):
    
    input("Tem apenas mais essa porta para abrir... Será que alguma coisa na mochila que abre essa porta com jeitinho?")
    limpar_tela()
    escolha = abreMochila(mochila)
    if escolha=="clava":
        acao=input("Usar a ",escolha," para abrir a porta?\n1-Sim\n2-Nao")
        if acao =="1":
            input("Voce acabou com a porta, agora so falta acabar com guarda que esta dentro da sala e coincidentemente te prendeu")
            briga(mochila)
            limpar_tela()
            ganhar()
        else:
            perder("Um guarda te surpreendeu por trás, te deu um soco na cabeça e você acabou desmaiando, mais sorte da próxima vez...")
    else:
        input("Sua tentativa de abrir a porta chamou a atenção do guarda que guardava o estava lá dentro, mas pelo menos a porta abriu!")
        briga(mochila)
        ganhar()
