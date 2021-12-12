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


def inserir_usuario(nome: str, email: str, senha: str, cargo: int) -> tuple[bool, str]:
    """
    Função para cadastrar um novo usuário no banco de dados
    :param nome: nome informado pelo usuário para cadastro
    :param email: email informado pelo usuário para cadastro
    :param senha: senha informada pelo usuário para cadastro
    :param cargo: cargo informado pelo usuário para cadastro
    :return: tuple(status, mensagem)
                status: True - se o usuário for cadastrado com sucesso
                        False - se ocorrer algum problema no cadastro
                mensagem: mensagem de texto para ser apresentada ao usuário indicando sucesso ou falha no cadastro
    """
    ret = verificar_usuario_existe(nome)
    if not ret[0]:
        return ret

    conn = conectar_servidor()
    cursor = conn.cursor()

    senha_criptografada = criptografar_senha(senha)
    cursor.execute(f"""INSERT INTO usuarios (nome, email, senha, cargo) 
                       VALUES ('{nome}', '{email}', '{senha_criptografada}', {cargo})""")
    conn.commit()
    desconectar_servidor(conn)

    if cursor.rowcount == 1:
        matricula = num_matricula_usuario(nome)
        ret = (True, f'O usuário {nome} foi adicionado com sucesso.\nNúmero de matrícula {matricula}')
    else:
        ret = (False, f'Erro ao adicionar o usuário: {nome}')
    return ret
# inserir_usuario


def desconectar_servidor(conn: sqlite3.Connection) -> None:
    """
    Função para desconectar do servidor de banco de dados
    :param conn: conexão ao servidor de banco de dados
    :return: None
    """
    conn.close()
# desconectar_servidor


def verificar_usuario_existe(nome: str) -> tuple[bool, str]:
    """Função para verificar se o usuário já está cadastrado no banco"""
    conn = conectar_servidor()
    cursor = conn.cursor()

    cursor.execute(f"SELECT id FROM usuarios WHERE nome='{nome}'")
    usuario = cursor.fetchall()

    if len(usuario) > 0:
        matricula = converter_id_para_matricula(usuario[0][0])
        ret = (False, f"O usuário {nome} já está castrado.\nNúmero de matrícula {matricula}")
    else:
        ret = (True, '')

    desconectar_servidor(conn)
    return ret
# verificar_usuario_existe


def num_matricula_usuario(nome):
    """Função que retorna o número da matrícula d eum usuário"""
    conn = conectar_servidor()
    cursor = conn.cursor()

    cursor.execute(f"SELECT id FROM usuarios WHERE nome='{nome}'")
    usuario = cursor.fetchall()
    matricula = converter_id_para_matricula(usuario[0][0])
    return matricula
# num_matricula_usuario


def verificar_dados_usuario(matricula, senha_login):
    """Função que verifica os dados do usuário para login no sistema"""
    conn = conectar_servidor()
    cursor = conn.cursor()
    id_usuario = converter_matricula_para_id(matricula)
    cursor.execute(f"SELECT senha FROM usuarios WHERE id={id_usuario}")
    usuario = cursor.fetchall()

    if len(usuario) <= 0:
        return -1

    senha_criptografada = usuario[0][0]
    ret = verificar_senha(senha_login, senha_criptografada)
    return ret
# verificar_dados_usuario
