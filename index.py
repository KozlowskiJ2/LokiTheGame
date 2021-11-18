from cela import cela
from salao import salao
from testeVoz import escutar
import speech_recognition as sr
from limparTela import limpar_tela
mochila = []
texto = ''
print("Bem vindo a Loki: The Game!")
limpar_tela()
salve = open("save.txt", 'r')
save = salve.read()

if save != '0':
    carregar = print("Deseja carregar os dados salvos?")
    carregar = escutar()
    limpar_tela()
    salve.close()
    if carregar == 'Sim' or carregar == 'Carregar':
        if save == '1':
            mochila = ['Clips', 'Chave medieval', 'Chave Dourada', ]
            salao(mochila)
        elif save == '2':
            mochila = ['Clips', 'Chave medieval', 'Chave Dourada',
                       'Chave de coração', 'arma estranha']
            salao(mochila, True)
cela(mochila)
