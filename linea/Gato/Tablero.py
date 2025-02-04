'''
Tablero.py: Dibua el tablero del juego de el gato
'''
import random

def dibuja_tablero(simbolos:dict):
    '''
    Dibuja el tablero del juego de el gato
    '''
    print(f'''
    {simbolos['1']} | {simbolos['2']} | {simbolos['3']}
    ---------
    {simbolos['4']} | {simbolos['5']} | {simbolos['6']}
    ---------
    {simbolos['7']} | {simbolos['8']} | {simbolos['9']}
    ''')

def ia(simbolos:dict):
    '''Juega la maquina'''
    ocupado = True
    while ocupado == True:
        x = random.choice(list(simbolos.keys()))
        if simbolos[x] not in ['X','O']:
            simbolos[x] = 'O'
            ocupado = False

def usuario(simbolos:dict):
    '''Juego el Usuario'''
    lista_numeros = [str(i) for i in range(1, 10)]
    ocupado = True
    while ocupado == True:
        x = input('Ingresa e número de la casilla:')
        if (x in lista_numeros):

            if simbolos[x] not in ['X','O']: 
                simbolos[x] = 'X'
                ocupado = False
            else:
                print('Casilla ocupada')
        else:
            print('Numero no valido')

def juego(simbolos:dict):
    '''Juego del gato'''

    lista_combinaciones = [
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9'],
        ['1','4','7'],
        ['2','5','8'],
        ['3','6','9'],
        ['1','5','9'],
        ['3','5','7']
    ]

def checa_winner(simbolos:dict, combinaciones:list):
    '''Checa si hay ganador'''
    for c in combinaciones:
        if simbolos[c[0]] == simbolos[c[1]] == simbolos[c[2]]:
            return simbolos[c[0]]
    return None

if __name__ == '__main__':
    numeros = [str(x) for x in range(1, 10)]
    simbolos = {x:x for x in numeros}
    dibuja_tablero(simbolos)
    ia(simbolos)
    dibuja_tablero(simbolos)
    usuario(simbolos)
    dibuja_tablero(simbolos)
    '''
    X = random.choice(numeros)
    numeros.remove(X)
    simbolos[X] = 'X'
    dibuja_tablero(simbolos)
    O = random.choice(numeros)
    numeros.remove(O)
    simbolos[O] = 'O'
    dibuja_tablero(simbolos)
    print(numeros)
    '''