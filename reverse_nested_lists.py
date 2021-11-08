l = [[1, 2], [3, 4], [5, 6, 7]]

def is_list(p): 
    return isinstance(p, list)

def deep_reverse(l):
    result = []
    for i in l:
        if isinstance(i, list):
            result.append(deep_reverse(i))
        else:
            result.append(i)
    result.reverse()
    return result
print(deep_reverse(l))