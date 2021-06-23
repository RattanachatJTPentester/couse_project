import socket

server = '45.33.32.156'

def scan(port):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((server,port))
        return True
    except:
        return False

for x in range(20,26):
    if scan(x):
        print(f'Port {x} is open')
    else:
        pass