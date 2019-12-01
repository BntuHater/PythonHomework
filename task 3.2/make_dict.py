def generate_squares(num:int):
    result = {}
    for i in range(1, num + 1):
        result[i] = i ** 2
    return result

print(generate_squares(5))