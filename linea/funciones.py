# archivo con todas las funciones necesarias para la aplicacion "linea"
import matplotlib.pyplot as plt

def calcular_y(x:float, m:float, b:float)->float:
    '''
    b: interseccion en y
    regresa el valor de y
    '''

    return m*x + b

def grafica_linea(X:list, Y:list, m:float, b:float):
    '''
    Grafica con una linea recta
    X: Lista de valores de X
    Y: Lista de valores de Y
    Regresa nada
    '''
    plt.plot(X,Y)
    plt.title(f'Línea con pendiente {m} y ordenada al origeb {b}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

def test_linea():

    '''
    Prueba de funcionamiento de calcular_y
    ''' 
    return calcular_y(0.0, 2.0, 3.0)

if __name__ == '__main__':
    if test_linea() == 3.0:
        print('Test exitoso')
    else:
        print('Test fallido')