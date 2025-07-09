from stats import get_book_text, get_num_words, get_num_characters, sort_alpha_content_by_characters
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    bookLength = get_num_words(book_text)
    bookCharacters = get_num_characters(book_text)
    sorted = sort_alpha_content_by_characters(bookCharacters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {bookLength} total words")
    print("--------- Character Count -------")
    for val in sorted:
        print(f"{val['char']}: {val['num']}")
    print("============= END ===============")
main()