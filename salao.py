def salao():
    porta = int(input("Você entra na sala com 3 portas, o que fazer?\n1-Porta da esquerda\n2-Porta do Centro\n3-Porta da direita"))
    saiuSala = False
    while saiuSala != False:
        if porta == 1:
            if portaDestruida == False:
                resp = int(input('A porta está aberta, deseja entrar?\n1-Sim\n2-Não'))
                if resp == 1:
                    saiuSala == True
                    break
                elif resp == 2:
                    continue
                else:
                    input("Opção inválida!")
            else:
                input("Parece que não dá mais pra acessar essa porta")
        elif porta == 2:
            input("A maçaneta dessa porta tem um simbolo de coração")
        elif porta == 3:
            input("A maçaneta dessa porta tem um simbolo de ave")
        else:
            input("Opção inválida!")
            
            
        

        