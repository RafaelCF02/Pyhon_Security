import ctypes

atributo_ocultar  = 0x02

arquivo = input('Digite o arquivo ou pasta no qual deseja ocultar \n[Lembre de colocar o caminho no qual ele se encontra]:  ')

retorno = ctypes.windll.kernel32.SetFileAttributesW(arquivo, atributo_ocultar)

if retorno:
    print('Arquivo ocultado')
else:
    print('Arquivo não foi ocultado')