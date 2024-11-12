import hashlib
import pickle

def to_string(candidate_id):
    if candidate_id == 1:
        return "Gabriel"
    elif candidate_id == 2:
        return "Joao"
    elif candidate_id == 3:
        return "Maria"
    else:
        return "Candidato desconhecido"

def carregar_planilha():
    try:
        with open('votos.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

def atualizar_votos(votos):
    with open('votos.pkl', 'wb') as f:
        pickle.dump(votos, f)

def contar_votos(votos):
    vote_counts = {1: 0, 2: 0, 3: 0}
    for voto in votos:
        vote_counts[voto] += 1
    return vote_counts

def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def verificar_senha(senha_fornecida, hash_armazenado):
    return gerar_hash(senha_fornecida) == hash_armazenado

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

senha_original = 'Gabriel'
shift = 4

senha_cesar = caesar_crypt(senha_original, shift)
print(f"Senha após cifra de César: {senha_cesar}")

hash_armazenado = gerar_hash(senha_cesar)
print(f"Hash da senha criptografada com César: {hash_armazenado}")

votos = carregar_planilha()

while True:
    voto = int(input('digite o numero do seu candidato (ou 0 para sair): '))
    if voto == 0:
        break
    elif voto in [1, 2, 3]:
        votos.append(voto)
        atualizar_votos(votos)
        print('computando seu voto ...')
    else:
        print("Numero de candidato inválido!")

acesso = input('Digite a senha para acessar a planilha: ')

acesso_cesar = caesar_crypt(acesso, shift)

if verificar_senha(acesso_cesar, hash_armazenado):
    votos = carregar_planilha()
    vote_counts = contar_votos(votos)
    print("Apuração dos votos:")
    print(f"Gabriel: {vote_counts[1]}")
    print(f"Joao: {vote_counts[2]}")
    print(f"Maria: {vote_counts[3]}")
else:
    print('Senha inválida!')