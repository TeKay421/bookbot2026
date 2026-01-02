from stats import num_words

def get_book_text(filepath):
        with open(filepath) as f:
                book = f.read()
        return book


def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words_in_book = num_words(book_text)
    print(f"Found {num_words_in_book} total words")

main()               