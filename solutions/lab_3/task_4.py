from typing import Callable, Sequence


def arithmetic_mean(values: list[float]) -> float:

    if not values:
        return 0.0
    total = 0.0
    for v in values:
        total += v
    return total / len(values)


def normalize_name(name: str) -> str:
    
    cleaned = name.strip()
    if not cleaned:
        return ""
    parts = cleaned.split()
    return " ".join(part.capitalize() for part in parts)


def build_report(
    student: str,
    results: list[int],
    *,
    precision: int = 2,
    prefix: str = "Результат",
) -> str:

    norm_student = normalize_name(student)
    if not norm_student:
        return f"{prefix}: имя студента не указано."
    if not results:
        return f"{prefix} ({norm_student}): нет оценок."

    mean_val = arithmetic_mean([float(x) for x in results])
    return f"{prefix} ({norm_student}): средний балл = {mean_val:.{precision}f}"


def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:

    if not tags:
        return ()
    seen: set[str] = set()
    unique_tags: list[str] = []
    for raw_tag in tags:
        tag = raw_tag.strip()
        if not tag:
            continue
        if lowercase:
            tag = tag.lower()
        if tag not in seen:
            seen.add(tag)
            unique_tags.append(tag)
    return tuple(unique_tags)


course = "Программирование на Python"


def outer_scope_demo() -> str:

    status = "в процессе"

    def inner_updater() -> None:
        nonlocal status
        local_note = "модуль 3 завершен"
        status = f"обновлено ({local_note})"

    inner_updater()
    return f"Курс: '{course}' (длина названия: {len(course)}), статус: {status}"


def add_result_fixed(value: int, results: list[int] | None = None) -> list[int]:

    new_results = [] if results is None else results.copy()
    new_results.append(value)
    return new_results


def apply_to_results(
    operation: Callable[[int], int], values: Sequence[int]
) -> list[int]:

    return [operation(v) for v in values]


def make_threshold_checker(threshold: int) -> Callable[[int], bool]:

    def checker(score: int) -> bool:
        return score >= threshold
    return checker


def run_tests_and_demos() -> None:
    assert arithmetic_mean([10.0, 20.0, 30.0]) == 20.0
    assert arithmetic_mean([5.5]) == 5.5
    assert arithmetic_mean([]) == 0.0

    assert normalize_name("  иван   иванов ") == "Иван Иванов"
    assert normalize_name("АННА-МАРИЯ   петрова") == "Анна-мария Петрова"
    assert normalize_name("   ") == ""

    assert build_report("  анна ",) == "Результат (Анна): средний балл = 85.00"
    assert build_report("борис",, precision=1, prefix="Итог") == "Итог (Борис): средний балл = 72.5"
    assert build_report("дарья", []) == "Результат (Дарья): нет оценок."

    assert collect_tags("Python", " python ", "", "LAB") == ("python", "lab")
    assert collect_tags("Python", "LAB", lowercase=False) == ("Python", "LAB")
    assert collect_tags("   ", "") == ()

    raw_tags = ["  Algo ", "Data", "algo", "  "]
    report_kwargs = {"precision": 3, "prefix": "Аттестация"}

    print("Распаковка *:", collect_tags(*raw_tags, lowercase=True))
    print("Распаковка **:", build_report("илья смирнов",, **report_kwargs))

    print("\nПроверка LEGB:")
    print(outer_scope_demo())
    print("Глобальная переменная course:", course)

    print("\nИсправление default-списка:")
    first_call = add_result_fixed(95)
    second_call = add_result_fixed(80)
    print("Первый вызов:", first_call, "| Второй вызов:", second_call)

    print("\nФункции высшего порядка и замыкания:")
    scores =

    def add_bonus(x: int) -> int:
        return min(100, x + 5)

    print("Именованная функция (+5):", apply_to_results(add_bonus, scores))
    print("Lambda (* 1.1):", apply_to_results(lambda x: int(x * 1.1), scores))

    pass_checker = make_threshold_checker(60)
    honors_checker = make_threshold_checker(90)
    print("Порог 60:", [pass_checker(s) for s in scores])
    print("Порог 90:", [honors_checker(s) for s in scores])


if __name__ == "__main__":
    run_tests_and_demos()
