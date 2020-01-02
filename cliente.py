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
    minha_vez,servidor=udp.recvfrom(1024)
    while minha_vez.decode()!='True':
        minha_vez,servidor=udp.recvfrom(1024)
    msg=''
    linha=input('Digite o numero da linha: ')
    if linha=='\x18':
        break
    msg+=linha
    coluna=input('Digite o numero da coluna: ')
    if coluna=='\x18':
        break
    msg+=coluna
    
    udp.sendto(msg.encode(), dest)
    msg_servidor,servidor=udp.recvfrom(1024)
    print(msg_servidor.decode())

udp.close()