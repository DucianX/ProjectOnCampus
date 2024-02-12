import string


def main():
    # Get a filename
    file_name = input("Plz input a file name.\n")

    try:
        # Open the file with read mode and copy it to 'text'
        with open(file_name, 'r') as file:
            text = file.read()

            # Count words
            word_count = len(text.split())

            # Count characters (excluding whitespace)
            char_count = 0
            for char in text:
                if not char.isspace():
                    char_count += 1

            # Count alphanumeric characters (excluding punctuations)
            alphanumeric_count = sum(1 for char in text if char.isalnum())

            # Print the counts
            print(f"Words: {word_count}\nCharacters: {char_count}")
            print(f"Letters & Numbers: {alphanumeric_count}")

    except FileNotFoundError:
        print(f"Can not open {file_name}.\n")


main()
