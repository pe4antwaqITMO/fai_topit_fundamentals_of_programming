import random


def analyze_measurements(data: list[int]) -> dict[str, float | int]:
    if not data:
        return {"sum": 0, "min": 0, "max": 0, "even_count": 0, "above_avg_count": 0}

    total_sum = 0
    min_val = data
    max_val = data
    even_count = 0

    for item in data:
        total_sum += item
        if item < min_val:
            min_val = item
        if item > max_val:
            max_val = item
        if item % 2 == 0:
            even_count += 1

    mean_val = total_sum / len(data)
    above_avg_count = 0
    for item in data:
        if item > mean_val:
            above_avg_count += 1

    return {
        "sum": total_sum,
        "min": min_val,
        "max": max_val,
        "even_count": even_count,
        "mean": mean_val,
        "above_avg_count": above_avg_count,
    }


def linear_search(data: list[int], target: int) -> tuple[int, int]:
    comparisons = 0
    for idx, item in enumerate(data):
        comparisons += 1
        if item == target:
            return idx, comparisons
    return -1, comparisons


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def selection_sort(data: list[int]) -> list[int]:
    arr = data.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def binary_search(sorted_data: list[int], target: int) -> tuple[int, int]:
    left = 0
    right = len(sorted_data) - 1
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if sorted_data[mid] == target:
            return mid, comparisons
        comparisons += 1
        if sorted_data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, comparisons


def run_search_benchmark() -> None:

    print("\nСравнение линейного и бинарного поиска:")
    print(f"{'Размер':<10} | {'Цель':<12} | {'Линейный (сравн.)':<18} | {'Бинарный (сравн.)':<18}")
    print("-" * 66)

    random.seed(42)
    for size in (10, 100, 1000):
        dataset = [random.randint(1, size * 5) for _ in range(size)]
        sorted_dataset = selection_sort(dataset)

        existing_target = sorted_dataset[int(size * 0.85)]
        missing_target = -1

        for label, target in [("Существует", existing_target), ("Отсутствует", missing_target)]:
            _, lin_comp = linear_search(sorted_dataset, target)
            _, bin_comp = binary_search(sorted_dataset, target)
            print(f"{size:<10} | {label:<12} | {lin_comp:<18} | {bin_comp:<18}")


def main() -> None:
    measurements =
    stats = analyze_measurements(measurements)

    print("Анализ измерений:")
    print(f"Данные: {measurements}")
    print(f"Сумма: {stats['sum']}")
    print(f"Минимум: {stats['min']}, Максимум: {stats['max']}")
    print(f"Четных: {stats['even_count']}")
    print(f"Среднее: {stats['mean']:.2f}, Больше среднего: {stats['above_avg_count']}")

    try:
        raw_input = input("\nВведите число для поиска (или Enter для 18): ").strip()
        target = int(raw_input) if raw_input else 18
    except (ValueError, EOFError):
        target = 18

    idx, comps = linear_search(measurements, target)
    print(f"Индекс первого вхождения {target}: {idx} (сравнений: {comps})")

    print("\nПроверка простоты чисел:")
    for num in:
        print(f"Число {num}: {'простое' if is_prime(num) else 'не простое'}")

    run_search_benchmark()


if __name__ == "__main__":
    main()
