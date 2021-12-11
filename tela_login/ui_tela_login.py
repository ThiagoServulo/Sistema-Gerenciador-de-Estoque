from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys


class Ui_tela_login(object):
    def setupUi(self, tela_login):
        icon = QIcon()
        icon.addFile(u"icones/icone_login.png", QSize(), QIcon.Normal, QIcon.Off)

        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)

        tela_login.resize(343, 151)
        tela_login.setMaximumSize(343, 151)
        tela_login.setMinimumSize(343, 151)
        tela_login.setWindowTitle(u"Bem Vindo")
        tela_login.setWindowIcon(icon)

        self.centralwidget = QWidget(tela_login)

        self.botao_login = QPushButton(self.centralwidget)
        self.botao_login.setGeometry(QRect(180, 90, 141, 41))
        self.botao_login.setFont(font)
        self.botao_login.setText(u"Login")

        self.label_matricula = QLabel(self.centralwidget)
        self.label_matricula.setGeometry(QRect(20, 20, 71, 16))
        self.label_matricula.setFont(font)
        self.label_matricula.setText(u"Matrícula:")

        self.label_criar_conta = QLabel(self.centralwidget)
        self.label_criar_conta.setGeometry(QRect(20, 50, 61, 16))
        self.label_criar_conta.setFont(font)
        self.label_criar_conta.setText(u"Senha:")

        self.texto_matricula = QLineEdit(self.centralwidget)
        self.texto_matricula.setGeometry(QRect(100, 19, 221, 21))
        self.texto_matricula.setFont(font)
        self.texto_matricula.setText(u"")
        self.texto_matricula.setMaxLength(20)

        self.texto_senha = QLineEdit(self.centralwidget)
        self.texto_senha.setGeometry(QRect(100, 49, 221, 21))
        self.texto_senha.setFont(font)
        self.texto_senha.setText(u"")
        self.texto_senha.setMaxLength(20)
        self.texto_senha.setEchoMode(QLineEdit.Password)

        self.botao_criar_conta = QPushButton(self.centralwidget)
        self.botao_criar_conta.setGeometry(QRect(20, 90, 141, 41))
        self.botao_criar_conta.setFont(font)
        self.botao_criar_conta.setText(u"Criar Conta")
        tela_login.setCentralWidget(self.centralwidget)
    # setupUi


class CriarTelaLogin(QMainWindow, Ui_tela_login):
    def __init__(self):
        super(CriarTelaLogin, self).__init__()
        self.setupUi(self)
    # __init__

    def mostrar_tela(self):
        self.texto_matricula.setText('')
        self.texto_senha.setText('')
        self.show()
    # mostrar_tela

    def closeEvent(self, event):
        sys.exit()
    # closeEvent
