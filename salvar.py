from limparTela import limpar_tela
def salvar(ponto):
    limpar_tela()
    input("Salvando game... Pressione ENTER para continuar")
    limpar_tela()
    salva = open("./texto.txt","w")
    salva.write(str(ponto))
    salva.close()

# def check(ponto):
