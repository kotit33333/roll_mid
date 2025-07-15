from data_base_folder import data_base_logic
from logic_of_choice import  frequency_mode, ml_mode, pattern_mode, random_mode


class AdaptiveSelector:
    def __init__(self, login):
        self.login = login
        self.history = self._get_history()

    def _get_history(self):
        # Получение данных из БД
        return data_base_logic.get_choices(self.login)

    def update_history(self):
        self.history = data_base_logic.get_choices(self.login)

    def predict(self) -> int:
        if len(self.history) < 10:
            return random_mode.predict()
        elif len(self.history) < 30:
            return frequency_mode.predict(self.history)
        elif len(self.history) < 50:
            return pattern_mode.predict(self.history)
        else:
            ml_mode.train_model(self.login)
            print('hell')
            return ml_mode.predict(self.history)

