import os

def count_words(text):
    """Counts the number of words in the given text."""
    words = text.split()
    return len(words)

def count_words_from_file(filename):
    """Reads a file and counts the number of words in it."""
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return None

    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return count_words(text)

def main():
    """Main function to prompt user input and count words."""
    print("Word Counter Program")
    print("Choose an option:")
    print("1. Enter text manually")
    print("2. Count words from a file")

    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        text = input("Enter a sentence or paragraph: ").strip()
        
        if not text:
            print("Error: No input provided. Please enter some text.")
            return
        
        word_count = count_words(text)
        print(f"Word Count: {word_count}")

    elif choice == "2":
        filename = input("Enter the filename (with extension): ").strip()
        word_count = count_words_from_file(filename)

        if word_count is not None:
            print(f"Word Count in '{filename}': {word_count}")

    else:
        print("Invalid choice. Please enter 1 or 2.")

if _name_ == "_main_":
    main()