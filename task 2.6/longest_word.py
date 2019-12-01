def get_longest_word(string:str):
    """ returns the longest word in a string """
    return max(string.replace('\t', ' ').replace('\n', ' ').split(), key = len)

print(get_longest_word('123 123456 qwerty zxcvbn zxcv'))    

    
