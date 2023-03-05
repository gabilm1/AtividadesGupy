def calcular_faturamento(vetor):
    # Inicializa as variáveis de controle
    menor_valor = float('inf')
    maior_valor = float('-inf')
    soma_faturamento = 0
    dias_acima_media = 0

    # Percorre o vetor de faturamento diário
    for item in vetor:
        valor = item["valor"]
        dia = item["dia"]

        # Verifica se o valor é o menor ou o maior já encontrado
        if valor < menor_valor:
            menor_valor = valor
        if valor > maior_valor:
            maior_valor = valor

        # Soma o valor para calcular a média
        soma_faturamento += valor

    # Calcula a média mensal de faturamento
    media_faturamento = soma_faturamento / len(vetor)

    # Conta os dias em que o valor de faturamento diário foi superior à média mensal
    for item in vetor:
        valor = item["valor"]
        if valor > media_faturamento:
            dias_acima_media += 1

    # Retorna as informações calculadas
    return {
        "menor_valor": menor_valor,
        "maior_valor": maior_valor,
        "dias_acima_media": dias_acima_media
    }


#Para testar a função é só inserir os dados de teste

vetor_faturamento = [
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612},
    {"dia": 7, "valor": 0.0},
    {"dia": 8, "valor": 42889.2258},
    {"dia": 9, "valor": 46251.174},
    {"dia": 10, "valor": 11191.4722},
    {"dia": 11, "valor": 0.0},
    {"dia": 12, "valor": 0.0},
    {"dia": 13, "valor": 3847.4823},
    {"dia": 14, "valor": 373.7838},
    {"dia": 15, "valor": 2659.7563},
    {"dia": 16, "valor": 48924.2448},
    {"dia": 17, "valor": 18419.2614},
    {"dia": 18, "valor": 0.0},
    {"dia": 19, "valor": 0.0},
    {"dia": 20, "valor": 35240.1826},
    {"dia": 21, "valor": 43829.1667},
    {"dia": 22, "valor": 18235.6852},
    {"dia": 23, "valor": 4355.0662},
    {"dia": 24, "valor": 13327.1025},
    {"dia": 25, "valor": 0.0},
    {"dia": 26, "valor": 0.0},
	{"dia": 27, "valor": 25681.8318},
	{"dia": 28, "valor": 1718.122},
	{"dia": 29, "valor": 13220.495},
    {"dia": 30,"valor": 8414.61}
]
   
