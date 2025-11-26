import xmltodict

# -------------------------------------------------------------
# Função: Lê o arquivo moedas.xml e retorna um dicionário
# contendo todas as moedas disponíveis.
# -------------------------------------------------------------
def nomes_moedas():
    # Abre o arquivo XML em modo binário (rb = read binary)
    with open("moedas.xml", "rb") as arquivo_moedas:
        # Converte o XML para um dicionário Python
        dic_moedas = xmltodict.parse(arquivo_moedas)

    # Dentro do XML, os dados ficam armazenados na chave "xml"
    moedas = dic_moedas["xml"]
    return moedas


# -------------------------------------------------------------
# Função: Lê o arquivo conversoes.xml e transforma os pares
# de conversão (ex: "USD-BRL") em um dicionário organizado.
#
# Exemplo de saída:
# {
#     "USD": ["BRL", "EUR"],
#     "BRL": ["USD"]
# }
# -------------------------------------------------------------
def conversoes_disponiveis():
    # Abre o arquivo XML de conversões
    with open("conversoes.xml", "rb") as arquivo_conversoes:
        dic_conversoes = xmltodict.parse(arquivo_conversoes)

    # Os pares de conversão estão dentro da chave "xml"
    conversoes = dic_conversoes["xml"]

    # Dicionário final que será retornado
    dic_conversoes_disponiveis = {}

    # Cada item do XML é algo como "USD-BRL"
    for par_conversao in conversoes:
        # Separa "USD-BRL" em duas variáveis: moeda_origem e moeda_destino
        moeda_origem, moeda_destino = par_conversao.split("-")

        # Caso a moeda de origem já exista no dicionário:
        # adicionamos mais uma moeda de destino à lista
        if moeda_origem in dic_conversoes_disponiveis:
            dic_conversoes_disponiveis[moeda_origem].append(moeda_destino)
        else:
            # Caso ainda não exista, criamos uma nova lista
            dic_conversoes_disponiveis[moeda_origem] = [moeda_destino]

    # Retorna o dicionário organizado
    return dic_conversoes_disponiveis
