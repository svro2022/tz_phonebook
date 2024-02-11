import json


class Phonebook:
    '''Класс для реализации телефонного справочника.'''
    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        '''Метод загрузки данных из файла.'''
        try:
            with open('phonebook.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        return data

    def save_data(self):
        '''Метод сохранения данных в файл.'''
        with open('phonebook.json', 'w') as file:
            json.dump(self.data, file, indent=4)

    def display_data(self, page, page_size):
        '''Метод вывода данных постранично.'''
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        page_data = self.data[start_index:end_index]
        for entry in page_data:
            print(f"Фамилия: {entry['surname']}")
            print(f"Имя: {entry['name']}")
            print(f"Отчество: {entry['patronymic']}")
            print(f"Организация: {entry['organization']}")
            print(f"Рабочий телефон: {entry['work phone']}")
            print(f"Личный телефон: {entry['personal phone']}")
            print("------------------------")

    def add_entry(self):
        '''Метод добавления новых данных.'''
        entry = {}
        entry['surname'] = input("Введите фамилию: ")
        entry['name'] = input("Введите имя: ")
        entry['patronymic'] = input("Введите отчество: ")
        entry['organization'] = input("Введите название организации: ")
        entry['work phone'] = input("Введите рабочий телефон: ")
        entry['personal phone'] = input("Введите личный телефон: ")
        self.data.append(entry)
        self.save_data()
        print("Запись добавлена!")

    def edit_entry(self):
        '''Метод редактирования данных.'''
        index = int(input("Введите индекс записи для редактирования: "))
        if index < 0 or index >= len(self.data):
            print("Неправильный индекс!")
            return
        entry = self.data[index]
        print(f"Фамилия: {entry['surname']}")
        print(f"Имя: {entry['name']}")
        print(f"Отчество: {entry['patronymic']}")
        print(f"Организация: {entry['organization']}")
        print(f"Рабочий телефон: {entry['work phone']}")
        print(f"Личный телефон: {entry['personal phone']}")
        field = input("Выберите поле для редактирования: (surname, name, patronymic, \n "
                      "organization, work phone, personal phone)")
        if field not in entry:
            print("Неправильное поле!")
            return
        value = input("Пишем новое значение: ")
        entry[field] = value
        self.save_data()
        print("Запись отредактирована!")

    def search_entries(self):
        '''Метод поиска записи по характеристикам.'''
        search_term = input("Введите характеристику для поиска (имя, фамилия, отчество или организация): ")
        results = []
        for entry in self.data:
            for field, value in entry.items():
                if field != "work phone" and field != "personal phone" and search_term.lower() in value.lower():
                    results.append(entry)
                    break
        if results:
            print("Результаты поиска:")
            for entry in results:
                print(f"Фамилия: {entry['surname']}")
                print(f"Имя: {entry['name']}")
                print(f"Отчество: {entry['patronymic']}")
                print(f"Организация: {entry['organization']}")
                print(f"Рабочий телефон: {entry['work phone']}")
                print(f"Личный телефон: {entry['personal phone']}")
                print("------------------------")
        else:
            print("Ничего не найдено!")
