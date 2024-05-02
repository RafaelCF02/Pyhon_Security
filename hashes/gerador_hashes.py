import hashlib

def md5(string):
    resultado = hashlib.md5(string.encode('utf-8'))
    return print(f'O resultado da string em MD5 é: {resultado.hexdigest()}')
    
def sha256(string):
    resultado = hashlib.sha256(string.encode('utf-8'))
    return print(f'O resultado da string em Sha256 é: {resultado.hexdigest()}')

def sha1(string):
    resultado = hashlib.sha1(string.encode('utf-8'))
    return print(f'O resultado da string em Sha1 é: {resultado.hexdigest()}')

def sha512(string):
    resultado = hashlib.sha512(string.encode('utf-8'))
    return print(f'O resultado da string em Sha512 é: {resultado.hexdigest()}')

while True:
    print('='*8,'Menu','='*8)
    palavra = str(input('Digite a palavra a ser transformada em hash: '))

    escolha = input('''Voce deseja transoforma em
                    1-[MD5]
                    2-[SHA256]
                    3-[SHA1]
                    4-[SHA512]
                    : ''')
    
    if escolha[0] == '1':
        print('='*8,'Resultado','='*8)
        md5(palavra)
        print('='*20)
    elif escolha[0] == '2':
        print('='*8,'Resultado','='*8)
        sha256(palavra)
        print('='*20)
    elif escolha[0] == '3':
        print('='*8,'Resultado','='*8)
        sha1(palavra)
        print('='*20) 
    elif escolha[0] == '4':
        print('='*8,'Resultado','='*8)
        sha512(palavra)
        print('='*20)   
    else:
        print('Valor invalido')
        continue

    repeticao = input('Deseja transformar mais uma palavra em hash? [S/N]: ').upper()

    if repeticao[0] == 'N':
        break
    elif repeticao[0] == 'S':
        continue
    else:
        print('Valor invalido')
        break
        