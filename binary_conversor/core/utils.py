import struct
import math

def float_to_binary_iee(num: float) -> dict:
    """
    Converte um numero float para sua representação binária IEEE 754 32 bits. (Separando inteiro de decimal)
    """

    ## ZERO CASE
    if num == 0:
        print("0 00000000 00000000000000000000000")
        exit()

    binary_int= [] ## LIST TO STORE INTEGER BINARY VALUES
    binary_decimal= [] ## LIST TO STORE DECIMAL BINARY VALUES

    decimal = abs(num) - math.floor(abs(num)) ## 5.75 - 5 = 0.75
    integer = math.floor(abs(num)) ## 5

    # SIGNAL
    signal = 0 if num >= 0 else 1 ## 0 FOR POSITIVE, 1 FOR NEGATIVE

    ## BINARY FOR INTEGER PART
    if integer == 0:
        binary_int.append(0)
    else:
        while integer > 1:
            rest_of_integer = integer % 2
            integer //= 2
            binary_int.append(rest_of_integer)
        binary_int.append(integer)
    binary_int.reverse() ## REPLACE THE LIST TO GET THE RIGHT ORDER

    ## BINARY FOR DECIMAL PART
    count = 0
    while decimal != 0 and count < 30: ## LIMIT TO 30 DECIMAL PLACES
        result_of_decimal = decimal * 2
        if result_of_decimal >= 1:
            binary_decimal.append(1)
            decimal = result_of_decimal - 1
        else:
            binary_decimal.append(0)
            decimal = result_of_decimal
        count += 1

    ## FULL BINARY NUMBER
    full_binary = binary_int + binary_decimal

    ## FIND THE FIRST "1" TO NORMALIZE
    if 1 in binary_int:
        first_one_index = binary_int.index(1)
        exponent_real = len(binary_int) - first_one_index - 1
        mantissa_bits = binary_int[first_one_index + 1:] + binary_decimal ## BITS AFTER THE FIRST "1"
    else:
        first_one_index = binary_decimal.index(1)
        exponent_real = -(first_one_index + 1)
        mantissa_bits = binary_decimal[first_one_index + 1:] ## BITS AFTER THE FIRST "1"

    ## EXPONENTIAL BIAS
    bias = 127 ## FOR 32 BITS
    exponent_biased = exponent_real + bias

    ## EXPONENT BINARY STRING (8 BITS)
    exponent= [] ## LIST TO STORE EXPONENT BINARY VALUES
    temp = exponent_biased
    while temp > 1:
        exponent.append(temp % 2)
        temp //= 2
    exponent.append(temp)
    exponent.reverse() ## REPLACE THE LIST TO GET THE RIGHT ORDER
    exponent_str = ''.join(str(bit) for bit in exponent).zfill(8) ## FILL WITH ZEROS TO THE LEFT TO GET 8 BITS 

    ## MANTISSA (23 BITS)
    mantissa = ''.join(str(bit) for bit in mantissa_bits)
    mantissa = mantissa.ljust(23, '0')[:23] ## FILL WITH ZEROS TO THE RIGHT TO GET 23 BITS

    ## FINAL OUTPUT
    ieee32 = f"{signal} {exponent_str} {mantissa}"

    return {
        "signal": signal,
        "exponent": exponent_str,
        "mantissa": mantissa
    }