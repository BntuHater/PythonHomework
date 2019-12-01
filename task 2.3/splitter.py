def split(string:str, separator = ' '):
    ''' returns list of splited string by any separator '''
    new_strings = []
    new_string = ''
    for char in string:
        if char == separator:
            if not new_string:
                continue
            new_strings.append(new_string)
            new_string = ''
            continue
        new_string += char
    return new_strings

string = ' hello     world ! asd '
print(split(string))
print(string.split())