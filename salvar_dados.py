import csv
import os

def salvar_dados(data_hora, temperatura, umidade):
    nome_arquivo = "dados.csv"
    novo_arquivo = not os.path.exists(nome_arquivo)  # Verifica se o arquivo existe

    with open(nome_arquivo, mode="a", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        
        if novo_arquivo:
            escritor.writerow(["Data/Hora", "Temperatura (°C)", "Umidade (%)"])  # Cabeçalho
        
        escritor.writerow([data_hora, temperatura, umidade])
