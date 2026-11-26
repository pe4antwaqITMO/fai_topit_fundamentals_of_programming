def mean(values: list[int] | list[float]) -> float:

    if not values:
        return 0.0
    total = 0.0
    for val in values:
        total += val
    return total / len(values)


def minimum(values: list[int] | list[float]) -> float | int | None:

    if not values:
        return None
    min_val = values
    for val in values[1:]:
        if val < min_val:
            min_val = val
    return min_val


def maximum(values: list[int] | list[float]) -> float | int | None:

    if not values:
        return None
    max_val = values
    for val in values[1:]:
        if val > max_val:
            max_val = val
    return max_val


def classify(score: float) -> str:

    if score >= 90:
        return "отличный"
    if score >= 75:
        return "хороший"
    if score >= 60:
        return "удовлетворительный"
    return "недостаточный"


def student_summary(name: str, results: list[int]) -> dict[str, object]:

    if not results:
        return {
            "name": name,
            "has_results": False,
            "mean": 0.0,
            "min": None,
            "max": None,
            "category": "нет оценок",
        }

    avg_score = mean(results)
    return {
        "name": name,
        "has_results": True,
        "mean": avg_score,
        "min": minimum(results),
        "max": maximum(results),
        "category": classify(avg_score),
    }


def find_top_students(students: dict[str, list[int]]) -> list[str]:

    best_avg = -1.0
    leaders: list[str] = []

    for name, results in students.items():
        if not results:
            continue
        avg = mean(results)
        if avg > best_avg:
            best_avg = avg
            leaders = [name]
        elif abs(avg - best_avg) < 1e-9:
            leaders.append(name)

    return leaders


def _sort_summaries_desc(summaries: list[dict[str, object]]) -> list[dict[str, object]]:
       arr = summaries.copy()
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if float(arr[j]["mean"]) > float(arr[max_idx]["mean"]):
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr


def group_summary(students: dict[str, list[int]]) -> dict[str, object]:

    category_counts = {
        "отличный": 0,
        "хороший": 0,
        "удовлетворительный": 0,
        "недостаточный": 0,
        "нет оценок": 0,
    }

    student_summaries: list[dict[str, object]] = []
    valid_means: list[float] = []

    for name, results in students.items():
        summary = student_summary(name, results)
        student_summaries.append(summary)
        cat = str(summary["category"])
        category_counts[cat] = category_counts.get(cat, 0) + 1
        if summary["has_results"]:
            valid_means.append(float(summary["mean"]))

    group_mean = mean(valid_means)
    leaders = find_top_students(students)
    rating = _sort_summaries_desc(student_summaries)

    return {
        "total_students": len(students),
        "group_mean": group_mean,
        "leaders": leaders,
        "category_counts": category_counts,
        "rating": rating,
    }


def format_report(
    student_data: list[dict[str, object]], group_data: dict[str, object]
) -> str:

    if group_data["total_students"] == 0:
        return "Группа пуста. Нет данных для формирования отчета."

    lines = ["Отчет по успеваемости группы:"]
    lines.append(f"Всего студентов: {group_data['total_students']}")
    lines.append(f"Общий средний балл группы: {group_data['group_mean']:.2f}")

    leaders = group_data["leaders"]
    leaders_str = ", ".join(leaders) if leaders else "не определены"
    lines.append(f"Лидер(ы): {leaders_str}")

    lines.append("\nРаспределение по категориям:")
    for cat, count in group_data["category_counts"].items():
        if count > 0:
            lines.append(f"  {cat}: {count}")

    lines.append("\nРейтинг студентов:")
    for rank, st in enumerate(student_data, start=1):
        if st["has_results"]:
            lines.append(
                f"{rank}. {st['name']}: среднее={st['mean']:.2f}, "
                f"min={st['min']}, max={st['max']} [{st['category']}]"
            )
        else:
            lines.append(f"{rank}. {st['name']}: нет оценок")

    return "\n".join(lines)


def main() -> None:
    scenarios = {
        "1. Обычный набор данных": {
            "Анна":,
            "Борис":,
            "Дарья":,
            "Илья":,
        },
        "2. Один студент": {
            "Елена":,
        },
        "3. Несколько лидеров": {
            "Анна":,
            "Борис":,
            "Виктор":,
        },
        "4. Пустая группа": {},
        "5. Студент без результатов": {
            "Анна":,
            "Олег": [],
        },
        "6. Граничные значения категорий": {
            "Студент_90":,
            "Студент_89":,
            "Студент_75":,
            "Студент_74":,
            "Студент_60":,
            "Студент_59":,
        },
    }

    for title, data in scenarios.items():
        print(f"\nСценарий: {title}")
        g_stats = group_summary(data)
        print(format_report(g_stats["rating"], g_stats))


if __name__ == "__main__":
    main()
