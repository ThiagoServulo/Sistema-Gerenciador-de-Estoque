import sqlite3
import os
from Bibliotecas.utils import *


def conectar_servidor() -> sqlite3.Connection:
    """
    Função para conectar ao servidor de banco de dados
    :return: retorna a conexão ao banco de dados
    """
    if not os.path.exists('gerenciador_estoque.bd'):
        cria_tabela_tipos_cargos()

    conn = sqlite3.connect('gerenciador_estoque.bd')

    conn.execute("""CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        senha TEXT NOT NULL,
        cargo INTEGER NOT NULL);"""
                 )

    return conn
# conectar_servidor


def cria_tabela_tipos_cargos() -> None:
    """
    Função para criar e inicializar valores da tabela tipos_cargos
    :return: None
    """
    conn = sqlite3.connect('gerenciador_estoque.bd')

    conn.execute("""CREATE TABLE IF NOT EXISTS tipos_cargos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cargo TEXT NOT NULL);"""
                 )

    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO tipos_cargos (cargo) VALUES ('Entregador')")
    cursor.execute(f"INSERT INTO tipos_cargos (cargo) VALUES ('Vendedor')")
    cursor.execute(f"INSERT INTO tipos_cargos (cargo) VALUES ('Gerente')")
    conn.commit()

    desconectar_servidor(conn)
# cria_tabela_tipos_cargos


def executa_query(query: str) -> list:
    """
    Função que executa uma query de consulta no servidor de banco de dados
    :param query: query de busca que será executada
    :return: lista de parâmetros contendo os dados retonados da consulta
    """
    conn = conectar_servidor()
    cursor = conn.cursor()
    cursor.execute(query)
    dados = cursor.fetchall()
    desconectar_servidor(conn)
    return dados
# executa_query


def executa_comando(comando: str) -> int:
    """
    Função que executa um comando (insert, update, delete) no banco de dados
    :param comando: comando que será executada
    :return: valor inteiro que indica se o comando foi executado com sucesso
    """
    conn = conectar_servidor()
    cursor = conn.cursor()
    cursor.execute(comando)
    conn.commit()
    desconectar_servidor(conn)
    return cursor.rowcount
# executa_comando


def inserir_usuario_banco(nome: str, email: str, senha: str, cargo: int) -> int:
    """
    Função para cadastrar um novo usuário no banco de dados
    :param nome: nome informado pelo usuário para cadastro
    :param email: email informado pelo usuário para cadastro
    :param senha: senha informada pelo usuário para cadastro
    :param cargo: cargo informado pelo usuário para cadastro
    :return: Número de matrícula - se o usuário for cadastrado com sucesso
             0 - se ocorrer algum problema no cadastro
    """
    if not verificar_usuario_existe(nome):
        return 0

    senha_criptografada = criptografar_senha(senha)

    if executa_comando(f"""INSERT INTO usuarios (nome, email, senha, cargo) 
                           VALUES ('{nome}', '{email}', '{senha_criptografada}', {cargo})""") == 1:
        matricula = num_matricula_usuario(nome)
        return matricula
    else:
        return 0
# inserir_usuario


def excluir_usuario_banco(matricula: int) -> bool:
    """
    Função que exclui um usuário do banco a partir da sua matrícula
    :param matricula: matrícula do usuário que será excluído
    :return: True - se o usuário for excluído com sucesso
             False - se ocorrer algum erro durante a exclusão
    """
    id_usuario = converter_matricula_para_id(matricula)
    if executa_comando(f"""DELETE FROM usuarios WHERE id = {id_usuario}""") == 1:
        return True
    else:
        return False
# excluir_usuario


def desconectar_servidor(conn: sqlite3.Connection) -> None:
    """
    Função para desconectar do servidor de banco de dados
    :param conn: conexão ao servidor de banco de dados
    :return: None
    """
    conn.close()
# desconectar_servidor


