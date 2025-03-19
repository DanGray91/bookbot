def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    text = text.lower()
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(dict):
    return dict["count"]

def sort_chars_by_count(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        char_info = {"char": char, "count": count}
        chars_list.append(char_info)
    
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list
