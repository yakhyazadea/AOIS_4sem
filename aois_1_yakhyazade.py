def decimal_to_binary(num):
    num = abs(num)
    array_binary = []
    result_array = [0 for i in range(8)]

    while num > 0:
        array_binary.append(num % 2)
        num = num // 2

    for index, i in enumerate(array_binary):
        result_array[7 - index] = i

    return result_array


def sum(num_1, num_2, bits):
    sum = [0 for i in range(bits)]
    i = bits-1
    carry = 0
    while i >= 0:
        sum[i] = num_1[i] + num_2[i] + carry
        carry = 0
        if sum[i] == 2:
            sum[i] = 0
            carry = 1
        elif sum[i] == 3:
            sum[i] = 1
            carry = 1
        i = i - 1

    return sum


def binary_to_decimal(num):
    num_decimal = 0
    i = 7
    while i > 0:

        num_decimal = num_decimal + num[i] * (2 ** (7 - i))
        i = i - 1

    if num[0] == 1:
        num_decimal = -num_decimal

    return num_decimal


def binary_to_ones_complement(num, bits):
    i = 0
    num = list(num)
    while i < bits:
        if num[i] == 0:
            num[i] = 1
        elif num[i] == 1:
            num[i] = 0
        i = i + 1
    return num


def decimal_to_twos_complement(num):
    num = abs(num)
    num = decimal_to_binary(num)
    num = binary_to_ones_complement(num, 8)
    num = add_one(num, 8)
    return num


def binary_to_twos_complement(num, bits):
    num = binary_to_ones_complement(num, bits)
    num = add_one(num, bits)
    return num


def add_one(num, bits):
    one_array = [0 for i in range(bits)]
    one_array[bits-1] = 1
    num = sum(num, one_array, bits)
    return num


def positive_positive(num_1, num_2):
    num_1 = decimal_to_binary(num_1)
    num_2 = decimal_to_binary(num_2)
    result = sum(num_1, num_2, 8)

    return result


def negative_negative(num_1, num_2):
    num_1 = decimal_to_twos_complement(num_1)
    num_2 = decimal_to_twos_complement(num_2)

    result = sum(num_1, num_2, 8)
    result = binary_to_twos_complement(result, 8)
    result[0] = 1
    print("X1:\n" + "".join(str(x) for x in num_1) + "\n")
    print("X2:\n" + "".join(str(x) for x in num_2) + "\n")
    return result


def negative_positive(num_1, num_2, sign):
    num_1 = decimal_to_twos_complement(num_1)
    num_2 = decimal_to_binary(num_2)
    result = sum(num_1, num_2, 8)
    if sign < 0:
        result = binary_to_twos_complement(result, 8)
        result[0] = 1
    print("X1:\n" + "".join(str(x) for x in num_1) + "\n")
    print("X2:\n" + "".join(str(x) for x in num_2) + "\n")
    return result


def positive_negative(num_1, num_2, sign):
    if type(num_1) == list:
        num_1 = add_zeros(num_1)
        num_2 = add_zeros(num_2)
        num_2 = binary_to_twos_complement(num_2, 8)
        result = sum(num_1, num_2, 8)
        if sign < 0:
            result = binary_to_twos_complement(result)
            result[0] = 1
    else:
        num_1 = decimal_to_binary(num_1)
        num_2 = decimal_to_twos_complement(num_2)
        result = sum(num_1, num_2, 8)
        if sign < 0:
            result = binary_to_twos_complement(result, 8)
            result[0] = 1
        print("X1:\n" + "".join(str(x) for x in num_1) + "\n")
        print("X2:\n" + "".join(str(x) for x in num_2) + "\n")

    return result

def multiply(num_1, num_2):

    result = [0 for i in range(8)]
    i = 0
    shift = 0
    while i <= 7:
        if num_2[7 - i] == 1:

            result = sum(result, shift_array(num_1, i), 8)

        i = i + 1
    return result

