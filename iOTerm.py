import paramiko
import socket

# vars
client = paramiko.SSHClient()
# add to known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
hostname = "192.168.0.4"
username = "root"
password = "alpine"

def to_do():
    print("[+] Your Device is jailbroken :)")
    print("[*] Current working directory /private/var/root")
    print("[*] Creating ParaTerm/")
    print("[*] cd into ParaTerm/")
    print("[*] Now in ParaTerm/")
    print("[*] touching ParaTerm.success")
    print("[+] ParaTerm.success has been written to ")

def connection():
    print("Loading to_do list...")
    commands = [
        "pwd",
        "id",
        "uname -a",
        "df -h",
        "cd",
        #"ls",
        # // Make a folder (not needed now ig.)"mkdir ParaTerm.checkme && cd test/ && ls",
        "mkdir /private/var/root/ParaTerm", #&& cd ParaTerm/",
        "touch ParaTerm.success",
        "mv ParaTerm.success /private/var/root/ParaTerm",
        "ls"
    ]

    file = [
        "cat /private/var/root/ParaTerm.success"
    ]
    to_do()

    # initialize the SSH client
    try:
        client.connect(hostname=hostname, username=username, password=password)
    except:
        print("[!] Cannot connect to the SSH Server")
        exit()

    # execute the commands
    for command in commands:
        #print("="*50, command, "="*50)
        stdin, stdout, stderr = client.exec_command(command)
        #print(stdout.read().decode())
        err = stderr.read().decode()
        if err:
            print(err)

def respring():
    print("Respringing Device...\n")
    client.connect(hostname=hostname, username=username, password=password)
    stdin, stdout, stderr = client.exec_command("killall backboardd")
    err = stderr.read().decode()
    if err:
        print(err)
    print("All done. :) ~ AusMan")
    

if __name__ == '__main__':
    connection()
    respring()
    client.close()