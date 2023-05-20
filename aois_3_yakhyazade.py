import aois_laba_2 as lab2

letters = ["a", "b", "c"]


def func_count_line(skl_array, index, pair_array):
    res = 0
    num = 0
    special = ""
    new_array = skl_array.copy()
    new_array.pop(index)
    i = 0
    while i < len(pair_array):
        if pair_array[i] != "0" and pair_array[i] != "1":
            special = str(i+1)
        i += 1
    i = 0
    while i < len(new_array):
        j = 0
        while j < len(new_array[i]):
            if special in new_array[i][j] and "!" in new_array[i][j]:
                num += 1
            elif special in new_array[i][j]:
                num -= 1

            j += 1

        i += 1
    if num == 0:
        res = 1


    return res



def func_get_sdnf_values(pair_array):
    res = ["a", "b", "c"]
    if pair_array[0][0] == "!":
        res[int(pair_array[0][1]) - 1] = "0"
    else:
        res[int(pair_array[0][0]) - 1] = "1"
    if pair_array[1][0] == "!":
        res[int(pair_array[1][1]) - 1] = "0"
    else:
        res[int(pair_array[1][0]) - 1] = "1"

    return res


def func_get_sknf_values(pair_array):
    res = ["a", "b", "c"]
    if pair_array[0][0] == "!":
        res[int(pair_array[0][1]) - 1] = "1"
    else:
        res[int(pair_array[0][0]) - 1] = "0"
    if pair_array[1][0] == "!":
        res[int(pair_array[1][1]) - 1] = "1"
    else:
        res[int(pair_array[1][0]) - 1] = "0"

    return res



def func_check_line(skl_array, index, type):

    if type == "sdnf":
        pair_array = func_get_sdnf_values(skl_array[index])

    if type == "sknf":
        pair_array = func_get_sknf_values(skl_array[index])


    res = func_count_line(skl_array, index, pair_array)
    if res == 1:
        return True
    else:
        return False



def func_check_lishniye_impicants(skl_array, type):
    res = []
    i = 0
    while i < len(skl_array):
        lishn = func_check_line(skl_array, i, type)
        if lishn == False:
            res.append(skl_array[i])

        i = i + 1

    return res


def func_check_excess(skl_array, type):
    return 0



def func_skleivaniye(array):
    res = []
    i = 0
    while i < len(array):
        j = 1
        while j < len(array[i]):
            true_false, pair = func_compare_triplets(array[i][0], array[i][j])
            if true_false:
                res.append(pair)
            j = j + 1

        i = i + 1

    return res


def func_array_to_sdnf(array):
    res = ''
    i = 0
    while i < len(array):

        if res != '':
            res = res + "v"
        res = res + '('
        if "!" in array[i][0]:
            res = res + "!"
            res = res + letters[int(array[i][0][1]) - 1]
        else:
            res = res + letters[int(array[i][0]) - 1]
        res = res + "&"
        if "!" in array[i][1]:
            res = res + "!"
            res = res + letters[int(array[i][1][1]) - 1]
        else:
            res = res + letters[int(array[i][1]) - 1]

        res = res + ')'

        i = i + 1

    return res


def func_array_to_sknf(array):
    res = ''
    i = 0
    while i < len(array):

        if res != '':
            res = res + "&"
        res = res + '('
        if "!" in array[i][0]:
            res = res + "!"
            res = res + letters[int(array[i][0][1]) - 1]
        else:
            res = res + letters[int(array[i][0]) - 1]
        res = res + "v"
        if "!" in array[i][1]:
            res = res + "!"
            res = res + letters[int(array[i][1][1]) - 1]
        else:
            res = res + letters[int(array[i][1]) - 1]

        res = res + ')'

        i = i + 1

    return res


def func_nums_to_formula(array, type):
    res = ""
    if type == "sdnf":
        res = func_array_to_sdnf(array)
    if type == "sknf":
        res = func_array_to_sknf(array)

    return res


def func_rascetniy_method(array):
    res = func_read_formula_signs(array)
    res = func_split_arrays(res)
    res = func_skleivaniye(res)

    return res


def func_compare_triplets(triplet_1, triplet_2):
    count = 0
    pair = []
    if triplet_1[0] == triplet_2[0]:
        count = count + 1
        pair.append(triplet_1[0])
    if triplet_1[1] == triplet_2[1]:
        count = count + 1
        pair.append(triplet_1[1])
    if triplet_1[2] == triplet_2[2]:
        count = count + 1
        pair.append(triplet_1[2])

    if count >= 2:
        return True, pair
    else:
        return False, pair


