from brigar import briga
from salvar import salvar
from salao import salao
from abrirPorta import abrir_Porta
def chave(mochila):
        input("Procurando por todos os bolsos do guarda você acha uma no seu bolso direito e outra na calça, certamente uma dessas abre a porta!")
        mochila.append("Chave Medieval")
        mochila.append("Chave Dourada")
        abriu = abrir_Porta(mochila,1)
        while abriu != True:
            abriu = abrir_Porta(mochila,1)          
        input("Toda fechadura tem sua chave!")
def corredor(mochila):
    input("Você sai da cela e um guarda está a sua espera. É, eu esperava que fosse mais de um!")
    briga(mochila)
    acao = input("Você olha para o corredor de celas e todas estão vazias, uma porta medieval fecha o corredor.\n1-Procurar pela chave\n2-Tentar arrombar a porta\n3-Voltar para a cela\n")
    if acao == "1":
        chave(mochila)
    elif acao == "2":
        resp = input('A porta parece bem pesada, um chute não vai resolver!\n1-tentar mesmo assim\n2-Procurar pela chave')
        if resp == "1":
            perdeu('A porta tinha um sensor que acabou sendo ativado quando você a forçou e alertou todos os guardas...mais sorte da próxima vez.')
        elif resp == "2":
            chave(mochila)
        else:
            perdeu("Siga as regras do jogo!")
    
    elif acao == "3":
        perdeu("Você foi procurar algo na cela e acabou esbarrando em um botão de alarme! Mais sorte da próxima vez!")
    else:
        perdeu("Sem trapacear!")
        corredor(mochila)
    salvar(1)
    salao(mochila)
        