from csv import writer
from typing import Literal
from collections import namedtuple
import os


def gera_relatorio_csv_vendas(tipo_relatorio: Literal[1, 2], nome_arquivo: str, lista_vendas: list[namedtuple]) -> bool:
    """
    Função que gera o relatório de vendas em um arquivo csv
    :param tipo_relatorio: tipo de relatório que será gerado
                           1 - relatório total
                           2 - relatório de uma data específica
    :param nome_arquivo: nome do arquivo de relatório de vendas que será gerado
    :param lista_vendas: lista condendo os dados de todas as vendas
    :return: True - se o relatório for gerado com sucesso
             False - se ocorrer um erro ao gerar o relatório
    """
    quantidade_total = preco_compra_total = preco_venda_total = lucro_total = 0
    if tipo_relatorio == 1:
        os.makedirs('.\\Relatorios\\Relatorios_vendas_total', exist_ok=True)
        path = f'.\\Relatorios\\Relatorios_vendas_total\\{nome_arquivo}.csv'
    else:
        os.makedirs('.\\Relatorios\\Relatorios_vendas_data', exist_ok=True)
        path = f'.\\Relatorios\\Relatorios_vendas_data\\{nome_arquivo}.csv'
    try:
        with open(path, 'w', newline='') as arquivo:
            escritor = writer(arquivo, delimiter=';')
            escritor.writerow(['Código', 'Descrição', 'Quantidade', 'Preço compra unitário', 'Preço venda unitário',
                               'Lucro líquido', 'Lucro percentual', 'Data', 'Funcionário'])

            for venda in lista_vendas:
                quantidade_total += venda.quantidade
                lucro_total += venda.lucro_liquido
                preco_compra_total += venda.preco_compra * venda.quantidade
                preco_venda_total += venda.preco_venda * venda.quantidade

                escritor.writerow([venda.codigo, venda.descricao, venda.quantidade,
                                   str(venda.preco_compra).replace('.', ','),
                                   str(venda.preco_venda).replace('.', ','),
                                   str(venda.lucro_liquido).replace('.', ','),
                                   f"{str(venda.lucro_percentual).replace('.', ',')}%",
                                   venda.data, venda.funcionario])

            escritor.writerow(['Total', '-', str(quantidade_total).replace('.', ','),
                               str(preco_compra_total).replace('.', ','),
                               str(preco_venda_total).replace('.', ','),
                               str(lucro_total).replace('.', ','),
                               '-', '-', '-'])
            return True
        return False

    except PermissionError:
        print('PermissionError')
        return False
# gera_relatorio_csv_vendas


def gera_relatorio_csv_produtos(tipo_relatorio: Literal[1, 3], nome_arquivo: str, lista_produtos: list[namedtuple]) -> bool:
    """
    Função que gera o relatório de estoque em um arquivo csv
    :param tipo_relatorio: tipo de relatório que será gerado
                           1 - relatório total
                           2 - relatório por produto
                           3 - relatório por quantidade
    :param nome_arquivo: nome do arquivo csv que será gerado
    :param lista_produtos: lista condendo os dados dos produtos em estoque
    :return: True - se o relatório for gerado com sucesso
             False - se ocorrer um erro ao gerar o relatório
    """
    quantidade_total = valor_estoque_total = 0
    if tipo_relatorio == 1:
        os.makedirs('.\\Relatorios\\Relatorios_estoque_completo', exist_ok=True)
        path = f'.\\Relatorios\\Relatorios_estoque_completo\\{nome_arquivo}.csv'
    elif tipo_relatorio == 3:
        os.makedirs('.\\Relatorios\\Relatorios_estoque_quantidade', exist_ok=True)
        path = f'.\\Relatorios\\Relatorios_estoque_quantidade\\{nome_arquivo}.csv'
    else:
        path = 0  # TODO: fazer o else
    try:
        with open(path, 'w', newline='') as arquivo:
            escritor = writer(arquivo, delimiter=';')
            escritor.writerow(['Código', 'Descrição', 'Marca', 'Fabricante', 'Quantidade',
                               'Preço Compra', 'Valor em Estoque', 'Data'])

            for produto in lista_produtos:
                quantidade_total += produto.quantidade
                valor_estoque_total += produto.valor_estoque
                escritor.writerow([produto.codigo, produto.descricao, produto.marca, produto.fabricante,
                                   produto.quantidade, str(produto.preco_compra).replace('.', ','),
                                   str(produto.valor_estoque).replace('.', ','), produto.data])

            escritor.writerow(['Total', '-', '-', '-', quantidade_total, '-',
                               str(valor_estoque_total).replace('.', ','), '-'])
            return True
        return False

    except PermissionError:
        print('PermissionError')
        return False
# gera_relatorio_csv_produtos
