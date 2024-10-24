def sorting(mass, n):  # сортировка вставками массива по времени обработки
    for i in range(1, n):
        j = i - 1
        key = mass[i]
        # Сортируем по времени обработки (второй элемент каждой пары)
        while j >= 0 and mass[j][1] > key[1]:
            mass[j + 1] = mass[j]
            j -= 1
        mass[j + 1] = key
    return mass

def processing(array, size, n, max_time):
    if n == 0:
        return []

    array = sorting(array, n)  # Сортируем по времени обработки
    packet = []  # Массив для результатов (время поступления или -1)

    current_time = 0  # Текущее время в системе
    buffer = []  # Буфер 

    for i in range(n):
        # Проверка на максимальное время в системе
        if array[i][1] > max_time:
            packet.append(-1)  # Пакет отбрасывается, если время ожидания слишком велико
            continue

        if (len(buffer) != 0):
            for j in range(len(buffer)):
                if (buffer[j][0] + buffer[j][1] <= current_time):
                    buffer.pop(j)
                
        # Обработка пакета
        if current_time <= array[i][0] and len(buffer) < size:  # Если текущее время меньше или равно времени прихода пакета            
            packet.append(array[i][0])  # Сохраняем время прихода
            buffer.append(array[i])
            current_time = array[i][0] + array[i][1]  # Обновляем текущее время
        else:
            # Если пакет не может быть обработан, добавляем -1
            packet.append(-1)
            buffer.append(array[i])  # Сохраняем пакет в буфере
    
    return packet
    
# Ввод
size = int(input("Размер буфера: "))
n = int(input("Число пакетов: ")) 
max_time = int(input("Максимальное время в буфере: "))

# Времени поступления и продолжительности
array = [[0] * 2 for _ in range(n)]
for i in range(n):
    line = input(f"arrival и duration для {i +  1} пакета: ")  
    array[i] = list(map(int, line.split()))

result = processing(array, size, n, max_time)

# Вывод массива на экран
print("Итог: ")
print(result)