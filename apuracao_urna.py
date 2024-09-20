import pickle
import hashlib

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

def contar_votos(votos):
    vote_counts = {1: 0, 2: 0, 3: 0}
    for voto in votos:
        vote_counts[voto] += 1
    return vote_counts

def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def verificar_senha(senha_fornecida, hash_armazenado):
    return gerar_hash(senha_fornecida) == hash_armazenado

hash_armazenado = gerar_hash("2209")

acesso = input('digite a senha para acessar a  planilha: ')
if verificar_senha(acesso, hash_armazenado):
    votos = carregar_planilha()
    vote_counts = contar_votos(votos)
    print("Apuração dos votos:")
    print(f"Gabriel: {vote_counts[1]}")
    print(f"Joao: {vote_counts[2]}")
    print(f"Maria: {vote_counts[3]}")
else:
<<<<<<< Updated upstream
    print('senha inválida!')
=======
    print('senha inválida!')
>>>>>>> Stashed changes
