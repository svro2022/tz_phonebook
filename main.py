from utils import Phonebook

'''Реализация приложения телефонного справочника'''
phonebook = Phonebook()

page_size = 5
current_page = 1
while True:

    print("1. Вывод записей")
    print("2. Добавление записи")
    print("3. Редактирование записи")
    print("4. Поиск записей")
    print("5. Выход")
    choice = input("Введите номер действия: ")
    if choice == "1":
        phonebook.display_data(current_page, page_size)
        page_choice = input("Введите номер страницы (или 'n'/'p' для перехода \n "
                            "к следующей/предыдущей странице): ")
        if page_choice == "n":
            current_page += 1
        elif page_choice == "p":
            current_page -= 1
            if current_page < 1:
                current_page = 1
        else:
            current_page = int(page_choice)
    elif choice == "2":
        phonebook.add_entry()
        # Вывод всех записей после добавления новой
        current_page = 1
        phonebook.display_data(current_page, page_size)
    elif choice == "3":
        phonebook.edit_entry()
    elif choice == "4":
        phonebook.search_entries()
    elif choice == "5":
        break
    else:
        print("Неправильный номер действия!")

print("Программа завершена!")
