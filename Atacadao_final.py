from modules.conector_atacadao import conector
from modules.comandos import comandos


if __name__ == "__main__":
    try:        
        while True:
            print("Bem Vindo a interface de cadastro de vendas!")
            print("[1] - Cadastrar últimas Vendas", "[2] - Cadastrar venda individual", "[3] - Buscar Total Vendido", 
                "[4] - Buscar vendedor com a melhor venda", "[5] - Vendedor com mais vendas", "[6] - Fornecedor mais utilizado", 
                "[7] - Comissão devida por funcionário", "[0] - Sair", sep = "\n")
            escolha = input("Digite a opção: ")

            if escolha == "1": # Adiciona multiplas vendas
                comandos.cadastrar_ultimas(int(input("Digite quantas vendas deseja cadastrar: ")))

            elif escolha == "2": # Adiciona vendas únicas
                comandos.cadastrar_ind()

            elif escolha == "3":
                comandos.vendas_total()
            
            elif escolha == "4":
                comandos.melhor_venda()

            elif escolha == "5":
                comandos.vendedor_vendas()

            elif escolha == "6":
                comandos.fornecedor_utilizado()

            elif escolha == "7":
                comandos.vendedor_comissao()
            
            elif escolha == "0":
                print("Obrigado por usar o Cadastrador de vendas - Atacadão")
                break
            
            else:
                print("Opção inválida, tente novamente!")
    
    except Exception as e:
        print(str(e))