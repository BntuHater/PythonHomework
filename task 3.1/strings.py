import string as s

def common_chars(strings):
    result = []
    for letter in set(strings[0]):
        for string in strings:
            if letter not in string:
                break
        else:
            result.append(letter)
    return result

def common(strings):
    return set(strings[0]).intersection()

def chars_in_at_least_one_string(strings:[str]):
    result = []
    for string in strings:
        for letter in s.ascii_lowercase:
            if letter in string.lower():
                if letter in result:
                    continue
                result.append(letter)
    return result

def chars_in_at_least_two_strings(strings:[str]):
    result = []
    for letter in s.ascii_lowercase:
        count = 0
        for string in strings:
            if letter in string:
                count += 1
                if count >= 2:
                    if letter in result:
                        break
                    result.append(letter)
    return result

def chars_not_in_strings(strings:[str]):
    result = []
    for letter in s.ascii_lowercase:
        flag = True
        for string in strings:
            if letter in string:
                flag = False
                break
        if flag:
            result.append(letter)
    return result

strings = [
    'hello',
    'world',
    'python',
]

print('test:', common(strings))
print(common_chars(strings))
print(chars_in_at_least_one_string(strings))
print(chars_in_at_least_two_strings(strings))
print(chars_not_in_strings(strings))