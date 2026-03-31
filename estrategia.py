from simulador import historico

def analisar_rodadas():
    if len(historico) < 5:
        return "AGUARDAR"

    ultimas = historico[-5:]

    baixos = sum(1 for x in ultimas if x < 2)
    altos = sum(1 for x in ultimas if x >= 2)

    if baixos >= 4:
        return "ENTRAR"
    elif altos >= 4:
        return "EVITAR"
    else:
        return "NEUTRO"
