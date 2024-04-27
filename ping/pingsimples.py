import os

ip_host = input("Digite o IP ou o Host a ser verificado: ")

print("=-="*30)

os.system(f'ping -n 6 {ip_host}')

print("=-="*30)