import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print('Socket criado com sucesso! ')
except socket.error as e:
    print(f'ERRO: {e}')


host = 'localhost'
port = 5432

s.bind((host,port))

mensagem = '\nServidor: Ola cliente'

while 1:
    dados, end = s.recvfrom(4096)
    if dados:
        print('Servidor enviando mensagem...')
        s.sendto(dados + (mensagem.encode()), end)

