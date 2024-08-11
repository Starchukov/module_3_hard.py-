def calculate_structure_sum (data_structure):
    s = 0
    if isinstance(data_structure, list):
        for i in data_structure:
            s += calculate_structure_sum(i)
    elif isinstance(data_structure, set):
        for i in data_structure:
            s += calculate_structure_sum(i)
    elif isinstance(data_structure, tuple):
        for i in data_structure:
            s += calculate_structure_sum(i)
    elif isinstance(data_structure, str):
        s += len(data_structure)
    elif isinstance(data_structure, (int, float)):
        s += data_structure
    if isinstance(data_structure, dict):
        for k, v in data_structure.items():
            s += calculate_structure_sum(k)
            s += calculate_structure_sum(v)
    return s

#1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
