from tela_login.ui_tela_login import CriarTelaLogin
from tela_cadastrar_usuario.ui_tela_cadastrar_usuario import CriarTelaCadastrarUsuario
from tela_alterar_usuario.ui_tela_alterar_usuario import CriarTelaAlterarUsuario
from tela_cadastrar_produto.ui_tela_cadastrar_produto import CriarTelaCadastrarProduto
from tela_principal.ui_tela_principal import CriarPrincipal
from tela_excluir_usuario.ui_tela_excluir_usuario import CriarTelaExcluirUsuario
from Bibliotecas.Lib_BancoDeDados import *


class Eventos:

    fonte = 'MS Shell Dlg 2'
    tamanho = 4

    def __init__(self):
        self.tela_login = CriarTelaLogin()
        self.tela_login.botao_login.clicked.connect(self.login)
        self.tela_login.botao_criar_conta.clicked.connect(self.abrir_tela_cadastrar_usuario)

        self.tela_cadastrar_usuario = CriarTelaCadastrarUsuario()
        self.tela_cadastrar_usuario.botao_cadastrar_usuario.clicked.connect(self.cadastrar_usuario)

        self.tela_alterar_usuario = CriarTelaAlterarUsuario()
        self.tela_alterar_usuario.botao_alterar_usuario.clicked.connect(self.alterar_usuario)

        self.tela_excluir_usuario = CriarTelaExcluirUsuario()
        self.tela_excluir_usuario.botao_excluir_usuario.clicked.connect(self.excluir_usuario)

        self.tela_cadastrar_produto = CriarTelaCadastrarProduto()
        self.tela_cadastrar_produto.botao_cadastrar_produto.clicked.connect(self.cadastrar_produto)

        self.tela_principal = CriarPrincipal()
        self.tela_principal.action_cadastrar_usuario.triggered.connect(self.tela_cadastrar_usuario.mostrar_tela)
        self.tela_principal.action_alterar_usuario.triggered.connect(self.tela_alterar_usuario.mostrar_tela)
        self.tela_principal.action_excluir_usuario.triggered.connect(self.tela_excluir_usuario.mostrar_tela)
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
        matricula = valida_matricula(self.tela_login.texto_matricula.text())
        if matricula == -1:
            QMessageBox.critical(self.tela_alterar_usuario, 'Erro',
                                 f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                 f"Matrícula inválida</font>")
        elif len(self.tela_login.texto_senha.text()) <= 0:
            QMessageBox.critical(self.tela_alterar_usuario,
                                 'Erro', f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                         f"Senha inválida</font>")
        else:
            ret = verificar_dados_usuario(matricula, self.tela_login.texto_senha.text())
            if ret == -1:
                QMessageBox.critical(self.tela_login, 'Erro',
                                     f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                     f"Matrícula não encontrada</font>")
            elif ret == 0:
                QMessageBox.critical(self.tela_login, 'Erro',
                                     f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                     f"Senha incorreta</font>")
            elif ret == 1:
                cargo = cargo_usuario(matricula)
                self.tela_principal.texto_matricula.setText(str(matricula))
                self.tela_principal.texto_data.setText(data_atual_banco())
                self.tela_principal.texto_cargo.setText(converte_codigo_cargo_para_nome(cargo))
                self.tela_login.hide()
                self.tela_principal.mostrar_tela(cargo)
    # login

    def abrir_tela_cadastrar_usuario(self) -> None:
        """
        Função que abre a tela de cadastro de usuário
        :return: None
        """
        self.tela_cadastrar_usuario.mostrar_tela()
        self.tela_login.hide()
    # abrir_tela_cadastrar_usuario

    def cadastrar_usuario(self) -> None:
        """
        Função responsável por criar um novo usuário no banco de dados
        :return: None
        """
        if len(self.tela_cadastrar_usuario.texto_usuario.text()) < 2:
            QMessageBox.critical(self.tela_cadastrar_usuario, 'Erro',
                                 f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                 f"Usuário inválido: O nome do usuário é muito pequeno</font>")
        elif len(self.tela_cadastrar_usuario.texto_email.text()) < 5 or \
                '@' not in self.tela_cadastrar_usuario.texto_email.text():
            QMessageBox.critical(self.tela_cadastrar_usuario, 'Erro',
                                 f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                 f"Email inválido</font>")
        elif len(self.tela_cadastrar_usuario.texto_senha_1.text()) < 4:
            QMessageBox.critical(self.tela_cadastrar_usuario, 'Erro',
                                 f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                 f"Senha inválida: A senha deve ter pelo menos 4 caracteres</font>")
        elif self.tela_cadastrar_usuario.texto_senha_1.text() != self.tela_cadastrar_usuario.texto_senha_2.text():
            QMessageBox.critical(self.tela_cadastrar_usuario, 'Erro',
                                 f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                 f"Senha inválida: As senhas digitadas são diferentes</font>")
        elif not (self.tela_cadastrar_usuario.radio_button_gerente.isChecked() or
                  self.tela_cadastrar_usuario.radio_button_vendedor.isChecked() or
                  self.tela_cadastrar_usuario.radio_button_entregador.isChecked()):
            QMessageBox.critical(self.tela_cadastrar_usuario, 'Erro',
                                 f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                 f"Cargo inválido: Selecione o cargo deste usuário</font>")
        else:
            nome = self.tela_cadastrar_usuario.texto_usuario.text()
            email = self.tela_cadastrar_usuario.texto_email.text()
            senha = self.tela_cadastrar_usuario.texto_senha_1.text()
            cargo = retorna_numero_cargo_selecionado(self.tela_cadastrar_usuario)
            matricula = inserir_usuario_banco(nome, email, senha, cargo)
            if matricula == 0:
                QMessageBox.critical(self.tela_cadastrar_usuario, 'Erro',
                                     f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                     f"Erro ao adicionar o usuário: {nome}</font>")
            else:
                opcao = QMessageBox.information(self.tela_cadastrar_usuario, 'Sucesso',
                                                f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                                f"O usuário {nome} foi adicionado com sucesso."
                                                f"\nNúmero de matrícula: {matricula}</font>")
                if opcao == QMessageBox.StandardButton.Ok:
                    self.tela_cadastrar_usuario.close()
                    if not self.tela_principal.isVisible():
                        self.iniciar()
    # criar_conta

    def cadastrar_produto(self) -> None:
        """
        Função responsável por acrescentar os produtos no banco de dados
        :return: None
        """
        if len(self.tela_cadastrar_produto.texto_descricao.text()) < 1:
            QMessageBox.critical(self.tela_cadastrar_produto, 'Erro',
                                 f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                 f"Insira a descrição do produto</font>")
        elif len(self.tela_cadastrar_produto.texto_marca.text()) < 1:
            QMessageBox.critical(self.tela_cadastrar_produto, 'Erro',
                                 f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                 f"Insira a marca do produto</font>")
        elif len(self.tela_cadastrar_produto.texto_tamanho.text()) < 1:
            QMessageBox.critical(self.tela_cadastrar_produto, 'Erro',
                                 f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                 f"Insira o tamanho do produto</font>")
        elif self.tela_cadastrar_produto.spin_box_quantidade.value() <= 0:
            QMessageBox.critical(self.tela_cadastrar_produto, 'Erro',
                                 f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                 f"Insira uma quantidade de produto válida</font>")
        elif self.tela_cadastrar_produto.double_spin_box_preco_compra.value() <= 0:
            QMessageBox.critical(self.tela_cadastrar_produto, 'Erro',
                                 f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                 f"Insira o preço de compra</font>")
        elif self.tela_cadastrar_produto.double_spin_box_preco_venda.value() <= 0:
            QMessageBox.critical(self.tela_cadastrar_produto, 'Erro',
                                 f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                 f"Insira o preço de venda</font>")
        elif self.tela_cadastrar_produto.double_spin_box_preco_venda.value() < \
                self.tela_cadastrar_produto.double_spin_box_preco_compra.value():
            QMessageBox.critical(self.tela_cadastrar_produto, 'Erro',
                                 f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                 f"O preço de venda deve ser menor que o de compra</font>")
        else:
            print('Sucesso')
    # cadastrar_produto

    def alterar_usuario(self) -> None:
        """
        Função que permite fazer alterações nos dados do usuário
        :return: None
        """
        matricula = valida_matricula(self.tela_alterar_usuario.texto_matricula.text())
        if matricula == -1:
            QMessageBox.critical(self.tela_alterar_usuario, 'Erro',
                                 f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                 f"Matrícula inválida</font>")
        elif not (self.tela_alterar_usuario.radio_button_gerente.isChecked() or
                  self.tela_alterar_usuario.radio_button_vendedor.isChecked() or
                  self.tela_alterar_usuario.radio_button_entregador.isChecked()):
            QMessageBox.critical(self.tela_alterar_usuario, 'Erro',
                                 f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                 f"Cargo inválido: Selecione o novo cargo deste usuário</font>")
        else:
            nome = nome_usuario(matricula)
            if verificar_usuario_existe(nome):
                QMessageBox.critical(self.tela_alterar_usuario, 'Erro',
                                     f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                     f"Este usuário não existe</font>")
                return
            if matricula == int(self.tela_principal.texto_matricula.text()):
                QMessageBox.critical(self.tela_alterar_usuario, 'Erro',
                                     f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                     f"Você não pode alterar seu própio cargo</font>")
                return
            cargo_atual = cargo_usuario(matricula)
            novo_cargo = retorna_numero_cargo_selecionado(self.tela_alterar_usuario)
            if novo_cargo == cargo_atual:
                QMessageBox.critical(self.tela_alterar_usuario, 'Erro',
                                     f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                     f"Este já é o cargo atual deste funcionário</font>")
                return
            nome_cargo = converte_codigo_cargo_para_nome(novo_cargo)
            opcao = QMessageBox.question(self.tela_alterar_usuario, 'Confirmar',
                                         f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                         f"Deseja alterar o cargo de {nome} para {nome_cargo.lower()}?</font>",
                                         QMessageBox.Yes | QMessageBox.No)
            if opcao == QMessageBox.Yes:
                if alterar_cargo_banco(matricula, novo_cargo):
                    QMessageBox.information(self.tela_alterar_usuario, 'Sucesso',
                                            f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                            f"O cargo de {nome} foi alterado com sucesso</font>")
                else:
                    QMessageBox.critical(self.tela_alterar_usuario, 'Erro',
                                         f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                         f"Não foi possível alterar o cargo de {nome}</font>")
            self.tela_alterar_usuario.hide()
    # alterar_dados_usuario

    def excluir_usuario(self) -> None:
        """
        Função que permite fazer a exclusão de um usuário
        :return: None
        """
        matricula = valida_matricula(self.tela_excluir_usuario.texto_matricula.text())
        if matricula == -1:
            QMessageBox.critical(self.tela_excluir_usuario, 'Erro',
                                 f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                 f"Matrícula inválida</font>")
            return
        nome = nome_usuario(matricula)
        if verificar_usuario_existe(nome):
            QMessageBox.critical(self.tela_excluir_usuario, 'Erro',
                                 f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                 f"Este usuário não existe</font>")
        else:
            nome = nome_usuario(matricula)
            opcao = QMessageBox.question(self.tela_excluir_usuario, 'Confirmar',
                                         f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                         f"Deseja excluir o usuário {nome}?</font>",
                                         QMessageBox.Yes | QMessageBox.No)
            if opcao == QMessageBox.Yes:
                if excluir_usuario_banco(matricula):
                    QMessageBox.information(self.tela_excluir_usuario, 'Sucesso',
                                            f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                            f"O usuário {nome} foi excluído com sucesso</font>")
                else:
                    QMessageBox.critical(self.tela_excluir_usuario, 'Erro',
                                         f"<font face={Eventos.fonte} size={Eventos.tamanho}>"
                                         f"Erro ao excluir usuário {nome}</font>")
            self.tela_excluir_usuario.hide()
        # excluir_usuario
