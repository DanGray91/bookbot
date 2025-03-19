import sys
from stats import get_book_text, count_words, count_characters, sort_chars_by_count

def main():
    if len(sys.argv) < 2:
    	print("Usage: python3 main.py <path_to_book>")
    	sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    char_count = count_characters(book_text)
    sorted_chars = sort_chars_by_count(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()
