import os,time

def armas(arma):

    match arma:
        
        case "arco":
            arma_arco={
                'nome': "Arco de treino",
                'dano': 5,
                'critico': 15,
                'tipo': 'longo alcance'
            }
            return 