from passlib.hash import pbkdf2_sha256 as cryp


def converter_id_para_matricula(id):
    """Função que converte o id da tabela usuário na matrícula do usuário"""
    return id + 5000
# converter_id_para_matricula


def criptografar_senha(senha):
    """Função que criptografa senha"""
    return cryp.hash(senha, rounds=200000, salt_size=16)
# criptografar_senha


#modificar
def verificar_senha(senha_login, senha_cadastrada):
    if cryp.verify(senha_login, senha_cadastrada):
        return True
    else:
        return False
# checa_senha