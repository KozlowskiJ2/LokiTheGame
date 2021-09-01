mochila = []
from cela import cela
input("Bem vindo a Loki: The Game, aperte ENTER para começar!")

salve = open("save.txt","r")
save = salve.read()

if save != '0':
    carregar = input("Deseja carregar os dados salvos?\n1-Sim\n2-Não\n")
    if carregar == '1':
        if save == '1':
            print()
        elif save == '2':
            print()
cela(mochila)
            
    

    

