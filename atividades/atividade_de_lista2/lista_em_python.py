def produto_mais_vendido(produtos):
    # Dicionário para contar a frequência de cada produto
    contagem = {}
    
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
    
    max_produto = None
    max_count = 0
    
    # Encontre o produto com a maior contagem
    for produto, count in contagem.items():
        if count > max_count:
            max_produto = produto
            max_count = count
    
    return max_produto

def obter_entrada_produtos():
    # Entrada de produtos como uma única string
    entrada = "Impressora, Teclado, Monitor, Monitor, Teclado, Impressora, Impressora"
    
    # Converta a string em uma lista de produtos, separando por vírgula e removendo espaços extras
    produtos = [produto.strip() for produto in entrada.split(',')]
    return produtos

# Obter a lista de produtos
produtos = obter_entrada_produtos()

# Exibir o produto mais vendido
print(produto_mais_vendido(produtos))