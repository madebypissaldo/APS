import pickle
import hashlib

class Voto:
    def __init__(self, candidate_id):
        self.candidate_id = candidate_id

    def __repr__(self):
        return f"Voto(candidate_id={self.candidate_id})"

    def to_string(self):
        if self.candidate_id == 1:
            return "Gabriel"
        elif self.candidate_id == 2:
            return "Joao"
        elif self.candidate_id == 3:
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
        vote_counts[voto.candidate_id] += 1
    return vote_counts

votos =  carregar_planilha()

def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def verificar_senha(senha_fornecida, hash_armazenado):
    return gerar_hash(senha_fornecida) == hash_armazenado

hash_armazenado = gerar_hash("2209")

acesso = input('digite a senha para acessar a  planilha: ')
if verificar_senha(acesso, hash_armazenado):
    vote_counts = contar_votos(votos)
    print("Apuração dos votos:")
    print(f"Gabriel: {vote_counts[1]}")
    print(f"Joao: {vote_counts[2]}")
    print(f"Maria: {vote_counts[3]}")
else:
    print('senha inválida!')