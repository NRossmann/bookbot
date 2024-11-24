def main():
    path_to_file = "books/frankenstein.csv"
    
    with open(path_to_file) as f:
        file_contents = f.read()
    
    char_frequency = get_character_frequency(file_contents)
    print(char_frequency)

def get_character_frequency(text):
    text = text.lower()
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

main()