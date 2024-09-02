def calculaPercentual(faturamento):

    total_faturamento = sum(faturamento.values())
    
#calcula e imprime o percentual de representação de cada estado
    percentuais = {}
    for estado, valor in faturamento.items():
        percentual = (valor / total_faturamento) * 100
        percentuais[estado] = percentual
    
    return percentuais

def main():
#faturamento por estado
    faturamento = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    
    percentuais = calculaPercentual(faturamento)
    
    # Exibe os percentuais de representação
    print("Percentual de representação de cada estado no faturamento total:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

if __name__ == "__main__":
    main()
