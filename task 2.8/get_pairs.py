def get_pairs(args:[]):
    """ returns a list of tuples containing pairs of elements """
    if len(args) <= 1:
        return None
    new_list = []
    result = []
    for i in range(1, len(args)):
        new_list.append(args[i - 1])
        new_list.append(args[i])
        result.append(tuple(new_list))
        del new_list[:]
    return result

def pairs(args:[]):
    if len(args) <= 1:
        return None
    new_list = []
    result = []
    for index, elem in enumerate(args):
        new_list.append(args[index - 1])
        new_list.append(elem)
        result.append(tuple(new_list))
        new_list = []
    return result

print(pairs([1, 2, 3, 4, 5]))
print(get_pairs([1, 2, 3, 4, 5]))