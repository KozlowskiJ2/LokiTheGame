from limparTela import limpar_tela
from testeVoz import escutar
from corredor import corredor
import random
from inicioEfim import perder
def cela(mochila):
    input("Olá, Loki! Ou devo dizer, variante? Em nome da Autoridade de Variância Temporal, você está preso por crimes cometidos contra a Linha do Tempo Sagrada.\nA partir de agora, você vai ficar aqui nessa prisão especial, revivendo em looping memórias ruins do seu passado.")
    input()
    input("...\n") 
    input("\né... parece que não tem nenhum guarda por aqui")

    acao = input("Acho que seria uma boa ideia tentar achar algo para fugir...\nProcurar ou Esperar\n")
    acao = escutar()
    input(acao)
    limpar_tela() 
    input(acao)
    if acao=="Procurar":
        procura(mochila)
    elif acao=="Esperar":
        espera(0,mochila)
    else:
        input(acao)
        cela(mochila)

def espera(i,mochila):
    i=i+1        
    acao = input("Ja passou um bom tempo, quer tentar procurar algo agora?\n1-Sim\n2-Não\n")
    limpar_tela() 
    if acao=="1":
        procura(mochila)
    elif i>=5:
        perder("Voce esperou tanto tempo que acabou morrendo de velhice ;(")
    elif acao=="2":
        espera(i,mochila)
    else:
        input("Selecione uma opção válida!")
        espera(i,mochila)  
        
def procura(mochila):
    opcao = input("Olha, um clips! Parece que você achou algo útil...\nColocar no bolso?\n1-Sim\n2-Não\n")
    if opcao=="1":
        mochila.append("Clips")
        input("Ninguém está te vendo! Parece uma ótima oportunidade para abrir a cela com isso.")
        limpar_tela() 
        input(f"Aperte ENTER para tentar abrir a cela com  {mochila[0]}")
        limpar_tela() 
        abrir_cela(i=0)

    elif opcao=="2":
        opcao=input("Tem certeza?\nEssa pode ser a única de chance de sair desse lugar\n1-Sim\n2-Pegar o clips")
        limpar_tela() 
        if opcao=="1":
          perder("Devido a sua escolha voce ficou o resto da sua vida na prisão e morreu;")
        elif opcao=="2":
            abrir_cela(i=0)

    else:
        input("Selecione uma opção válida")
        procura(mochila)   

    corredor(mochila)  

def abrir_cela(i):
    tentativa=random.randint(0,1)
    if tentativa==0 or i==3:
        input("Nada que o deus da trapaça não consiga fazer, não é mesmo? Parabéns, parece que você abriu a cela")
        limpar_tela() 
        input("Ops... um guarda está vindo. Parece que você fez muito barulho. Se prepare para lutar...\n")
        limpar_tela() 
    elif tentativa==1:
        input("Ops, voce não conseguiu...\nAperte ENTER para tentar de novo")
        limpar_tela() 
        i=i+1
        abrir_cela(i)
    