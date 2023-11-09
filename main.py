def num_of_words(long_string):
    return len(long_string.split())


def num_of_letters(long_string):
    long_string = long_string.lower()
    char_dict = {}
    for i in long_string:
        if i.isalpha():
            if i in char_dict:
                char_dict[i] += 1
            else:
                char_dict[i] = 1
    return char_dict


file_location = "books/frankenstein.txt"
with open(file_location) as file:
    file_contents = file.read()

print("--- Begin report of {file_location} ---")
print(f"{num_of_words(file_contents)} words found in the document")
print("")

letters = num_of_letters(file_contents)

for character in letters:
    print(f"The '{character}' was found {letters[character]}")
print("--- End Report ---")
