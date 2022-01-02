from csv import writer
import os


def gera_relatorio_csv_vendas(lista_vendas: list[tuple], data_atual: str) -> bool:
    """
    Função que gera o relatório de vendas em um arquivo csv
    :param lista_vendas: lista condendo os dados de todas as vendas
    :param data_atual: data atual do sistema para nomear o arquivo
    :return: True - se o relatório for gerado com sucesso
             False - se ocorrer um erro ao gerar o relatório
    """
    data_atual = data_atual.replace('/', '_')
    print(lista_vendas)
    os.makedirs('.\\Relatorios\\Relatorios_vendas', exist_ok=True)
    with open(f'.\\Relatorios\\Relatorios_vendas\\relatorio_vendas_total_{data_atual}.csv', 'w') as arquivo:
        escritor = writer(arquivo, delimiter=';')
        escritor.writerow(['Código', 'Descrição', 'Quantidade', 'Preço compra', 'Preço venda', 'Lucro líquido',
                          'Lucro percentual', 'Data', 'Funcionário'])
        for venda in lista_vendas:
            print(venda)
        return True
    return False
# gera_relatorio_csv_vendas
