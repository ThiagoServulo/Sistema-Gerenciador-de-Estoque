from tela_login.ui_tela_login import CriarTelaLogin
from tela_cadastrar_usuario.ui_tela_cadastrar_usuario import CriarTelaCadastrarUsuario
from tela_alterar_usuario.ui_tela_alterar_usuario import CriarTelaAlterarUsuario
from tela_cadastrar_produto.ui_tela_cadastrar_produto import CriarTelaCadastrarProduto
from tela_principal.ui_tela_principal import CriarTelaPrincipal
from tela_excluir_usuario.ui_tela_excluir_usuario import CriarTelaExcluirUsuario
from tela_excluir_produto.ui_tela_excluir_produto import CriarTelaExcluirProduto
from tela_alterar_produto.ui_tela_alterar_produto import CriarTelaAlterarProduto
from tela_relatorio_vendas_data.ui_tela_relatorios_venda_data import CriarTelaSelecionarDataRelatorioVendas
from Bibliotecas.Lib_BancoDeDados import *
from Bibliotecas.Lib_Arquivos_CSV import *
from PySide2.QtWidgets import *
# import PySide2.QtCore


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

        self.tela_excluir_produto = CriarTelaExcluirProduto()
        self.tela_excluir_produto.botao_excluir_produto.clicked.connect(self.excluir_produto)

        self.tela_alterar_produto = CriarTelaAlterarProduto()
        self.tela_alterar_produto.botao_alterar_produto.clicked.connect(self.alterar_produto)

        self.tela_selecionar_data_relatorio_vendas = CriarTelaSelecionarDataRelatorioVendas()
        self.tela_selecionar_data_relatorio_vendas.botao_confirmar.clicked.connect(self.gerar_relatorio_vendas_dia)

        self.tela_principal = CriarTelaPrincipal()
        self.tela_principal.botao_adicionar_venda.clicked.connect(self.adicionar_venda)
        self.tela_principal.action_cadastrar_usuario.triggered.connect(self.tela_cadastrar_usuario.mostrar_tela)
        self.tela_principal.action_alterar_usuario.triggered.connect(self.tela_alterar_usuario.mostrar_tela)
        self.tela_principal.action_excluir_usuario.triggered.connect(self.tela_excluir_usuario.mostrar_tela)
        self.tela_principal.action_cadastrar_produto.triggered.connect(self.tela_cadastrar_produto.mostrar_tela)
        self.tela_principal.action_alterar_produto.triggered.connect(self.tela_alterar_produto.mostrar_tela)
        self.tela_principal.action_excluir_produto.triggered.connect(self.tela_excluir_produto.mostrar_tela)
        self.tela_principal.action_relatorio_vendas_total.triggered.connect(self.gerar_relatorio_vendas_total)
        self.tela_principal.action_relatorio_vendas_dia.triggered.\
            connect(self.tela_selecionar_data_relatorio_vendas.mostrar_tela)

    # __init__

    def iniciar(self) -> None:
        """
        Função que mostra a Tela de Login
        :return: None
        """
        self.tela_login.mostrar_tela()
    # iniciar

    def login(self) -> None:
        """
        Função que valida os dados da Tela de Login
        :return: None
        """
        matricula = valida_matricula(self.tela_login.texto_matricula.text())
        if matricula == -1:
            QMessageBox.critical(self.tela_alterar_usuario, 'Erro',
                                 f"<font face={self.fonte} size={self.tamanho}>"
                                 f"Matrícula inválida</font>")
        elif len(self.tela_login.texto_senha.text()) <= 0:
            QMessageBox.critical(self.tela_alterar_usuario,
                                 'Erro', f"<font face={self.fonte} size={self.tamanho}>"
                                         f"Senha inválida</font>")
        else:
            ret = verificar_dados_usuario(matricula, self.tela_login.texto_senha.text())
            if ret == -1:
                QMessageBox.critical(self.tela_login, 'Erro',
                                     f"<font face={self.fonte} size={self.tamanho}>"
                                     f"Matrícula não encontrada</font>")
            elif ret == 0:
                QMessageBox.critical(self.tela_login, 'Erro',
                                     f"<font face={self.fonte} size={self.tamanho}>"
                                     f"Senha incorreta</font>")
            elif ret == 1:
                cargo = cargo_usuario(matricula)
                self.tela_principal.texto_matricula.setText(str(matricula))
                self.tela_principal.texto_data.setText(data_atual_banco())
                self.tela_principal.texto_cargo.setText(converte_codigo_cargo_para_nome(cargo))
                self.tela_login.hide()
                self.atualizar_tabela_produtos()
                self.tela_principal.mostrar_tela(cargo)
    # login

    def abrir_tela_cadastrar_usuario(self) -> None:
        """
        Função que mostra a Tela Cadastrar Usuários
        :return: None
        """
        self.tela_cadastrar_usuario.mostrar_tela()
        self.tela_login.hide()
    # abrir_tela_cadastrar_usuario

    def cadastrar_usuario(self) -> None:
        """
        Função que valida os dados da Tela Cadastrar Usuários
        :return: None
        """
        if len(self.tela_cadastrar_usuario.texto_usuario.text()) < 2:
            QMessageBox.critical(self.tela_cadastrar_usuario, 'Erro',
                                 f"<font face={self.fonte} size={self.tamanho}>"
                                 f"Usuário inválido: O nome do usuário é muito pequeno</font>")
        elif len(self.tela_cadastrar_usuario.texto_email.text()) < 5 or \
                '@' not in self.tela_cadastrar_usuario.texto_email.text():
            QMessageBox.critical(self.tela_cadastrar_usuario, 'Erro',
                                 f"<font face={self.fonte} size={self.tamanho}>"
                                 f"Email inválido</font>")
        elif len(self.tela_cadastrar_usuario.texto_senha_1.text()) < 4:
            QMessageBox.critical(self.tela_cadastrar_usuario, 'Erro',
                                 f"<font face={self.fonte} size={self.tamanho}>"
                                 f"Senha inválida: A senha deve ter pelo menos 4 caracteres</font>")
        elif self.tela_cadastrar_usuario.texto_senha_1.text() != self.tela_cadastrar_usuario.texto_senha_2.text():
            QMessageBox.critical(self.tela_cadastrar_usuario, 'Erro',
                                 f"<font face={self.fonte} size={self.tamanho}>"
                                 f"Senha inválida: As senhas digitadas são diferentes</font>")
        elif not (self.tela_cadastrar_usuario.radio_button_gerente.isChecked() or
                  self.tela_cadastrar_usuario.radio_button_vendedor.isChecked() or
                  self.tela_cadastrar_usuario.radio_button_entregador.isChecked()):
            QMessageBox.critical(self.tela_cadastrar_usuario, 'Erro',
                                 f"<font face={self.fonte} size={self.tamanho}>"
                                 f"Cargo inválido: Selecione o cargo deste usuário</font>")
        else:
            nome = self.tela_cadastrar_usuario.texto_usuario.text()
            email = self.tela_cadastrar_usuario.texto_email.text()
            senha = self.tela_cadastrar_usuario.texto_senha_1.text()
            cargo = retorna_numero_cargo_selecionado(self.tela_cadastrar_usuario)
            status = inserir_usuario_banco(nome, email, senha, cargo)
            if status == -1:
                QMessageBox.critical(self.tela_cadastrar_usuario, 'Erro',
                                     f"<font face={self.fonte} size={self.tamanho}>"
                                     f"Este usuário já está cadastrado"
                                     f"\nNúmero de matrícula: {num_matricula_usuario(nome)}</font>")
            elif status == 0:
                QMessageBox.critical(self.tela_cadastrar_usuario, 'Erro',
                                     f"<font face={self.fonte} size={self.tamanho}>"
                                     f"Erro ao adicionar o usuário: {nome}</font>")
            else:
                opcao = QMessageBox.information(self.tela_cadastrar_usuario, 'Sucesso',
                                                f"<font face={self.fonte} size={self.tamanho}>"
                                                f"O usuário {nome} foi adicionado com sucesso."
                                                f"Número de matrícula: {num_matricula_usuario(nome)}</font>")
                if opcao == QMessageBox.StandardButton.Ok:
                    self.tela_cadastrar_usuario.close()
                    if not self.tela_principal.isVisible():
                        self.iniciar()
    # criar_conta

    def cadastrar_produto(self) -> None:
        """
        Função que valida os dados da Tela Cadastrar Produtos
        :return: None
        """
        if len(self.tela_cadastrar_produto.texto_descricao.text()) < 1:
            QMessageBox.critical(self.tela_cadastrar_produto, 'Erro',
                                 f"<font face={self.fonte} size={self.tamanho}>"
                                 f"Insira a descrição do produto</font>")
        elif len(self.tela_cadastrar_produto.texto_marca.text()) < 1:
            QMessageBox.critical(self.tela_cadastrar_produto, 'Erro',
                                 f"<font face={self.fonte} size={self.tamanho}>"
                                 f"Insira a marca do produto</font>")
        elif len(self.tela_cadastrar_produto.texto_fabricante.text()) < 1:
            QMessageBox.critical(self.tela_cadastrar_produto, 'Erro',
                                 f"<font face={self.fonte} size={self.tamanho}>"
                                 f"Insira o fabricante do produto</font>")
        elif self.tela_cadastrar_produto.spin_box_quantidade.value() <= 0:
            QMessageBox.critical(self.tela_cadastrar_produto, 'Erro',
                                 f"<font face={self.fonte} size={self.tamanho}>"
                                 f"Insira uma quantidade de produto válida</font>")
        elif self.tela_cadastrar_produto.double_spin_box_preco_compra.value() <= 0:
            QMessageBox.critical(self.tela_cadastrar_produto, 'Erro',
                                 f"<font face={self.fonte} size={self.tamanho}>"
                                 f"Insira o preço de compra</font>")
        else:
            descricao = self.tela_cadastrar_produto.texto_descricao.text()
            marca = self.tela_cadastrar_produto.texto_marca.text()
            fabricante = self.tela_cadastrar_produto.texto_fabricante.text()
            quantidade = self.tela_cadastrar_produto.spin_box_quantidade.value()
            preco_compra = self.tela_cadastrar_produto.double_spin_box_preco_compra.value()
            opcao = QMessageBox.question(self.tela_cadastrar_produto, 'Confirmar',
                                         f"<font face={self.fonte} size={self.tamanho}>"
                                         f"Deseja cadastrar o produto {descricao}?</font>",
                                         QMessageBox.Yes | QMessageBox.No)
            if opcao == QMessageBox.Yes:
                status = inserir_produto_banco(descricao, marca, fabricante, quantidade, preco_compra)
                if status == -1:
                    QMessageBox.critical(self.tela_cadastrar_produto, 'Erro',
                                         f"<font face={self.fonte} size={self.tamanho}>"
                                         f"Este produto já está cadastrado</font>")
                elif status == 0:
                    QMessageBox.critical(self.tela_cadastrar_produto, 'Erro',
                                         f"<font face={self.fonte} size={self.tamanho}>"
                                         f"Erro ao cadastrar produto</font>")
                else:
                    QMessageBox.information(self.tela_cadastrar_produto, 'Sucesso',
                                            f"<font face={self.fonte} size={self.tamanho}>"
                                            f"O produto {descricao} foi cadastrado com sucesso</font>")
                    self.atualizar_tabela_produtos()
                self.tela_cadastrar_produto.close()
    # cadastrar_produto

    def alterar_usuario(self) -> None:
        """
        Função que valida os dados da Tela Alterar Usuários
        :return: None
        """
        matricula = valida_matricula(self.tela_alterar_usuario.texto_matricula.text())
        if matricula == -1:
            QMessageBox.critical(self.tela_alterar_usuario, 'Erro',
                                 f"<font face={self.fonte} size={self.tamanho}>"
                                 f"Matrícula inválida</font>")
        elif not (self.tela_alterar_usuario.radio_button_gerente.isChecked() or
                  self.tela_alterar_usuario.radio_button_vendedor.isChecked() or
                  self.tela_alterar_usuario.radio_button_entregador.isChecked()):
            QMessageBox.critical(self.tela_alterar_usuario, 'Erro',
                                 f"<font face={self.fonte} size={self.tamanho}>"
                                 f"Cargo inválido: Selecione o novo cargo deste usuário</font>")
        else:
            nome = nome_usuario(matricula)
            if verificar_usuario_existe(nome):
                QMessageBox.critical(self.tela_alterar_usuario, 'Erro',
                                     f"<font face={self.fonte} size={self.tamanho}>"
                                     f"Este usuário não existe</font>")
                return
            if matricula == int(self.tela_principal.texto_matricula.text()):
                QMessageBox.critical(self.tela_alterar_usuario, 'Erro',
                                     f"<font face={self.fonte} size={self.tamanho}>"
                                     f"Você não pode alterar seu própio cargo</font>")
                return
            cargo_atual = cargo_usuario(matricula)
            novo_cargo = retorna_numero_cargo_selecionado(self.tela_alterar_usuario)
            if novo_cargo == cargo_atual:
                QMessageBox.critical(self.tela_alterar_usuario, 'Erro',
                                     f"<font face={self.fonte} size={self.tamanho}>"
                                     f"Este já é o cargo atual deste funcionário</font>")
                return
            nome_cargo = converte_codigo_cargo_para_nome(novo_cargo)
            opcao = QMessageBox.question(self.tela_alterar_usuario, 'Confirmar',
                                         f"<font face={self.fonte} size={self.tamanho}>"
                                         f"Deseja alterar o cargo de {nome} para {nome_cargo.lower()}?</font>",
                                         QMessageBox.Yes | QMessageBox.No)
            if opcao == QMessageBox.Yes:
                if alterar_cargo_banco(matricula, novo_cargo):
                    QMessageBox.information(self.tela_alterar_usuario, 'Sucesso',
                                            f"<font face={self.fonte} size={self.tamanho}>"
                                            f"O cargo de {nome} foi alterado com sucesso</font>")
                else:
                    QMessageBox.critical(self.tela_alterar_usuario, 'Erro',
                                         f"<font face={self.fonte} size={self.tamanho}>"
                                         f"Não foi possível alterar o cargo de {nome}</font>")
            self.tela_alterar_usuario.hide()
    # alterar_dados_usuario

    def excluir_usuario(self) -> None:
        """
        Função que valida os dados da Tela Excluir Usuário
        :return: None
        """
        matricula = valida_matricula(self.tela_excluir_usuario.texto_matricula.text())
        if matricula == -1:
            QMessageBox.critical(self.tela_excluir_usuario, 'Erro',
                                 f"<font face={self.fonte} size={self.tamanho}>"
                                 f"Matrícula inválida</font>")
            return
        nome = nome_usuario(matricula)
        if verificar_usuario_existe(nome):
            QMessageBox.critical(self.tela_excluir_usuario, 'Erro',
                                 f"<font face={self.fonte} size={self.tamanho}>"
                                 f"Este usuário não existe</font>")
        else:
            nome = nome_usuario(matricula)
            opcao = QMessageBox.question(self.tela_excluir_usuario, 'Confirmar',
                                         f"<font face={self.fonte} size={self.tamanho}>"
                                         f"Deseja excluir o usuário {nome}?</font>",
                                         QMessageBox.Yes | QMessageBox.No)
            if opcao == QMessageBox.Yes:
                if excluir_usuario_banco(matricula):
                    QMessageBox.information(self.tela_excluir_usuario, 'Sucesso',
                                            f"<font face={self.fonte} size={self.tamanho}>"
                                            f"O usuário {nome} foi excluído com sucesso</font>")
                else:
                    QMessageBox.critical(self.tela_excluir_usuario, 'Erro',
                                         f"<font face={self.fonte} size={self.tamanho}>"
                                         f"Erro ao excluir usuário {nome}</font>")
            self.tela_excluir_usuario.close()
    # excluir_usuario

    def atualizar_tabela_produtos(self) -> None:
        """
        Função que atualiza a tabela de produtos na Tela Principal
        :return: Nenhum
        """
        quantidade_produtos = quantidade_produtos_cadastrados()
        if quantidade_produtos == -1:
            return
        self.tela_principal.tabela.setRowCount(quantidade_produtos)
        produto_maior_id = maior_id_produto()
        num_linha = 0
        num_produto = 1
        while num_produto <= produto_maior_id:
            tupla_produto = busca_produto_por_id(num_produto)
            num_produto += 1
            if tupla_produto == ():
                continue
            self.formata_colunas_tabela_produtos(tupla_produto)
            for num_coluna in range(7):
                self.tela_principal.tabela.setItem(num_linha, num_coluna,
                                                   QTableWidgetItem(str(tupla_produto[num_coluna])))
                # todo: .setFlags(PySide2.QtCore.Qt.ItemIsEnabled)
            num_linha += 1
        self.tela_principal.tabela.setColumnWidth(1, self.tela_principal.maior_coluna_1 * 10)
        self.tela_principal.tabela.setColumnWidth(2, self.tela_principal.maior_coluna_2 * 12)
        self.tela_principal.tabela.setColumnWidth(3, self.tela_principal.maior_coluna_3 * 10)
    # atualizar_tabela_produtos

    def formata_colunas_tabela_produtos(self, tupla_produto: tuple) -> None:
        """
        Função que compara e salva a maior string de cada colua da tabela para auxiliar na sua formatação
        :param tupla_produto: tupla contendo os dados dos produtos
        :return: Nenhum
        """
        if len(tupla_produto[1]) > self.tela_principal.maior_coluna_1:
            self.tela_principal.maior_coluna_1 = len(tupla_produto[1])
        if len(tupla_produto[2]) > self.tela_principal.maior_coluna_2:
            self.tela_principal.maior_coluna_2 = len(tupla_produto[2])
        if len(tupla_produto[3]) > self.tela_principal.maior_coluna_3:
            self.tela_principal.maior_coluna_3 = len(tupla_produto[3])
    # formata_colunas_tabela_produtos

    def excluir_produto(self) -> None:
        """
        Função que valida os dados da Tela Excluir Produtos
        :return: Nenhum
        """
        id_produto_str = self.tela_excluir_produto.texto_id_produto.text()
        id_produto_int = valida_id_produto(id_produto_str)
        if id_produto_int == -1:
            QMessageBox.critical(self.tela_excluir_produto, 'Erro',
                                 f"<font face={self.fonte} size={self.tamanho}>"
                                 f"ID do produto inválido</font>")
        else:
            descricao = descricao_produto(id_produto_int)
            if descricao == '':
                QMessageBox.critical(self.tela_excluir_produto, 'Erro',
                                     f"<font face={self.fonte} size={self.tamanho}>"
                                     f"O produto com ID: {id_produto_int} não foi encontrado</font>")
            else:
                opcao = QMessageBox.question(self.tela_excluir_usuario, 'Confirmar',
                                             f"<font face={self.fonte} size={self.tamanho}>"
                                             f"Deseja excluir o produto {descricao}?</font>",
                                             QMessageBox.Yes | QMessageBox.No)
                if opcao == QMessageBox.Yes:
                    if excluir_produto_banco(id_produto_int):
                        QMessageBox.information(self.tela_excluir_usuario, 'Sucesso',
                                                f"<font face={self.fonte} size={self.tamanho}>"
                                                f"O produto {descricao} foi excluído com sucesso</font>")
                        self.atualizar_tabela_produtos()
                    else:
                        QMessageBox.critical(self.tela_excluir_usuario, 'Erro',
                                             f"<font face={self.fonte} size={self.tamanho}>"
                                             f"Erro ao excluir produto {descricao}</font>")
                self.tela_excluir_produto.close()
    # excluir_produto

    def alterar_produto(self):
        """
        Função que valida os dados da Tela Alterar Produtos
        :return:
        """
        id_produto_str = self.tela_alterar_produto.texto_id_produto.text()
        id_produto_int = valida_id_produto(id_produto_str)
        if id_produto_int == -1:
            QMessageBox.critical(self.tela_alterar_produto, 'Erro',
                                 f"<font face={self.fonte} size={self.tamanho}>"
                                 f"ID do produto inválido</font>")
        else:
            quantidade = self.tela_alterar_produto.spin_box_quantidade.value()
            if quantidade <= 0:
                QMessageBox.critical(self.tela_alterar_produto, 'Erro',
                                     f"<font face={self.fonte} size={self.tamanho}>"
                                     f"Quantidade do produto inválida</font>")
            else:
                descricao = descricao_produto(id_produto_int)
                if descricao == '':
                    QMessageBox.critical(self.tela_alterar_produto, 'Erro',
                                         f"<font face={self.fonte} size={self.tamanho}>"
                                         f"O produto com ID: {id_produto_int} não foi encontrado</font>")
                else:
                    opcao = QMessageBox.question(self.tela_alterar_produto, 'Confirmar',
                                                 f"<font face={self.fonte} size={self.tamanho}>"
                                                 f"Deseja alterar a quantidade do produto {descricao}?</font>",
                                                 QMessageBox.Yes | QMessageBox.No)
                    if opcao == QMessageBox.Yes:
                        if alterar_produto_banco(id_produto_int, quantidade):
                            QMessageBox.information(self.tela_alterar_produto, 'Sucesso',
                                                    f"<font face={self.fonte} size={self.tamanho}>"
                                                    f"O produto {descricao} foi alterado com sucesso</font>")
                            self.atualizar_tabela_produtos()
                        else:
                            QMessageBox.critical(self.tela_alterar_produto, 'Erro',
                                                 f"<font face={self.fonte} size={self.tamanho}>"
                                                 f"Erro ao alterar o produto {descricao}</font>")
                    self.tela_alterar_produto.close()
    # alterar_produto

    def adicionar_venda(self) -> None:
        """
        Função que valida os dados de venda da Tela Principal
        :return: Nenhum
        """
        id_produto_str = self.tela_principal.texto_codigo_produto.text()
        id_produto_int = valida_id_produto(id_produto_str)
        if id_produto_int == -1:
            QMessageBox.critical(self.tela_principal, 'Erro',
                                 f"<font face={self.fonte} size={self.tamanho}>"
                                 f"ID do produto inválido</font>")
        else:
            quantidade_venda = self.tela_principal.spin_box_quantidade.value()
            if quantidade_venda <= 0:
                QMessageBox.critical(self.tela_principal, 'Erro',
                                     f"<font face={self.fonte} size={self.tamanho}>"
                                     f"Quantidade do produto inválida</font>")
            else:
                preco_venda = self.tela_principal.double_spin_box_preco_venda.value()
                if preco_venda <= 0:
                    QMessageBox.critical(self.tela_principal, 'Erro',
                                         f"<font face={self.fonte} size={self.tamanho}>"
                                         f"Preço de venda do produto inválido</font>")
                else:
                    descricao = descricao_produto(id_produto_int)
                    if descricao == '':
                        QMessageBox.critical(self.tela_principal, 'Erro',
                                             f"<font face={self.fonte} size={self.tamanho}>"
                                             f"O produto com ID: {id_produto_int} não foi encontrado"
                                             f"</font>")
                    else:
                        quantidade_estoque = quantidade_produto(id_produto_int)
                        print(quantidade_estoque)
                        if quantidade_venda > quantidade_estoque:
                            QMessageBox.critical(self.tela_principal, 'Erro',
                                                 f"<font face={self.fonte} size={self.tamanho}>"
                                                 f"O estoque não possui a quantidade de produto suficiente"
                                                 f"para esta venda</font>")
                        else:
                            if not alterar_produto_banco(id_produto_int, (quantidade_estoque - quantidade_venda)):
                                QMessageBox.critical(self.tela_principal, 'Erro',
                                                     f"<font face={self.fonte} size={self.tamanho}>"
                                                     f"Erro ao adicionar venda</font>")
                            else:
                                opcao = QMessageBox.question(self.tela_principal, 'Confirmar',
                                                             f"<font face={self.fonte} size={self.tamanho}>"
                                                             f"Deseja adiconar esta venda? "
                                                             f"Produto: {descricao}. "
                                                             f"Quantidade: {quantidade_venda}. "
                                                             f"Preço de venda: {preco_venda}</font>",
                                                             QMessageBox.Yes | QMessageBox.No)
                                if opcao == QMessageBox.Yes:
                                    matricula = self.tela_principal.texto_matricula.text()
                                    if adiciona_venda_banco(id_produto_int, quantidade_venda,
                                                            preco_venda, int(matricula)):
                                        QMessageBox.information(self.tela_principal, 'Sucesso',
                                                                f"<font face={self.fonte} size={self.tamanho}>"
                                                                f"A venda do produto {descricao} foi adicionada "
                                                                f"com sucesso</font>")
                                        self.atualizar_tabela_produtos()
                                    else:
                                        QMessageBox.critical(self.tela_principal, 'Erro',
                                                             f"<font face={self.fonte} size={self.tamanho}>"
                                                             f"Erro ao adicionar a venda do produto {descricao}"
                                                             f"</font>")
    # adicionar_venda

    def gerar_relatorio_vendas_total(self) -> None:
        """
        Função que gera o relatório total de vendas
        :return: Nenhum
        """
        opcao = QMessageBox.question(self.tela_principal, 'Confirmar',
                                     f"<font face={self.fonte} size={self.tamanho}>"
                                     f"Deseja gerar relatório total de vendas?",
                                     QMessageBox.Yes | QMessageBox.No)
        if opcao == QMessageBox.Yes:
            data = data_atual_banco()
            lista_vendas = busca_dados_vendas('')
            if not lista_vendas:
                QMessageBox.critical(self.tela_principal, 'Erro',
                                     f"<font face={self.fonte} size={self.tamanho}>"
                                     f"Erro ao buscar dados das vendas</font>")
                return
            if gera_relatorio_csv_vendas(lista_vendas, data):
                QMessageBox.information(self.tela_principal, 'Sucesso',
                                        f"<font face={self.fonte} size={self.tamanho}>"
                                        f"Relatório gerado com sucesso</font>")
            else:
                QMessageBox.critical(self.tela_principal, 'Erro',
                                     f"<font face={self.fonte} size={self.tamanho}>"
                                     f"Erro ao gerar relatório de vendas</font>")
    # gerar_relatorio_vendas_total

    def gerar_relatorio_vendas_dia(self) -> None:
        """
        Função que valida os dados da Tela de Seleção de Data para gerar Relatório de Vendas
        :return: Nenhum
        """
        data_selecionada = str(self.tela_selecionar_data_relatorio_vendas.calendario.selectedDate())
        data_selecionada = data_selecionada.split('(')[1]
        data_selecionada = data_selecionada.split(')')[0]
        data_selecionada = data_selecionada.split(', ')
        dia = int(data_selecionada[2])
        mes = int(data_selecionada[1])
        ano = int(data_selecionada[0])
        if valida_data(dia, mes, ano):
            opcao = QMessageBox.question(self.tela_selecionar_data_relatorio_vendas, 'Confirmar',
                                         f"<font face={self.fonte} size={self.tamanho}>"
                                         f"Deseja gerar relatório de vendas do dia "
                                         f"{dia}/{mes}/{ano} ?</font>",
                                         QMessageBox.Yes | QMessageBox.No)
            if opcao == QMessageBox.Yes:
                print('Gerar relatorio')
        else:
            QMessageBox.critical(self.tela_selecionar_data_relatorio_vendas, 'Erro',
                                 f"<font face={self.fonte} size={self.tamanho}>"
                                 f"A data escolhida deve ser menor ou igual a atual"
                                 f"</font>")
    # gerar_relatorio_vendas_dia