def shift_array(array, n):
    shifted_array = [0 for i in range(8)]
    i = 0
    while i <= 7:
        if (i+n) <= 7:
            shifted_array[i] = array[i + n]
        else:
            shifted_array[i] = 0
        i = i + 1
    return shifted_array


def remove_zeros(num):
    i = 0
    while i <= 7:
        if num[0] == 0 and num[i] == 0:
            num.pop(0)
        else:
            return num

    return num


def add_zeros(num):
    res = [0 for x in range(8)]
    for i in range(len(num)):
        res[8-len(num)+i] = num[i]


    return res


def divide(num_1, num_2):
    num_1 = remove_zeros(num_1)
    num_2 = remove_zeros(num_2)
    result = []
    temp = [num_1[0]]
    remainder = []

    for i in range(len(num_1)):
        if int("".join(str(x) for x in temp)) >= int("".join(str(x) for x in num_2)):
            result.append(1)
            remainder = positive_negative(temp, num_2, 1)

            temp = remainder
            if (i + 1) < len(num_1):
                temp.append(num_1[i + 1])
        else:
            result.append(0)
            if(i+1) < len(num_1):

                temp.append(num_1[i+1])

    result = add_zeros(result)
    fraction_result = calculate_fraction(temp, num_2)

    return result, fraction_result

def calculate_fraction(temp, num_2):
    result = []
    if int("".join(str(x) for x in temp)) > 0:
        temp.append(0)
        for i in range(25):
            if int("".join(str(x) for x in temp)) >= int("".join(str(x) for x in num_2)):
                result.append(1)
                remainder = positive_negative(temp, num_2, 1)

                temp = remainder
                temp.append(0)
            else:
                result.append(0)
                temp.append(0)
    else:
        result = [0]

    return result


def binary_fraction_to_decimal(num):
    i = 0
    result = 0
    while i < len(num):
        result = result + (2 ** (len(num) - i - 1)) * num[i]
        i += 1
    return result


def floating_point_to_binary_mantissa(num):
    num_sign = float(num)
    binary_mantissa = []
    if num[0] == "-":
        sign = 1
    else:
        sign = 0
    split_num_array = num.split('.')
    intpart = int(split_num_array[0])
    fractpart = float('0.' + split_num_array[1])

    if intpart != 0:
        normalised_mantissa, exponent_binary = non_zero_int_part(intpart, fractpart)
    else:
        fractpart_binary = fraction_to_binary(fractpart, 23)
        exp_shift = 0
        i = 0
        while i < 23:
            if fractpart_binary[i] == 0:
                exp_shift = i + 1
            elif fractpart_binary[i] == 1:
                exp_shift = i + 1
                i = 23
            i = i + 1

        exponent = 127 - exp_shift
        exponent_binary = decimal_to_binary(exponent)
        normalised_mantissa = fraction_to_binary(fractpart, 23 + exp_shift)
        normalised_mantissa = normalised_mantissa[exp_shift:]

    normalised_mantissa = complete_23_bits(normalised_mantissa)
    binary_mantissa.extend([sign, exponent_binary, normalised_mantissa])

    return binary_mantissa

def non_zero_int_part(intpart, fractpart):

    intpart_binary = decimal_to_binary(intpart)
    intpart_binary = remove_zeros(intpart_binary)
    fractpart_binary = fraction_to_binary(fractpart, 23)
    exponent = 127 + len(intpart_binary) - 1
    exponent_binary = decimal_to_binary(exponent)
    intpart_binary.pop(0)
    normalised_mantissa = intpart_binary + fractpart_binary
    return normalised_mantissa, exponent_binary

def fraction_to_binary(fraction_part, bits):
    res = []
    power = -1
    i = 0
    while i < bits:
        if fraction_part < pow(2, power):
            res.append(0)
        else:
            res.append(1)
            fraction_part = fraction_part - pow(2, power)

        power = power - 1
        i = i + 1

    return res

