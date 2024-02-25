def get_hint(ticket_number, keyword):
    hints = {
        12345: "Подсказка 1: Это связано с темой A.",
        67890: "Подсказка 2: Это связано с темой B.",
        "keyword1": "Подсказка 3: Это связано с ключевым словом X.",
        "keyword2": "Подсказка 4: Это связано с ключевым словом Y."
    }

    if ticket_number in hints:
        return hints[ticket_number]
    elif keyword in hints.values():
        return next(key for key, value in hints.items() if value == keyword)
    else:
        return "Подсказка не найдена."

ticket_number = input("Введите номер билета: ")
keyword = input("Введите название темы или ключевое слово: ")

hint = get_hint(ticket_number, keyword)
print(hint)
