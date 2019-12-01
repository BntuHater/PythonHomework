def foo(nums:[int]):
    """ 
        returns a new list such that each element at index i 
        of the new list is the product of all the numbers 
        in the original array except the one at i
    """
    result = []
    for i in range(len(nums)):
        new = 1
        for j in range(len(nums)):
            if i == j:
                continue
            new *= nums[j]
        result.append(new)
    return result

print(foo([1, 2, 3, 4, 5]))