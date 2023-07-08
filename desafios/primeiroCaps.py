def uppercase_first_letter(string):
    result = ""
    capitalize_next = True

    for char in string:
        if capitalize_next and char.isalpha():
            char = char.upper()
            capitalize_next = False
        elif char == "." or char == "!" or char == "?":
            capitalize_next = True

        result += char

    return result