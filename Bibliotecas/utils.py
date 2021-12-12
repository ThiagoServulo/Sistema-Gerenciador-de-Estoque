from passlib.hash import pbkdf2_sha256 as cryp


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
