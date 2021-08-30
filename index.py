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
        mochila.append("clips")
        print("Acho que da para abrir essa porta com isso e com um pouco de furtilidade...\nPegue no bolso o clips")
        # puxar abrir mochila
        print("Aperte ENTER para tentar com ",mochila[0])
        input()
        #vai para uma função que tenta abrir gerando números aleatorios de 1 ou 0, tendo no maximo 3 tentativas falhas, apos isso vai sozinho
        abrir_cela(i=0)

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

cela()
#puxar brigar