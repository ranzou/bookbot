import sys
from stats import *

def get_book_text(filepath):
    return filepath.read()


def main():
    arguments = sys.argv
    if len(arguments) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(arguments[1]) as f:
        text = get_book_text(f)
        num_words = word_count(text)
        character_counts = sort_char_dict(char_count(text))
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {arguments[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in character_counts:
            if item["char"].isalpha():
                print(f"{item["char"]}: {item["num"]}")
        print("============= END ===============")

main()