def verificar_usuario_existe(nome: str) -> bool:
    """
    Função para verificar se o usuário já está cadastrado no banco
    :param nome: nome do usuário a ser verificado
    :return: True - se o usuário não estiver cadastrado
             False - se o usuário já estiver cadastrado
    """
    dados = executa_query(f"SELECT id FROM usuarios WHERE nome='{nome}'")
    if len(dados) > 0:
        matricula = converter_id_para_matricula(dados[0][0])
        return False
    else:
        return True
# verificar_usuario_existe


def nome_usuario(matricula: int) -> str:
    """
    Função que retorna o nome do usuário
    :param matricula: número de matrícula do usuário a ser consultado
    :return: retorna o nome do usuário, se este for encontrado, ou uma string vazia caso o número de matrícula seja inválido
    """
    id_usuario = converter_matricula_para_id(matricula)
    dados = executa_query(f"SELECT nome FROM usuarios WHERE id='{id_usuario}'")

    if len(dados) <= 0:
        return ''

    return dados[0][0]
# nome_usuario


def num_matricula_usuario(nome: str) -> int:
    """
    Função que retorna o número da matrícula do usuário
    :param nome: nome do usuário a ser consultado
    :return: retorna o número da matrícula do usuário informado
             se o usuário nao for encontrado será retornado -1
    """
    dados = executa_query(f"SELECT id FROM usuarios WHERE nome='{nome}'")

    if len(dados) <= 0:
        return -1

    return converter_id_para_matricula(dados[0][0])
# num_matricula_usuario


def verificar_dados_usuario(matricula: int, senha_login: str) -> int:
    """
    Função que verifica os dados do usuário para login no sistema
    :param matricula: matrícula do usuário a ser verificado
    :param senha_login: senha do usuário a ser verificado
    :return: -1 - se o usuário não existir
              0 - se o usuário existir mas a senha infromada estiver incorreta
              1 - se o usuário existir e a senha infromada estiver correta
    """

    id_usuario = converter_matricula_para_id(matricula)
    dados = executa_query(f"SELECT senha FROM usuarios WHERE id={id_usuario}")

    if len(dados) <= 0:
        return -1

    senha_criptografada = dados[0][0]
    return verificar_senha(senha_login, senha_criptografada)
# verificar_dados_usuario


def cargo_usuario(matricula: int) -> int:
    """
    Função que retorna o código do cargo do usuário
    :param matricula: matrícula do usuário a ser consultado
    :return: -1 - se o usuário não for econtrado
             1  - se o usuário for entregador
             2  - se o usuário for vendedor
             3  - se o usuário for gerente
    """
    id_usuario = converter_matricula_para_id(matricula)
    dados = executa_query(f"SELECT cargo FROM usuarios WHERE id={id_usuario}")

    if len(dados) <= 0:
        return -1

    return dados[0][0]
# cargo_usuario


def data_atual_banco() -> str:
    """
    Função que retorna a data atual do servidor de banco de dados
    :return: string contendo a data atual no formato: 'dd/mm/aaaa'
             se ocorrer algum erro ao buscar a data será retornado uma string vazia: ''
    """
    dados = executa_query(f"SELECT strftime('%d/%m/%Y','now')")

    if len(dados) <= 0:
        return ''

    return dados[0][0]
# data_atual_banco


def alterar_cargo_banco(matricula: int, cargo: int) -> bool:
    """
    Função que altera o cargo de um usuário
    :param matricula: matrícula do usuário que terá o cargo alterado
    :param cargo: novo cargo deste usuário
    :return: True  - se a alteração ocorrer com sucesso
             False - se ocorrer algum erro durante a alteração
    """
    id_usuario = converter_matricula_para_id(matricula)

    if executa_comando(f"UPDATE usuarios SET cargo={cargo} WHERE id={id_usuario}") == 1:
        return True
    else:
        return False
# alterar_cargo
