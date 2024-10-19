import hashlib

# Função para gerar o hash de uma senha
def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# Função para verificar se a senha fornecida corresponde ao hash
def verificar_senha(senha_fornecida, hash_armazenado):
    return gerar_hash(senha_fornecida) == hash_armazenado

# Hash armazenado (por exemplo, de uma senha já salva)
hash_armazenado = gerar_hash("2209")

# Verificação de senha
senha_fornecida = input('digite sua senha: ')
if verificar_senha(senha_fornecida, hash_armazenado):
    print("Senha correta!")
else:
    print("Senha incorreta!")