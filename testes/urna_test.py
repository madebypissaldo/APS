import time
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

votos = carregar_planilha()

while True:
    voto = int(input('digite o numero do seu candidato (ou 0 para sair): '))
    if voto == 0:
        break
    elif voto in [1, 2, 3]:
        votos.append(voto)
        atualizar_votos(votos)
        print('computando seu voto ...')
        time.sleep(5)
    else:
        print("Numero de candidato inválido!")