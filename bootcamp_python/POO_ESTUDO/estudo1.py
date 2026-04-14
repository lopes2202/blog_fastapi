# Lê a linha de entrada e separa os produtos em uma lista
produtos = input("").strip().split()

qntd_produto = {
    
}

# TODO: Crie uma estrutura para contar quantas vezes cada produto aparece na lista
# Dica: Use um laço para percorrer a lista e atualizar a contagem de cada produto
 
# Inicialize variáveis para armazenar o produto mais frequente e sua contagem
mais_frequente = None
maior_contagem = -1

# Percorra a lista original para garantir o critério de desempate (primeira ocorrência)
for produto in produtos:
    qntd_produto[produto] = qntd_produto.get(produto, 0) + 1
    if qntd_produto[produto] > maior_contagem:
        mais_frequente = produto
        maior_contagem =  qntd_produto[produto]
# Imprima o produto mais frequente
print(mais_frequente)