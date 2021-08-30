def chave():
        input("Procurando por todos os bolsos do guarda existe um molho com 4 chaves no seu bolso direito, certamente uma dessas abre a porta!")
        chave = int(input("Você vai até a porta para abri-la com as chaves, qual chave deseja usar?\n1-Chave Pequena\n2-Chave dourada\n3-Chave Medieval\n4-Chave grande"))
        while chave != 3
            chave = int(input("Não entra! Qual chave quer tentar?\n1-Chave Pequena\n2-Chave dourada\n3-Chave Medieval\n4-Chave grande"))
        input("Uma porta medival para uma chave medieval!")
def corredor():
    input("Você sai da cela e um guarda está a sua espera, eu esperava mais de um!")
    brigar()
    acao = int(input("Você olha para o corredor de celas e todas estão vazias, uma porta medieval fecha o corredor.\n1-Procurar pela chave\n2-Tentar arrombar a porta\n3-Voltar para a cela"))
    if acao == 1:
        chave()
    elif acao == 2:
        resp = int(input('A porta parece bem pesada, um chute não vai resolver!\n1-tentar mesmo assim\n2-Procurar pela chave'))
        if resp == 1:
            perdeu('A porta tinha um sensor que acabou sendo ativado quando você a forçou e alertou todos os guardas...mais sorte da próxima vez.')
        elif resp == 2:
            chave()
        else:
            perdeu("Siga as regras do jogo!")
    
    elif acao == 3:
        perdeu("Você foi procurar algo na cela e acabou esbarrando em um botão de alarme! Mais sorte da próxima vez?")
    else:
        perdeu("Sem trapacear!")


            

        