from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets


class Ui_tela_alterar_dados(object):
    def setupUi(self, tela_alterar_dados):
        if not tela_alterar_dados.objectName():
            tela_alterar_dados.setObjectName(u"tela_alterar_dados")
        tela_alterar_dados.resize(411, 172)
        tela_alterar_dados.setMaximumSize(411, 172)
        tela_alterar_dados.setMinimumSize(411, 172)
        tela_alterar_dados.setWindowTitle(u"Alterar Dados")
        icon = QIcon()
        icon.addFile(u"icones/icone_login.png", QSize(), QIcon.Normal, QIcon.Off)
        tela_alterar_dados.setWindowIcon(icon)
        self.centralwidget = QWidget(tela_alterar_dados)
        self.centralwidget.setObjectName(u"centralwidget")
        self.texto_matricula = QLineEdit(self.centralwidget)
        self.texto_matricula.setObjectName(u"texto_matricula")
        self.texto_matricula.setGeometry(QRect(130, 20, 261, 21))
        font = QFont()
        font.setPointSize(12)
        self.texto_matricula.setFont(font)
        self.texto_matricula.setText(u"")
        self.texto_matricula.setMaxLength(20)
        self.texto_matricula.setPlaceholderText(u"")
        self.label_matricula = QLabel(self.centralwidget)
        self.label_matricula.setObjectName(u"label_matricula")
        self.label_matricula.setGeometry(QRect(20, 20, 71, 16))
        self.label_matricula.setFont(font)
        self.label_matricula.setText(u"Matr\u00edcula:")
        self.group_box_alterar_cargo = QGroupBox(self.centralwidget)
        self.group_box_alterar_cargo.setObjectName(u"group_box_alterar_cargo")
        self.group_box_alterar_cargo.setEnabled(True)
        self.group_box_alterar_cargo.setGeometry(QRect(20, 50, 371, 61))
        self.group_box_alterar_cargo.setFont(font)
        self.group_box_alterar_cargo.setTitle(u"Alterar cargo")
        self.radio_button_vendedor = QRadioButton(self.group_box_alterar_cargo)
        self.radio_button_vendedor.setObjectName(u"radio_button_vendedor")
        self.radio_button_vendedor.setGeometry(QRect(10, 30, 91, 17))
        self.radio_button_vendedor.setText(u"Vendedor")
        self.radio_button_gerente = QRadioButton(self.group_box_alterar_cargo)
        self.radio_button_gerente.setObjectName(u"radio_button_gerente")
        self.radio_button_gerente.setGeometry(QRect(140, 30, 81, 17))
        self.radio_button_gerente.setText(u"Gerente")
        self.radio_button_entregador = QRadioButton(self.group_box_alterar_cargo)
        self.radio_button_entregador.setObjectName(u"radio_button_entregador")
        self.radio_button_entregador.setGeometry(QRect(250, 30, 101, 17))
        self.radio_button_entregador.setText(u"Entregador")
        self.botao_alterar_dados = QPushButton(self.centralwidget)
        self.botao_alterar_dados.setObjectName(u"botao_alterar_dados")
        self.botao_alterar_dados.setGeometry(QRect(130, 120, 141, 41))
        self.botao_alterar_dados.setFont(font)
        self.botao_alterar_dados.setText(u"Alterar dados")
        tela_alterar_dados.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(tela_alterar_dados)
    # setupUi


class CriarTelaAlterarDados(QtWidgets.QMainWindow, Ui_tela_alterar_dados):
    def __init__(self):
        super(CriarTelaAlterarDados, self).__init__()
        self.setupUi(self)
