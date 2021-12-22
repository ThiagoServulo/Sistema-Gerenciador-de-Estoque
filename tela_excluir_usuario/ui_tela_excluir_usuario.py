from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys


class Ui_tela_excluir_usuario(object):
    def __init__(self):
        self.centralwidget = QWidget()
        self.texto_matricula = QLineEdit()
        self.botao_excluir_usuario = QPushButton()
        self.label_matricula = QLabel()
    # __init__

    def setupUi(self, tela_excluir_usuario):
        icon = QIcon()
        icon.addFile(u"icones/icone_excluir_usuario.png", QSize(), QIcon.Normal, QIcon.Off)

        font = QFont()
        font.setPointSize(12)

        tela_excluir_usuario.setWindowTitle("Excluir Usuário")
        tela_excluir_usuario.resize(311, 105)
        tela_excluir_usuario.setMaximumSize(311, 105)
        tela_excluir_usuario.setMinimumSize(311, 105)
        tela_excluir_usuario.setFont(font)
        tela_excluir_usuario.setWindowIcon(icon)

        self.texto_matricula = QLineEdit(tela_excluir_usuario)
        self.texto_matricula.setGeometry(QRect(120, 10, 161, 21))
        self.texto_matricula.setFont(font)
        self.texto_matricula.setText(u"")
        self.texto_matricula.setMaxLength(20)

        self.botao_excluir_usuario = QPushButton(tela_excluir_usuario)
        self.botao_excluir_usuario.setGeometry(QRect(80, 50, 141, 41))
        self.botao_excluir_usuario.setFont(font)
        self.botao_excluir_usuario.setText(u"Excluir Usuário")

        self.label_matricula = QLabel(tela_excluir_usuario)
        self.label_matricula.setGeometry(QRect(30, 10, 71, 16))
        self.label_matricula.setFont(font)
        self.label_matricula.setText(u"Matrícula:")
    # setupUi


class CriarTelaExcluirUsuario(QMainWindow, Ui_tela_excluir_usuario):
    def __init__(self):
        super(CriarTelaExcluirUsuario, self).__init__()
        self.setupUi(self)
    # __init__

    def mostrar_tela(self):
        self.texto_matricula.setText(u"")
        self.show()
    # mostrar_tela


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CriarTelaExcluirUsuario()
    window.show()
    sys.exit(app.exec_())
