from csv import writer
from collections import namedtuple
import os


def gera_relatorio_csv_vendas(lista_vendas: list[namedtuple], data_atual: str) -> bool:
    """
    Função que gera o relatório de vendas em um arquivo csv
    :param lista_vendas: lista condendo os dados de todas as vendas
    :param data_atual: data atual do sistema para nomear o arquivo
    :return: True - se o relatório for gerado com sucesso
             False - se ocorrer um erro ao gerar o relatório
    """
    quantidade_total = preco_compra_total = preco_venda_total = lucro_total = 0
    data_atual = data_atual.replace('/', '_')
    os.makedirs('.\\Relatorios\\Relatorios_vendas', exist_ok=True)
    try:
        with open(f'.\\Relatorios\\Relatorios_vendas\\relatorio_vendas_total_{data_atual}.csv', 'w',
                  newline='') as arquivo:
            escritor = writer(arquivo, delimiter=';')
            escritor.writerow(['Código', 'Descrição', 'Quantidade', 'Preço compra unitário', 'Preço venda unitário',
                               'Lucro líquido', 'Lucro percentual', 'Data', 'Funcionário'])
            for venda in lista_vendas:
                # TODO: trocar . por , nos dados float
                escritor.writerow([venda.codigo, venda.descricao, venda.quantidade, venda.preco_compra,
                                   venda.preco_venda, venda.lucro_liquido, f'{venda.lucro_percentual}%',
                                   venda.data, venda.funcionario])

                quantidade_total += venda.quantidade
                lucro_total += venda.lucro_liquido
                preco_compra_total += venda.preco_compra * venda.quantidade
                preco_venda_total += venda.preco_venda * venda.quantidade

            escritor.writerow(['Total', '-', quantidade_total, preco_compra_total, preco_venda_total, lucro_total,
                              '-', '-', '-'])
            return True
        return False

    except PermissionError:
        print('PermissionError')
        return False
# gera_relatorio_csv_vendas
