def vicitator_table():
    arguments_number = 3
    arguments = create_dictionary(arguments_number)
    b = [0 for i in range(len(arguments['x1']))]
    d = b.copy()
    for i in range(len(arguments['x1'])):
        sum = arguments['x1'][i] - arguments['x2'][i] - arguments['x3'][i]
        if sum == -1:
            b[i] = 1
            d[i] = 1
        if sum == -2:
            b[i] = 1
            d[i] = 0
        if sum == 1:
            d[i] = 1
        sum = 0
    return d, b

def create_dictionary(arguments_number):
    dictionary = []
    for i in range(arguments_number):
        index = i + 1
        same = 2 ** (arguments_number - index)
        array = [0 for j in range(same)]
        array += [1 for j in range(same)]
        while len(array) < 2 ** (arguments_number):
            array += array
        dictionary.append(['x' + str(index), array])
    dictionary = dict(dictionary)
    return dictionary


def string_formula(formula):
    arg_length = 3
    inside = '&'
    outside = 'v'
    substring = []
    for i in range(len(formula)):
        args = []
        for j in range(len(formula[i])):
            if formula[i][j] == 0:
                args.append('!x' + str(j + 1))
            if formula[i][j] == 1:
                args.append('x' + str(j + 1))
        substring.append(inside.join(args))
        if len(substring[-1]) > arg_length:
            substring[-1] = '(' + substring[-1] + ')'
    output = outside.join(substring)
    return output

def merge(formula, arguments_number):
    merged = []
    unmerged = []
    used = [False for i in range(len(formula))]
    for i in range(arguments_number):
        for j in range(len(formula) - 1):
            for k in range(j + 1, len(formula)):
                if is_mergable(formula[j], formula[k], i, arguments_number):
                    used[j] = True
                    used[k] = True
                    merged.append(formula[j].copy())
                    merged[-1].pop(i)
                    merged[-1].insert(i, -1)
                    break
    for i in range(len(used)):
        if not (used[i]):
            unmerged.append(formula[i])
    return merged, unmerged

def PDNF(table, arguments_number):
    formula = []
    arguments = create_dictionary(arguments_number)
    for i in range(len(table)):
        if table[i] == 1:
            bracket = []
            for arg_index in range(1, arguments_number + 1):
                bracket.append(arguments['x' + str(arg_index)][i])
            formula.append(bracket)
    return formula

def is_mergable(constit1, constit2, arg_index, arguments_number):
    mergability = True
    for i in range(arguments_number):
        if i != arg_index and constit1[i] != constit2[i]:
            mergability = False
            break
        if i == arg_index and constit1[i] == constit2[i]:
            mergability = False
            break
    return mergability

def simplify(formula):
    arguments_number = len(formula[0])
    i = arguments_number
    simplified = []
    merged = formula
    while i > 1:
        merged, unmerged = merge(merged, arguments_number)
        merged = delete_excess(merged)
        simplified += unmerged
        i -= 1
    simplified += merged
    formula = delete_identical(simplified)
    return simplified


def delete_excess(formula):
    new_formula = formula.copy()
    no_change = 1
    i = 0
    while i < len(new_formula):
        res = []
        for other in new_formula:
            if new_formula[i] != other:
                sub = substitute(new_formula[i], other)
                if sub[1] == no_change:
                    res.append(sub[0])
        pos, neg = False, False
        for arg in res:
            if arg == 0: neg = True
            if arg == 1: pos = True
        if pos and neg:
            new_formula.pop(i)
        else:
            i += 1
    return new_formula


def delete_identical(formula):
    i = 0
    while i < len(formula) - 1:
        same = False
        for j in range(i + 1, len(formula)):
            if formula[i] == formula[j]:
                same = True
        if same:
            formula.pop(i)
        else:
            i += 1
    return formula

def substitute(values, formula):
    for i in range(len(values)):
        if values[i] == -1:
            missed_value = i
    for i in range(len(formula)):
        if formula[i] != -1 and i != missed_value:
            existing_arg = i
    res = []
    res.append(formula[missed_value])
    if formula[existing_arg] == values[existing_arg]:
        res.append(1)
    else:
        res.append(0)
    return res

def plus_one():
    arguments_number = 4
    arguments = create_dictionary(arguments_number)
    one_binary = [0, 0, 0, 1]
    one_decimal = 1
    y = [[0 for m in range(len(arguments['x1']))] for n in range(arguments_number)]
    for i in range(len(arguments['x1']) - one_decimal):
        index = arguments_number
        plusone = 0
        while index > 0:
            sum = arguments['x'+str(index)][i] + one_binary[index-1] + plusone
            plusone = 0
            if sum >= 2:
                sum -= 2
                plusone = 1
            y[index-1][i] = sum
            index -= 1
    return y


print('\n1(Вариант 2)\nОдноразрядный двоичный вычитатель на 3 входа (ОДВ-3) с представлением выходных функций в СДНФ:\n')
arguments_number = 3
d, b = vicitator_table()
arguments =     create_dictionary(arguments_number)
print('X1  : ' + ' '.join([str(el) for el in arguments['x1']]))
print('X2  : ' + ' '.join([str(el) for el in arguments['x2']]))
print('X3  : ' + ' '.join([str(el) for el in arguments['x3']]) + "\n")
print('di  : ' + ' '.join([str(el) for el in d]))
print('bi+1: ' + ' '.join([str(el) for el in b]))

d_pdnf = PDNF(d, arguments_number)
print('\nСДНФ(di):\n' + string_formula(d_pdnf))
d_simplified = simplify(d_pdnf)
d_simplified = string_formula(d_simplified)
print('ТДНФ(di):\n' + d_simplified)


b_pdnf = PDNF(b, arguments_number)
print('\nСДНФ(bi+1):\n' + string_formula(b_pdnf))
b_simplified = simplify(b_pdnf)
b_simplified = string_formula(b_simplified)
print('ТДНФ(bi+1):\n' + b_simplified)


print('\n\n2(Вариант "a")\nn=1:\n')
arguments_number = 4
arguments = create_dictionary(arguments_number)
for i in range(arguments_number):
    print('X' + str(i+1) +': ' + ' '.join([str(el) for el in arguments['x'+str(i+1)]]))
result = plus_one()
for i in range(arguments_number):
    print('Y' + str(i+1) + ': ' + ' '.join([str(el) for el in result[i]]))

for i in range(arguments_number):
    y_pdnf = PDNF(result[i], arguments_number)
    print('\nСДНФ(y' + str(i+1) + '): ' + string_formula(y_pdnf))
    y_simplified = simplify(y_pdnf)
    y_simplified = string_formula(y_simplified)
    print('ТДНФ(y' + str(i+1) + '): ' + y_simplified)