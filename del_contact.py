def del_data():
    contact = input("Введите фамилию или имя контакта, который хотите удалить: ")
    with open('phonebook.txt', 'r+', encoding = 'utf-8') as data:
        count = 0
        lines = data.readlines()
        for line in lines:
            if contact in line:
                print(line)
                count+=1
                del_line = line
                conf = input("Удалить? (да/нет): ")
                if conf.lower() == 'да':
                    data = open('phonebook.txt', 'r', encoding = 'utf-8').read()
                    data = data.replace(del_line," ")
                    with open('phonebook.txt', 'w', encoding = 'utf-8') as data1:
                        data1.write(data)
                        print(f"Контакт удален")      
                else:
                    print("ok")                    
        if count == 0:  
            print(f"{contact} отсутствует в контактах!")
            return
        

