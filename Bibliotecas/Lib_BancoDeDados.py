import sqlite3
from Bibliotecas.utils import *


# --------------------------------------------------------------------------------------------------
# ----------------------------------------- Funções Gerais -----------------------------------------
# --------------------------------------------------------------------------------------------------


def conectar_servidor() -> sqlite3.Connection:
    """
    Função para conectar ao servidor de banco de dados
    :return: retorna a conexão ao banco de dados
    """
    conn = sqlite3.connect('gerenciador_estoque.bd')

    conn.execute("""CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        senha TEXT NOT NULL,
        cargo INTEGER NOT NULL);"""
                 )

    conn.execute("""CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        marca TEXT NOT NULL,
        fabricante TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco_compra REAL NOT NULL,
        data_atualizacao TEXT NOT NULL);"""
                 )

    conn.execute("""CREATE TABLE IF NOT EXISTS vendas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao_produto TEXT NOT NULL,
        quantidade_venda INTEGER NOT NULL,
        preco_compra REAL NOT NULL,
        preco_venda REAL NOT NULL,
        data_venda TEXT NOT NULL,
        nome_usuario TEXT NOT NULL);"""
                 )

    return conn
# conectar_servidor


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


def desconectar_servidor(conn: sqlite3.Connection) -> None:
    """
    Função para desconectar do servidor de banco de dados
    :param conn: conexão ao servidor de banco de dados
    :return: None
    """
    conn.close()
# desconectar_servidor


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


# --------------------------------------------------------------------------------------------------
# --------------------------------------- Funções de Usuário ---------------------------------------
# --------------------------------------------------------------------------------------------------


def inserir_usuario_banco(nome: str, email: str, senha: str, cargo: int) -> int:
    """
    Função para cadastrar um novo usuário no banco de dados
    :param nome: nome informado pelo usuário para cadastro
    :param email: email informado pelo usuário para cadastro
    :param senha: senha informada pelo usuário para cadastro
    :param cargo: cargo informado pelo usuário para cadastro
    :return: 1  - se o usuário for cadastrado com sucesso
             0  - se ocorrer algum problema no cadastro
             -1 - se o usuário já estiver cadastrado
    """
    if not verificar_usuario_existe(nome):
        return -1

    senha_criptografada = criptografar_senha(senha)

    if executa_comando(f"""INSERT INTO usuarios (nome, email, senha, cargo) 
                           VALUES ('{nome}', '{email}', '{senha_criptografada}', {cargo})""") == 1:
        return 1
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


def verificar_usuario_existe(nome: str) -> bool:
    """
    Função para verificar se o usuário já está cadastrado no banco
    :param nome: nome do usuário a ser verificado
    :return: True - se o usuário não estiver cadastrado
             False - se o usuário já estiver cadastrado
    """
    dados = executa_query(f"SELECT id FROM usuarios WHERE nome='{nome}'")

    if len(dados) > 0:
        return False

    return True
# verificar_usuario_existe