def complete_23_bits(normalised_mantissa):

    res = [0 for x in range(23)]
    i = 0
    while i < len(normalised_mantissa) and i < 23:
        res[i] = normalised_mantissa[i]
        i = i + 1
    return res


def sum_of_floating_point(num_1, num_2):
    plus_one = False
    sum_binary_mantissa = []
    res_sign = 0
    res_mantissa, plus_one = get_mantissa_of_sum(num_1, num_2)
    res_exponent = get_exponent_of_sum(num_1, num_2, plus_one)
    sum_binary_mantissa.append(res_sign)
    sum_binary_mantissa.append(res_exponent)

    if plus_one == True:
        res_mantissa.insert(0, 0)
        res_mantissa = complete_23_bits(res_mantissa)
    sum_binary_mantissa.append(res_mantissa)

    #print(sum_binary_mantissa)
    return sum_binary_mantissa



def get_exponent_of_sum(num_1, num_2, plus_one):
    res = []
    if exponent_to_decimal(num_1[1]) > exponent_to_decimal(num_2[1]):
        res = num_1[1]
    else:
        res = num_2[1]
    if plus_one == True:
        one_arr = [0, 0, 0, 0, 0, 0, 0, 1]
        res = sum(res, one_arr, 8)

    return res

def get_mantissa_of_sum(num_1, num_2):
    diff = exponent_to_decimal(num_1[1]) - exponent_to_decimal(num_2[1])
    mantissa_1 = num_1[2]
    mantissa_1.insert(0, 1)
    mantissa_2 = num_2[2]
    mantissa_2.insert(0, 1)
    if diff <= 0:
        mantissa_1 = shift_mantissa(num_1, abs(diff))
    elif diff > 0:
        mantissa_2 = shift_mantissa(num_2, abs(diff))
    mantissa_1 = complete_23_bits(mantissa_1)
    mantissa_2 = complete_23_bits(mantissa_2)


    if num_1[0] == 1:
        mantissa_1 = binary_to_twos_complement(mantissa_1, 23)
        mantissa_1[0] = 1


    elif num_2[0] == 1:
        mantissa_1 = binary_to_twos_complement(mantissa_2, 23)
        mantissa_2[0] = 1
    return sum_of_mantissas(mantissa_1, mantissa_2)


def sum_of_mantissas(mantissa_1, mantissa_2):
    sum = [0 for i in range(23)]
    i = 22
    carry = 0
    while i >= 0:
        sum[i] = mantissa_1[i] + mantissa_2[i] + carry
        carry = 0
        if i == 0 and sum[i] == 2:
            plus_one = True
        else:
            plus_one = False

        if sum[i] == 2:
            sum[i] = 0
            carry = 1
        elif sum[i] == 3:
            sum[i] = 1
            carry = 1

        i = i - 1
    sum.pop(0)
    sum = complete_23_bits(sum)
    return sum, plus_one


def shift_mantissa(num, difference):
    num_mantissa = num[2]
    res = []
    i = 0
    while i < 23:
        if i < difference:
           res.append(0)
        else:
            res.append(num_mantissa[i-difference])
        i = i + 1

    return res


def exponent_to_decimal(num):
    num = add_one(num, 8)
    exponent_decimal = 0
    i = 7
    while i > 0:

        exponent_decimal = exponent_decimal + num[i] * (2 ** (7 - i))
        i = i - 1

    return exponent_decimal


def floating_to_decimal(num):
    i = 1
    exp = 0
    mantissa = 0
    while i < 9:
        exp = exp + (2 ** (8 - i)) * num[1][i-1]
        i = i + 1
    while i < 32:
        mantissa = mantissa + (2 ** (32 - i - 1)) * num[2][i-9]
        i = i + 1
    decimal = 2 ** (exp - 127) * (1 + mantissa / 2 ** 23)
    if num[0] == 1:
        decimal = -decimal
    return decimal


