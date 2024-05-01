import hashlib

arquivo1 = './hashes/a.txt'
arquivo2 = './hashes/b.txt'

hash1 = hashlib.new('ripemd160')

hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'O arquivo {arquivo1} e diferente do arquivo: {arquivo2}')
    print(f'o hash do arquivo a.txt é {hash1.hexdigest()}')
    print(f'o hash do arquivo b.txt é {hash2.hexdigest()}')
else:
    print(f'O arquivo {arquivo1} e igual ao arquivo: {arquivo2}')
    print(f'o hash do arquivo a.txt é {hash1.hexdigest()}')
    print(f'o hash do arquivo b.txt é {hash2.hexdigest()}')