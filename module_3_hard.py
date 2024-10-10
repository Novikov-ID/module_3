def calculate_structure_sum(*args):
    all_sum = 0

    for i in args:
        if isinstance(i, (int, float)):
            all_sum += i
        elif isinstance(i, str):
            all_sum += len(i)
        elif isinstance(i, dict):
            for j in i.values():
                if isinstance(j, (int, float)):
                    all_sum += j
                elif isinstance(j, str):
                    all_sum += len(j)

            for k in i.keys():
                if isinstance(k, (int, float)):
                    all_sum += k
                elif isinstance(k, str):
                    all_sum += len(k)
        elif isinstance(i, (list, tuple, set)):
            all_sum += calculate_structure_sum(*i)

    return all_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)