# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_relatorio_estoque_quantidadeEsApIm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_tela_relatorio_estoque_quantidade(object):
    def setupUi(self, tela_relatorio_estoque_quantidade):
        if not tela_relatorio_estoque_quantidade.objectName():
            tela_relatorio_estoque_quantidade.setObjectName(u"tela_relatorio_estoque_quantidade")
        tela_relatorio_estoque_quantidade.resize(327, 166)
        self.botao_gerar_relatorio_estoque_quantidade = QPushButton(tela_relatorio_estoque_quantidade)
        self.botao_gerar_relatorio_estoque_quantidade.setObjectName(u"botao_gerar_relatorio_estoque_quantidade")
        self.botao_gerar_relatorio_estoque_quantidade.setGeometry(QRect(80, 110, 151, 41))
        font = QFont()
        font.setPointSize(12)
        self.botao_gerar_relatorio_estoque_quantidade.setFont(font)
        self.botao_gerar_relatorio_estoque_quantidade.setText(u"Gerar Relat\u00f3rio")
        self.label_tipo = QLabel(tela_relatorio_estoque_quantidade)
        self.label_tipo.setObjectName(u"label_tipo")
        self.label_tipo.setGeometry(QRect(10, 71, 131, 21))
        self.label_tipo.setFont(font)
        self.label_tipo.setText(u"Tipo:")
        self.label_codigo_produto = QLabel(tela_relatorio_estoque_quantidade)
        self.label_codigo_produto.setObjectName(u"label_codigo_produto")
        self.label_codigo_produto.setGeometry(QRect(10, 11, 121, 21))
        self.label_codigo_produto.setFont(font)
        self.label_codigo_produto.setText(u"C\u00f3digo Produto:")
        self.texto_matricula = QLineEdit(tela_relatorio_estoque_quantidade)
        self.texto_matricula.setObjectName(u"texto_matricula")
        self.texto_matricula.setGeometry(QRect(140, 10, 171, 21))
        self.texto_matricula.setFont(font)
        self.texto_matricula.setText(u"")
        self.texto_matricula.setMaxLength(20)
        self.combo_box_tipo = QComboBox(tela_relatorio_estoque_quantidade)
        self.combo_box_tipo.setObjectName(u"combo_box_tipo")
        self.combo_box_tipo.setGeometry(QRect(140, 70, 81, 22))
        self.label_quantidade = QLabel(tela_relatorio_estoque_quantidade)
        self.label_quantidade.setObjectName(u"label_quantidade")
        self.label_quantidade.setGeometry(QRect(10, 40, 121, 21))
        self.label_quantidade.setFont(font)
        self.label_quantidade.setText(u"Quantidade:")
        self.spin_box_quantidade = QSpinBox(tela_relatorio_estoque_quantidade)
        self.spin_box_quantidade.setObjectName(u"spin_box_quantidade")
        self.spin_box_quantidade.setGeometry(QRect(140, 40, 81, 21))
        self.spin_box_quantidade.setFont(font)

        self.retranslateUi(tela_relatorio_estoque_quantidade)

        QMetaObject.connectSlotsByName(tela_relatorio_estoque_quantidade)
    # setupUi

    def retranslateUi(self, tela_relatorio_estoque_quantidade):
        tela_relatorio_estoque_quantidade.setWindowTitle(QCoreApplication.translate("tela_relatorio_estoque_quantidade", u"Relat\u00f3rio Quantidade", None))
    # retranslateUi

