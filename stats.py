def num_words(text):
    word_count = 0
    for num in text.split():
        word_count += 1
    return word_count