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
