class Produto:
    #Atributos
    nome:str
    preco:float
    saldo:int #quantidade de produtos
    

    #Métodos
    def valorTotalEmEstoque(self) -> float: #vc está definindo que o resultado da def será do tipo float
        return self.preco * self.saldo
        #essa método vai calcular o valor total em estoque

    def adicionarProdutos(self, quantidade) -> int:
        self.saldo = self.saldo + quantidade
        return self.saldo
        #essa função armazena a entrada de mais produtos ao saldo/quantidade em estoque

    def removerProdutos(self, quantidade) -> int:
        self.saldo = self.saldo - quantidade
        #essa função vai remover a qty de produtos do usuário da quantidade total em estoque

    def dadosDoProduto(self) -> str:
        saida = f"""  #saída de dados
                Dados do Produto:
                \tNome do Produto: {self.nome}
                \tValor de compra do Produto: R${self.preco}
                \tQuantidade em estoque: {self.saldo}
                \tValor total em estoque: {self.valorTotalEmEstoque():.2f}""" #valorTotalEmEstoque é um método
        return saida