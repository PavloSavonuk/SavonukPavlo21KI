class PavloSavonuk:
    def __init__(self, first_name=None, last_name=None, birth_year=None):
        self.first_name = first_name if first_name is not None else 'Павло'
        self.last_name = last_name if last_name is not None else 'Савонюк'
        self.birth_year = birth_year if birth_year is not None else 2008

    def calculate_course(self):
        current_year = 2025
        course = current_year - self.birth_year
        return f"Курс відповідно до року народження: {course} років"

    def create_name_list(self):
        name_list = [self.first_name, self.last_name]
        return name_list


class AdvancedPavlo(PavloSavonuk):
    def __init__(self, first_name=None, last_name=None, birth_year=None,
                 hobby=None, city=None, college=None):
        super().__init__(first_name, last_name, birth_year)
        self.hobby = hobby if hobby is not None else 'Плавання'
        self.city = city if city is not None else 'Луцьк'
        self.college = college if college is not None else 'Коледж ТФК ЛНТУ'

    def display_full_profile(self):
        profile = (f"Ім'я: {self.first_name}, Прізвище: {self.last_name}, "
                   f"Рік народження: {self.birth_year}, Хобі: {self.hobby}, "
                   f"Місто: {self.city}, Коледж: {self.college}")
        return profile

    def _protected_method(self):
        return f"{self.first_name} захоплюється {self.hobby}."

    def __private_method(self):
        return f"Це приватне повідомлення для {self.first_name} {self.last_name}."

    def reveal_private_message(self):
        return self.__private_method()


# Тестуємо
adv_pavlo = AdvancedPavlo()
print(adv_pavlo.display_full_profile())
print(adv_pavlo._protected_method())
print(adv_pavlo.reveal_private_message())
