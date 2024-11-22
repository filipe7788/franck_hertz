import os
import pandas as pd

# Caminho da pasta onde o script está
current_directory = os.getcwd()

# Lista todos os arquivos no diretório
files = [f for f in os.listdir(current_directory) if f.endswith('.TXT')]

for file in files:
    # Caminho completo do arquivo TXT
    txt_file_path = os.path.join(current_directory, file)
    try:
        # Tenta abrir o arquivo com a codificação UTF-8
        df = pd.read_csv(txt_file_path, sep="\t", decimal=",", encoding="utf-8")
    except UnicodeDecodeError:
        try:
            # Se UTF-8 falhar, tenta Latin-1
            df = pd.read_csv(txt_file_path, sep="\t", decimal=",", encoding="latin-1")
        except Exception as e:
            print(f"Erro ao converter {file}: {e}")
            continue  # Passa para o próximo arquivo

    # Define o nome do arquivo CSV
    csv_file_path = os.path.splitext(txt_file_path)[0] + ".csv"
    
    try:
        # Salva como CSV
        df.to_csv(csv_file_path, index=False, decimal=".", sep=",")
        print(f"Convertido: {file} -> {os.path.basename(csv_file_path)}")
    except Exception as e:
        print(f"Erro ao salvar {file} como CSV: {e}")
