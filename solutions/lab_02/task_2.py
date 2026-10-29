import copy

original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)

original.append(["Databases", 5])
original[0][1] = 3

print(original)
print(alias)
print(shallow)
print(deep)

print(id(original), id(alias), id(shallow), id(deep))
print(id(original[0]), id(alias[0]), id(shallow[0]), id(deep[0]))
print(id(original[0][1]), id(alias[0][1]), id(shallow[0][1]), id(deep[0][1]))

wrong_matrix = [[0] * 3] * 3
wrong_matrix[0][0] = 1
print(wrong_matrix)

correct_matrix = [[0] * 3 for _ in range(3)]
correct_matrix[0][0] = 1
print(correct_matrix)
