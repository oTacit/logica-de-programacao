# ==============================================================================
# PROVA PRÁTICA AV1 - 3º BIMESTRE
# ARQUIVO: av1_saneamento_dados.py
# Nome do Aluno: Vítor Matielo Gervazoni
# Data: 18/09/2026
# ==============================================================================

# Lista de cadastros brutos recebidos do sistema
cadastros_brutos = [
    "  joao da silva;11988887777  ",
    "  maria sousa;21977776666  ",
    "  carlos edgardo oliveira;31966665555  ",
    "  ana paula lima;41955554444  "
]

print("==================================================")
print("     SISTEMA DE SANEAMENTO DE DADOS - AV1")
print("==================================================\n")

# Percorrer a lista usando for e range()
for i in range(len(cadastros_brutos)):

    # 1. Remover espaços extras do início e fim
    cadastro = cadastros_brutos[i].strip()

    # 2. Separar o nome e o telefone
    nome, telefone = cadastro.split(";")

    # 3. Converter o nome para letras maiúsculas
    nome = nome.upper()

    # 4. Extrair o DDD usando fatiamento
    ddd = telefone[0:2]

    # 5. Exibir o resultado padronizado
    print(f"Funcionário: {nome} | DDD: {ddd} | Telefone: {telefone}")

print("\n==================================================")
print("           PROCESSAMENTO CONCLUÍDO")
print("==================================================")