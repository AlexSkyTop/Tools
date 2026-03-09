from itertools import zip_longest

def mat_to_text(matrix, n):
    result = []
    for col in zip_longest(*matrix, fillvalue=""):
        result.extend(col)
    return "".join(result)

print(mat_to_text(a, 2))
