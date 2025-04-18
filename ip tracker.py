import requests
from termcolor import colored

def tracker(ip):
    try:
        print(colored(f"\n[+] Recherche d'infos sur : {ip}", "cyan"))
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        data = response.json()

        if data["status"] == "success":
            print(colored("=== Résultat de la recherche ===", "green"))
            print(colored(f"📍 Pays      : {data['country']}", "yellow"))
            print(colored(f"🏙️  Ville     : {data['city']}", "yellow"))
            print(colored(f"🌍 Région    : {data['regionName']}", "yellow"))
            print(colored(f"🛰️ FAI       : {data['isp']}", "yellow"))
            print(colored(f"📡 IP        : {data['query']}", "yellow"))
            print(colored(f"🕒 Fuseau    : {data['timezone']}", "yellow"))
            print(colored(f"📌 Coord     : {data['lat']}, {data['lon']}", "yellow"))
        else:
            print(colored("[-] Impossible de récupérer les infos.", "red"))

    except Exception as e:
        print(colored(f"❌ Erreur : {e}", "red"))

if __name__ == "__main__":
    print(colored("====== MINOX IP LOCATOR 🌐 ======", "magenta"))
    ip_input = input(colored("💡 Entrez une IP à localiser : ", "cyan"))
    tracker(ip_input)
