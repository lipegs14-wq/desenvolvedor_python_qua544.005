cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Porto Alegre"]

cidades_ordenadas = sorted(cidades)
for cidade in cidades_ordenadas:
    print(cidade)  # Imprime cada cidade em ordem alfabética

    cidades_ordenadas= sorted(cidades, reverse=True)

    for cidade in cidades_ordenadas:
        print(cidade)  # Imprime cada cidade em ordem alfabética reversa