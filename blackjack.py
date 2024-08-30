import random
 
cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K','A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
          'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K','A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
          'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K','A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
          'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K','A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
          'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K','A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
valores = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
dinero = 100
 
def calcular_suma(cartas):
    total = sum([valores[carta] for carta in cartas])
    aces = cartas.count('A')
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total
 
def blackjack():
    global dinero
    while dinero > 0:
        cartasJugador = []
        cartasCrupier = []
 
        print(f'Tienes {dinero} dólares')
        try:
            apuesta = int(input('Cuánto quieres apostar? '))
            if apuesta <= 0:
                print('La apuesta debe ser mayor a 0.')
                continue
            if apuesta > dinero:
                print('No tienes suficiente dinero')
                continue
        except ValueError:
            print('Ingresa un valor numérico válido.')
            continue
 
        dinero -= apuesta
        print('Repartiendo cartas...')
        cartasJugador.extend([random.choice(cartas), random.choice(cartas)])
        cartasCrupier.extend([random.choice(cartas), random.choice(cartas)])
 
        print(f'Tus cartas: {cartasJugador}, suma: {calcular_suma(cartasJugador)}')
        print(f'Carta del crupier: {cartasCrupier[0]}')
 
        if calcular_suma(cartasJugador) == 21 and calcular_suma(cartasCrupier) == 21:
                print('Empate, ambos tienen blackjack')
                dinero += apuesta
        elif calcular_suma(cartasCrupier) == 21 and len(cartasCrupier) > 2:
                print(f'Cartas del crupier: {cartasCrupier}, suma: {calcular_suma(cartasCrupier)}')
                print(f'Perdiste, tus cartas suman {jugador_suma}')
        elif calcular_suma(cartasJugador) == 21 and len(cartasJugador) == 2:
            print('¡Felicitaciones, tienes un blackjack!')
            print(f'Las cartas del crupier son {cartasCrupier}')
            dinero += apuesta * 2.5
        elif calcular_suma(cartasJugador) == 21 and calcular_suma(cartasCrupier) <  21:
            print(f'Ganaste, tus cartas suman {jugador_suma}')
            dinero += apuesta * 2
        elif calcular_suma(cartasJugador) == 21 and calcular_suma(cartasCrupier) >  21:
            print(f'Ganaste, el crupier se pasó. Las cartas del crupier suman {crupier_suma}')
            dinero += apuesta * 2
        elif calcular_suma(cartasCrupier) == 21 and len(cartasCrupier) == 2:
                print(f'Perdiste, el crupier tiene blackjack. Las cartas del crupier son {cartasCrupier}')
        
        else:
            # Turno del jugador
            while calcular_suma(cartasJugador) < 21:
                accion = input('¿Quieres otra carta? (s/n) ')
                if accion.lower() == 's':
                    cartasJugador.append(random.choice(cartas))
                    print(f'Tus cartas: {cartasJugador}, suma: {calcular_suma(cartasJugador)}')
                else:
                    break
 
            # Turno del crupier
            while calcular_suma(cartasCrupier) < 17:
                cartasCrupier.append(random.choice(cartas))
                print(f'Cartas del crupier: {cartasCrupier}, suma: {calcular_suma(cartasCrupier)}')
 
            # Resultados
            jugador_suma = calcular_suma(cartasJugador)
            crupier_suma = calcular_suma(cartasCrupier)
 
            if jugador_suma > 21:
                print(f'Perdiste, te pasaste. Tus cartas suman {jugador_suma}')
            elif crupier_suma > 21:
                print(f'Ganaste, el crupier se pasó. Las cartas del crupier suman {crupier_suma}')
                dinero += apuesta * 2
            elif jugador_suma > crupier_suma:
                print(f'Ganaste, tus cartas suman {jugador_suma}')
                dinero += apuesta * 2
            elif jugador_suma < crupier_suma:
                if len(cartasCrupier) == 2:
                    print(f'Cartas del crupier: {cartasCrupier}, suma: {calcular_suma(cartasCrupier)}')
                    print(f'Perdiste, tus cartas suman {jugador_suma}')
            else:
                print(f'Empate, ambos tienen {jugador_suma}')
                dinero += apuesta
    print('Te has quedado sin dinero. ¡Gracias por jugar!')
 
blackjack()