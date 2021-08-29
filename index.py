mochila = []

def cela():
    print("Voce esta preso...\nAperte ENTER para continuar")
    input()
    print("Acho que seria uma boa ideia tentar achar algo para fugir...")

    acao = int(input(print("1-Para procurar\n2-Esperar")))
    if acao==1:
        print("Parece que você achou algo útil...")
        opcao=int(input(print("Colocar no bolso?\n1-Sim\n2-Não")))
        if opcao==1:
            mochila.append("clips")
            print("Acho que da para abrir essa porta com isso e com um pouco de furtilidade...\nPegue no bolso no clips")
            # puxar abrir mochila
            print("Aperte ENTER para tentar com ",mochila[0])
            input()
            print("Voce conseguiu abrir a cela!!!, Entretanto...um guarda te viu e está vindo, se prepare...\n")
            # puxar brigar

    elif acao==2:
        i=0
        espera(i)
    
    else:
        print("Opcao invalida...")

def espera(i):
    i=i+1
    acao = int(input(print("Ja passou um bom tempo, quer tentar procurar algo agora?\n1-Sim\n2-Não")))
    if acao==1:
        print("Parece que você achou algo útil...")
        print("Acho que da para abrir essa porta com isso e com um pouco de furtilidade...")
    elif i>=5:
        print("Voce esperou tanto tempo que acabou morrendo de velhice );")
    elif acao==2:
        espera(i)
    

cela()
