import random

historico = []

def gerar_multiplicador():
    r = random.random()

    if r < 0.50:
        return round(random.uniform(1.00, 1.50), 2)
    elif r < 0.80:
        return round(random.uniform(1.50, 3.00), 2)
    elif r < 0.95:
        return round(random.uniform(3.00, 10.00), 2)
    else:
        return round(random.uniform(10.00, 50.00), 2)

def nova_rodada():
    multi = gerar_multiplicador()
    historico.append(multi)

    if len(historico) > 20:
        historico.pop(0)

    return multi
