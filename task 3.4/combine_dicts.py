def combine_dicts(*dicts:dict):
    result = {}
    for dictionary in dicts:
        for key, value in dictionary.items():
            result[key] = value
    return result

dict1 = {
    'a': 1,
    'b': 2,
}
dict2 = {
    'a': 2,
    'c': 3,
}
dict3 = {
    'a': 3,
    'd': 4,
}
print(combine_dicts(dict1, dict2, dict3))