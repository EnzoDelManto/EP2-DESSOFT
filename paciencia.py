#BIBLIOTECAS
import random
import runpy

#FUNÇÕES
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

def empilha(lista, i_ori, i_des):
    y = lista[i_ori]
    lista.remove(y)
    lista.remove(lista[i_des])
    lista.insert(i_des, y)
    return lista

def possui_movimentos_possiveis(baralho):
    len_b = len(baralho)
    while len_b > 0:
        len_b -= 1
        if lista_movimentos_possiveis(baralho, len_b) != []:
            return True
    else:
        return False

#INSTRUÇÕES JOGO
print('''\033[1;32;40mPaciência Acordeão

O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.

Existem apenas dois movimentos possíveis:

-Empilhar uma carta sobre a carta imediatamente anterior  
-Ou empilhar uma carta sobre a terceira carta anterior. 

Para que um movimento possa ser realizado uma das duas condições abaixo deve ser atendida: 

-As duas cartas possuírem o mesmo valor
-Ou as duas cartas possuírem o mesmo naipe.

Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada. 

Bom jogo!
''')

jogo_ativo = True
while jogo_ativo:
#CRIAR BARALHO ALEATÓRIO
    baralho = cria_baralho()
    for n, carta in enumerate(baralho):
        k = n+1
        if extrai_naipe(carta) == '♥':
            print('\033[1;31;40m{0}.'.format(k),carta)
        elif extrai_naipe(carta) == '♦':
            print('\033[1;35;40m{0}.'.format(k),carta)
        elif extrai_naipe(carta) == '♣':
            print('\033[1;32;40m{0}.'.format(k),carta)
        elif extrai_naipe(carta) == '♠':
            print('\033[1;34;40m{0}.'.format(k),carta)

    #ESCOLHER CARTA
    while len(baralho) > 1 and possui_movimentos_possiveis(baralho) != False:
        escolha_carta = int(input('\033[1;37;40mDigite o número da carta desejada:(1 a {0}):'.format(len(baralho))))

#SE O NÚMERO DA CARTA FOR INVÁLIDO
        while escolha_carta > len(baralho) or escolha_carta < 1:
            escolha_carta = int(input('\033[1;37;40mDigite o número de uma carta válida(1 a {0}):'.format(len(baralho))))
        indice = escolha_carta-1
        verifica = lista_movimentos_possiveis(baralho,indice)
        bind = baralho[indice]

#SE A CARTA NÃO PUDER SE MOVER
        while verifica == []:
            reescolher = int(input('Essa carta não pode se mover. Escolha outra: '))
            indice2 = reescolher-1
            verifica = lista_movimentos_possiveis(baralho,indice2)

#SE A CARTA SOMENTE PUDER EMPILHAR NO VIZINHO IMEDIATAMENTE ANTERIOR
        if verifica == [1]:
            empilha(baralho, indice, indice-1)

            for n, carta in enumerate(baralho):
                k = n+1
                if extrai_naipe(carta) == '♥':
                    print('\033[1;31;40m{0}.'.format(k),carta)
                elif extrai_naipe(carta) == '♦':
                    print('\033[1;35;40m{0}.'.format(k),carta)
                elif extrai_naipe(carta) == '♣':
                    print('\033[1;32;40m{0}.'.format(k),carta)
                elif extrai_naipe(carta) == '♠':
                    print('\033[1;34;40m{0}.'.format(k),carta)

#SE A CARTA SOMENTE PUDER EMPILHAR NO TERCEIRO VIZINHO ANTERIOR
        elif verifica == [3]:
            empilha(baralho, indice, indice-3)

            for n, carta in enumerate(baralho):
                k = n+1
                if extrai_naipe(carta) == '♥':
                    print('\033[1;31;40m{0}.'.format(k),carta)
                elif extrai_naipe(carta) == '♦':
                    print('\033[1;35;40m{0}.'.format(k),carta)
                elif extrai_naipe(carta) == '♣':
                    print('\033[1;32;40m{0}.'.format(k),carta)
                elif extrai_naipe(carta) == '♠':
                    print('\033[1;34;40m{0}.'.format(k),carta)

#SE A CARTA SOMENTE PUDER EMPILHAR EM AMBOS
        elif verifica == [1,3]:
            escolha = int(input('Sobre qual carta você quer empilhar o {0}? Digite o número da carta: '.format(bind)))

#SE A CARTA ESCOLHIDA FOR INVÁLIDA
            while escolha != indice and escolha != indice-2:
                escolha = int(input('Carta inválida, digite novamente:'))

#SE O USUÁRIO ESCOLHER O VIZINHO IMEDIATAMENTE ANTERIOR
            if escolha == indice:
                empilha(baralho, indice, indice-1)

                for n, carta in enumerate(baralho):
                    k = n+1
                    if extrai_naipe(carta) == '♥':
                        print('\033[1;31;40m{0}.'.format(k),carta)
                    elif extrai_naipe(carta) == '♦':
                        print('\033[1;35;40m{0}.'.format(k),carta)
                    elif extrai_naipe(carta) == '♣':
                        print('\033[1;32;40m{0}.'.format(k),carta)
                    elif extrai_naipe(carta) == '♠':
                        print('\033[1;34;40m{0}.'.format(k),carta)

#SE O USUÁRIO ESCOLHER O TERCEIRO VIZINHO ANTERIOR
            elif escolha == indice-2:
                empilha(baralho, indice, indice-3)
                for n, carta in enumerate(baralho):
                    k = n+1
                    if extrai_naipe(carta) == '♥':
                        print('\033[1;31;40m{0}.'.format(k),carta)
                    elif extrai_naipe(carta) == '♦':
                        print('\033[1;35;40m{0}.'.format(k),carta)
                    elif extrai_naipe(carta) == '♣':
                        print('\033[1;32;40m{0}.'.format(k),carta)
                    elif extrai_naipe(carta) == '♠':
                        print('\033[1;34;40m{0}.'.format(k),carta)

#GANHOU O JOGO
    if len(baralho) == 1:
        print('Parabéns! Você venceu!')
        jogo_ativo = False

#PERDEU O JOGO
    elif possui_movimentos_possiveis(baralho) == False:
        print('Você perdeu! ):')
        jogo_ativo = False

#JOGAR NOVAMENTE?
    restart = str(input('Quer jogar novamente?(s/n): '))
    while restart != 's' and restart != 'n':
        restart = str(input('Resposta inválida, digite novamente(s/n)'))
    if restart == "s":
        jogo_ativo = True
    elif restart == "n":
        print('Até mais!')
        jogo_ativo = False
