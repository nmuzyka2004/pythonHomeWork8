def add_new_contact():
    with open('phonebook.txt', 'a', encoding = 'utf-8') as data:
        last_name = input("Фамилия: ")
        name = input("Имя: ")
        number = input("Номер телефона: ")
        about = input("Описание: ")
        contact = [last_name, name, number, about]
        s = ' '
        data.writelines(s.join(contact) + '\n')
        print(f"Новый контакт {last_name} добавлен в справочник")
