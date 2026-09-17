produtos = []


def cadastrar(nome, preco, quantidade):
    produto = {
        "nome": nome.strip().title(),
        "preco": preco,
        "quantidade": quantidade
    }
    produtos.append(produto)
    return produto


def valor_estoque(produto):
    return produto["preco"] * produto["quantidade"]


def buscar(nome):
    for produto in produtos:
        if produto["nome"].lower() == nome.strip().lower():
            return produto
    return None


def relatorio():
    total = 0
    print("\n===== RELATÓRIO =====")

    for p in produtos:
        valor = valor_estoque(p)
        total += valor
        print(f"{p['nome']} | Qtd: {p['quantidade']} | R$ {valor:.2f}")

    print(f"Valor total: R$ {total:.2f}")


def sistema():
    while True:
        print("\n1-Cadastrar | 2-Entrada | 3-Saída | 4-Relatório | 5-Sair")
        opcao = input("Opção: ").strip()

        try:
            if opcao == "1":
                nome = input("Produto: ")
                preco = float(input("Preço: R$ "))
                qtd = int(input("Quantidade: "))

                if preco < 0 or qtd < 0:
                    print("Valores inválidos!")
                    continue

                cadastrar(nome, preco, qtd)
                print("Produto cadastrado!")

            elif opcao in ["2", "3"]:
                produto = buscar(input("Produto: "))

                if not produto:
                    print("Produto não encontrado!")
                    continue

                qtd = int(input("Quantidade: "))

                if qtd <= 0:
                    print("Quantidade inválida!")
                    continue

                if opcao == "2":
                    produto["quantidade"] += qtd
                elif qtd <= produto["quantidade"]:
                    produto["quantidade"] -= qtd
                else:
                    print("Estoque insuficiente!")
                    continue

                print("Estoque atualizado!")

            elif opcao == "4":
                relatorio()

            elif opcao == "5":
                print("Sistema encerrado!")
                break

            else:
                print("Opção inválida!")

        except ValueError:
            print("Digite valores válidos!")


sistema()