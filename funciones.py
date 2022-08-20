from ast import Return


def suma(a: int,b: int)-> int:
    x = a + b
    print(x) 



def multiplicación(num1, num2):
    """Función que calcula la multiplicación de dos números
    
    Args:
         num1(int,float,str): Número a multiplicar
         num2(int,float,str): Número a multiplicar

    Returns:
        int, float, str: multiplicar
    """
    resp = num1*num2
    return resp

k = multiplicación(3,5)
print(k)   