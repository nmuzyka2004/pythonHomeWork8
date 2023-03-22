from print_all import *
from find_data import *
from add_new import *
from change import *
from del_contact import *

def show_menu():
    print(f"Выберите необходимое действие: \n"
          "1. Отобразить весь справочник \n"
          "2. Поиск абонента по фамилии \n"
          "3. Поиск абонента по имени \n"
          "4. Поиск абонента по номеру телефона \n"
          "5. Добавить нового абонента в справочник: \n"
          "6. Изменить данные абонента: \n"
          "7. Удалить данные абонента из справочника: \n"
          "0. Выход из меню: \n")
    choice = int(input())
    if choice == 1:
        print_all()
    elif choice == 2:
        find_by_last_name()      
    elif choice == 3:
        find_by_name()
    elif choice == 4:
        find_by_number()
    elif choice == 5:
        add_new_contact()
    elif choice == 6:
        change_data()
    elif choice == 7:
        del_data()
    else:
        exit()







