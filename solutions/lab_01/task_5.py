"""
Программа для формирования информационной карточки вычислительного эксперимента.
Выполняет сбор данных, расчет временных и математических характеристик,
а также диагностику типов данных.
"""

# Входные данные
investigator = input("Введите имя исследователя: ")
experiment_name = input("Введите название эксперимента: ")
runs_count = int(input("Введите количество выполненных запусков: "))
run_duration = float(input("Введите длительность одного запуска в секундах: "))
real_part = float(input("Введите действительную часть коэффициента: "))
imag_part = float(input("Введите мнимую часть коэффициента: "))

# Вычисления
total_duration_sec = runs_count * run_duration
total_duration_min = total_duration_sec / 60
coeff = complex(real_part, imag_part)
squared_modulus = real_part ** 2 + imag_part ** 2
has_runs = bool(runs_count)

# Вывод основной карточки результата
print("=" * 40)
print(f"ЭКСПЕРИМЕНТ: {experiment_name}")
print(f"Исследователь: {investigator}")
print(f"Запуски: {runs_count}")
print(f"Общее время: {total_duration_sec:.2f} с ({total_duration_min:.2f} мин)")
print(f"Коэффициент: {coeff}")
print(f"Квадрат модуля: {squared_modulus:.2f}")
print(f"Есть выполненные запуски: {has_runs}")
print("=" * 40)

# Диагностическая строка с типами введенных значений
print("\n[ДИАГНОСТИКА ТИПОВ ВВЕДЕННЫХ ЗНАЧЕНИЙ]")
print(f"investigator: {type(investigator)}")
print(f"experiment_name: {type(experiment_name)}")
print(f"runs_count: {type(runs_count)}")
print(f"run_duration: {type(run_duration)}")
print(f"real_part: {type(real_part)}")
print(f"imag_part: {type(imag_part)}")
