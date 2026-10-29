import gc

first = []
second = []

first.append(second)
second.append(first)

print(first[0] is second)
print(second[0] is first)

print(gc.isenabled())
print(gc.get_threshold())
print(gc.get_count())

id_first = id(first)
id_second = id(second)

del first, second
print(gc.collect())

# Доп. эксперимент с отключением
gc.disable()
a = []
b = []
a.append(b)
b.append(a)
del a, b
print(gc.collect())
gc.enable()

# Модель графа
n1 = {"name": "N1", "links": []}
n2 = {"name": "N2", "links": []}
n3 = {"name": "N3", "links": []}
n4 = {"name": "Independent", "links": []}

n1["links"].append(n2)
n2["links"].append(n3)
n3["links"].append(n1)

print(gc.collect()) # чистим перед тестом

del n1, n2, n3
print(gc.collect()) # смотрим сколько собрал граф

print(n4["name"])
