def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    content = text.lower()
    result = {}
    for letter in content:
        if letter in result:
            result[letter] += 1
        else: 
            result[letter] = 1
    return result

def sort_alpha_content_by_characters(dictionary):
    val = []
    for value in dictionary:
        if value.isalpha():
            val.append({"char": value, "num": dictionary[value] })
    val.sort(reverse=True, key = lambda x: x["num"])
    return list(val)
