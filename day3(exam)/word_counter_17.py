# program to count the occurrences of each word in a sentence

# function to get the sentence entered by the user
def get_user_input():
    user_input = input("Provide the sentence: ")
    return user_input

# function to split the given string into list of words
def get_list_of_words(user_input):
    list_of_words_with_duplicates = user_input.split()
    list_of_words = set(list_of_words_with_duplicates)
    return (list_of_words, list_of_words_with_duplicates)

# function to count and print the occurance of each word in the given string
def word_count_and_print(list_of_words, list_of_words_with_duplicates):
    for word in list_of_words:
        word_occurrence = list_of_words_with_duplicates.count(word)
        if(word_occurrence > 1):
            print(f"{word} : occurred {word_occurrence} times in the given string")
        else:
            print(f"{word} : occurred {word_occurrence} time in the given string")

def main():
    user_input = get_user_input()
    (list_of_words, list_of_words_with_duplicates) = get_list_of_words(user_input)
    word_count_and_print(list_of_words, list_of_words_with_duplicates)

main()