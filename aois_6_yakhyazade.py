length_of_the_table = 20
length_of_the_en_alphabet = 26

table_array = [["noun", "a word used to identify any of a class of people or things"], ["pronoun", "a word that stands in for a noun often to avoid the need to repeat the same noun over and over"], ["verb", "a word that indicates an action or a state of being"], ["adjective", "a word that describes the quality or the state of being of a noun"], ["adverb", "a word that can modify or describe other words in a sentence"], ["preposition", "a short word that is used before a noun or pronoun to indicate the relationship between it and other words in a sentence"], ["conjunction", "an uninflected linguistic form that joins together sentences or phrases or words"], ["article", "a piece of writing other than fiction or poetry that forms an independent part of a publication"], ["gerund", "a verb form which functions as a noun"], ["interjection", "a word or phrase used to express a feeling or to request or demand something"], ["determiner", "a word that appears before a noun and specifies something about the number or ownership of the noun"], ["colon", "a punctuation mark used to signal when what comes next is directly related to the previous sentence"], ["comma", "a punctuation mark that represents a short pause and is used to divide parts of a sentence"], ["semicolon", "a punctuation mark used chiefly in a coordinating function between major sentence elements"], ["consonant", "a letter that represents certain speech sounds that involve blocking the air before it leaves the mouth"], ["vowel", "a letter that represents a speech sound where air leaves the mouth without blockage"]]


def print_the_table(hash_table):
    print('\n № ||     Keyword   ||  V  || h(V)||  C || Definition')
    print('---||---------------||-----||-----||----||-------------------------------------------------------------------')
    for i in range(length_of_the_table - 1):
        print(str(hash_table[i][0]).center(3), end="||")
        print(str(hash_table[i][1]).center(15), end="||")
        print(str(hash_table[i][2]).center(5), end="||")
        print(str(hash_table[i][3]).center(5), end="||")
        print(str(hash_table[i][4]).center(4), end="||")
        print(str(hash_table[i][5]).center(3))
    print('---------------------------------------------------------------------------------------------------------')


def get_alphabet_position(letter):
    alphabet_pos = ord(letter) - ord('a')
    return alphabet_pos

def find_value_from_key(row_key):
    letter_1_pos = get_alphabet_position(row_key[0])
    letter_2_pos = get_alphabet_position(row_key[1])
    value = letter_1_pos*length_of_the_en_alphabet + letter_2_pos
    return value


def find_address_from_value(row_value):
    address = row_value % length_of_the_en_alphabet
    return address


#print("col")
#print(collision)

def find_collision_row(row_address):
    if(hash_table[row_address][4] == ""):
        return row_address
    else:
        return find_collision_row(hash_table[row_address][4])



def add_row(row):
    if(hash_table[row[0]][1] == ""):
        hash_table[row[0]] = row
    elif(hash_table[row[0]][0] != hash_table[row[0]][3]):
        key_2 = hash_table[row[0]][1]
        definition_2 = hash_table[row[0][5]]
        delete_row(key_2)
        hash_table[row[0]] = row
        add_row(key_2, definition_2)
    else:
        empty_address = 0
        for i in range(length_of_the_table):
            if(hash_table[i][1] == ""):
                empty_address = i
                break
        collision_row = find_collision_row(row[0])
        hash_table[collision_row][4] = empty_address
        row[0] = empty_address
        hash_table[empty_address] = row




hash_table = []
for i in range(length_of_the_table - 1):
    hash_table.append([i, "", "", "", "", ""])
collision = []
for index in range(len(table_array)):
    row_key = table_array[index][0]
    row_definition = table_array[index][1]
    row_value = find_value_from_key(row_key)
    row_address = find_address_from_value(row_value)
    new_row = [row_address, row_key, row_value, row_address, "", row_definition]
    if(hash_table[row_address][1] != ""):
        collision.append(new_row)
    else:
        hash_table[row_address] = new_row

for col_row in collision:
    add_row(col_row)



def find_previous_row(row_address):
    for i in range(length_of_the_table):
        if hash_table[i][4] == row_address:
            return i


def delete_row(row_key, row_address = ""):
    row = ["", "", "", "", "", ""]
    if(row_address == ""):
        row_value = find_value_from_key(row_key)
        row_address = find_address_from_value(row_value)
    if(hash_table[row_address][1] == row_key):
        if(hash_table[row_address][4] != ""):
            col_index = hash_table[row_address][4]
            hash_table[row_address] = hash_table[col_index]
            row[0] = row_address
            hash_table[row_address] = row
        elif(row_address == hash_table[row_address][3] and hash_table[row_address][4] == ""):
            row[0] = row_address
            hash_table[row_address] = row
        else:
            previous_address = find_previous_row(row_address)
            hash_table[previous_address][4] = hash_table[row_address][4]
            row[0] = row_address
            hash_table[row_address] = row
    else:
        delete_row(row_key, row_address=hash_table[row_address][4])


def check_for_key(row_key):
    for i in range(length_of_the_table):
        if hash_table[i][1] == row_key:
            return True
    return False

def find_row(row_key):
    for i in range(length_of_the_table):
        if hash_table[i][1] == row_key:
            return hash_table[i]
    return

while True:
    print("Choose the action:")
    choice = int(input("Print table - 1\nSearch - 2\nAdd - 3\nDelete - 4\n"))
    match choice:
        case 1:
            print_the_table(hash_table)
        case 2:
            input_key = (input("Input key:\n"))
            if(check_for_key(input_key)):
                found_row = find_row(input_key)
                print(str(found_row[0]).center(3), end="||")
                print(str(found_row[1]).center(15), end="||")
                print(str(found_row[2]).center(5), end="||")
                print(str(found_row[3]).center(5), end="||")
                print(str(found_row[4]).center(4), end="||")
                print(str(found_row[5]).center(3))
        case 3:
            input_key = (input("Input key:\n"))
            input_definition = (input("Input definition:\n"))
            input_value = find_value_from_key(input_key)
            input_address = find_address_from_value(input_value)
            input_row = [input_address, input_key, input_value, input_address, "", input_definition]
            add_row(input_row)
        case 4:
            input_key = (input("Input key:\n"))
            if(check_for_key(input_key)):
                delete_row(input_key)
                print_the_table(hash_table)
        case _:
            print("Wrong input number, try typing 1,2,3 or 4\n")

