def split_by_index(string:str, indexes:[int]):
    """ splits a string by indexes """
    new_list = []
    for i, index in enumerate(indexes):
        if index in range(0, len(string)):
            if i == 0:
                new_list.append(string[:index])
            elif index < indexes[i - 1]:
                continue
            else:
                new_list.append(string[indexes[i - 1]:index])
            last = index

    if indexes[len(indexes) - 1] < len(string) - 1:
        new_list.append(string[last:])
    return new_list

print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
print(split_by_index('0123456789', [-5, 4, 15, 8]))
print(split_by_index('no luck', [42]))