import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Cliente criado com sucesso')

except socket.error as e:
    print(f'ERRO: {e}')

host = 'localhost'
porta = 5433
mensagem = 'Olá servidor'

try:
    print(f'Cliente: {mensagem}')
    s.sendto(mensagem.encode(), (host, 5432))

    dados,servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(f'Cliente: {dados}')

finally:
    print('Cliente: Fechando a conexao')
    s.close()