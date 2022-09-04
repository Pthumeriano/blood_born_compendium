import socket 

portas = [21, 23, 80, 443, 8080]

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp
cliente.settimeout(0.1)

print('porta codigo')
for i in portas: 
    codigo = cliente.connect_ex(('',i))
    print(i, codigo)    
