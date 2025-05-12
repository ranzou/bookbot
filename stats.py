import string
def word_count(text):
    list = text.split()
    return len(list)

def char_count(text):
    lower_chars = list(text.lower())
    s = set(string.ascii_lowercase)
    character_count = dict.fromkeys(s, 0)

    for character in lower_chars:
        if character in character_count:
            character_count[character] += 1

    return character_count

def sort_on(dict):
    return dict["num"]

def sort_char_dict(char_counts):
    l = []
    for k,v in char_counts.items():
        l.append({"char": k, "num": v})

    l.sort(reverse=True, key=sort_on)
    return l
