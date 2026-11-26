def add_submission(
    record: tuple[str, str, int],
    students: set[str],
    labs: set[str],
    student_attempts: dict[str, list[tuple[str, int]]],
    best_scores: dict[tuple[str, str], int],
    attempt_counts: dict[tuple[str, str], int],
) -> None:

    student, lab, score = record
    pair_key = (student, lab)

    students.add(student)
    labs.add(lab)

    if student not in student_attempts:
        student_attempts[student] = []
    student_attempts[student].append((lab, score))

    if pair_key not in best_scores or score > best_scores[pair_key]:
        best_scores[pair_key] = score

    attempt_counts[pair_key] = attempt_counts.get(pair_key, 0) + 1


def process_query(
    query: str,
    student_attempts: dict[str, list[tuple[str, int]]],
    best_scores: dict[tuple[str, str], int],
    attempt_counts: dict[tuple[str, str], int],
) -> str:

    parts = query.strip().split()
    if not parts:
        return "Ошибка: пустой запрос."

    cmd = parts.lower()

    match cmd:
        case "student":
            if len(parts) != 2:
                return "Использование: student <имя>"
            name = parts
            if name not in student_attempts:
                return f"Студент '{name}' не найден."
            return f"Попытки {name}: {student_attempts[name]}"

        case "best":
            if len(parts) != 3:
                return "Использование: best <имя> <работа>"
            key = (parts, parts)
            if key not in best_scores:
                return f"Нет данных по паре {key}."
            return f"Лучший балл {key} по {key}: {best_scores[key]}"

        case "attempts":
            if len(parts) != 3:
                return "Использование: attempts <имя> <работа>"
            key = (parts, parts)
            if key not in attempt_counts:
                return f"Нет попыток для пары {key}."
            return f"Количество попыток {key} по {key}: {attempt_counts[key]}"

        case "completed":
            if len(parts) != 2:
                return "Использование: completed <работа>"
            target_lab = parts
            completed_students = [
                st for (st, lb) in best_scores.keys() if lb == target_lab
            ]
            if not completed_students:
                return f"Работу '{target_lab}' еще никто не сдавал."
            return f"Сдали {target_lab}: {', '.join(sorted(completed_students))}"

        case _:
            return f"Неизвестная команда: '{cmd}'"


def main() -> None:
    submissions = [
        ("anna", "lab_01", 5),
        ("boris", "lab_01", 4),
        ("anna", "lab_02", 5),
        ("daria", "lab_01", 3),
        ("boris", "lab_02", 5),
        ("anna", "lab_01", 4),
    ]

    students: set[str] = set()
    labs: set[str] = set()
    student_attempts: dict[str, list[tuple[str, int]]] = {}
    best_scores: dict[tuple[str, str], int] = {}
    attempt_counts: dict[tuple[str, str], int] = {}

    for sub in submissions:
        add_submission(sub, students, labs, student_attempts, best_scores, attempt_counts)

    print("1. Все студенты:", students)
    print("2. Все лабораторные:", labs)
    print("3. Попытки студентов:", student_attempts)
    print("4. Лучшие результаты:", best_scores)
    print("5. Количество попыток:", attempt_counts)

    lab01_students = {st for (st, lb) in best_scores if lb == "lab_01"}
    lab02_students = {st for (st, lb) in best_scores if lb == "lab_02"}
    both_labs = lab01_students & lab02_students
    print("\nСдали обе работы (lab_01 и lab_02):", both_labs)

    new_record = ("daria", "lab_02", 4)
    add_submission(new_record, students, labs, student_attempts, best_scores, attempt_counts)
    print(
        f"\nДобавлена запись {new_record}. Теперь обе работы сдали:",
        {st for (st, lb) in best_scores if lb == "lab_01"}
        & {st for (st, lb) in best_scores if lb == "lab_02"},
    )

    queries = [
        "student anna",
        "best anna lab_01",
        "attempts boris lab_02",
        "completed lab_01",
        "best unknown lab_01",
        "delete anna",
    ]
    print("\nТекстовые запросы:")
    for q in queries:
        print(f"> {q}\n  {process_query(q, student_attempts, best_scores, attempt_counts)}")


if __name__ == "__main__":
    main()
