arguments = [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0 , 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1]]

operations = ["v", "&", ">", "~", "!"]


def call_func(operation, x1, x2):
    if operation == "v":
        return func_disjunction(x1, x2)
    if operation == "&":
        return func_conjunction(x1, x2)
    if operation == ">":
        return func_implication(x1, x2)
    if operation == "~":
        return func_equivalence(x1, x2)
    if operation == "!":
        return func_negation(x1, x2)


def func_expression_next_right(expression, i):
    iter = i + 1
    while iter < len(expression):
        if expression[iter] != 0:
            return expression[iter], iter
        iter += 1

def func_expression_next_left(expression, i):
    iter = i - 1
    while iter >= 0:
        if expression[iter] != 0:
            return expression[iter], iter
        iter -= 1

def func_look_for_element_right(element, expression, i, compare):
    iter = i + 1
    number = 0
    while iter < len(expression):
        if compare == True:
            if expression[iter] == element:
                return number
            if expression[iter] > number:
                number = expression[iter]

        else:
            if expression[iter] == element:
                return iter
        iter += 1

def func_look_for_element_left(element, expression, i, compare):
    iter = i - 1
    number = 0
    while iter >= 0:
        if compare == True:
            if expression[iter] == element:
                return number
            if expression[iter] > number:
                number = expression[iter]

        else:
            if expression[iter] == element:
                return iter
        iter -= 1


def func_find_truth_table(expression):
    arrays = []
    i = 0
    operations_count = 0
    while i < len(expression):
        res_array = []
        if expression[i] in operations:
            expr_right, index_right = func_expression_next_right(expression, i)
            expr_left, index_left = func_expression_next_left(expression, i)

            if expression[i] == "!" and expr_right != "(":

                exp = expression[index_right]
                if type(exp) is int:
                    number_left = func_look_for_element_right(")", expression, i, True)
                    exp = arrays[number_left - 1]
                    # expression[i] = 0
                if exp == "a":
                    exp = arguments[0]
                if exp == "b":
                    exp = arguments[1]
                if exp == "c":
                    exp = arguments[2]
                res_array = func_negation(exp)
                arrays.append(res_array)
                operations_count += 1
                expression[i] = 0
                expression[func_look_for_element_right(")", expression, i, False)] = 0
                expression[i + 1] = operations_count
                expression[func_look_for_element_left("(", expression, i, False)] = 0

                i = 0

            elif expr_right != "(" and expr_left != ")":

                exp_1 = expression[index_left]
                exp_2 = expression[index_right]
                if type(exp_1) is int:
                    number_right = func_look_for_element_left("(", expression, i, True)
                    exp_1 = arrays[number_right-1]
                if type(exp_2) is int:
                    number_left = func_look_for_element_right(")", expression, i, True)
                    exp_2 = arrays[number_left-1]

                if exp_1 == "a":
                    exp_1 = arguments[0]
                if exp_2 == "a":
                    exp_2 = arguments[0]
                if exp_1 == "b":
                    exp_1 = arguments[1]
                if exp_2 == "b":
                    exp_2 = arguments[1]
                if exp_1 == "c":
                    exp_1 = arguments[2]
                if exp_2 == "c":
                    exp_2 = arguments[2]



                res_array = call_func(expression[i], exp_1, exp_2)

                arrays.append(res_array)
                operations_count += 1

                expression[i] = 0
                expression[i-1] = 0
                expression[func_look_for_element_right(")", expression, i, False)] = 0
                expression[i+1] = operations_count
                expression[func_look_for_element_left("(", expression, i, False)] = 0

                i = 0

        i = i + 1



    return arrays[operations_count-1]


def func_count_brackets(expression, i):
    iter = i
    brackets_right = 0
    brackets_left = 0
    while iter < len(expression):
        if expression[i] == ")":
            brackets_right += 1
        iter += 1
    iter = i
    while iter > 0:
        if expression[i] == "(":
            brackets_left += 1
        iter -= 1
    if brackets_right == brackets_left:
        return True
    else:
        return False




def func_negation(x):
    res_array = []
    i = 0
    while i < 8:
        if x[i] == 0:
            res_array.append(1)
        else:
            res_array.append(0)
        i += 1
    return res_array


def func_disjunction(x1, x2):
    res_array = []
    i = 0
    while i < 8:
        if x1[i] == 1 or x2[i] == 1:
            res_array.append(1)
        else:
            res_array.append(0)
        i += 1
    return res_array


def func_conjunction(x1, x2):
    res_array = []
    i = 0
    while i < 8:
        if x1[i] == 1 and x2[i] == 1:
            res_array.append(1)
        else:
            res_array.append(0)
        i += 1
    return res_array


def func_implication(x1, x2):
    res_array = []
    i = 0
    while i < 8:
        if x1[i] == 1 and x2[i] == 0:
            res_array.append(0)
        else:
            res_array.append(1)
        i += 1
    return res_array


def func_equivalence(x1, x2):
    res_array = []
    i = 0
    while i < 8:
        if x1[i] == x2[i]:
            res_array.append(1)
        else:
            res_array.append(0)
        i += 1
    return res_array


def func_binary_to_decimal(num_binary):
    num_decimal = 0
    i = 7
    while i >= 0:
        num_decimal = num_decimal + num_binary[i] * (2 ** (7 - i))
        i = i - 1


    return num_decimal


def func_sknf(array):
    res = ''
    i = 0
    while i < len(array):
        if array[i] == 0:

            if res != '':
                res = res + "&"
            res = res + '('
            if arguments[0][i] == 1:
                res = res + "!a"
            else:
                res = res + "a"
            res = res + "v"
            if arguments[1][i] == 1:
                res = res + "!b"
            else:
                res = res + "b"
            res = res + "v"
            if arguments[2][i] == 1:
                res = res + "!c"
            else:
                res = res + "c"
            res = res + ')'


        i = i + 1


    return res


def func_sdnf(array):
    res = ''
    i = 0
    while i < len(array):
        if array[i] == 1:

            if res != '':
                res = res + "v"
            res = res + '('
            if arguments[0][i] == 0:
                res = res + "!a"
            else:
                res = res + "a"
            res = res + "&"
            if arguments[1][i] == 0:
                res = res + "!b"
            else:
                res = res + "b"
            res = res + "&"
            if arguments[2][i] == 0:
                res = res + "!c"
            else:
                res = res + "c"
            #if res != '' and res[len(res) - 1] != "(":
                #res = res + "&"

            res = res + ')'


        i = i + 1


    return res

def func_get_numeric_form(array):
    i = 0
    arr_dis = []
    arr_con = []
    while i < len(array):
        if array[i] == 1:
            arr_dis.append(i)
        else:
            arr_con.append(i)
        i = i + 1
    return arr_con, arr_dis

input_expression = list(input("\nInput the expression:\n"))
print("The Truth Table")
print("A: " + " ".join(str(x) for x in arguments[0]))
print("B: " + " ".join(str(x) for x in arguments[1]))
print("C: " + " ".join(str(x) for x in arguments[2]))

result = func_find_truth_table(input_expression)
print("Result: " + " ".join(str(x) for x in result))

index_form = func_binary_to_decimal(result)
print("Index form: ")
print(index_form)

con_numberic_form, dis_numberic_form = func_get_numeric_form(result)
numberic_form = ("/\(" + ", ".join(str(x) for x in con_numberic_form) + ") = \/(" + ", ".join(str(x) for x in dis_numberic_form) + ")")
print("Numeric form: ")
print(numberic_form)


print("СКНФ: ")
print(func_sknf(result))
print("СДНФ: ")
print(func_sdnf(result))