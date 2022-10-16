from fractions import Fraction


def NumeroFraccionario(numero_decimal):
    if type (numero_decimal) != float or numero_decimal >=1 or numero_decimal < 0: return None
    elif numero_decimal == 0: return 0
    lim_decimales = 24
    lista_binario = []
    
    while numero_decimal > 0 and lim_decimales > 0:
        lista_binario.append(int(numero_decimal * 2))
        numero_decimal = numero_decimal * 2 - int(numero_decimal * 2)
        lim_decimales -= 1
        
    numero_binario = '0.'
    
    for num in lista_binario:
        numero_binario += str(num)
    return numero_binario

for i in range (2,10):
    print('Fraccion 1/', i, ':', 1/i, 'y en binario:', NumeroFraccionario(1/i))