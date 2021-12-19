from PySide2.QtWidgets import *
from tela_login.ui_tela_login import CriarTelaLogin
from tela_criar_conta.ui_tela_criar_conta import CriarTelaCriarConta
from tela_alterar_dados.ui_tela_alterar_dados import CriarTelaAlterarDados
from tela_cadastrar_produto.ui_tela_cadastrar_produto import CriarTelaCadastrarProduto
from tela_principal.ui_tela_principal import CriarPrincipal
from Bibliotecas.Lib_BancoDeDados import *


class Eventos:
    def __init__(self):
        self.tela_login = CriarTelaLogin()
        self.tela_login.botao_login.clicked.connect(self.login)
        self.tela_login.botao_criar_conta.clicked.connect(self.abrir_tela_criar_conta)

        self.tela_criar_conta = CriarTelaCriarConta()
        self.tela_criar_conta.botao_criar_conta.clicked.connect(self.criar_conta)

        self.tela_alterar_dados = CriarTelaAlterarDados()
        self.tela_alterar_dados.botao_alterar_dados.clicked.connect(self.alterar_dados_usuario)

        self.tela_cadastrar_produto = CriarTelaCadastrarProduto()
        self.tela_cadastrar_produto.botao_cadastrar_produto.clicked.connect(self.cadastrar_produto)

        self.tela_principal = CriarPrincipal()
        self.tela_principal.action_cadastrar.triggered.connect(self.tela_criar_conta.mostrar_tela)
        self.tela_principal.action_alterar.triggered.connect(self.tela_alterar_dados.mostrar_tela)
    # __init__

    def iniciar(self) -> None:
        """
        Função que inicia a aplicação apresentando a janela de login
        :return: None
        """
        self.tela_login.mostrar_tela()
    # iniciar

    def login(self) -> None:
        """
        Função responsável por checar se os dados do usuário são válidos para este acessar o sistema
        :return: None
        """
        if len(self.tela_login.texto_matricula.text()) > 0 and len(self.tela_login.texto_senha.text()) > 0:
            try:
                matricula = int(self.tela_login.texto_matricula.text())
            except ValueError:
                QMessageBox.critical(self.tela_login, 'Erro', "<font face='MS Shell Dlg 2' size=4>Matrícula inválida</font>")
                return
            ret = verificar_dados_usuario(matricula, self.tela_login.texto_senha.text())
            if ret == -1:
                QMessageBox.critical(self.tela_login, 'Erro', "<font face='MS Shell Dlg 2' size=4>Matrícula não encontrada</font>")
            elif ret == 0:
                QMessageBox.critical(self.tela_login, 'Erro', "<font face='MS Shell Dlg 2' size=4>Senha incorreta</font>")
            elif ret == 1:
                cargo = cargo_usuario(matricula)
                self.tela_principal.texto_matricula.setText(str(matricula))
                self.tela_principal.texto_data.setText(data_atual_banco())
                self.tela_principal.texto_cargo.setText(converte_codigo_cargo_para_nome(cargo))
                self.tela_login.hide()
                self.tela_principal.mostrar_tela(cargo)
        else:
            QMessageBox.critical(self.tela_login, 'Erro', "<font face='MS Shell Dlg 2' size=4>Usuário ou senha inválidos</font>")
    # login

    def abrir_tela_criar_conta(self) -> None:
        """
        Função que abre a tela de cadastro de usuário
        :return: None
        """
        self.tela_criar_conta.mostrar_tela()
        self.tela_login.hide()
    # abrir_tela_criar_conta

    def criar_conta(self) -> None:
        """
        Função responsável por criar um novo usuário no banco de dados
        :return: None
        """
        if len(self.tela_criar_conta.texto_usuario.text()) < 2:
            QMessageBox.critical(self.tela_criar_conta, 'Erro', "<font face='MS Shell Dlg 2' size=4>Usuário inválido: O nome do usuário é muito pequeno</font>")
        elif len(self.tela_criar_conta.texto_email.text()) < 5 or '@' not in self.tela_criar_conta.texto_email.text():
            QMessageBox.critical(self.tela_criar_conta, 'Erro', "<font face='MS Shell Dlg 2' size=4>Email inválido</font>")
        elif len(self.tela_criar_conta.texto_senha_1.text()) < 4:
            QMessageBox.critical(self.tela_criar_conta, 'Erro', "<font face='MS Shell Dlg 2' size=4>Senha inválida: A senha deve ter pelo menos 4 caracteres</font>")
        elif self.tela_criar_conta.texto_senha_1.text() != self.tela_criar_conta.texto_senha_2.text():
            QMessageBox.critical(self.tela_criar_conta, 'Erro', "<font face='MS Shell Dlg 2' size=4>Senha inválida: As senhas digitadas são diferentes</font>")
        elif not (self.tela_criar_conta.radio_button_gerente.isChecked() or
                  self.tela_criar_conta.radio_button_vendedor.isChecked() or
                  self.tela_criar_conta.radio_button_entregador.isChecked()):
            QMessageBox.critical(self.tela_criar_conta, 'Erro', "<font face='MS Shell Dlg 2' size=4>Cargo inválido: Selecione o cargo deste usuário</font>")
        else:
            nome = self.tela_criar_conta.texto_usuario.text()
            email = self.tela_criar_conta.texto_email.text()
            senha = self.tela_criar_conta.texto_senha_1.text()
            if self.tela_criar_conta.radio_button_entregador.isChecked():
                cargo = 1
            elif self.tela_criar_conta.radio_button_vendedor.isChecked():
                cargo = 2
            else:
                cargo = 3
            ret = inserir_usuario(nome, email, senha, cargo)
            mensagem = ret[1]
            if not ret[0]:
                QMessageBox.critical(self.tela_criar_conta, 'Erro', mensagem)
            else:
                opcao = QMessageBox.information(self.tela_criar_conta, 'Sucesso', mensagem)
                if opcao == QMessageBox.StandardButton.Ok:
                    self.tela_criar_conta.close()
                    if not self.tela_principal.isVisible():
                        self.iniciar()
    # criar_conta

    def cadastrar_produto(self) -> None:
        """
        Função responsável por acrescentar os produtos no banco de dados
        :return: None
        """
        if len(self.tela_cadastrar_produto.texto_descricao.text()) < 1:
            QMessageBox.critical(self.tela_cadastrar_produto, 'Erro', "<font face='MS Shell Dlg 2' size=4>Insira a descrição do produto</font>")
        elif len(self.tela_cadastrar_produto.texto_marca.text()) < 1:
            QMessageBox.critical(self.tela_cadastrar_produto, 'Erro', "<font face='MS Shell Dlg 2' size=4>Insira a marca do produto</font>")
        elif len(self.tela_cadastrar_produto.texto_tamanho.text()) < 1:
            QMessageBox.critical(self.tela_cadastrar_produto, 'Erro', "<font face='MS Shell Dlg 2' size=4>Insira o tamanho do produto</font>")
        elif self.tela_cadastrar_produto.spin_box_quantidade.value() <= 0:
            QMessageBox.critical(self.tela_cadastrar_produto, 'Erro', "<font face='MS Shell Dlg 2' size=4>Insira uma quantidade de produto válida</font>")
        elif self.tela_cadastrar_produto.double_spin_box_preco_compra.value() <= 0:
            QMessageBox.critical(self.tela_cadastrar_produto, 'Erro', "<font face='MS Shell Dlg 2' size=4>Insira o preço de compra</font>")
        elif self.tela_cadastrar_produto.double_spin_box_preco_venda.value() <= 0:
            QMessageBox.critical(self.tela_cadastrar_produto, 'Erro', "<font face='MS Shell Dlg 2' size=4>Insira o preço de venda</font>")
        elif self.tela_cadastrar_produto.double_spin_box_preco_venda.value() < self.tela_cadastrar_produto.double_spin_box_preco_compra.value():
            QMessageBox.critical(self.tela_cadastrar_produto, 'Erro', "<font face='MS Shell Dlg 2' size=4>O preço de venda deve ser menor que o de compra</font>")
        else:
            print('Sucesso')
    # cadastrar_produto

    def alterar_dados_usuario(self) -> None:
        """
        Função que permite fazer alterações nos dados do usuário
        :return: None
        """
        if len(self.tela_alterar_dados.texto_matricula.text()) < 1:
            QMessageBox.critical(self.tela_alterar_dados, 'Erro', "<font face='MS Shell Dlg 2' size = 4>Insira a matrícula do funcionário</font>")
        elif not (self.tela_alterar_dados.radio_button_gerente.isChecked() or
                  self.tela_alterar_dados.radio_button_vendedor.isChecked() or
                  self.tela_alterar_dados.radio_button_entregador.isChecked()):
            QMessageBox.critical(self.tela_alterar_dados, 'Erro', "<font face='MS Shell Dlg 2' size = 4>Cargo inválido: Selecione o novo cargo deste usuário</font>")
        else:
            try:
                matricula = int(self.tela_alterar_dados.texto_matricula.text())
            except ValueError:
                QMessageBox.critical(self.tela_alterar_dados, 'Erro', "<font face='MS Shell Dlg 2' size=4>Matrícula inválida</font>")
                return
            nome = nome_usuario(matricula)
            (status, mensagem) = verificar_usuario_existe(nome)
            if status:
                QMessageBox.critical(self.tela_alterar_dados, 'Erro', "<font face='MS Shell Dlg 2' size=4>Este usuário não existe</font>")
                return
            if matricula == int(self.tela_principal.texto_matricula.text()):
                QMessageBox.critical(self.tela_alterar_dados, 'Erro', "<font face='MS Shell Dlg 2' size=4>Você não pode alterar seu própio cargo</font>")
                return
            cargo_atual = cargo_usuario(matricula)
            if self.tela_alterar_dados.radio_button_entregador.isChecked():
                novo_cargo = 1
            elif self.tela_alterar_dados.radio_button_vendedor.isChecked():
                novo_cargo = 2
            else:
                novo_cargo = 3
            if novo_cargo == cargo_atual:
                QMessageBox.critical(self.tela_alterar_dados, 'Erro', "<font face='MS Shell Dlg 2' size=4>Este já é o cargo atual deste funcionário</font>")
                return
            nome_cargo = converte_codigo_cargo_para_nome(novo_cargo)
            opcao = QMessageBox.question(self.tela_alterar_dados, 'Confirmar', f"<font face='MS Shell Dlg 2' size=4>Deseja alterar o cargo de {nome} para {nome_cargo.lower()}?</font>", QMessageBox.Yes | QMessageBox.No)
            if opcao == QMessageBox.Yes:
                if alterar_cargo(matricula, novo_cargo):
                    QMessageBox.information(self.tela_alterar_dados, 'Sucesso', f"<font face='MS Shell Dlg 2' size=4>O cargo de {nome} foi alterado com sucesso</font>")
                else:
                    QMessageBox.critical(self.tela_alterar_dados, 'Erro', f"<font face='MS Shell Dlg 2' size=4>Não foi possível alterar o cargo de {nome}</font>")
            self.tela_alterar_dados.hide()
    # alterar_dados_usuario
