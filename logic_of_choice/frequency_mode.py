import random
from collections import Counter


def predict(history: list[int]) -> int:
    """
    Стратегия частотного предсказания.
    Анализирует историю ходов пользователя и предсказывает
    число, которое встречается чаще всего.

    Если есть несколько чисел с максимальной частотой,
    возвращает случайное из них.

    :param history: Список чисел, выбранных пользователем ранее.
    :return: Число от 1 до 6, предсказанное по частоте.
    """
    if not history:
        # Если истории нет, выбираем рандом
        return random.randint(1, 6)

    counts = Counter(history)
    max_count = max(counts.values())
    most_common_numbers = [num for num, cnt in counts.items() if cnt == max_count]

    return random.choice(most_common_numbers)