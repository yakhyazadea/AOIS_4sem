import random


def get_g_l(g, l, a, s, index, matches):
    if index < len(a):
        g = g or (not(a[index]) and s[index] and not(l))
        l = l or (a[index] and not(s[index]) and not(g))
        if(a[index] == s[index]):
            matches += 1
        index += 1
        return get_g_l(g, l, a, s, index, matches)
    else:
        return g, l, matches


def compare_words(a, s):
    match = 0
    g, l, matches = get_g_l(0, 0, a, s, 0, match)
    if(g > l):
        return ">"
    if(g < l):
        return "<"
    if(g == l):
        return "="



def find_closest_bigger_word(words_array, the_word):
    the_bigger_numbers_array = []
    for word in words_array:
        if(compare_words(the_word, word) == ">"):
            the_bigger_numbers_array.append(word)
    if (len(the_bigger_numbers_array) == 0):
        return []
    else:
        array_2 = the_bigger_numbers_array.copy()
        for i in range(len(the_bigger_numbers_array[0])):
            the_closest_bigger_word = []
            for word in array_2:
                if (word[i] == 0):
                    the_closest_bigger_word.append(word)
            if the_closest_bigger_word != []:
                array_2 = the_closest_bigger_word
    return array_2




def find_closest_smaller_word(words_array, the_word):
    ##print("words_array")
    #print(words_array)
    #print("the_word")
    #print(the_word)
    the_smaller_numbers_array = []
    for word in words_array:
        if (compare_words(the_word, word) == "<"):
            the_smaller_numbers_array.append(word)
    if(len(the_smaller_numbers_array) == 0):
        return []
    else:
        array_2 = the_smaller_numbers_array.copy()
        for i in range(len(the_smaller_numbers_array[0])):
            the_closest_smaller_word = []
            for word in array_2:
                if (word[i] == 1):
                    the_closest_smaller_word.append(word)
            if the_closest_smaller_word != []:
                array_2 = the_closest_smaller_word
    return array_2





def generate_words(number_of_words, length_of_words):
    words_array = [[random.randint(0, 1) for n in range(length_of_words)] for j in range(number_of_words)]
    print(words_array)
    return words_array

def count_number_of_ones(the_word):
    number_of_ones = 0
    for i in the_word:
        if(i == 1):
            number_of_ones += 1
    return number_of_ones


def boolean_function(words_array, function):
    result = []
    for i in range(len(words_array)):
        num_of_ones = count_number_of_ones(words_array[i])
        if (function == "~"):
            if(num_of_ones == len(words_array[i]) or num_of_ones == 0):
                result.append(words_array[i])
        elif function == "/\\":
            if(num_of_ones == len(words_array[i])):
                result.append(words_array[i])
        elif function == "\\/":
            if(num_of_ones > 0):
                result.append(words_array[i])
        elif function == "+":
            if (num_of_ones == 1):
                result.append(words_array[i])
    return result

words_array = []
while(True):
    number_of_words = int(input("\nNumber of words: "))
    length_of_words = int(input("Length of words: "))

    words_array = generate_words(number_of_words, length_of_words)

    print("\n")
    print("Choose the action:")
    choice = int(input("Regenerate words - 1\nClosest smaller - 2\nClosest bigger - 3\nSearch based on boolean functions - 4\n"))
    match(choice):
        case 1:
            number_of_words = input("Number of words: ")
            length_of_words = input("Length of words: ")

            words_array = generate_words(number_of_words, length_of_words)
        case 2:
            the_word = input("Input the word: ")
            the_word = the_word.replace(' ', '')
            the_word = [int(x) for x in the_word.split(',')]
            closest_smaller = find_closest_smaller_word(words_array, the_word)
            if closest_smaller == []:
                print("There is no smaller word than the input word")
            else:
                print("Closest smaller:")
                print(closest_smaller)
        case 3:
            the_word = input("Input the word: ")
            the_word = the_word.replace(' ', '')
            the_word = [int(x) for x in the_word.split(',')]
            closest_bigger = find_closest_bigger_word(words_array, the_word)
            if closest_bigger == []:
                print("There is no bigger word than the input word")
            else:
                print("Closest bigger:")
                print(closest_bigger)

        case 4:
            function = input("Input the function: ")
            result = boolean_function(words_array, function)
            if result == []:
                print("No suitable word found")
            else:
                print("Result:")
                print(result)
