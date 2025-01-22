def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    
    # Generate report
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    
    char_frequency = get_char_frequency(text)
    sorted_chars = sorted(char_frequency.items(), key=lambda item: item[1], reverse=True)
    
    for char, count in sorted_chars:
        if char.isalpha():  # Filter to include only alphabet characters
            print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

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
            frequency[char] += 1  # Correctly increment the count
        else:
            frequency[char] = 1
    return frequency

if __name__ == "__main__":
    main()