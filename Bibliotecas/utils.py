from passlib.hash import pbkdf2_sha256 as cryp
from typing import Literal
import datetime


def converter_id_para_matricula(id_usuario: int) -> int:
    """
    Função que converte o id da tabela usuário na matrícula do usuário
    :param id_usuario: id do usuário a ser convertido
    :return: matrícula do usuário
    """
    return id_usuario + 5000
# converter_id_para_matricula


def converter_matricula_para_id(matricula: int) -> int:
    """
    Função que converte a matrícula do usuáriopara o id da tabela
    :param matricula: matrícula do usuário a ser convertida
    :return: id do usuário
    """
    return matricula - 5000
# converter_matricula_para_id


def valida_matricula(matricula_str: str) -> int:
    """
    Função que valida o número de matrícula
    :param matricula_str: número da matrícula no formato string
    :return: número da matrícula no formato inteiro. Se o número de matrícula for inválido será retornado -1
    """
    if len(matricula_str) < 1:
        return -1
    else:
        try:
            matricula_int = int(matricula_str)
        except ValueError:
            return -1
        else:
            return matricula_int
# valida_matricula


def criptografar_senha(senha: str) -> str:
    """
    Função que criptografa a senha
    :param senha: senha descriptografada
    :return: senha criptografada
    """
    return cryp.hash(senha, rounds=200000, salt_size=16)
# criptografar_senha


def verificar_senha(senha_login: str, senha_cadastrada: str) -> int:
    """
    Função que verifica se a senha informada é a mesma da cadastrada por aquele usuário
    :param senha_login: senha informada pela usuário
    :param senha_cadastrada: senha criptografada cadastrada no banco
    :return: 1 - se a senha de login for a mesma da cadastrada
             0 - se a senha de login for diferente da cadastrada
    """
    if cryp.verify(senha_login, senha_cadastrada):
        return 1
    else:
        return 0
# verificar_senha


def converte_codigo_cargo_para_nome(codigo_cargo: int) -> str:
    """
    Função que converte o código do cargo para o nome do cargo
    :param codigo_cargo: código do cargo a ser convertido
    :return: 'Entregador' - se o código do cargo for 1
              'Vendedor'  - se o código do cargo for 2
              'Gerente'   - se o código do cargo for 3
    """
    if codigo_cargo == 1:
        return 'Entregador'
    elif codigo_cargo == 2:
        return 'Vendedor'
    elif codigo_cargo == 3:
        return 'Gerente'
# converte_codigo_cargo_para_nome


def retorna_numero_cargo_selecionado(self) -> int:
    """
    Função que retorna o código do cargo a partir do radio button selecionado
    :param self: tela onde se localiza o radio button
    :return: 1 - se o cargo selecionado for 'Entregador'
             2 - se o cargo selecionado for 'Vendedor'
             3 - se o cargo selecionado for 'Gerente'
    """
    if self.radio_button_entregador.isChecked():
        return 1
    elif self.radio_button_vendedor.isChecked():
        return 2
    elif self.radio_button_gerente.isChecked():
        return 3
# retorna_numero_cargo_selecionado


def valida_id_produto(id_produto_str: str) -> int:
    """
    Função que valida o id do produto
    :param id_produto_str: id do produto no formato String
    :return: retorna o id do produto no formato int se ele for válido,
             caso contrário será retornado o valor -1
    """
    if len(id_produto_str) <= 0:
        return -1
    else:
        try:
            id_produt_int = int(id_produto_str)
        except ValueError:
            return -1
        else:
            return id_produt_int
# valida_id_produto


def valida_data(dia: int, mes: int, ano: int) -> bool:
    """
    Função que verifica se a data selecionada é válida, ou seja, se a data selecionada é menor ou igual a atual
    :param dia: dia selecionado
    :param mes: mês selecionado
    :param ano: ano selecionado
    :return: True - se a data selecionada for válida
             False - se a data selecionada for inválida
    """
    data_selecionada = datetime.date(day=dia, month=mes, year=ano)
    data_atual = datetime.date.today()
    delta = data_atual - data_selecionada
    if delta.days >= 0:
        return True
    else:
        return False
# valida_data


def converte_simbolo_tipo_para_string(simbolo: Literal['>', '<', '=']) -> str:
    """
    Função que converte um símbolo em uma string com seu significado
    :param simbolo: símbolo que será transcrito
    :return: string contendo o nome do símbolo informado
    """
    if simbolo == '>':
        tipo = 'maior'
    elif simbolo == '<':
        tipo = 'menor'
    else:
        tipo = 'igual'
    return tipo
# converte_simbolo_tipo_para_string
