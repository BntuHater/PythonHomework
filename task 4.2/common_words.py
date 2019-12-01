import string

def most_common_words(filename:str, number_of_words = 3):
    with open(filename) as rf:
        content = rf.read()
    for char in content.lower():
        if char not in string.ascii_lowercase and char != ' ':
            content = content.replace(char, ' ')
    words = content.split()
    ratio = {}
    for word in words:
        ratio[word] = words.count(word)
    words = []
    for word, occurrence in ratio.items():
        words.append([word, occurrence])
    sorted_words = sorted(words, key = lambda s: s[1], reverse = True)
    return [word[0] for word in sorted_words[:number_of_words]]
    
filename = 'data/lorem_ipsum.txt'
print(most_common_words(filename))
