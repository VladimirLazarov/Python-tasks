def alternate_case_characters(input_str):
    result = ""
    for i, char in enumerate(input_str):
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result

def alternate_case_words(input_str):
    words = input_str.split()
    result_words = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            result_words.append(word.lower())
        else:
            result_words.append(word.upper())
    return ' '.join(result_words)

def main():
    input_str = "Hello World"

    result_characters = alternate_case_characters(input_str)
    print("Alternate case characters: " + result_characters)

    result_words = alternate_case_words(input_str)
    print("Alternate case words: " + result_words)

if __name__ == "__main__":
    main()