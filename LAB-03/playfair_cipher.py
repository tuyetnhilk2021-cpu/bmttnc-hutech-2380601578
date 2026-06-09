import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.playfair import Ui_MainWindow


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:500/api/playfair/encrypt"

        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": self.ui.txt_key.text()
        }

        try:
            response = requests.post(url, json=payload)

            print("Response status code:", response.status_code)
            print("Response text:", response.text)

            if response.status_code == 200:
                data = response.json()

                # ✅ FIX KEY ĐÚNG
                result = data.get("encrypted_text", "")

                self.ui.txt_cipher_text.setPlainText(result)

                QMessageBox.information(self, "Success", "Encrypted Successfully")

            else:
                QMessageBox.warning(self, "Error", "API Error")

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", str(e))

    def call_api_decrypt(self):
        url = "http://127.0.0.1:500/api/playfair/decrypt"

        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),
            "key": self.ui.txt_key.text()
        }

        try:
            response = requests.post(url, json=payload)

            print("Response status code:", response.status_code)
            print("Response text:", response.text)

            if response.status_code == 200:
                data = response.json()

                # ✅ FIX KEY ĐÚNG
                result = data.get("decrypted_text", "")

                self.ui.txt_plain_text.setPlainText(result)

                QMessageBox.information(self, "Success", "Decrypted Successfully")

            else:
                QMessageBox.warning(self, "Error", "API Error")

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())