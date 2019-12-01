def get_digits(number:int):
    """ returns a tuple of given integer's digits """
    string = str(number)
    num_list = []
    for char in string:
        num_list.append(int(char))  
    return tuple(num_list)
    
print(get_digits(123456))