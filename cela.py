from limparTela import limpar_tela
import random
def cela(mochila):
    print("Olá, Loki! Ou devo dizer, variante? Em nome da Autoridade de Variância Temporal, você está preso por crimes cometidos contra a Linha do Tempo Sagrada.A partir de agora, você vai ficar aqui nessa prisão especial, revivendo em looping memórias ruins do seu passado.")
    input()
    print("...\n"          
          "\né... parece que não tem nenhum guarda por aqui")

    acao = int(input("Acho que seria uma boa ideia tentar achar algo para fugir...\n1-Procurar\n2-Esperar\n"))
    limpar_tela() #limpa a saída do usuário
    if acao==1:
        procura(mochila)
    elif acao==2:
        espera(i=0)#vai para uma função que pergunta para o usuario se ele quer procurar até ele falar que sim ou juntar 5 tentativas, ai perde
    else:
        input("Selecione uma opção válida!")

def espera(i):
    i=i+1        
    acao = int(input("Ja passou um bom tempo, quer tentar procurar algo agora?\n1-Sim\n2-Não\n"))
    if acao==1:
        procura()
    elif i>=5:
        print("Voce esperou tanto tempo que acabou morrendo de velhice ;(")
        #def perder()
    elif acao==2:
        espera(i)
    
    else:
        input("Selecione uma opção válida!")    
        
def procura(mochila):
    opcao = int(input("Olha, um clips! Parece que você achou algo útil...\nColocar no bolso?\n1-Sim\n2-Não\n"))
    if opcao==1:
        mochila.append("clips")
        print("Ninguém está te vendo! Parece uma ótima oportunidade para abrir a cela com isso.\nPegue o clips no bolso")
        # puxar abrir mochila
        print("Aperte ENTER para tentar abrir a cela com ", mochila[0])
        input()
        #vai para uma função que tenta abrir gerando números aleatorios de 1 ou 0, tendo no maximo 3 tentativas falhas, apos isso vai sozinho
        abrir_cela(i=0)

    elif opcao==2:
        opcao=int(input("Tem certeza?\nEssa pode ser a única de chance de sair desse lugar\n1-Sim\n2-Pegar o clips"))
        if opcao==1:
          input("Devido a sua escolha voce ficou o resto da sua vida na prisão e morreu;")
            #def perder()
        elif opcao==2:
            abrir_cela(i=0)

    else:
        input("Selecione uma opção válida")        

def abrir_cela(i):
    tentativa=random.randint(0,1)
    if tentativa==0 or i==3:
        print("Nada que o deus da trapaça não consiga fazer, não é mesmo? Parabéns, parece que você abriu a cela")
        print("Ops... um guarda está vindo. Parece que você fez muito barulho. Se prepare para lutar...\n")
    elif tentativa==1:
        print("Ops, voce não conseguiu...\nAperte ENTER para tentar de novo")
        input()
        i=i+1
        abrir_cela(i)