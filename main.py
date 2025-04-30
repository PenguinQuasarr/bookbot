import sys
from stats import count_words, count_characters, sorted_dict

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    book_dict = count_characters(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    count_words(book_text)
    print("--------- Character Count -------")
    
    for item in sorted_dict(book_dict):
        for k, v in item.items():
            print(f"{k}: {v}")

    print("============= END ===============")



main()
