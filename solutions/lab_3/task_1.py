def get_work_description(work_type: str) -> str:
    match work_type:
        case "exam":
            return "экзаменационная работа"
        case "project":
            return "проектная работа"
        case "practice":
            return "практическая работа"
        case _:
            return "неизвестный тип работы"


def classify_student(score: int, work_type: str, absences: int) -> tuple[bool, str, str]:

  
    if not (0 <= score <= 100) or not (0 <= absences <= 5):
        msg = f"Ошибка данных: балл={score}, пропуски={absences} вне допустимых диапазонов."
        return False, "ошибка", msg

   
    levels = ["недостаточный", "удовлетворительный", "хороший", "отличный"]
    if score >= 90:
        level_idx = 3
    elif score >= 75:
        level_idx = 2
    elif score >= 60:
        level_idx = 1
    else:
        level_idx = 0

    
    if absences > 3 and level_idx > 0:
        level_idx -= 1

    final_level = levels[level_idx]


    work_desc = get_work_description(work_type)

    result_str = (
        f"Работа: {work_desc} ({work_type}) | Балл: {score} | "
        f"Пропуски: {absences} -> Итоговый уровень: {final_level}"
    )
    return True, final_level, result_str


def main() -> None:

    test_cases = [
        (0, "exam", 0),
        (59, "practice", 2),
        (60, "project", 1),
        (74, "exam", 4),     
        (75, "practice", 3), 
        (89, "project", 5),  
        (90, "exam", 4),     
        (100, "project", 0),
        (105, "exam", 1),    
        (80, "unknown", 6),  
    ]

    print("=== ТЕСТОВЫЕ СЦЕНАРИИ (ЧАСТЬ 4) ===")
    for score, w_type, abs_cnt in test_cases:
        _, _, output = classify_student(score, w_type, abs_cnt)
        print(output)


    records = [
        (95, "exam", 1),
        (82, "project", 4),
        (67, "practice", 0),
        (54, "exam", 2),
        (91, "project", 5),
        (76, "practice", 3),
        (60, "exam", 4),
        (88, "project", 2),
        (100, "practice", 0),
        (45, "unknown", 1),
    ]

    summary_counts = {
        "отличный": 0,
        "хороший": 0,
        "удовлетворительный": 0,
        "недостаточный": 0,
    }

    print("\n=== ПРАКТИЧЕСКОЕ РАСШИРЕНИЕ (10 ЗАПИСЕЙ) ===")
    for record in records:
        s, w, a = record
        is_valid, level, text = classify_student(s, w, a)
        print(text)
        if is_valid and level in summary_counts:
            summary_counts[level] += 1

    print("\n--- Итоговая сводка по уровням ---")
    for lvl, count in summary_counts.items():
        print(f"{lvl.capitalize()}: {count}")


if __name__ == "__main__":
    main()
