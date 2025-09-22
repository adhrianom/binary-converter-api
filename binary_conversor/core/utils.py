import struct
import math

def float_to_binary_iee(num: float) -> dict:
    """
    Converte um numero float para sua representação binária IEEE 754 32 bits. (Separando inteiro de decimal)
    """
    binary_int = []
    binary_dec = []

    integer = math.floor(num)
    decimal = num - math.floor(num)

    # Parte inteira
    while integer > 1:
        rest_of_integer = integer % 2
        result_of_integer = integer // 2
        integer = result_of_integer
        binary_int.append(rest_of_integer)
    binary_int.append(integer)

    binary_int = binary_int[::-1]  # Inverte a lista

    # Parte decimal
    count = 0
    while decimal > 0 and count < 5:  # Limita a 5 casa decimais
        result_of_decimal = decimal * 2
        if result_of_decimal >= 1:
            binary_dec.append(1)
            decimal = result_of_decimal - 1
        else:
            binary_dec.append(0)
            decimal = result_of_decimal
        count += 1

    return {
        "original": num,
        "binary_int": binary_int,
        "binary_dec": binary_dec
    }