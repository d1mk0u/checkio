def count_words(text, words):
    result = 0
    for w in words:
        if w in text.lower():
            result += 1
    return result

text = "How aresjfhdskfhskd you?"
words = {"how", "are", "you", "hello"}
print count_words(text, words)
