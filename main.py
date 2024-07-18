def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    number_of_words = count_words(text)
    character_dictionary = count_characters(text)
    print(sort_on(character_dictionary))

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(book):
    words = book.split()
    words_count = len(words)
    
def count_characters(book):
    character_dictionary = {}
    for letter in book:
        lowered_letter = letter.lower()
        if lowered_letter in character_dictionary:
            character_dictionary[lowered_letter] += 1
        else:
            character_dictionary[lowered_letter] = 1
    return character_dictionary    

def generate_report(book):
    
main()