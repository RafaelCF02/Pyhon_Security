import itertools

string = input('Escreva a string a ser permutada: ')
resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))