def nome_usuario(matricula: int) -> str:
    """
    Função que retorna o nome do usuário
    :param matricula: número de matrícula do usuário a ser consultado
    :return: string contendo o nome do usuário
             se o número de matrícula for inválido será retornado uma string vazia
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


# --------------------------------------------------------------------------------------------------
# --------------------------------------- Funções de Produtos --------------------------------------
# --------------------------------------------------------------------------------------------------


def inserir_produto_banco(descricao: str, marca: str, fabricante: str, quantidade: int, preco_compra: float) -> int:
    """
    Função que insere um produto no banco de dados
    :param descricao: descrição do produto
    :param marca: marca do produto
    :param fabricante: fabricante do produto
    :param quantidade: quantidade comprada do produto
    :param preco_compra: preço de compra do do produto
    :return: 1  - se o produto for cadastrado com sucesso
             0  - se ocorrer algum problema no cadastro
             -1 - se o produto já estiver cadastrado
    """
    if not verificar_produto_existe(descricao):
        return -1

    if executa_comando(f"""INSERT INTO produtos (descricao, marca, fabricante, quantidade, preco_compra, 
                            data_atualizacao) VALUES ('{descricao}', '{marca}', '{fabricante}', {quantidade}, 
                            {preco_compra}, '{data_atual_banco()}')""") == 1:
        return 1
    else:
        return 0
# inserir_produto_banco


def verificar_produto_existe(descricao: str) -> bool:
    """
    Função para verificar se o produto já está cadastrado no banco
    :param descricao: descricao do produto a ser verificado
    :return: True - se o produto não estiver cadastrado
             False - se o produto já estiver cadastrado
    """
    dados = executa_query(f"SELECT id FROM produtos WHERE descricao='{descricao}'")

    if len(dados) > 0:
        return False

    return True
# verificar_produto_existe


def descricao_produto(id_produto: int) -> str:
    """
    Função que busca a descrição de um produto através do seu id
    :param id_produto: id do produto a ser buscado
    :return: string contendo a descrição do produto
             se o id não for encontrado será retonado uma string vazia
    """
    dados = executa_query(f"SELECT descricao FROM produtos WHERE id={id_produto}")

    if len(dados) <= 0:
        return ''

    return dados[0][0]
# descricao_produto


def maior_id_produto() -> int:
    """
    Função que retorna o id do último produto cadastrado
    :return: id do último produto cadastrado
             -1 - se não houver nenhum produto cadastrado
    """
    dados = executa_query(f"SELECT MAX(id) FROM produtos")

    if len(dados) <= 0:
        return -1

    return dados[0][0]
# maior_id_produto


def quantidade_produtos_cadastrados() -> int:
    """
    Função que verifica a quantidade de produtos cadastrados
    :return: quantidade de produtos cadastrados
             -1 - se não houverem produtos cadastrados
    """
    dados = executa_query(f"SELECT COUNT(id) FROM produtos")

    if len(dados) <= 0:
        return -1

    return dados[0][0]
# quantidade_produtos_cadastrados


def busca_produto_por_id(id_produto: int) -> tuple:
    """
    Função que busca os dados de um produto através do seu id
    :param id_produto: id do produto a ser procurado
    :return: tupla de valores contendo os dados do produto:
             (id, descrição, marca, fabricante, quantidade, preço de compra, data da última atualização).
             Se não houverem produtos cadastrados será retonado uma tupla vazia
    """
    dados = executa_query(f"SELECT * FROM produtos WHERE id={id_produto}")

    if len(dados) <= 0:
        return ()

    return dados[0]
# busca_produto_por_id


def excluir_produto_banco(id_produto: int) -> bool:
    """
    Função que exclui um produto do banco
    :param id_produto: id do produto a ser excluído
    :return: True - se o produto for excluído com sucesso
             False - se ocorrer algum erro durante a exclusão
    """
    descricao = descricao_produto(id_produto)

    if not verificar_produto_existe(descricao):
        if executa_comando(f"""DELETE FROM produtos WHERE id={id_produto}""") == 1:
            return True

    return False
# excluir_produto_banco


def alterar_produto_banco(id_produto: int, quantidade: int) -> bool:
    """
    Função que altera a quantidade de um produto em estoque
    :param id_produto: id do produto a ser alterado
    :param quantidade: quantidade do produto em estoque
    :return: True - se a quantidade do produto for alterada com sucesso
             False - se ocorrer algum erro durante a alteração
    """
    data_banco = data_atual_banco()

    if data_banco != '':
        descricao = descricao_produto(id_produto)
        if not verificar_produto_existe(descricao):
            if executa_comando(f"UPDATE produtos SET quantidade={quantidade}, "
                               f"data_atualizacao='{data_banco}' WHERE id={id_produto}") == 1:
                return True

    return False
# alterar_produto_banco


def quantidade_produto(id_produto: int) -> int:
    """
    Função que retorna a quantidade de um produto em estoque
    :param id_produto: id do produto a ser verificado
    :return: quantidade do produto em estoque
    """
    dados = executa_query(f"SELECT quantidade FROM produtos WHERE id={id_produto}")
    return dados[0][0]
# quantidade_produto


# --------------------------------------------------------------------------------------------------
# ---------------------------------------- Funções de Vendas ---------------------------------------
# --------------------------------------------------------------------------------------------------


def adiciona_venda_banco(id_produto: int, quantidade: int, preco_venda: float, matricula: int) -> bool:
    """
    Função que adiciona oa dados da venda no banco
    :param id_produto: id do produto vendido
    :param quantidade: quantidade do produto vendida
    :param preco_venda: preço unitário de venda do produto
    :param matricula: matrícula do usuário responsável pela venda
    :return: True - se a venda for adicionada corretamente
             False - se ocorrer algum erro ao adicionar a venda
    """
    data_banco = data_atual_banco()
    tupla_produto = busca_produto_por_id(id_produto)
    descricao = tupla_produto[1]
    preco_compra = tupla_produto[5]
    usuario = nome_usuario(matricula)

    if data_banco != '':
        if executa_comando(f"""INSERT INTO vendas (descricao_produto, quantidade_venda, preco_compra, preco_venda,
                                    data_venda, nome_usuario) VALUES ('{descricao}', {quantidade}, {preco_compra}, 
                                    {preco_venda}, '{data_banco}', '{usuario}')""") == 1:
            return True

    return False
# adiciona_venda_banco


def busca_dados_vendas(data: str) -> list[tuple]:
    """
    Função que busca dados da venda pela data.
    Se a data informada for uma string vazia, será buscado todas as vendas
    :param data: data das vendas a serem buscadas
    :return: lista de tuplas contendo os dados da venda
    """
    if data == '':
        dados = executa_query(f"SELECT * FROM vendas")
    else:
        dados = executa_query(f"SELECT * FROM vendas WHERE data_venda={data}")

    return dados
# busca_dados_vendas

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
