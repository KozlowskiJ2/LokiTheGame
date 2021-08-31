from limparTela import limpar_tela
def salao():
    porta = int(input("Você entra na sala com 3 portas, o que fazer?\n1-Porta da esquerda\n2-Porta do Centro\n3-Porta da direita\n"))
    saiuSala = False
    while saiuSala == False:
        if porta == 1:
            resp = int(input('A porta está aberta, deseja entrar?\n1-Sim\n2-Não\n'))
            if resp == 1:
                saiuSala == True
                break
            elif resp == 2:
                input('Voltamos pra busca...')

            else:
                input("Opção inválida!")
        elif porta == 2:
            input("Essa porta tá trancada, tem um simbolo de coração na maçaneta")
        elif porta == 3:
            input("É uma porta de madeira bem pesada, não deve ser fácil de abrir...trancada")
        else:
            input("Opção inválida!")
        limpar_tela()
        porta = int(input("Você volta pro centro da sala, o que fazer?\n1-Porta da esquerda\n2-Porta do Centro\n3-Porta da direita\n"))
salao()

            
        

        