from simulador import nova_rodada
from estrategia import analisar_rodadas

saldo = 100
aposta = 5
meta_cashout = 1.8

def rodar_bot():
    global saldo

    resultado = nova_rodada()
    decisao = analisar_rodadas()

    print(f"\nRodada: {resultado}x")
    print(f"Decisão: {decisao}")

    if decisao == "ENTRAR":
        if resultado >= meta_cashout:
            ganho = aposta * (meta_cashout - 1)
            saldo += ganho
            print(f"✅ Ganhou: +{ganho:.2f}")
        else:
            saldo -= aposta
            print(f"❌ Perdeu: -{aposta}")
    else:
        print("⏸️ Fora da rodada")

    print(f"💰 Saldo: {saldo:.2f}")
