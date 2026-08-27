def formatar_citacao(nome_completo):
    partes = nome_completo.strip().split()
    sobrenome = partes[-1].upper()
    primeiro_nome = " ".join(partes[:-1])
    return sobrenome + ", " + primeiro_nome

resultado1 = formatar_citacao("Carlos Eduardo Andrade")
print(resultado1)  # Saída esperada: ANDRADE, Carlos Eduardo


def gerar_codigo(ano, cpf):
    # Passos da lógica:
    # 1. Remove espaços em branco antes ou depois do CPF
    cpf_limpo = cpf.strip()
    # 2. Realiza o fatiamento para pegar apenas os 3 primeiros dígitos (índices 0, 1 e 2)
    tres_digitos = cpf_limpo[0:3]
    # 3. Monta e retorna o código formatado
    return "ALU-" + str(ano) + "-" + tres_digitos

# --- TESTE DA FUNÇÃO ---
resultado2 = gerar_codigo("2026", "456.789.123-00")
print(resultado2)  # Saída esperada: ALU-2026-456
