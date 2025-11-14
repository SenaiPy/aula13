import produtoOOP as p #Importar o módulo

p1 = p.Produto() #Instanciar o objeto

#Entrada de dados
print("Digite os dados do produto")
p1.nome = input("\tNome: ")
p1.preco = float(input("\tPreço: R$ "))
p1.saldo = int(input("\tQuantidade: "))

#Saída de dados
print("Dados do produto")

print(p1.dadosDoProduto())

#Adicinar Produtos
qty = int(input("Digite o número de produtos a ser adicionado ao estoque: "))
p1.adicionarProdutos(qty)

#Saída de dados 2
print("------Dados atualizado-----------")
print(p1.dadosDoProduto())

#Remover produtos
qty = int(input("Digite o número de produtos a ser removido oo estoque: "))
p1.removerProdutos(qty)

#Saída de dados 3
print("------Dados atualizado-----------")
print(p1.dadosDoProduto())
