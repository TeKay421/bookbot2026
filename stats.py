def num_words(text):
    word_count = 0
    for num in text.split():
        word_count += 1
    return word_count

def num_characters(text):
    char_count = {}
    for ch in text:
        ch = ch.lower()
        char_count[ch] = char_count.get(ch, 0) + 1
    return char_count

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        if ch.isalpha():
            sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    

def sort_on(items):
    return items["num"]