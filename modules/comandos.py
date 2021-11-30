from modules.conector_atacadao import conector
from modules.auto_vendas import gerador_vendas
"""
Comandos de insert no banco de dados, e os selects de busca
"""
class comandos:
    try:
        def cadastrar_ultimas(novas):
            vendas_insert = gerador_vendas.gerador(novas)
            for venda in vendas_insert:
                query = f"INSERT INTO vendas (idproduto, idvendedor, valortotal, comissao) VALUES {venda}"                
                conector.executar(query)

            # query = "SELECT * FROM vendas;"
            # resultado = conector.buscar(query)
            # print(resultado)

        def cadastrar_ind():
            venda = []
            idproduto = input("Informe o ID do produto: ")
            idvendedor = input("Informe o ID do vendedor: ")
            valortotal = float(input("Informe o valor total da venda: U$ "))
            comissao = round(valortotal * 0.08, 2)
            venda.append(idproduto)
            venda.append(idvendedor)
            venda.append(valortotal)
            venda.append(comissao)
            venda = tuple(venda)
            query = f"INSERT INTO vendas (idproduto, idvendedor, valortotal, comissao) VALUES {venda}"                
            conector.executar(query)

        def vendas_total():
            query = f"select sum(valortotal) from vendas"
            valorTotal = conector.buscar(query)
            print(f" O valor total vendido foi: US$ {valorTotal[0][0]}")

        def melhor_venda():
            query = "select V.nome, Ven.valortotal from vendedor V, vendas Ven where V.idvendedor = Ven.idvendedor and Ven.idvendedor = (select idvendedor from vendas where valortotal = (select max(valortotal) from vendas)) order by Ven.valortotal desc;"
            vendedor_vendaMax = conector.buscar(query)
            print(f" A melhor vendedor foi: {vendedor_vendaMax[0][0]}, vendeu um valor de: US$ {vendedor_vendaMax[0][1]}")

        def vendedor_vendas():
            query = "select V.nome, count(Ven.idvenda) from vendedor V, vendas Ven where V.idvendedor = Ven.idvendedor group by V.nome order by count(Ven.idvenda);"
            vendedor_vendas = conector.buscar(query)
            melhores = []
            vendas_feitas = []
            for i in range(len(vendedor_vendas)):                              
                vendas_feitas.append(vendedor_vendas[i][1])
            for venda in vendas_feitas:                            
                if venda == max(vendas_feitas):
                    indice = vendas_feitas.index(venda)
                    melhores.append(vendedor_vendas[indice])
                    vendedor_vendas.remove(vendedor_vendas[indice])
        
            print(f"Os melhores venderores foram:\n")
            for melhor in melhores:
                print(f"Vendedor(a): {melhor[0]} fez {melhor[1]} vendas")
            print("\n")

        def fornecedor_utilizado():
            query = "select F.nome, count(F.idfornecedor) from fornecedor F where F.idfornecedor in (select idfornecedor from produto where idproduto in (select idproduto from vendas)) group by F.nome order by count(F.idfornecedor) desc;"
            fornecedorUtilizado = conector.buscar(query)
            maiorFornecedor=[]
            utilizacoes = []
            for i in range(len(fornecedorUtilizado)):
                utilizacoes.append(fornecedorUtilizado[i][1])
            for quantidade in utilizacoes:
                if quantidade == max(utilizacoes):
                    indice = utilizacoes.index(quantidade)
                    maiorFornecedor.append(fornecedorUtilizado[indice])
                    fornecedorUtilizado.remove(fornecedorUtilizado[indice])

            print("Os fornecedores mais usados foram:\n")
            for fornecedor in maiorFornecedor:
                print(f"O fornecedor {fornecedor[0]} foi utilizado {fornecedor[1]}.\n")  

        
        def vendedor_comissao():
            query = "select V.nome, sum(Ven.comissao) from vendedor V, vendas Ven where V.idvendedor = Ven.idvendedor group by V.nome order by V.nome;"
            comissoes = conector.buscar(query)
            
            for venda in comissoes:
                print(f"O vendedor(a) {venda[0]}, deverá receber uma comissão de US$ {venda[1]}")
            print("\n")







    except Exception as e:
        print(str(e))
            