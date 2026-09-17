dados_brutos = [
   "  carlos eduardo silva;desenvolvedor;11988887777  ",
   "  ana paula mendes;analista de rh;21977776666  ",
   "  roberto carlos oliveira;gerente de projetos;31966665555  "
]

def limpar_e_formatar_texto(texto):
   texto_limpo = texto.strip()
   texto_maiusculo = texto_limpo.upper()
   texto_normalizado = " ".join(texto_maiusculo.split())
   return texto_normalizado


def extrair_codigo_ou_ddd(dado):
   valor_limpo = dado.strip()
   codigo = valor_limpo[:2]
   return codigo


def processar_e_exibir_cadastros(lista_dados):
   total = 0

   for cadastro in lista_dados:
       partes = cadastro.split(";")
       nome = limpar_e_formatar_texto(partes[0])
       cargo = limpar_e_formatar_texto(partes[1])
       telefone = partes[2].strip()
       ddd = extrair_codigo_ou_ddd(telefone)

       print(f"Nome: {nome} | Cargo: {cargo} | DDD: {ddd} | Telefone: {telefone}")
       total += 1

   return total


def main():
   print("==================================================")
   print("     SISTEMA DE GESTÃO MODULARIZADO - AV2        ")
   print("==================================================\n")

   print("Iniciando o processamento dos dados...\n")

   total_processado = processar_e_exibir_cadastros(dados_brutos)
   print(f"Total de registros processados: {total_processado}")

   print("\n==================================================")
   print("             PROCESSAMENTO CONCLUÍDO              ")
   print("==================================================")

if __name__ == "__main__":
   main()
