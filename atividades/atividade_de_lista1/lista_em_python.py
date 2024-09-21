def analise_vendas(vendas):
    # Calcule o total de vendas e realize a média mensal:
    total_vendas = sum(vendas)

    media_vendas = total_vendas / len(vendas)

    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Entrada como uma única string, sem a necessidade de lista
    entrada = "120, 150, 170, 130, 200, 250, 180, 220, 210, 160, 140, 190"
    
    # Converta a string em uma lista de inteiros, separando por vírgula e removendo espaços
    vendas = list(map(int, entrada.split(',')))
    return vendas

vendas = obter_entrada_vendas()

print(analise_vendas(vendas))
