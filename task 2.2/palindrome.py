def is_palindrome(string:str):
    """ checks whether a string is a palindrome or nah """
    i = 0
    new_string = string.replace(' ', '').lower()
    while i < (len(new_string) / 2):
        if new_string[i] != new_string[len(new_string) - i - 1]: #  i think that string[::-1] is reverse func variety
            return False
        return True

def palindrome(string:str):
    return string.replace(' ', '').lower() == string[::-1].replace(' ', '').lower()

string_1 = 'qwerty'
string_2 = 'Was it a car or a cat I saw'

print(is_palindrome(string_1))
print(is_palindrome(string_2))

print(palindrome(string_1))
print(palindrome(string_2))
