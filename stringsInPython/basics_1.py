def main():
    # Define a sample string
    sample_string = "Hello, World!"

    # 1. Length of the string
    print("Length of the string:", len(sample_string))

    # 2. Convert to lowercase
    print("Lowercase:", sample_string.lower())

    # 3. Convert to uppercase
    print("Uppercase:", sample_string.upper())

    # 4. Capitalize the first letter
    print("Capitalized:", sample_string.capitalize())

    # 5. Count occurrences of a substring
    substring = "l"
    print("Count of '" + substring + "':", sample_string.count(substring))

    # 6. Check if string starts with a specific prefix
    prefix = "Hell"
    print("Starts with '" + prefix + "':", sample_string.startswith(prefix))

    # 7. Check if string ends with a specific suffix
    suffix = "!"
    print("Ends with '" + suffix + "':", sample_string.endswith(suffix))

    # 8. Find the index of a substring
    substring = "Wo"
    print("Index of '" + substring + "':", sample_string.find(substring))

    # 9. Replace a substring with another substring
    old_substring = "World"
    new_substring = "Universe"
    replaced_string = sample_string.replace(old_substring, new_substring)
    print("Replaced string:", replaced_string)

    # 10. Split the string into a list
    split_string = sample_string.split(",")
    print("Split string:", split_string)

    # 11. Join a list of strings into one string
    words = ["Hello", "from", "the", "other", "side"]
    joined_string = " ".join(words)
    print("Joined string:", joined_string)

    # 12. Strip leading and trailing whitespace
    whitespace_string = "    Hello, World!    "
    stripped_string = whitespace_string.strip()
    print("Stripped string:", stripped_string)

    # 13. Check if all characters are alphanumeric
    alphanumeric_string = "Hello123"
    print("Is alphanumeric:", alphanumeric_string.isalnum())

    # 14. Check if all characters are alphabetic
    alphabetic_string = "Hello"
    print("Is alphabetic:", alphabetic_string.isalpha())

    # 15. Check if all characters are digits
    digit_string = "12345"
    print("Is digit:", digit_string.isdigit())

    # 16. Check if string is in lowercase
    lowercase_string = "hello"
    print("Is lowercase:", lowercase_string.islower())

    # 17. Check if string is in uppercase
    uppercase_string = "HELLO"
    print("Is uppercase:", uppercase_string.isupper())

    # 18. Check if string is titlecased
    titlecased_string = "Hello World"
    print("Is titlecased:", titlecased_string.istitle())

    # 19. Check if string is whitespace
    whitespace_string = "   "
    print("Is whitespace:", whitespace_string.isspace())

    # 20. Access individual characters
    print("Individual characters:")
    for char in sample_string:
        print(char)

if __name__ == "__main__":
    main()
