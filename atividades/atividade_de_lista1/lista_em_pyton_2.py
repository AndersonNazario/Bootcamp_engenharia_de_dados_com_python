def analise_vendas(vendas):
    # Calcule o total de vendas e realize a média mensal:
    total_vendas = sum(vendas)

    media_vendas = total_vendas / len(vendas)

    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Use uma lista de vendas diretamente
    entrada = ["120", "150", "170", "130", "200", "250", "180", "220", "210", "160", "140", "190"]
    vendas = list(map(int, entrada.split(',')))
    # Já que `entrada` já é uma lista de inteiros, não é necessário o `split()` e `map()`
    vendas = entrada
    return vendas

vendas = obter_entrada_vendas()

print(analise_vendas(vendas))