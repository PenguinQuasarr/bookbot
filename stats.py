def count_words(input_string):
    num_words = len(input_string.split())
    print(f"Found {num_words} total words")


def count_characters(input_string):
    character_dict = {}

    for letter in input_string:
        letter = letter.lower()
        if letter in character_dict:
            character_dict[letter] += 1
        else:
            character_dict[letter] = 1

    return character_dict

def sorted_dict(input_dict):
    sorted_input = []

    temp_list = list(input_dict.items())
    temp_list.sort(key=lambda item: item[1], reverse=True)

    for k, v in temp_list:
        if k.isalpha():
            sorted_input.append({k:v})

    return sorted_input
   


