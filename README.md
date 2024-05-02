# PythonPDV

# Curriculo 
https://sites.google.com/view/curriculorodolphoguilherme/p%C3%A1gina-inicial

#LinkeIn
https://www.linkedin.com/in/rodolpho-guilherme-viana-624602ba/

# Classe para produtos
class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

# Classe para o carrinho de compras
class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total

    def mostrar_carrinho(self):
        if len(self.produtos) == 0:
            print("Carrinho vazio.")
        else:
            print("Produtos no carrinho:")
            for produto in self.produtos:
                print(f"Código: {produto.codigo}, Nome: {produto.nome}, Preço: {produto.preco}")

# Função para exibir o menu
def exibir_menu():
    print("----- Pet Shop -----")
    print("1. Adicionar produto ao carrinho")
    print("2. Calcular total da compra")
    print("3. Mostrar carrinho")
    print("4. Sair")

# Função principal
def main():
    carrinho = Carrinho()
    produtos = [
        Produto(1, "Ração para cães", 160.0),
        Produto(2, "Ração para gatos", 140.0),
        Produto(3, "Coleira", 15.0),
        Produto(4, "Brinquedo para cães", 20.0),
        Produto(5, "Brinquedo para gatos", 18.0)
    ]

    while True:
        exibir_menu()
        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            codigo = int(input("Digite o código do produto: "))
            produto = next((p for p in produtos if p.codigo == codigo), None)
            if produto:
                carrinho.adicionar_produto(produto)
                print("Produto adicionado ao carrinho.")
            else:
                print("Produto não encontrado.")

        elif opcao == "2":
            total = carrinho.calcular_total()
            print(f"Total da compra: R$ {total}")

        elif opcao == "3":
            carrinho.mostrar_carrinho()

        elif opcao == "4":
            print("Obrigado por utilizar o sistema. Volte sempre!")
            break

        else:
            print("Opção inválida. Por favor, selecione novamente.")

if __name__ == "__main__":
    main()
