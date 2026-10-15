student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10

# 1. Первый и последний символ имени
print("Первый символ:", student[0], "| Последний символ:", student[-1])

# 2. Срез с именем и фамилией
first_name = student[0:4]
last_name = student[5:13]
print("Имя:", first_name, "| Фамилия:", last_name)

# 3. Верхний и нижний регистр
print("В верхнем:", student.upper())
print("В нижнем:", student.lower())

# 4. Инициалы А.С.
initials = student[0] + "." + student[5] + "."
print("Инициалы:", initials)

# 5. Название курса в обратном порядке
print("Курс наоборот:", course[::-1])

# 6. Форматирование строки тремя способами
percentage = (completed / total) * 100

res_percent = f"{student} — {course}: {completed}/{total} ({percentage:.1f}%)"
res_format = "{} — {}: {}/{} ({:.1f}%)".format(student, course, completed, total, percentage)
res_fstring = f"{student} — {course}: {completed}/{total} ({percentage:.1f}%)"

print("Способ %:       " + "%s — %s: %d/%d (%.1f%%)" % (student, course, completed, total, percentage))
print("Способ .format():" + res_format)
print("Способ f-строка: " + res_fstring)

# 7. Unicode исследования
symbol = "Я"
print("Символ:", symbol)
print("Кодовая позиция:", ord(symbol))
print("Восстановленный символ:", chr(ord(symbol)))
print("UTF-8 байты:", symbol.encode("utf-8"))
print("Длина байтовой строки:", len(symbol.encode("utf-8")))

# 8. Попытка изменить первый символ (неизменяемость)
# student[0] = "О"  # TypeError: 'str' object does not support item assignment
