def find_message(text):
    result = ""
    for ch in text:
        # print ch
        if ch.isupper():
            result += ch
    return result
