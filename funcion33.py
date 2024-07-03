def _init_(self, id_jugador, nombre, VALORANT, Fortnite, FiFa, tipo):
    self.id_jugador = id_jugador
    self.nombre = nombre
    self.VALORANT = VALORANT
    self.Fortnite = Fortnite
    self.FiFa = FiFa
    self.tipo = tipo

def _repr_(self):
    return f'{self.id_jugador}\t{self.nombre}\t{self.VALORANT}\t{self.Fortnite}\t{self.FiFa}\t{self.tipo}'

def registrar_puntajes(jugador):
    id_jugador = input('ingrese  el ID del jugador:')
    nombre = input('registre el nombre de los jugadores')
    VALORANT = int(input('ingrese el puntaje en VALORANT'))
    Fortnite = int(input('ingrese el puntaje en Fortnite'))
    FiFa = int(input('ingrese el puntaje en FiFa'))
    tipo = input('ingrese el tipo (principiante-avanzado-experto):')

    jugador = jugador(id_jugador,nombre, VALORANT, Fortnite, FiFa, tipo)
    jugador.append(jugador)
    print('puntaje registrado con exitpo\n')

def listar_todos_los_puntajes(jugador):
    print('nombre\tpuntaje\ttipo')
    for nombre, detalles in jugador.item():
        print(f'{nombre},{detalles['puntajes']},{detalles['tipo']}')
        print()

def imprimir_por_tipo(jugador):
    tipo = input('ingrese tipo para imprimir (principiante-avanzado-experto):')
    jugadores_filtrados = {nombre: detalles for nombre, detalles in jugador.item() if detalles['tipo'] == tipo}
    if jugadores_filtrados:
        with open (f'puntajes {tipo}.txt','W') as file:
            file.write ('Nombre\tPuntajes\tTipo\n')
            for nombre, detalles in jugadores_filtrados.items():
                file.write(f'{nombre}\t{detalles['puntaje']}\t{detalles['tipo']}\n')
                print(f'puntajes de tipo{tipo}guardados en puntajes_{tipo}.txt\n')
            else:
               print(f'no hay jugadores de ese tipo{tipo}')
       





