import requests
from bs4 import BeautifulSoup
from ipwhois import IPWhois
import whois

# Fonction pour rechercher un username sur plusieurs sites sociaux
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

# Fonction pour analyser une adresse IP
def check_ip(ip):
    print(f"\n🌍 Analyse IP : {ip}")
    try:
        # Recherche via IPWhois pour obtenir des informations ASN
        obj = IPWhois(ip)
        results = obj.lookup_rdap()
        print(f"📌 Pays : {results['network']['country']}")
        print(f"🏢 Organisation : {results['network']['name']}")
        print(f"🔗 ASN : {results['asn']}")

        # Géolocalisation de l'IP via ipinfo.io
        geolocation_url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(geolocation_url)
        if response.status_code == 200:
            geo_data = response.json()
            city = geo_data.get('city', 'Non renseignée')
            region = geo_data.get('region', 'Non renseignée')
            country = geo_data.get('country', 'Non renseignée')
            location = geo_data.get('loc', 'Non renseignée')
            
            print(f"📍 Localisation : {city}, {region}, {country}")
            print(f"📡 Latitude/Longitude : {location}")

            # Lien vers Google Maps
            if location != 'Non renseignée':
                lat, lon = location.split(',')
                maps_link = f"https://www.google.com/maps?q={lat},{lon}"
                print(f"🗺️ Voir sur la carte : {maps_link}")
            else:
                print("❓ Impossible d'afficher la localisation sur la carte.")
            
            # Lien vers ipinfo.io pour plus de détails
            ipinfo_link = f"https://ipinfo.io/{ip}"
            print(f"🔗 Détails IP : {ipinfo_link}")

        else:
            print("⚠️ Impossible d'obtenir la géolocalisation.")

    except Exception as e:
        print(f"⚠️ Erreur IP : {e}")

# Fonction pour analyser un domaine
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

# Menu principal
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
