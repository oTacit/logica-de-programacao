def atividade_1():
    # Atividade (1) - Lousa
    notas = [8.5, 7.0, 9.5, 6.0]

    print("Lista completa de notas:", notas)
    print("-" * 40)

    print("Primeira nota (indice 0):", notas[0])
    print("Segunda nota (indice 1):", notas[1])
    print("Terceira nota (indice 2):", notas[2])
    print("Quarta nota (indice 3):", notas[3])
    print("-" * 40)

    total_elementos = len(notas)
    print("Quantidade total de elementos (len):", total_elementos)

    ultimo_indice = total_elementos - 1
    print("Última nota da lista (índice N-1):", notas[ultimo_indice])
    print("-" * 40)


def atividade_2():
    # Atividade (2) - E-Class
    atleta = ["Lucas", 16, 1.75, "Basquete"]

    print("Nome do atleta:", atleta[0])
    print("Modalidade:", atleta[len(atleta) - 1])
    print("Total de informações:", len(atleta))


def menu():
    while True:
        print("\n===== MENU DE ATIVIDADES =====")
        print("1 - Atividade 1 (Lousa)")
        print("2 - Atividade 2 (E-Class)")
        print("0 - Sair")
        print("=" * 30)

        opcao = input("Escolha uma opção: ").strip()
        print()

        if opcao == "1":
            atividade_1()
        elif opcao == "2":
            atividade_2()
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Digite 1, 2 ou 0.")


menu()
