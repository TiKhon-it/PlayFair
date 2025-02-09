from Vigenere import Vigenere
from Caesar import Caesar
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QLabel, QLineEdit, QTextEdit, QApplication
from PyQt5.QtGui import QFont
from playFair import BibaBoba


class Encrypt(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(
            "background-color: {}".format('#ffffff'))

        u1 = QVBoxLayout(self)
        u2 = QHBoxLayout(self)
        u3 = QHBoxLayout(self)
        u4 = QHBoxLayout(self)

        self.cypher = QComboBox(self)
        self.cypher.addItem("Зашифровка")
        self.cypher.addItem("Расшифровкa")
        self.cypher.setFont(QFont("Times", 16))
        u1.addWidget(self.cypher, 1)

        u1.addLayout(u2, 2)
        u1.addLayout(u3, 3)
        u1.addLayout(u4, 4)

        self.label = QLabel(self)
        self.label.setText('Ключ:       ')
        self.label.setStyleSheet(
            "background-color: {}".format('#c4d1ff'))
        self.label.setFont(QFont("Times", 16))
        u2.addWidget(self.label, 0)

        self.key = QLineEdit(self)
        self.key.setText("")
        self.key.setFont(QFont("Times", 16))
        u2.addWidget(self.key, 1)

        self.label = QLabel(self)
        self.label.setText('''Надо зашифровать:''')
        self.label.setStyleSheet(
            "background-color: {}".format('#c4d1ff'))
        self.label.setFont(QFont("Times", 16))
        u3.addWidget(self.label, 0)

        self.plaintext = QTextEdit(self)
        self.plaintext.setFont(QFont("Times", 14))
        self.plaintext.setObjectName("textEdit1")
        u3.addWidget(self.plaintext, 1)

        self.label = QLabel(self)
        self.label.setText('''Ответ:''')
        self.label.setStyleSheet(
            "background-color: {}".format('#c4d1ff'))
        self.label.setFont(QFont("Times", 16))
        u4.addWidget(self.label, 0)

        self.ciphertext = QTextEdit()
        self.ciphertext.setEnabled(False)
        self.ciphertext.setFont(QFont("Times", 14))
        self.ciphertext.setObjectName("ciphertext")
        u4.addWidget(self.ciphertext, 1)

        self.btn = QPushButton('Готово', self)
        self.btn.resize(1100, 50)
        self.btn.clicked.connect(self.encryption)
        self.btn.setFont(QFont("Times", 16))
        u1.addWidget(self.btn, 5)

    def encryption(self):
        plaintext = self.plaintext.toPlainText()
        key = self.key.text()
        self.ciphertext.setEnabled(True)
        if self.cypher.currentText() == "Зашифровка":
            if not key.isalpha():
                self.key.setText("Ключ должен быть написан английскими буквами")
            else:
                self.ciphertext.setPlainText(BibaBoba.playfair_encrypt(plaintext, key))
        elif self.cypher.currentText() == "Расшифровкa":
            if not key.isalpha():
                self.key.setText("Ключ должен быть написан английскими буквами")
            else:
                self.ciphertext.setPlainText(BibaBoba.playfair_decrypt(plaintext, key))

                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Encrypt()
    login.show()
    app.exec_()
