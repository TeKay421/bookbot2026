import sys
from stats import num_words, num_characters, chars_dict_to_sorted_list

if len(sys.argv) != 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)

def get_book_text(filepath):
        with open(filepath) as f:
                book = f.read()
        return book


def main():
    book_text = get_book_text(sys.argv[1])
    num_words_in_book = num_words(book_text)
    num_chars_in_book = num_characters(book_text)
    sorted_list = chars_dict_to_sorted_list(num_chars_in_book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words_in_book} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_list:
           print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")

main()               