import re

def identificar_bandeira(numero_cartao):
    """
    Identifica a bandeira do cartão de crédito com base no número do cartão.

    Parâmetros:
    numero_cartao (str): Número do cartão de crédito.

    Retorna:
    str: Nome da bandeira do cartão de crédito.
    """
    bandeiras = {
        'Visa': r'^4[0-9]{12}(?:[0-9]{3})?$',
    'MasterCard': r'^5[1-5][0-9]{14}$',
    'American Express': r'^3[47][0-9]{13}$',
    'Diners Club': r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$',
    'Discover': r'^6(?:011|5[0-9]{2})[0-9]{12}$',
    'HiperCard': r'^(6062|3841|6370|6371|6372)[0-9]{12}$',
    'Credshop': r'^(6014|6015|6016|6017|6018|6019)[0-9]{12}$',
    'Elo': r'^(4011|4312|4389|4576|4577|5041|5067|5090|6500|6516|6517|6518|6519)[0-9]{12,15}$',
    'Hiper': r'^(637|638|639|640|641|642|643|644|645|646|647|648|649|650|651|652|653|654|655|656|657|658|659|660|661|662|663|664|665|666|667|668|669|670|671|672|673|674|675|676|677|678|679|680|681|682|683|684|685|686|687|688|689|690|691|692|693|694|695|696|697|698|699)[0-9]{12,15}$',
    'Chase': r'^(4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})$'
    }

    for bandeira, padrao in bandeiras.items():
        if re.match(padrao, numero_cartao):
            return bandeira

    return 'Bandeira desconhecida'

if __name__ == "__main__":
    numero_cartao = input("Digite o número do cartão de crédito: ")
    bandeira = identificar_bandeira(numero_cartao)
    print(f"A bandeira do cartão é: {bandeira}")
