def find_by_last_name():
    last_name = input("Введите фамилию для поиска: ")
    with open('phonebook.txt', 'r', encoding = 'utf-8') as data:
        count = 0
        for line in data:
            if line.split(' ')[0] == last_name:
                print(line)
                count+=1
        if count == 0:  
            print(f"{last_name} отсутствует в контактах!")
    

def find_by_name():
    name = input("Введите имя для поиска: ")
    with open('phonebook.txt', 'r', encoding = 'utf-8') as data:
        count = 0
        for line in data:
            if line.split(' ')[1] == name:
                print(line)
                count+=1
        if count == 0:    
            print(f"{name} отсутствует в контактах!")



def find_by_number():
    number = input("Введите номер телефона для поиска: ")
    with open('phonebook.txt', 'r', encoding = 'utf-8') as data:
        for line in data:
            if line.split(' ')[2] == number:
                print(line)
                return
    print("Такой номер отсутствует в контактах!")

