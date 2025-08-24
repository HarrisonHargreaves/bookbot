from stats import count_words
from stats import count_each_character
from stats import sort_character_count

import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    filepath = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    book_text = get_book_text(filepath)
    word_count = count_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    character_count = count_each_character(book_text)
    sorted_character_count = sort_character_count(character_count)

    print("--------- Character Count -------")
    for char, count in sorted_character_count.items():
        print(f"{char}: {count}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