def func_read_formula_signs(array):
    res = []
    triplet = []
    i = 0
    while i < len(array):
        if array[i] == "a":
            if array[i - 1] == "!":
                triplet.append("!1")
            else:
                triplet.append("1")

        elif array[i] == "b":
            if array[i - 1] == "!":
                triplet.append("!2")
            else:
                triplet.append("2")

        elif array[i] == "c":
            if array[i - 1] == "!":
                triplet.append("!3")
            else:
                triplet.append("3")

        if array[i] == ")":
            res.append(triplet)
            triplet = []

        i = i + 1

    return res


def func_split_arrays(array):
    count = len(array) - 2
    res = []
    i = 0
    res.append(array)
    while i < count:
        array = array[1:]
        res.append(array)
        i = i + 1

    return res


def func_check_if_constituenta_contains_implicanta(constituenta, implicanta):
    if implicanta[0] in constituenta and implicanta[1] in constituenta:
        return True
    else:
        return False


def func_create_matrix(constituenti, implicanti):
    i = 0
    res_array = []
    while i < len(implicanti):
        j = 0
        line_array = ["" for x in constituenti]
        while j < len(constituenti):
            if func_check_if_constituenta_contains_implicanta(constituenti[j], implicanti[i]):
                line_array[j] = "X"
            j = j + 1

        res_array.append(line_array)
        i = i + 1

    return res_array


def find_x(matrix, missing, index):
    find = False
    i = 0
    while i < len(matrix):
        if i != missing:
            if matrix[i][index] == 'X':
                find = True
        i = i + 1
    return find


def func_delete_excess(matrix, implicanti):
    i = 0
    new_array = implicanti.copy()
    matrix_2 = matrix.copy()
    while i < len(new_array):
        lishniy = True
        for j in range(len(matrix_2[i])):
            if not (find_x(matrix_2, i, j)):
                lishniy = False
        if lishniy:
            new_array.pop(i)
            matrix_2.pop(i)
        else:
            i += 1
    return new_array


def func_split_into_table_constituenti(array, type):
    res = []
    i = 0
    if type == "sdnf":
        str1 = "v"
        str2 = "&"
    else:
        str1 = "&"
        str2 = "v"
    while i < len(array):
        triplet = ''
        if triplet != '':
            triplet = triplet + str1
        triplet = triplet + "("
        if "!" in array[i][0]:
            triplet = triplet + "!"
            triplet = triplet + letters[int(array[i][0][1]) - 1]
        else:
            triplet = triplet + letters[int(array[i][0]) - 1]
        triplet = triplet + str2
        if "!" in array[i][1]:
            triplet = triplet + "!"
            triplet = triplet + letters[int(array[i][1][1]) - 1]
        else:
            triplet = triplet + letters[int(array[i][1]) - 1]
        triplet = triplet + str2
        if "!" in array[i][2]:
            triplet = triplet + "!"
            triplet = triplet + letters[int(array[i][2][1]) - 1]
        else:
            triplet = triplet + letters[int(array[i][2]) - 1]
        triplet = triplet + ")"

        res.append(triplet)
        i = i + 1

    return res



def func_tablicno_rascetniy_menthod(array, type):
    res = []
    array = func_read_formula_signs(array)
    constituenti = array.copy()
    if type == "sdnf":
        print_constituenti = func_split_into_table_constituenti(array, "sdnf")
    else:
        print_constituenti = func_split_into_table_constituenti(array, "sknf")
    implicanti = func_split_arrays(array)
    implicanti = func_skleivaniye(implicanti)
    if type == "sdnf":
        print_implicanti = func_array_to_sdnf(implicanti)
        print_implicanti = print_implicanti.split("v")
        matrix = func_create_matrix(constituenti, implicanti)
        res = func_delete_excess(matrix, implicanti)
        res = func_array_to_sdnf(res)
    else:
        print_implicanti = func_array_to_sknf(implicanti)
        print_implicanti = print_implicanti.split("&")
        matrix = func_create_matrix(constituenti, implicanti)
        res = func_delete_excess(matrix, implicanti)
        res = func_array_to_sknf(res)

    print("\nТаблица:")
    func_print_matrix(print_constituenti, print_implicanti, matrix)
    if type == "sdnf":
        print("ТДНФ:")
    else:
        print("ТКНФ:")
    print(res)

    return res


def func_print_matrix(constituenti, implicanti, matrix):
    print("\t\t", end="")
    for x in constituenti:
        print(x + "  ", end="")
    print("")
    i = 0
    while i < len(implicanti):
        print(implicanti[i] + "  ", end="")
        for x in matrix[i]:
            print("    " + x + "    ", end="")
        print("\n")
        i = i + 1
    print("")

    return 0


