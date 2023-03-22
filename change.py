def change_data():
    contact = input("Введите фамилию или имя контакта, который хотите изменить: ")
    with open('phonebook.txt', 'r+', encoding = 'utf-8') as data:
        count = 0
        lines = data.readlines()
        for line in lines:
            if contact in line:
                print(line)
                old_line = line
                count+=1              
                conf = input("Изменить? (да/нет): ")
                if conf.lower() == 'да':
                    print("1.Изменить фамилию")
                    print("2.Изменить имя")
                    print("3.Изменить номер телефона")
                    print("4.Изменить описание")        
                    line = line.split(' ')
                    change_contact = int(input())
                    if change_contact == 1:
                        line[0] = input("Введите нужную фамилию: ")
                    elif change_contact == 2:
                        line[1] = input("Введите нужное имя: ")
                    elif change_contact == 3:
                        line[2] = input("Введите нужный номер телефона: ")
                    elif change_contact == 4:
                        line[3] = input("Введите нужное описание: ")
                    else:
                        return                  
                    new_line = ' '.join(line)                 
                    with open('phonebook.txt', 'r', encoding = 'utf-8') as data:
                        lines = data.read()
                    new_data = lines.replace(old_line, new_line)    
                    with open('phonebook.txt', 'w', encoding = 'utf-8') as data:
                        data.write(new_data)                  
                        print("Внесены изменения")
                else:
                   print("ok")                    
        if count == 0:  
            print(f"{contact} отсутствует в контактах!")
            return

    