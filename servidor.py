import socket
jogo_da_velha=[['-','-','-'],['-','-','-'],['-','-','-']]
def exibir():
    x=''
    for linha in range(3):
        for coluna in range(3):
            if coluna!=1:
                jogo='|'+jogo_da_velha[linha][coluna]+'|'
            else:
                jogo=jogo_da_velha[linha][coluna]
            x+=jogo
        x+='\n'
    return x

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

HOST = ''  # Endereco IP do Servidor
PORT = 5000 # Porta que o Servidor está
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

jogadores=[]
print('Servidor no ar...')
print('Aguardando Jogadores...')
while len(jogadores)!=2:
    msg,jogador=udp.recvfrom(1024)
    if jogador not in jogadores:
        jogadores.append(jogador)
print('Jogadores Prontos!')
print(jogadores)
inicio_do_jogo='start'
udp.sendto(inicio_do_jogo.encode(),jogadores[0])
udp.sendto(inicio_do_jogo.encode(),jogadores[1])

sua_vez='False'
udp.sendto(sua_vez.encode(),jogadores[0])
udp.sendto(sua_vez.encode(),jogadores[1])

numero_de_jogadas=0
while True:
    ############################################# JOGADOR 1 #############################################
    
    #Enviando permissão para o jogador realizar sua jogada
    sua_vez='True'
    udp.sendto(sua_vez.encode(),jogadores[0])
    
    #Exibindo jogadas realizada
    if numero_de_jogadas==0:
        primeira_jogada='primeira jogada'
        udp.sendto(primeira_jogada.encode(),jogadores[0])
    else:
        return_jogo=exibir()
        udp.sendto(return_jogo.encode(),jogadores[0])

    #Eviando mensagem de derrota
    lose=vitoria(jogo_da_velha)
    if lose==True:
        msg_de_derrota='lose'
    else:
        msg_de_derrota='-'
    udp.sendto(msg_de_derrota.encode(),jogadores[0])

    #Enviando condição de empate
    draw=empate(jogo_da_velha)
    if draw==True:
        msg_de_empate='draw'
    else:
        msg_de_empate='-'
    udp.sendto(msg_de_empate.encode(),jogadores[0])

    #Recebendo jogada do 1º jogador
    msg, jogador = udp.recvfrom(1024)  
    while jogador!=jogadores[0]:
        msg, jogador = udp.recvfrom(1024)
    msg=msg.decode()
    jogada(jogo_da_velha,int(msg[0]),int(msg[1]),'x')
    print('Recebi de ',jogador, msg) 
    return_jogada=exibir()
    
    #Enviando jogada realizada
    udp.sendto(return_jogada.encode(),jogadores[0])

    #Enviando condição de vitoria
    win=vitoria(jogo_da_velha)
    if win == True:
        msg_de_vitoria='win'
    else:
        msg_de_vitoria='lose'
    udp.sendto(msg_de_vitoria.encode(),jogadores[0])

    #Testando condição de empate
    draw=empate(jogo_da_velha)
    if draw==True:
        msg_de_empate='draw'
    else:
        msg_de_empate='-'
    udp.sendto(msg_de_empate.encode(),jogadores[0])

    numero_de_jogadas+=1
    ############################################# JOGADOR 2 #############################################
    
    #Enviando permissão para o jogador realizar sua jogada
    sua_vez='True'
    udp.sendto(sua_vez.encode(),jogadores[1])
    
    #Exibindo jogadas realizadas
    return_jogo=exibir()
    udp.sendto(return_jogo.encode(),jogadores[1])
    
    #Eviando mensagem de derrota
    lose=vitoria(jogo_da_velha)
    if lose==True:
        msg_de_derrota='lose'
    else:
        msg_de_derrota='-'
    udp.sendto(msg_de_derrota.encode(),jogadores[1])

    #Enviando condição de empate
    draw=empate(jogo_da_velha)
    if draw==True:
        msg_de_empate='draw'
    else:
        msg_de_empate='-'
    udp.sendto(msg_de_empate.encode(),jogadores[1])

    #Recebendo jogada do 2º jogador
    msg, jogador = udp.recvfrom(1024)  
    msg=msg.decode()
    jogada(jogo_da_velha,int(msg[0]),int(msg[1]),'o')
    print('Recebi de ',jogador, msg) 

    #Enviando jogada realizada
    return_jogada=exibir()
    udp.sendto(return_jogada.encode(),jogadores[1])

    #Enviando msg de vitoria
    win=vitoria(jogo_da_velha)
    if win == True:
        msg_de_vitoria='win'
    else:
        msg_de_vitoria='lose'
    udp.sendto(msg_de_vitoria.encode(),jogadores[1])

    #Enviando condição de empate
    draw=empate(jogo_da_velha)
    if draw==True:
        msg_de_empate='draw'
    else:
        msg_de_empate='-'
    udp.sendto(msg_de_empate.encode(),jogadores[1])

udp.close()