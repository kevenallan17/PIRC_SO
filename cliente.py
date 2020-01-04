import socket

HOST = 'LocalHost'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor está

# abre um socket UDP
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

msg='conect'
udp.sendto(msg.encode(), dest)

print('Para sair use CTRL+X\n')

start='stop'


while start!='start':
    start,servidor=udp.recvfrom(1024)
    start=start.decode()
    
print('O jogo vai começar')

while True:
    #Permissao para jogar
    minha_vez,servidor=udp.recvfrom(1024)
    while minha_vez.decode()!='True':
        minha_vez,servidor=udp.recvfrom(1024)
    
    #Jogada do oponente
    
    jogada_do_oponente,servidor=udp.recvfrom(1024)
    if jogada_do_oponente.decode()=='primeira jogada':
        print('')
    else:
        print('Seu oponente jogou:')
        print(jogada_do_oponente.decode())
    #Aramazenando minha jogada
    msg=''
    print('Sua vez!')
    linha=input('Digite o numero da linha: ')
    if linha=='\x18':
        break
    while linha<'0' or linha>'2':
        linha=input('Linha Invalida! Digite outra linha: ')
    
    msg+=linha
    coluna=input('Digite o numero da coluna: ')
    if coluna=='\x18':
        break
    while coluna<'0' or coluna>'2':
        coluna=input('Coluna Invalida! Digite outra coluna: ')
    
    msg+=coluna
    #Enviado jogada
    udp.sendto(msg.encode(), dest)

    
    #Vizualizando a minha jogada
    print('Você jogou:')
    minha_jogada,servidor=udp.recvfrom(1024)
    print(minha_jogada.decode())

    print('Agora é a vez do seu oponente!')
    print()
    
    
    
udp.close()