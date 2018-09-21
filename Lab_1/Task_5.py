l = ['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]

def flatten(l):

    return flatten(l[0]) + (flatten(l[1:]) if len(l) > 1 else []) if type(l) is list else [l]

print(flatten(l))