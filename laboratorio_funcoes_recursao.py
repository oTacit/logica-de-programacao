TAXA_PROCESSAMENTO = 2.00


# PARTE 1: CALCULADORA DE FRETE
def calcular_frete(valor_compra, peso_kg):
    frete = peso_kg * 5

    if valor_compra >= 200:
        frete = frete * 0.5

    return frete


# PARTE 2: CUPOM E TAXAS
def aplicar_cupom(valor_item, cupom_desconto):
    desconto = valor_item * (cupom_desconto / 100)
    valor_final = valor_item - desconto
    valor_final = valor_final + TAXA_PROCESSAMENTO

    return valor_final


# PARTE 3: RECURSIVIDADE
def exibir_cronograma_regressivo(parcelas_restantes, valor_parcela):
    if parcelas_restantes == 0:
        print("Todas as parcelas foram quitadas!")
        return

    print(f"Restam {parcelas_restantes} parcela(s) de R$ {valor_parcela}")

    exibir_cronograma_regressivo(parcelas_restantes - 1, valor_parcela)


# TESTES

print("=== TESTE PARTE 1: CALCULADORA DE FRETE ===")
frete = calcular_frete(200, 4)
print("Frete Final Esperado (10.0):", frete)

print()

print("=== TESTE PARTE 2: CUPOM E TAXAS DE ESCOPO ===")
preco = aplicar_cupom(100, 10)
print("Preço Final Esperado (92.0):", preco)

print()

print("=== TESTE PARTE 3: CRONOGRAMA RECURSIVO ===")
exibir_cronograma_regressivo(3, 150)