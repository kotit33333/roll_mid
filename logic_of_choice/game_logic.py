from logic_of_choice import adaptive_selector
from data_base_folder import data_base_logic

selectors = {}

def start_session(login):
    selectors[login] = adaptive_selector.AdaptiveSelector(login)

def process_user_choice(login, user_choice):
    selector = selectors.get(login)
    if not selector:
        selector = adaptive_selector.AdaptiveSelector(login)
        selectors[login] = selector
    predicted = selector.predict()
    is_correct = (predicted == user_choice)
    data_base_logic.add_choice_to_db(login, user_choice, is_correct)
    selector.update_history()  # если добавил такой метод
    return predicted, is_correct