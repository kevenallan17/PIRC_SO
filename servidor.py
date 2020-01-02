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
while True:
    # JOGADOR 1
    sua_vez='True'
    udp.sendto(sua_vez.encode(),jogadores[0])
    msg, jogador = udp.recvfrom(1024)  # quantidade de bytes que espera receber
    while jogador!=jogadores[0]:
        msg, jogador = udp.recvfrom(1024)
    msg=msg.decode()
    jogada(jogo_da_velha,int(msg[0]),int(msg[1]),'x')
    print('Recebi de ',jogador, msg) # decode = de bytes para string
    return_cliente=exibir()
    udp.sendto(return_cliente.encode(),jogador)
    
    # JOGADOR 2
    udp.sendto(sua_vez.encode(),jogadores[1])
    msg, jogador = udp.recvfrom(1024)  # quantidade de bytes que espera receber
    msg=msg.decode()
    jogada(jogo_da_velha,int(msg[0]),int(msg[1]),'o')
    print('Recebi de ',jogador, msg) # decode = de bytes para string
    return_cliente=exibir()
    udp.sendto(return_cliente.encode(),jogador)
udp.close()