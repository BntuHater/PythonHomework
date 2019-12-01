def replace(string:str):
    """ replaces all " symbols with ' and vise versa """
    new_string = ''
    for char in string:
        if char == "'":
            new_string += '"'
        elif char == '"':
            new_string += "'"
        else:
            new_string += char
    return new_string

def replacer(string:str):
    return string.translate(string.maketrans({'"': "'", "'": '"'}))

string = 'qwe"asd"zxc\'fgh\'ert'
print('before:', string)
print('after:', replace(string))
print('another after:', replacer(string))
