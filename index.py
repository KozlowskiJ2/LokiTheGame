mochila = []
from limparTela import limpar_tela
from salao import salao
from cela import cela
input("Bem vindo a Loki: The Game, aperte ENTER para começar!")
limpar_tela()
salve = open("save.txt","r")
save = salve.read()

if save != '0':
    carregar = input("Deseja carregar os dados salvos?\n1-Sim\n2-Não\n")
    limpar_tela()
    salve.close()
    if carregar == '1':
        if save == '1':
            mochila = ['Clips','Chave medieval','Chave Dourada',]
            salao(mochila)
        elif save == '2':
            mochila = ['Clips','Chave medieval','Chave Dourada','Chave de coração','arma misteriosa']
            salao(mochila,True)
cela(mochila)
            
    

    

