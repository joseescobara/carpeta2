
from ast import Return
from logging import exception


def suma(a: int,b: int)-> int:
    x = a + b
    print(x) 



def división(num1, num2):
    """Función que calcula la multiplicación de dos números
    
    Args:
         num1(int,float,str): Número a multiplicar
         num2(int,float,str): Número a multiplicar

    Returns:
        int, float, str: multiplicar
    """
    try:
        resp = num1/num2
        return resp
    except exception as e:
        raise "Se está dividiendo por cero, por favor cambie los argumentos"



división(12,0)