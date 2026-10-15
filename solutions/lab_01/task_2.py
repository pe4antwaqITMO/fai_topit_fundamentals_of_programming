a = 1000
b = a
c = int("1000")

# Прогноз сравнений:
# a == b: True  (значения одинаковые — 1000)
# a is b: True  (b ссылается на тот же объект, что и a, после b = a)
# a == c: True  (значения одинаковые — 1000)
# a is c: False (c конструируется из строки заново, CPython создаст новый объект int в памяти)

print("Типы:", type(a), type(b), type(c))
print("Идентификаторы:", id(a), id(b), id(c))
print("a == b:", a == b)
print("a is b:", a is b)
print("a == c:", a == c)
print("a is c:", a is c)

# Пункт 3: Изменение c на None и корректная проверка через `is`
c = None
print("c is None:", c is None)

# Пункт 4: Эксперимент со строками
first = "python"
second = "py" + "thon"

# Прогноз: first == second -> True, first is second -> True (из-за интернирования строк во время компиляции)
print("first == second:", first == second)
print("first is second:", first is second)
