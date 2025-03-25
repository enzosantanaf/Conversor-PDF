import os
from tkinter import filedialog

# Seleciona o arquivo sem extensão
arquivo_original = filedialog.askopenfilename(title="Selecione o arquivo que é um PDF sem extensão")

# Define o novo caminho com extensão .pdf
novo_arquivo = f"{arquivo_original}.pdf"

# Renomeia o arquivo (ou copia, se preferir manter o original)
os.rename(arquivo_original, novo_arquivo)

print(f"Arquivo renomeado como: {novo_arquivo}")
