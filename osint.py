import requests
from bs4 import BeautifulSoup
from ipwhois import IPWhois
import whois

def check_username(username):
    print(f"\n🔍 Recherche de l'utilisateur : {username}")
    sites = {
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}"
    }
    for name, url in sites.items():
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                print(f"✅ {name} : {url}")
            elif r.status_code == 404:
                print(f"❌ {name} : Non trouvé")
        except Exception as e:
            print(f"⚠️ Erreur {name} : {e}")

def check_ip(ip):
    print(f"\n🌍 Analyse IP : {ip}")
    try:
        obj = IPWhois(ip)
        results = obj.lookup_rdap()
        print(f"📌 Pays       : {results['network']['country']}")
        print(f"🏢 Organisation : {results['network']['name']}")
        print(f"🔗 ASN        : {results['asn']}")
    except Exception as e:
        print(f"⚠️ Erreur IP : {e}")

def check_domain(domain):
    print(f"\n🔎 Analyse de domaine : {domain}")
    try:
        dom = whois.whois(domain)
        print(f"📅 Créé le : {dom.creation_date}")
        print(f"🔒 Expire le : {dom.expiration_date}")
        print(f"📧 E-mail : {dom.emails}")
        print(f"🌐 Registrar : {dom.registrar}")
    except Exception as e:
        print(f"⚠️ Erreur domaine : {e}")

def main():
    print("""
  🧠 MINOX OSINT TOOL – Version Avancée 🔥
  -----------------------------------------
  1️⃣ Rechercher un username
  2️⃣ Analyser une IP
  3️⃣ Analyser un domaine
  """)
    choix = input("👉 Choisis une option (1/2/3) : ")

    if choix == "1":
        username = input("🔤 Entre le pseudo : ")
        check_username(username)
    elif choix == "2":
        ip = input("🌐 Entre l'adresse IP : ")
        check_ip(ip)
    elif choix == "3":
        domain = input("💻 Entre le nom de domaine : ")
        check_domain(domain)
    else:

         print("❌ Choix invalide")

if __name__ == "__main__":
    main()
