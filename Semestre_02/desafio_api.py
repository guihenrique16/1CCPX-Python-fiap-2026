# def eh_sucesso(codigo):
#     """Retorna True se o codigo HTTP estiver entre 200 e 299."""
#     return 200 <= codigo <= 299

# def calcular_percentual_sucesso(requisicoes):
#     """Calcula o percentual de requisicoes bem-sucedidas de uma lista."""
#     total = len(requisicoes)
#     if total == 0:
#         return 0.0
#     sucessos = sum(1 for codigo in requisicoes if eh_sucesso(codigo))
#     return (sucessos / total) * 100

# def contar_erros(requisicoes):
#     """Conta quantos codigos de erro (fora de 200-299) existem na lista."""
#     return sum(1 for codigo in requisicoes if not eh_sucesso(codigo))

# def teve_dois_erros_seguidos(requisicoes):
#     """Verifica se existem dois erros consecutivos na lista de requisicoes."""
#     for i in range(len(requisicoes) - 1):
#         if not eh_sucesso(requisicoes[i]) and not eh_sucesso(requisicoes[i + 1]):
#             return True
#     return False

# def classificar_endpoint(requisicoes):
#     """Classifica o endpoint como CRITICO, ESTAVEL ou INSTAVEL."""
#     if teve_dois_erros_seguidos(requisicoes):
#         return "CRITICO"
#     percentual = calcular_percentual_sucesso(requisicoes)
#     if percentual >= 80:
#         return "ESTAVEL"
#     return "INSTAVEL"

# def analisar_api(endpoints, status):
#     """Executa a analise completa da API e retorna um relatorio."""
#     relatorio = []
#     for nome, requisicoes in zip(endpoints, status):
#         relatorio.append({
#             "endpoint": nome,
#             "percentual_sucesso": calcular_percentual_sucesso(requisicoes),
#             "total_erros": contar_erros(requisicoes),
#             "dois_erros_seguidos": teve_dois_erros_seguidos(requisicoes),
#             "classificacao": classificar_endpoint(requisicoes)
#         })
#     return relatorio

# def endpoint_com_mais_erros(relatorio):
#     """Retorna o endpoint com o maior numero de erros."""
#     return max(relatorio, key=lambda item: item["total_erros"])

# def exibir_relatorio(relatorio):
#     """Imprime o relatorio de forma organizada."""
#     print("=" * 55)
#     print("RELATORIO DE MONITORAMENTO DA API")
#     print("=" * 55)
#     for item in relatorio:
#         print(f"\nEndpoint: {item['endpoint']}")
#         print(f"  Sucesso: {item['percentual_sucesso']:.1f}%")
#         print(f"  Total de erros: {item['total_erros']}")
#         print(f"  Dois erros seguidos: {'Sim' if item['dois_erros_seguidos'] else 'Nao'}")
#         print(f"  Classificacao: {item['classificacao']}")

#     pior = endpoint_com_mais_erros(relatorio)
#     print("\n" + "-" * 55)
#     print(f"Endpoint com mais erros: {pior['endpoint']} ({pior['total_erros']} erros)")
#     print("=" * 55)


# if __name__ == "__main__":
#     endpoints = ["/login", "/produtos", "/pedidos"]
#     status = [
#         [200, 200, 401, 200, 500],
#         [200, 200, 200, 200, 200],
#         [201, 500, 502, 201, 500]
#     ]

#     relatorio = analisar_api(endpoints, status)
#     exibir_relatorio(relatorio)


endpoints = ["/login", "/produtos", "/pedidos"]
status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]

def sucesso(codigo):
    return codigo >= 200 and codigo <= 299

def erros_seguidos(requisicoes): 
    for i in range(len(requisicoes) - 1):
        codigo_atual = requisicoes[i]
        prox_codigo = requisicoes[i+1]

        if not sucesso(codigo_atual) and not sucesso(prox_codigo):
            return True
    return False

def analisar_endpoint(requisicoes):
    qtd_sucessos = 0

    for codigo in requisicoes:
        if sucesso(codigo):
            qtd_sucessos += 1

    qtd_total_req = len(requisicoes)
    qtd_erros = qtd_total_req - qtd_sucessos
    percentual_sucessos = (qtd_sucessos/ qtd_total_req) * 100

    tem_erros_seguidos = erros_seguidos(requisicoes)

    if tem_erros_seguidos:
        classificacao = "CRITICO"
    elif percentual_sucessos >= 80:
        classificacao = "ESTAVEL"
    else:
        classificacao = "CRITICO"

    return(qtd_sucessos, qtd_erros, percentual_sucessos, classificacao)

#PERCORRENDO    
maior_qtd_erros = -1
endpoint_maior_erro = "" 

for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    reqs_endpoint = status[i]

    sucessos, erros, percentual, classificacao = analisar_endpoint(reqs_endpoint)
    
    print(f"Endpoint: {nome_endpoint}")
    print(f"Requisições: {reqs_endpoint}")
    print(f"Sucessos: {sucessos}")
    print(f"Erros: {erros}")
    print(f"% de sucessos: {percentual}")
    print(f"Status: {classificacao}")
    print("*" * 50)

    if erros > maior_qtd_erros:
        maior_qtd_erros = erros
        endpoint_maior_erro = nome_endpoint

print(f"Endpoint + erros: {endpoint_maior_erro} ({maior_qtd_erros})")


