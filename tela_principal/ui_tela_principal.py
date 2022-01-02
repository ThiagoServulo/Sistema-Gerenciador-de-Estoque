from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys


class Ui_tela_principal(object):

    maior_coluna_1 = 0
    maior_coluna_2 = 0
    maior_coluna_3 = 0

    def __init__(self):
        self.action_cadastrar_usuario = QAction()
        self.action_alterar_usuario = QAction()
        self.action_excluir_usuario = QAction()
        self.action_cadastrar_produto = QAction()
        self.action_alterar_produto = QAction()
        self.action_excluir_produto = QAction()
        self.action_relatorio_vendas_total = QAction()
        self.action_relatorio_vendas_dia = QAction()
        self.action_relatorio_produtos_completo = QAction()
        self.action_relatorio_produtos_customizado = QAction()
        self.action_relatorio_produtos_quantidade = QAction()
        self.centralwidget = QWidget()
        self.gridLayout = QGridLayout()
        self.group_box_vendas = QGroupBox()
        self.gridLayout_2 = QGridLayout()
        self.botao_adicionar_venda = QPushButton()
        self.label_codigo_produto = QLabel()
        self.spin_box_quantidade = QSpinBox()
        self.label_preco_venda = QLabel()
        self.double_spin_box_preco_venda = QDoubleSpinBox()
        self.label_quantidade = QLabel()
        self.texto_codigo_produto = QLineEdit()
        self.gridLayout.addWidget()
        self.group_box_dados = QGroupBox()
        self.gridLayout_3 = QGridLayout()
        self.label_matricula = QLabel()
        self.texto_matricula = QLineEdit()
        self.label_data = QLabel()
        self.texto_data = QLineEdit()
        self.vertical_spacer = QSpacerItem()
        self.label_cargo = QLabel()
        self.texto_cargo = QLineEdit()
        self.horizontal_spacer = QSpacerItem()
        self.tabela = QTableWidget()
        self.menubar = QMenuBar()
        self.menu_usuarios = QMenu()
        self.menu_produtos = QMenu()
        self.menu_relatorios_vendas = QMenu()
        self.menu_relatorio_produtos = QMenu()
    # __init__

    def setupUi(self, tela_principal):
        icon = QIcon()
        icon.addFile(u"icones/icone_produto.png", QSize(), QIcon.Normal, QIcon.Off)

        font = QFont()
        font.setPointSize(12)

        tela_principal.resize(715, 600)
        tela_principal.setMinimumSize(715, 600)
        tela_principal.setWindowTitle(u"Gerenciador de Estoque")
        tela_principal.setWindowIcon(icon)

        self.action_cadastrar_usuario = QAction(tela_principal)
        self.action_cadastrar_usuario.setText("Cadastrar")
        self.action_cadastrar_usuario.setShortcut("F1")

        self.action_alterar_usuario = QAction(tela_principal)
        self.action_alterar_usuario.setText("Alterar")
        self.action_alterar_usuario.setShortcut("F2")

        self.action_excluir_usuario = QAction(tela_principal)
        self.action_excluir_usuario.setText("Excluir")
        self.action_excluir_usuario.setShortcut("F3")

        self.action_cadastrar_produto = QAction(tela_principal)
        self.action_cadastrar_produto.setText("Cadastrar")
        self.action_cadastrar_produto.setShortcut("F4")

        self.action_alterar_produto = QAction(tela_principal)
        self.action_alterar_produto.setText("Alterar")
        self.action_alterar_produto.setShortcut("F5")

        self.action_excluir_produto = QAction(tela_principal)
        self.action_excluir_produto.setText("Excluir")
        self.action_excluir_produto.setShortcut("F6")

        self.action_relatorio_vendas_total = QAction(tela_principal)
        self.action_relatorio_vendas_total.setText("Relatório Total")
        self.action_relatorio_vendas_total.setShortcut("F7")

        self.action_relatorio_vendas_dia = QAction(tela_principal)
        self.action_relatorio_vendas_dia.setText("Relatório Dia")
        self.action_relatorio_vendas_dia.setShortcut("F8")

        self.action_relatorio_produtos_completo = QAction(tela_principal)
        self.action_relatorio_produtos_completo.setText("Relatório Completo")
        # self.action_relatorio_produtos_completo.setShortcut("F6")

        self.action_relatorio_produtos_customizado = QAction(tela_principal)
        self.action_relatorio_produtos_customizado.setText("Relatório por Produto")
        # self.action_relatorio_produtos_customizado.setShortcut("F7")

        self.action_relatorio_produtos_quantidade = QAction(tela_principal)
        self.action_relatorio_produtos_quantidade.setText("Relatório por Quantidade")
        # self.action_relatorio_produtos_quantidade.setShortcut("F8")

        self.centralwidget = QWidget(tela_principal)
        self.gridLayout = QGridLayout(self.centralwidget)

        self.group_box_vendas = QGroupBox(self.centralwidget)
        self.group_box_vendas.setTitle("Vendas")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_box_vendas.sizePolicy().hasHeightForWidth())
        self.group_box_vendas.setSizePolicy(sizePolicy)
        self.group_box_vendas.setMaximumSize(QSize(400, 200))
        self.group_box_vendas.setFont(font)

        self.gridLayout_2 = QGridLayout(self.group_box_vendas)
        self.botao_adicionar_venda = QPushButton(self.group_box_vendas)
        self.botao_adicionar_venda.setText("Adicionar venda")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(60)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.botao_adicionar_venda.sizePolicy().hasHeightForWidth())
        self.botao_adicionar_venda.setSizePolicy(sizePolicy1)
        self.botao_adicionar_venda.setMinimumSize(QSize(200, 35))
        self.botao_adicionar_venda.setFont(font)

        self.gridLayout_2.addWidget(self.botao_adicionar_venda, 4, 1, 1, 1)

        self.label_codigo_produto = QLabel(self.group_box_vendas)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_codigo_produto.sizePolicy().hasHeightForWidth())
        self.label_codigo_produto.setSizePolicy(sizePolicy2)
        self.label_codigo_produto.setMaximumSize(QSize(300, 16777215))
        self.label_codigo_produto.setFont(font)
        self.label_codigo_produto.setText(u"Código do produto:")

        self.gridLayout_2.addWidget(self.label_codigo_produto, 0, 0, 1, 1)

        self.spin_box_quantidade = QSpinBox(self.group_box_vendas)
        sizePolicy2.setHeightForWidth(self.spin_box_quantidade.sizePolicy().hasHeightForWidth())
        self.spin_box_quantidade.setSizePolicy(sizePolicy2)
        self.spin_box_quantidade.setMaximumSize(QSize(200, 16777215))
        self.spin_box_quantidade.setFont(font)

        self.gridLayout_2.addWidget(self.spin_box_quantidade, 1, 1, 1, 1)

        self.label_preco_venda = QLabel(self.group_box_vendas)
        self.label_preco_venda.setText("Preço de venda:")
        sizePolicy2.setHeightForWidth(self.label_preco_venda.sizePolicy().hasHeightForWidth())
        self.label_preco_venda.setSizePolicy(sizePolicy2)
        self.label_preco_venda.setMaximumSize(QSize(300, 16777215))
        self.label_preco_venda.setFont(font)

        self.gridLayout_2.addWidget(self.label_preco_venda, 2, 0, 1, 1)

        self.double_spin_box_preco_venda = QDoubleSpinBox(self.group_box_vendas)
        sizePolicy2.setHeightForWidth(self.double_spin_box_preco_venda.sizePolicy().hasHeightForWidth())
        self.double_spin_box_preco_venda.setSizePolicy(sizePolicy2)
        self.double_spin_box_preco_venda.setMaximumSize(QSize(200, 16777215))
        self.double_spin_box_preco_venda.setFont(font)

        self.gridLayout_2.addWidget(self.double_spin_box_preco_venda, 2, 1, 1, 1)

        self.label_quantidade = QLabel(self.group_box_vendas)
        sizePolicy2.setHeightForWidth(self.label_quantidade.sizePolicy().hasHeightForWidth())
        self.label_quantidade.setSizePolicy(sizePolicy2)
        self.label_quantidade.setMaximumSize(QSize(300, 16777215))
        self.label_quantidade.setFont(font)
        self.label_quantidade.setText(u"Quantidade:")

        self.gridLayout_2.addWidget(self.label_quantidade, 1, 0, 1, 1)

        self.texto_codigo_produto = QLineEdit(self.group_box_vendas)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.texto_codigo_produto.sizePolicy().hasHeightForWidth())
        self.texto_codigo_produto.setSizePolicy(sizePolicy3)
        self.texto_codigo_produto.setMaximumSize(QSize(200, 16777215))
        self.texto_codigo_produto.setFont(font)

        self.gridLayout_2.addWidget(self.texto_codigo_produto, 0, 1, 1, 1)

        self.gridLayout.addWidget(self.group_box_vendas, 0, 0, 1, 1)

        self.group_box_dados = QGroupBox(self.centralwidget)
        self.group_box_dados.setTitle("Dados Gerais")
        sizePolicy.setHeightForWidth(self.group_box_dados.sizePolicy().hasHeightForWidth())
        self.group_box_dados.setSizePolicy(sizePolicy)
        self.group_box_dados.setMaximumSize(QSize(400, 200))
        self.group_box_dados.setFont(font)
        self.gridLayout_3 = QGridLayout(self.group_box_dados)
        self.label_matricula = QLabel(self.group_box_dados)
        sizePolicy2.setHeightForWidth(self.label_matricula.sizePolicy().hasHeightForWidth())
        self.label_matricula.setSizePolicy(sizePolicy2)
        self.label_matricula.setMaximumSize(QSize(300, 16777215))
        self.label_matricula.setFont(font)
        self.label_matricula.setText(u"Matrícula usuário:")

        self.gridLayout_3.addWidget(self.label_matricula, 0, 1, 1, 1)

        self.texto_matricula = QLineEdit(self.group_box_dados)
        sizePolicy3.setHeightForWidth(self.texto_matricula.sizePolicy().hasHeightForWidth())
        self.texto_matricula.setSizePolicy(sizePolicy3)
        self.texto_matricula.setMaximumSize(QSize(200, 16777215))
        self.texto_matricula.setFont(font)
        self.texto_matricula.setInputMethodHints(Qt.ImhPreferUppercase)
        self.texto_matricula.setInputMask(u"")
        self.texto_matricula.setText(u"")
        self.texto_matricula.setReadOnly(True)

        self.gridLayout_3.addWidget(self.texto_matricula, 0, 2, 1, 1)

        self.label_data = QLabel(self.group_box_dados)
        self.label_data.setText("Data Atual:")
        self.label_data.setFont(font)

        self.gridLayout_3.addWidget(self.label_data, 2, 1, 1, 1)

        self.texto_data = QLineEdit(self.group_box_dados)
        sizePolicy3.setHeightForWidth(self.texto_data.sizePolicy().hasHeightForWidth())
        self.texto_data.setSizePolicy(sizePolicy3)
        self.texto_data.setMaximumSize(QSize(200, 16777215))
        self.texto_data.setFont(font)
        self.texto_data.setInputMask(u"")
        self.texto_data.setText(u"")
        self.texto_data.setReadOnly(True)

        self.gridLayout_3.addWidget(self.texto_data, 2, 2, 1, 1)
        self.vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_3.addItem(self.vertical_spacer, 3, 2, 1, 1)

        self.label_cargo = QLabel(self.group_box_dados)
        self.label_cargo.setText("Cargo:")
        self.gridLayout_3.addWidget(self.label_cargo, 1, 1, 1, 1)
        self.texto_cargo = QLineEdit(self.group_box_dados)
        self.texto_cargo.setInputMask(u"")
        self.texto_cargo.setText(u"")
        self.texto_cargo.setPlaceholderText(u"")
        self.texto_cargo.setReadOnly(True)

        self.gridLayout_3.addWidget(self.texto_cargo, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.group_box_dados, 0, 1, 1, 1)
        self.horizontal_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.horizontal_spacer, 0, 2, 1, 1)

        font_header = QFont()
        font_header.setPointSize(12)
        font_header.setBold(True)

        self.tabela = QTableWidget(self.centralwidget)
        self.tabela.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setText('Código')
        __qtablewidgetitem.setFont(font_header)
        self.tabela.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tabela.setColumnWidth(0, (len(__qtablewidgetitem.text()) * 20))
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setText('Descrição')
        __qtablewidgetitem1.setFont(font_header)
        self.maior_coluna_1 = (len(__qtablewidgetitem1.text()))
        self.tabela.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setText('Marca')
        __qtablewidgetitem2.setFont(font_header)
        self.maior_coluna_2 = (len(__qtablewidgetitem2.text()))
        self.tabela.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setText('Fabricante')
        __qtablewidgetitem3.setFont(font_header)
        self.maior_coluna_3 = (len(__qtablewidgetitem3.text()))
        self.tabela.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setText('Quantidade')
        __qtablewidgetitem4.setFont(font_header)
        self.tabela.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabela.setColumnWidth(4, (len(__qtablewidgetitem4.text()) * 12))
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setText('Preço de Compra')
        __qtablewidgetitem5.setFont(font_header)
        self.tabela.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tabela.setColumnWidth(5, (len(__qtablewidgetitem5.text()) * 10))
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setText('Data Última Atualização')
        __qtablewidgetitem6.setFont(font_header)
        self.tabela.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabela.setColumnWidth(6, (len(__qtablewidgetitem6.text()) * 10))
        self.tabela.setFont(font)
        self.gridLayout.addWidget(self.tabela, 1, 0, 1, 3)

        tela_principal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(tela_principal)
        self.menubar.setGeometry(QRect(0, 0, 715, 21))

        self.menu_usuarios = QMenu(self.menubar)
        self.menu_usuarios.setTitle("Usuários")
        self.menu_usuarios.addAction(self.action_cadastrar_usuario)
        self.menu_usuarios.addAction(self.action_alterar_usuario)
        self.menu_usuarios.addAction(self.action_excluir_usuario)
        self.menubar.addAction(self.menu_usuarios.menuAction())

        self.menu_produtos = QMenu(self.menubar)
        self.menu_produtos.setTitle("Produtos")
        self.menu_produtos.addAction(self.action_cadastrar_produto)
        self.menu_produtos.addAction(self.action_alterar_produto)
        self.menu_produtos.addAction(self.action_excluir_produto)
        self.menubar.addAction(self.menu_produtos.menuAction())

        self.menu_relatorios_vendas = QMenu(self.menubar)
        self.menu_relatorios_vendas.setTitle("Relatórios Vendas")
        self.menu_relatorios_vendas.addAction(self.action_relatorio_vendas_total)
        self.menu_relatorios_vendas.addAction(self.action_relatorio_vendas_dia)
        self.menubar.addAction(self.menu_relatorios_vendas.menuAction())

        self.menu_relatorio_produtos = QMenu(self.menubar)
        self.menu_relatorio_produtos.setTitle("Relatório Estoque")
        self.menu_relatorio_produtos.addAction(self.action_relatorio_produtos_completo)
        self.menu_relatorio_produtos.addAction(self.action_relatorio_produtos_customizado)
        self.menu_relatorio_produtos.addAction(self.action_relatorio_produtos_quantidade)
        self.menubar.addAction(self.menu_relatorio_produtos.menuAction())

        tela_principal.setMenuBar(self.menubar)
    # setupUi


class CriarTelaPrincipal(QMainWindow, Ui_tela_principal):
    def __init__(self):
        super(CriarTelaPrincipal, self).__init__()
        self.setupUi(self)
    # __init__

    def mostrar_tela(self, cargo_usuario: int):
        if cargo_usuario == 1:
            self.menu_usuarios.setEnabled(False)
            self.menu_relatorio_produtos.setEnabled(False)
            self.menu_relatorios_vendas.setEnabled(False)
        elif cargo_usuario == 2:
            self.menu_usuarios.setEnabled(False)
            self.menu_relatorio_produtos.setEnabled(True)
            self.menu_relatorios_vendas.setEnabled(True)
        else:
            self.menu_usuarios.setEnabled(True)
            self.menu_relatorio_produtos.setEnabled(True)
            self.menu_relatorios_vendas.setEnabled(True)
        self.show()
    # mostrar_tela


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CriarTelaPrincipal()
    window.mostrar_tela(3)
    sys.exit(app.exec_())
