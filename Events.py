from PySide2.QtWidgets import *
from tela_login.ui_tela_login import CriarTelaLogin
from tela_criar_conta.ui_tela_criar_conta import CriarTelaCriarConta
from tela_alterar_dados.ui_tela_alterar_dados import CriarTelaAlterarDados


class Eventos:
    def __init__(self):
        self.tela_login = CriarTelaLogin()
        self.tela_login.botao_login.clicked.connect(self.login)
        self.tela_login.botao_criar_conta.clicked.connect(self.criar_conta)
        self.tela_criar_conta = CriarTelaCriarConta()
        # self.tela_criar_conta.botao_criar_conta.clicked.connect()
        self.tela_alterar_dados = CriarTelaAlterarDados()
        # self.tela_alterar_dados.botao_alterar.clicked.connect()

    def iniciar(self):
        """Função que inicia a aplicação apresentando a janela de login"""
        self.tela_login.show()
    # iniciar

    def login(self):
        if len(self.tela_login.texto_matricula.text()) > 0 and len(self.tela_login.texto_senha.text()) > 0:
            print('entrar')
        else:
            QMessageBox.critical(self.tela_login, 'Erro', 'Usuário ou senha inválido')
    # login

    def criar_conta(self):
        self.tela_criar_conta.show()
        self.tela_login.hide()
    # criar_conta
