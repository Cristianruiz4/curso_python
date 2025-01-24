# archivo con todas las funciones necesarias para la aplicacion "linea"

def calcular_y(x, m, b):
    '''
    b: interseccion en y
    regresa el valor de y
    '''

    return (m*x) + b

def test_linea():

    '''
    Prueba de funcionamiento de calcular_y
    '''

    return calcular_y(0,2,3)

    if __name__ == '__main__':
        if test_linea() == 3:
            print('Test exitoso')
        else:
            print('Test fallido')