while True:

    choice = input("\nChoose the operation:\n1: +\n2: -\n3: *\n4: /\n5: + floating point\n")
    match choice:
        case "1":
            x1 = int(input("Input X1:\n"))
            x2 = int(input("Input X2:\n"))

            if x1 >= 0 and x2 >= 0:
                result = (positive_positive(x1, x2))
            elif x1 < 0 and x2 < 0:
                result = (negative_negative(x1, x2))
            elif x1 < 0 and x2 >= 0:
                x_sign = x1 + x2
                result = (negative_positive(x1, x2, x_sign))
            elif x1 >= 0 and x2 < 0:
                x_sign = x1 + x2
                result = (positive_negative(x1, x2, x_sign))

            print("Sum of X1 and X2:\n" + "".join(str(x) for x in result) + " or", binary_to_decimal(result))

        case "2":
            x1 = int(input("Input X1:\n"))
            x2 = int(input("Input X2:\n"))
            if x1 >= 0 and x2 >= 0:
                x_sign = x1 - x2
                result = (positive_negative(x1, x2, x_sign))
            elif x1 < 0 and x2 < 0:
                x_sign = x1 - x2
                result = (negative_positive(x1, x2, x_sign))
            elif x1 < 0 and x2 >= 0:
                result = (negative_negative(x1, x2))
            elif x1 >= 0 and x2 < 0:
                result = (positive_positive(x1, x2))

            print("Sum of X1 and X2:\n" + "".join(str(x) for x in result) + " or", binary_to_decimal(result))

        case "3":
            x1 = int(input("Input X1:\n"))
            x2 = int(input("Input X2:\n"))

            if x1 < 0:
                x1 = decimal_to_twos_complement(x1)
            else:
                x1 = decimal_to_binary(x1)
            if x2 < 0:
                x2 = decimal_to_twos_complement(x2)
            else:
                x2 = decimal_to_binary(x2)

            result = multiply(x1, x2)

            if result[0] == 1:
                result = binary_to_twos_complement(result)
                result[0] = 1

            print("X1:\n" + "".join(str(x) for x in x1) + "\n")
            print("X2:\n" + "".join(str(x) for x in x2) + "\n")
            print("Multiplication of X1 by X2:\n" + "".join(str(x) for x in result) + " or", binary_to_decimal(result))

        case "4":
            x1 = int(input("Input X1:\n"))
            x2 = int(input("Input X2:\n"))
            sign = 0
            if x1 < 0:
                sign += 1
            if x2 < 0:
                sign += 1


            x1 = decimal_to_binary(x1)
            x2 = decimal_to_binary(x2)

            result, fraction_result = divide(x1, x2)


            print("X1:\n" + "".join(str(x) for x in x1) + "\n")
            print("X2:\n" + "".join(str(x) for x in x2) + "\n")
            print("Division of X1 by X2:\n" + "".join(str(x) for x in result) + "." +
                  "".join(str(x) for x in fraction_result) + "\nor")

            result = binary_to_decimal(result) + binary_fraction_to_decimal(fraction_result) / 2 ** 25
            if sign == 1:
                result = -result
            print(result)


        case "5":
            x1 = input("Input X1:\n")
            x2 = input("Input X2:\n")
            x1 = floating_point_to_binary_mantissa(x1)
            x2 = floating_point_to_binary_mantissa(x2)

            print("X1:\n" + str(x1[0]) + " " + "".join(str(x) for x in x1[1]) + " " + "".join(str(x) for x in x1[2]) + "\n")
            print("X2:\n" + str(x2[0]) + " " + "".join(str(x) for x in x2[1]) + " " + "".join(str(x) for x in x2[2]) + "\n")
            result = sum_of_floating_point(x1, x2)
            print("Sum of X1 and X2:\n" + str(result[0]) + " " + "".join(str(x) for x in result[1]) + " " + "".join(
                str(x) for x in result[2]) + "\n")
            result = floating_to_decimal(result)
            print("or")
            print(result)