import faturamento.json

def processar_faturamento(arquivo_json):
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)
    
#dias com faturamento
    faturamentos = [d['faturamento'] for d in dados if d['faturamento'] > 0]

    if not faturamentos:
        print("Não há dados de faturamento disponíveis.")
        return

#menor e o maior valor de faturamento
    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)

#media mensal (ignora zeros)
    media_mensal = sum(faturamentos) / len(faturamentos)

#conta dias com faturamento superior a media
    dias_acima_media = sum(1 for f in faturamentos if f > media_mensal)

    print(f"Menor valor de faturamento: R$ {menor_faturamento}")
    print(f"Maior valor de faturamento: R$ {maior_faturamento}")
    print(f"Número de dias com faturamento superior à média: {dias_acima_media}")

if __name__ == "__main__":
    processar_faturamento('faturamento.json')