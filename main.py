def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    number_of_words = count_words(text)
    character_dictionary = count_characters(text)
    print(generate_report(character_dictionary))

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
    
def count_characters(book):
    """
    Count the number of characters found in a book.

    :param book: str - containing the text from the book.
    :return: dictionary - of characters and count of characters found in the text.
    """
    character_dictionary = {}
    for letter in book:
        lowered_letter = letter.lower()
        if lowered_letter in character_dictionary:
            character_dictionary[lowered_letter] += 1
        else:
            character_dictionary[lowered_letter] = 1
    return character_dictionary    

def generate_report(dictionary):
    """
    

    :param book: str - containing the text from the book.
    :return: int - count of characters found in the text.
    """
    dictionary_list = [{key: value} for key, value in dictionary.items()]
    dictionary_list.sort(reverse = True, key = sort_on)
    return dictionary_list
    
main()