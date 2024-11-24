import string

def main():
    path_to_file = "books/frankenstein.csv"
    
    with open(path_to_file) as f:
        file_contents = f.read()
    
    write_book_report(file_contents, path_to_file)

def write_book_report(book, file_path):
    total_words = get_total_words(book)
    char_frequency = get_character_frequency(book)
    
    report = []
    report.append(f"--- Begin report of {file_path} ---")
    report.append(f"{total_words} words found in the document\n")
    
    sorted_chars = sorted(char_frequency.items())
    for char, freq in sorted_chars:
        report.append(f"The '{char}' character was found {freq} times")
    
    report.append("--- End report ---")
    
    report_content = "\n".join(report)
    print(report_content)

def get_character_frequency(text):
    text = text.lower()
    frequency = {}
    for char in text:
        if char in string.ascii_lowercase:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency

def get_total_words(text):
    return len(text.split())

main()