def func_tablicniy_method(array, type):
    res = []

    new_array = array
    array = func_read_formula_signs(array)
    num_array = func_check_the_number(array, type)
    lines = func_fill_the_lines(num_array, type)
    func_print_graph(lines)
    res = func_read_formula_signs(new_array)
    res = func_split_arrays(res)
    res = func_skleivaniye(res)

    return res


def func_fill_the_lines(array, type):
    lines = [[" ", " ", " ", " "], [" ", " ", " ", " "]]
    i = 0
    if type == "sdnf":
        num = 1
    else:
        num = 0
    while i < len(array):
        sum = array[i][1] + array[i][2]
        if array[i][0] == 1:
            num_line = 0
        else:
            num_line = 1
        if sum == 0:
            lines[num_line][0] = num
        if array[i][1] == 0 and array[i][2] == 1:
            lines[num_line][1] = num
        if array[i][1] == 1 and array[i][2] == 0:
            lines[num_line][3] = num
        if sum == 2:
            lines[num_line][2] = num

        i = i + 1

    return lines


def func_check_the_number(array, type):
    res = []
    i = 0
    while i < len(array):
        array[i]
        j = 0
        new_triplet = []
        while j < len(array[i]):
            if "!" in array[i][j]:
                if type == "sdnf":
                    new_triplet.append(0)
                else:
                    new_triplet.append(1)
            else:
                if type == "sdnf":
                    new_triplet.append(1)
                else:
                    new_triplet.append(0)

            j = j + 1
        res.append(new_triplet)
        i = i + 1

    return res


def func_print_graph(lines):
    print("a")
    print("  ^")
    print("1 | ", end="")
    for x in lines[0]:
        print(str(x) + "  ", end="")
    print("")
    print("0 | ", end="")
    for x in lines[1]:
        print(str(x) + "  ", end="")
    print("")
    print("  ------------->")
    print("    00 01 11 10   b c")

    return 0


input_expression = list(input("\nInput the expression:\n"))
truth_table = lab2.func_find_truth_table(input_expression)
#truth_table = [0, 1, 1, 1, 0, 0, 1, 0]  # delete
sdnf_formula = lab2.func_sdnf(truth_table)
sknf_formula = lab2.func_sknf(truth_table)

print("\nРасчетный метод:\n")
print("СДНФ:")
print(sdnf_formula)

res = func_rascetniy_method(sdnf_formula)
print("ТДНФ:")
res_2 = func_check_lishniye_impicants(res, "sdnf")
res = func_nums_to_formula(res, "sdnf")
print(res)
print("ТДНФ:")
res_2 = func_nums_to_formula(res_2, "sdnf")
print(res_2)



print("\nСКНФ:")
print(sknf_formula)

res = func_rascetniy_method(sknf_formula)
print("ТКНФ:")
res_2 = func_check_lishniye_impicants(res, "sknf")
res = func_nums_to_formula(res, "sknf")
print(res)
print("ТКНФ:")
res_2 = func_nums_to_formula(res_2, "sknf")
print(res_2)

print("\n\nРасчетно-табличный метод:\n")
print("СДНФ:")
print(sdnf_formula)
res = func_rascetniy_method(sdnf_formula)
print("\nТДНФ:")
res = func_nums_to_formula(res, "sdnf")
print(res)
res = func_tablicno_rascetniy_menthod(sdnf_formula, "sdnf")


print("\nСКНФ:")
print(sknf_formula)
res = func_rascetniy_method(sknf_formula)
print("\nТКНФ:")
res = func_nums_to_formula(res, "sknf")
print(res)
res = func_tablicno_rascetniy_menthod(sknf_formula, "sknf")



print("\n\nТабличный метод:\n")
print("\nСДНФ:")
print(sdnf_formula)
print("\nГрафик:")
res_2 = func_tablicniy_method(sdnf_formula, "sdnf")
print("\nТДНФ:")
res = func_nums_to_formula(res_2, "sdnf")
print(res)
print("\nТДНФ:")
res_2 = func_check_lishniye_impicants(res_2, "sdnf")
res_2 = func_nums_to_formula(res_2, "sdnf")
print(res_2)

print("\nСКНФ:")
print(sdnf_formula)
print("\nГрафик:")
res_2 = func_tablicniy_method(sknf_formula, "sknf")
print("\nТКНФ:")
res = func_nums_to_formula(res_2, "sknf")
print(res)
print("\nТКНФ:")
res_2 = func_check_lishniye_impicants(res_2, "sknf")
res_2 = func_nums_to_formula(res_2, "sknf")
print(res_2)
