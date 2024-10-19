import pickle
import hashlib

# Função para converter o ID do candidato em nome
def to_string(candidate_id):
    if candidate_id == 1:
        return "Gabriel"
    elif candidate_id == 2:
        return "Joao"
    elif candidate_id == 3:
        return "Maria"
    else:
        return "Candidato desconhecido"

# Função para carregar os votos de um arquivo
def carregar_planilha():
    try:
        with open('votos.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

# Função para contar os votos
def contar_votos(votos):
    vote_counts = {1: 0, 2: 0, 3: 0}
    for voto in votos:
        vote_counts[voto] += 1
    return vote_counts

# Função para gerar o hash da senha
def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# Função para verificar se a senha fornecida está correta
def verificar_senha(senha_fornecida, hash_armazenado):
    return gerar_hash(senha_fornecida) == hash_armazenado

# Função de criptografia por cifra de César
def caesar_crypt(text, shift):
    result = ''
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

# Função de descriptografia por cifra de César
def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result

# Definindo a senha original e o shift para a cifra de César
senha_original = 'Gabriel'
shift = 4

# Criptografando a senha original com a cifra de César
senha_cesar = caesar_crypt(senha_original, shift)
print(f"Senha após cifra de César: {senha_cesar}")

# Gerando o hash da senha criptografada com a cifra de César
hash_armazenado = gerar_hash(senha_cesar)
print(f"Hash da senha criptografada com César: {hash_armazenado}")

# Solicitar a senha e aplicar as duas criptografias
acesso = input('Digite a senha para acessar a planilha: ')

# Criptografar a senha digitada com a cifra de César
acesso_cesar = caesar_crypt(acesso, shift)

# Verificar se a senha criptografada com César e em hash é igual ao hash armazenado
if verificar_senha(acesso_cesar, hash_armazenado):
    votos = carregar_planilha()
    vote_counts = contar_votos(votos)
    print("Apuração dos votos:")
    print(f"Gabriel: {vote_counts[1]}")
    print(f"Joao: {vote_counts[2]}")
    print(f"Maria: {vote_counts[3]}")
else:
    print('Senha inválida!')
