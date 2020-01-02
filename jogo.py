def exibir():
    for linha in range(3):
        for coluna in range(3):
            if coluna!=1:
                jogo='|'+jogo_da_velha[linha][coluna]+'|'
            else:
                jogo=jogo_da_velha[linha][coluna]
            print(jogo,end="")
        print()

def jogada(vetor,linha,coluna,objeto):
    if vetor[linha][coluna]=='-':
        vetor[linha][coluna]=objeto
        return True
    return False

def empate(vetor):
    contador=9
    for l in range(3):
        for c in range(3):
            if vetor[l][c]=='-':
                contador-=1
    if contador==9:
        return True
    else:
        return False

def vitoria(vetor):
    #VITORIA POR LINHA
    for l in range(3):
        linha=[]
        for c in range(3):
            linha.append(vetor[l][c])
        if linha.count('x')==3 or linha.count('o')==3:
            return True
    #VITORIA EM COLUNA 
    for l in range(3):
        coluna=[]
        for c in range(3):
            coluna.append(vetor[c][l])
        if coluna.count('x')==3 or coluna.count('o')==3:
            return True
    #VITORIA NA DIAGONAL PRINCIPAL
    diagonal=[]
    for l in range(3):
        for c in range(3):
            if l==c:
                diagonal.append(vetor[l][c])
    if diagonal.count('x')==3 or diagonal.count('o')==3:
        return True
    #VITORIA NA DIAGONAL INVERSA
    diagonal_inversa=[]
    for l in range(3):
        diagonal_inversa.append(vetor[l][3-l-1])
    if diagonal_inversa.count('x')==3 or diagonal_inversa.count('o')==3:
        return True
    
#INICIO DO JOGO
jogo_da_velha=[['-','-','-'],['-','-','-'],['-','-','-']]
'''
exibir()

while True:
    #################################### JOGADADOR 1 ####################################    
    print('JOGADOR 1')
    jogada_linha=int(input('Numero da linha: '))
    while jogada_linha<0 or jogada_linha>2:
        print('LINHA INVÁLIDA!')
        jogada_linha=int(input('Informe outra Linha: '))
    
    jogada_coluna=int(input('Numero da coluna: '))
    while jogada_coluna<0 or jogada_coluna>2:
        print('COLUNA INVÁLIDA!')
        jogada_coluna=int(input('Informe outra Coluna: '))
    result=jogada(jogo_da_velha,jogada_linha,jogada_coluna,'x')
    
    #==================================== JOGADA INVALIDA ====================================

    while result==False:
        print('Jogada Inválida!')
        print('Faça outra jogada:')
        print('JOGADOR 1')
        jogada_linha=int(input('Numero da linha: '))
        while jogada_linha<0 or jogada_linha>2:
            print('LINHA INVÁLIDA!')
            jogada_linha=int(input('Informe outra Linha: '))
    
        jogada_coluna=int(input('Numero da coluna: '))
        while jogada_coluna<0 or jogada_coluna>2:
            print('COLUNA INVÁLIDA!')
            jogada_coluna=int(input('Informe outra Coluna: '))
        result=jogada(jogo_da_velha,jogada_linha,jogada_coluna,'x')
    
    #==================================== VITORIA ====================================
    win=vitoria(jogo_da_velha)
    if win==True:
        exibir()
        print('JOGADOR 1 VENCEU')
        break
    #==================================== EMPATE ====================================
    draw=empate(jogo_da_velha)
    if draw==True:
        print('JOGO FINALIZADO EM EMPATE!')
        exibir()
        break
    exibir()
    
    print()
    #################################### JOGADADOR 2 ####################################     
    print('JOGADOR 2')
    jogada_linha=int(input('Numero da linha: '))
    while jogada_linha<0 or jogada_linha>2:
        print('LINHA INVÁLIDA!')
        jogada_linha=int(input('Informe outra Linha: '))
    
    jogada_coluna=int(input('Numero da coluna: '))
    while jogada_coluna<0 or jogada_coluna>2:
        print('COLUNA INVÁLIDA!')
        jogada_coluna=int(input('Informe outra Coluna: '))
    
    result=jogada(jogo_da_velha,jogada_linha,jogada_coluna,'o')

    #==================================== JOGADA INVALIDA ====================================


    while result==False:
        print('Jogada Inválida!')
        print('Faça outra jogada:')
        print('JOGADOR 2')
        jogada_linha=int(input('Numero da linha: '))
        while jogada_linha<0 or jogada_linha>2:
            print('LINHA INVÁLIDA!')
            jogada_linha=int(input('Informe outra Linha: '))
    
        jogada_coluna=int(input('Numero da coluna: '))
        while jogada_coluna<0 or jogada_coluna>2:
            print('COLUNA INVÁLIDA!')
            jogada_coluna=int(input('Informe outra Coluna: '))
        result=jogada(jogo_da_velha,jogada_linha,jogada_coluna,'o')
    #==================================== VITORIA ====================================
    win=vitoria(jogo_da_velha)
    if win==True:
        exibir()
        print('JOGADOR 2 VENCEU')
        break
    #==================================== EMPATE ====================================
    draw=empate(jogo_da_velha)
    if draw==True:
        exibir()
        print('JOGO FINALIZADO EM EMPATE!')
        break
    exibir()
    print()
'''