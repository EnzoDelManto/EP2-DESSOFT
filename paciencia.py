import random
def cria_baralho():
    baralho = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦']
    random.shuffle(baralho)
    return baralho

def extrai_naipe(carta):
    if len(carta) == 2:
        return carta[1]
    else:
        return carta[2]

def extrai_valor(carta):
    if len(carta) == 2:
        return carta[0]
    else:
        return carta[0] + carta[1]

def lista_movimentos_possiveis(baralho, i):
    movs = []
    ct = baralho[i]
    
    if i == 0:
        movs = []
    elif 3 > i > 0:
        ant1 = baralho[i-1]
        if extrai_naipe(ct) != extrai_naipe(ant1) and extrai_valor(ct) != extrai_valor(ant1):
            movs = []
        elif extrai_naipe(ct) == extrai_naipe(ant1) or extrai_valor(ct) == extrai_valor(ant1):
            movs.append(1)

    elif i >= 3:
        ant1 = baralho[i-1]
        ant3 = baralho[i-3]
        if extrai_naipe(ct) != extrai_naipe(ant3) and extrai_naipe(ct) != extrai_naipe(ant1) and extrai_valor(ct) != extrai_valor(ant3) and extrai_valor(ct) != extrai_valor(ant1):
            movs = []

        if extrai_naipe(ct) == extrai_naipe(ant1) or extrai_valor(ct) == extrai_valor(ant1):
            movs.append(1)
                
        if extrai_naipe(ct) == extrai_naipe(ant3) or extrai_valor(ct) == extrai_valor(ant3):
            movs.append(3)
    return movs