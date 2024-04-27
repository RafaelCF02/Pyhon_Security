import os 
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump  = dump.splitlines()
    
    for ip in dump:
        print(ip)
        os.system(f'ping -n 2 {ip}')
        print("=-=" * 20)
        time.sleep(5)