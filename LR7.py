# Проверки
def check_number(number):
    if len(number) > 7:
        return False

    if (number[0] == '0'):
        return False

    for i in number:
        if (i not in '0123456789'):
            return False

    return True

def check_find_number(command, numbers_names):
    cnt = 0 # кол-во совпадение

    for i in range(len(numbers_names)):
        if (numbers_names[i][0] == command[1]):
            cnt += 1

    if (cnt > 0):
        return True
    else:
        return False

def check(command, numbers_names, max_n):
    if (len(command) == 3):
        if (check_number(command[1])):
            if (len(command[2]) <= 15): 
                if (len(numbers_names) != max_n):
                    return True
                else:    
                    if (check_find_number(command, numbers_names)):
                        return True
    
    return False

# Команды
def add(command, numbers_names, max_n):
    if (check(command, numbers_names, max_n)):
        for i in range(len(numbers_names)):
            if numbers_names[i][0] == command[1]:
                numbers_names[i][1] = command[2]
                return 

        numbers_names.append([command[1], command[2]])
        return numbers_names
    else:
        print("Error")
        return

def find(numbers_names, command):
    for i in range(len(numbers_names)):
        if numbers_names[i][0] == command[1]:
            return numbers_names[i][1]
        if numbers_names[i][1] == command[1]:
            return numbers_names[i][0]
    else:
        return ("Not found")

def delete(numbers_names, command):
    for i in range(len(numbers_names)):
        if numbers_names[i][0] == command[1]:
            return numbers_names.pop(i)
    else:
        print("Not found")
        return


n = int(input("Число запросов: "))
max_n = int(input("Максимальное кол-во контактов: "))
numbers_names = [] # [[number0, name0], [number1, name1], ...]

for i in range(n):  
    print("Введите команду: ")
    command = input().split()

    # Добавить
    if (command[0] == 'add'):
        add(command, numbers_names, max_n)
    
    # Найти
    if (command[0] == 'find'):
        print(find(numbers_names, command))

    # Удалить
    if (command[0] == 'del'):
        delete(numbers_names, command)
