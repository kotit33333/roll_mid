from collections import defaultdict
import random

def predict(history):
    if len(history) < 2:
        # Мало данных — рандом
        return random.randint(1, 6)

    transitions = defaultdict(lambda: defaultdict(int))

    # Собираем статистику переходов: для каждого числа считаем, сколько раз за ним идет каждое следующее
    for i in range(len(history) - 1):
        curr_state = history[i]
        next_state = history[i + 1]
        transitions[curr_state][next_state] += 1

    last = history[-1]
    next_counts = transitions.get(last, {})

    if not next_counts:
        return random.randint(1, 6)  # Нет данных — рандом

    # Выбираем следующий с максимальной вероятностью
    max_count = max(next_counts.values())
    candidates = [num for num, cnt in next_counts.items() if cnt == max_count]

    return random.choice(candidates)
