def count_letters(string:str):
    result = {}
    for letter in string:
        result[letter] = string.count(letter)
    return result
    
print(count_letters('stringsample'))