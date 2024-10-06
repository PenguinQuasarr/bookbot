
# Reads and returns a text file
def read_book():
    with open("books/frankenstein.txt", mode="r") as book:
        return book.read()

# Counts the words in the text file and then returns the length
def count_words():
    book_word_count = read_book().split()
    return len(book_word_count)

# Counts the characters in the text file then returns as a dict
def count_characters():
    character_dict = {}
    for cha in read_book():
        if cha.isalpha():
            try:
                character_dict[cha.lower()] += 1
            except:
                character_dict[cha.lower()] = 1
    return character_dict

# Prints a report of the book
def print_report():
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words()} words found in the document\n")

    report_dict = count_characters()

    sorted_dict = dict(sorted(report_dict.items(), reverse=True, key=lambda x: x[1]))

    for letter, count in sorted_dict.items():
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

    
print_report()

