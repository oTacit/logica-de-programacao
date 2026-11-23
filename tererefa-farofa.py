produtos = [
    {"codigo": "101", "nome": "Teclado", "preco": 89.90, "quantidade": 15},
    {"codigo": "102", "nome": "Mouse", "preco": 49.90, "quantidade": 20},
    {"codigo": "103", "nome": "Monitor", "preco": 799.90, "quantidade": 8}
]

perguntas = {
    1: (
        "Por que utilizar uma lista de dicionarios?",
        "A lista armazena varios produtos, enquanto cada dicionario guarda as informacoes de um produto, como codigo, nome, preco e quantidade."
    ),
    2: (
        "Como funciona a busca sequencial?",
        "O programa percorre a lista produto por produto, comparando o codigo ou nome ate encontrar o registro desejado."
    ),
    3: (
        "Para que serve a variavel indice?",
        "Ela indica a posicao de um produto dentro da lista. Se o resultado for -1, significa que o produto nao foi encontrado."
    ),
    4: (
        "Qual a diferenca entre pop() e remove()?",
        "O pop() remove um elemento utilizando seu indice e pode retornar o elemento removido. O remove() procura e remove um elemento pelo proprio valor."
    ),
    5: (
        "Por que utilizar append()?",
        "O append() adiciona um novo dicionario ao final da lista de produtos."
    ),
    6: (
        "Por que a busca binaria precisa de uma lista ordenada?",
        "Porque ela divide a lista em partes e elimina metade das possibilidades a cada comparacao. Sem ordenacao, o resultado pode estar incorreto."
    ),
    7: (
        "Como adicionar um novo campo ao produto?",
        "Basta adicionar uma nova chave e seu valor no dicionario durante o cadastro e incluir essa informacao na listagem."
    ),
    8: (
        "O que acontece quando um produto nao existe?",
        "A busca retorna -1 e o sistema informa que o produto nao foi encontrado."
    ),
    9: (
        "Para que servem as funcoes?",
        "Elas dividem o programa em tarefas menores, deixando o codigo organizado, reutilizavel e mais facil de manter."
    ),
    10: (
        "O que acontece quando o usuario digita uma opcao invalida?",
        "O sistema verifica a entrada e apresenta uma mensagem de erro, permitindo que o usuario tente novamente."
    )
}


def buscar(lista, termo):
    termo = termo.strip().lower()

    for indice, produto in enumerate(lista):
        if (produto["codigo"].lower() == termo or
                produto["nome"].lower() == termo):
            return indice, indice + 1

    return -1, len(lista)


def ler_texto(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor:
            return valor

        print("Este campo nao pode ficar vazio.")


def ler_preco():
    while True:
        try:
            valor = float(input("Preco: R$ ").replace(",", "."))

            if valor >= 0:
                return valor

            print("O preco nao pode ser negativo.")

        except ValueError:
            print("Digite um valor numerico valido.")


def ler_quantidade():
    while True:
        try:
            valor = int(input("Quantidade: "))

            if valor >= 0:
                return valor

            print("A quantidade nao pode ser negativa.")

        except ValueError:
            print("Digite um numero inteiro valido.")


def cadastrar(lista):
    print("\n===== CADASTRO DE PRODUTO =====")

    codigo = ler_texto("Codigo: ")
    indice, _ = buscar(lista, codigo)

    if indice != -1:
        print("Ja existe um produto com esse codigo.")
        return

    nome = ler_texto("Nome: ")
    preco = ler_preco()
    quantidade = ler_quantidade()

    lista.append({
        "codigo": codigo,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    })

    print("\nProduto cadastrado com sucesso!")


def listar(lista):
    print("\n===== ESTOQUE DE PRODUTOS =====")

    if not lista:
        print("Nenhum produto cadastrado.")
        return

    print(f"{'CODIGO':<10}{'NOME':<20}{'PRECO':>12}{'QUANTIDADE':>15}")
    print("-" * 57)

    for produto in lista:
        print(
            f"{produto['codigo']:<10}"
            f"{produto['nome']:<20}"
            f"R$ {produto['preco']:>9.2f}"
            f"{produto['quantidade']:>15}"
        )

    print("-" * 57)
    print(f"Total de produtos cadastrados: {len(lista)}")


def buscar_produto(lista):
    print("\n===== BUSCA DE PRODUTO =====")

    if not lista:
        print("Estoque vazio.")
        return

    termo = ler_texto("Digite o codigo ou nome: ")
    indice, comparacoes = buscar(lista, termo)

    if indice == -1:
        print("\nProduto nao encontrado.")
    else:
        produto = lista[indice]
        print("\nProduto encontrado!")
        print(f"Codigo: {produto['codigo']}")
        print(f"Nome: {produto['nome']}")
        print(f"Preco: R$ {produto['preco']:.2f}")
        print(f"Quantidade: {produto['quantidade']}")

    print(f"Comparacoes realizadas: {comparacoes}")


def remover(lista):
    print("\n===== REMOVER PRODUTO =====")

    if not lista:
        print("Estoque vazio.")
        return

    termo = ler_texto("Digite o codigo ou nome: ")
    indice, comparacoes = buscar(lista, termo)

    if indice == -1:
        print("Produto nao encontrado.")
    else:
        removido = lista.pop(indice)
        print(f"Produto '{removido['nome']}' removido com sucesso!")

    print(f"Comparacoes realizadas: {comparacoes}")


def menu_estoque():
    while True:
        print("\n" + "=" * 40)
        print("           GESTAO DE ESTOQUE")
        print("=" * 40)
        print("1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Buscar produto")
        print("4. Remover produto")
        print("5. Voltar ao menu principal")
        print("=" * 40)

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar(produtos)
        elif opcao == "2":
            listar(produtos)
        elif opcao == "3":
            buscar_produto(produtos)
        elif opcao == "4":
            remover(produtos)
        elif opcao == "5":
            break
        else:
            print("Opcao invalida. Tente novamente.")


def menu_defesa():
    while True:
        print("\n" + "=" * 40)
        print("         PREPARACAO PARA DEFESA")
        print("=" * 40)
        print("1. Ver todas as perguntas e respostas")
        print("2. Escolher uma pergunta")
        print("3. Voltar ao menu principal")
        print("=" * 40)

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            for numero, (pergunta, resposta) in perguntas.items():
                print(f"\n{numero}. {pergunta}")
                print(f"Resposta: {resposta}")

            input("\nPressione ENTER para continuar...")

        elif opcao == "2":
            for numero, (pergunta, _) in perguntas.items():
                print(f"{numero}. {pergunta}")

            try:
                numero = int(input("\nNumero da pergunta: "))

                if numero in perguntas:
                    pergunta, resposta = perguntas[numero]
                    print(f"\n{pergunta}")
                    print(f"\nResposta:\n{resposta}")
                else:
                    print("Pergunta inexistente.")

            except ValueError:
                print("Digite um numero valido.")

            input("\nPressione ENTER para continuar...")

        elif opcao == "3":
            break

        else:
            print("Opcao invalida.")


def menu_principal():
    while True:
        print("\n" + "=" * 44)
        print("       SISTEMA DE GESTAO DE ESTOQUE")
        print("=" * 44)
        print("1. Acessar sistema de estoque")
        print("2. Preparacao para defesa oral")
        print("3. Encerrar programa")
        print("=" * 44)

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            menu_estoque()
        elif opcao == "2":
            menu_defesa()
        elif opcao == "3":
            print("\nPrograma encerrado.")
            break
        else:
            print("Opcao invalida. Escolha de 1 a 3.")


menu_principal()
