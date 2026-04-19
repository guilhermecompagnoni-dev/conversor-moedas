def converter(valor, moeda_origem, moeda_destino):
    taxas = {
        "USD": 1.0,
        "BRL": 5.0,
        "EUR": 0.9
    }

    if moeda_origem not in taxas or moeda_destino not in taxas:
        raise ValueError("Moeda inválida")

    valor_em_usd = valor / taxas[moeda_origem]
    valor_convertido = valor_em_usd * taxas[moeda_destino]

    return round(valor_convertido, 2)


if __name__ == "__main__":
    valor = float(input("Digite o valor: "))
    origem = input("Moeda origem (USD, BRL, EUR): ")
    destino = input("Moeda destino (USD, BRL, EUR): ")

    resultado = converter(valor, origem, destino)
    print(f"Valor convertido: {resultado}")