import random

V_len = 3
A_len = 4
S_len = 5
word_len = 16

def string_index(current_index, column_index):
    index = current_index + column_index
    if index > word_len - 1: index -= word_len
    return index

def add_word(normal_table, diagonal_table, word):
    for i in range(word_len):
        if read_column(diagonal_table, i) == [0 for k in range(word_len)]:
            normal_table[i] = word
            for j in range(word_len):
                diagonal_table[string_index(i, j)][i] = word[j]
            break

def sum(num1, num2):
    num1.insert(0, 0)
    num2.insert(0, 0)
    result = []
    add_one = 0
    for i in range(S_len):
        result.insert(0, num1[S_len-i-1]+num2[S_len-i-1]+add_one)
        add_one = 0
        if result[0] > 1:
            add_one += 1
            result[0] -= 2
    return result

def word_addition(normal_table, diagonal_table, V):
    for i in range(word_len):
        word =  read_column(diagonal_table, i)
        if [word[0], word[1], word[2]] == V:
            A = [word[V_len+a] for a in range(A_len)]
            B = [word[V_len+A_len+a] for a in range(A_len)]
            S = sum(A, B)
            for j in range(V_len+A_len*2, word_len):
                diagonal_table[string_index(i, j)][i] = S[j-V_len-A_len*2]
            normal_table[i] = read_column(diagonal_table, i)

def read_column(diagonal_table, index):
    return [diagonal_table[string_index(index, i)][index] for i in range(word_len)]

def f1(x1, x2):
    result = [0 for i in range(word_len)]
    for i in range(len(x1)):
        if x1[i] == 1 and x2[i] == 1: result[i] = 1
    return result

def f14(x1, x2):
    result = [0 for i in range(word_len)]
    for i in range(len(x1)):
        if not(x1[i] == 1 and x2[i] == 1): result[i] = 1
    return result

def f12(x1):
    result = [0 for i in range(word_len)]
    for i in range(len(x1)):
        if x1 == 0: result[i] = 1
    return result

def compare(word_1, word_2):
    g = False
    l = False
    for i in range(len(word_1)):
        g1 = g or (not(word_2[i]) and word_1[i] and not(l))
        l1 = l or (word_2[i] and not(word_1[i]) and not(g))
        g = g1
        l = l1
    if not(l) and g: return ">"
    elif not(g) and l: return "<"
    else: return "="

normal_table = [[0 for i in range(word_len)] for j in range(word_len)]
diagonal_table = [[0 for i in range(word_len)] for j in range(word_len)]
while True:
    operation = input("\n1 - add new word\n2 - read column\n3 - bool function\n4 - find nearest smaller\n5 - find nearest bigger\n6 - sum\n7 - show the tables\n")
    match(operation):
        case '1':
            creation_way = input("\n1 - keyboard input\n2 - random word\n")
            match(creation_way):
                case '1':
                    new_word = input()
                    new_word = new_word.replace(' ','')
                    new_word = [int(el) for el in new_word]
                    add_word(normal_table, diagonal_table, new_word)
                case '2':
                    new_word = [random.randint(0,1) for n in range(word_len)]
                    add_word(normal_table, diagonal_table, new_word)
        case '2':
            index = int(input('index of column: '))
            column = read_column(diagonal_table, index)
            print(column)
        case '3':
            bool_function = input('\n1 - f1\n2 - f14\n3 - f3\n4 - f12:\n')
            index_1 = int(input('first word index: '))
            index_2 = int(input('second word index: '))
            word_1 = read_column(diagonal_table, index_1)
            word_2 = read_column(diagonal_table, index_2)
            match(bool_function):
                case '1': add_word(normal_table, diagonal_table, f1(word_1, word_2))
                case '2': add_word(normal_table, diagonal_table, f14(word_1, word_2))
                case '3': add_word(normal_table, diagonal_table, word_1)
                case '4': add_word(normal_table, diagonal_table, f12(word_1, word_2))
        case '4':
            keyword = input('keyword: ').replace(' ','')
            keyword = [int(el) for el in keyword]
            smaller = []
            for i in range(word_len):
                if compare(read_column(diagonal_table, i), keyword) == '<':
                    smaller.append(read_column(diagonal_table, i))
            if smaller == []:
                print("no words smaller than this")
            else:
                biggest = smaller[0]
                for i in range(1, len(smaller)):
                    if compare(smaller[i], biggest) == '>':
                        biggest = smaller[i]
                print(biggest)
        case '5':
            keyword = input('keyword: ').replace(' ','')
            keyword = [int(el) for el in keyword]
            bigger = []
            for i in range(word_len):
                if compare(read_column(diagonal_table, i), keyword) == '>':
                    bigger.append(read_column(diagonal_table, i))
            if bigger == []:
                print("no words bigger than this")
            else:
                smallest = bigger[0]
                for i in range(1, len(bigger)):
                    if compare(bigger[i], smallest) == '<':
                        smallest = bigger[i]
                print(smallest)
        case '6':
            V = input('V: ')
            V = [int(el) for el in V]
            word_addition(normal_table, diagonal_table, V)
        case '7':
            print('\nnormal:')
            for i in range(word_len):
                print('|'.join(str(normal_table[i][j]) for j in range(word_len)))
            print('\ndiagonal:')
            for i in range(word_len):
                print('|'.join(str(diagonal_table[i][j]) for j in range(word_len)))
