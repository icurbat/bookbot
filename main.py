def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    number_of_words = count_words(text)
    character_dictionary = count_characters(text)
    sorted_dictionary = sort_dictionary(character_dictionary)
    generate_report(number_of_words, sorted_dictionary, path)

def get_book_text(path):
    """
    Retrieve the text from a book.

    :param path: str - the file path to the text file containing the book.
    :return: str - the complete text extracted from the specified file.
    """

    with open(path) as f:
        return f.read()
    
def count_words(book):
    """
    Count the number of words found in a book.

    :param book: str - containing the text from the book.
    :return: int - count of words found in the text. 
    """

    words = book.split()
    words_count = len(words)
    return words_count
    
def count_characters(book):
    """
    Count the number of characters found in a book.

    :param book: str - containing the text from the book.
    :return: dictionary - of characters and count of characters found in the text.
    """

    character_dictionary = {}
    for letter in book:
        lowered_letter = letter.lower()
        if lowered_letter.isalpha():
            if lowered_letter in character_dictionary:
                character_dictionary[lowered_letter] += 1
            else:
                character_dictionary[lowered_letter] = 1
    return character_dictionary    
    
def sort_dictionary(dictionary):
    """
    Sort a dictionary of characters and character count in descending order by the character count.

    :param dictionary: dictionary - of characters and count of characters found in the text.
    :return: dictionary - sorted version of the input dictionary.
    """

    dictionary_list = [{"name": key, "num": value} for key, value in dictionary.items()]
    dictionary_list.sort(reverse = True, key = sort_on)
    return dictionary_list

def sort_on(dict):
    return dict["num"]

def generate_report(number_of_words, sorted_dictionary, path):
    print(f"--- Begin report of {path} ---")
    print(f"{number_of_words} words found in the document")
    for dictionary in sorted_dictionary:
        name_of_char = dictionary["name"]
        count_of_char = dictionary["num"]
        print(f"The '{name_of_char}' character was found {count_of_char} times")
    print("--- End report ---")

main()