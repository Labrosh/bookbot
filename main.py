def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    print(f"{num_words} words found in this document")
    print(f"{char_count} characters found in this document")
    char_frequency = get_char_frequency(text)
    for char, count in char_frequency.items():
        print(f"'{char}': {count}")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(book_path):
    with open(book_path,) as file:
        text = file.read()
    return text

def get_char_count(text):
    return len(text)

def get_char_frequency(text):
    frequency = {}
    for char in text:
        char = char.lower()
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

if __name__ == "__main__":
    main()