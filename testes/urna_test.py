import time
import pickle

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

def atualizar_votos(votos):
    with open('votos.pkl', 'wb') as f:
        pickle.dump(votos, f)

def contar_votos(votos):
    vote_counts = {1: 0, 2: 0, 3: 0}
    for voto in votos:
        vote_counts[voto.candidate_id] += 1
    return vote_counts

votos = carregar_planilha()

while True:
    voto = int(input('digite o numero do seu candidato (ou 0 para sair): '))
    if voto == 0:
        break
    elif voto in [1, 2, 3]:
        novo_voto = Voto(voto)
        votos.append(novo_voto)
        atualizar_votos(votos)
        print('computando seu voto ...')
        time.sleep(5)
    else:
        print("Numero de candidato inválido!")