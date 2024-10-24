# Функция для поиска максимума в окне
def maxInWinN2(arr, n, m):
    maxArr = []
    queue = []

    for i in range(n):
        if queue and queue[0] < i - m + 1:
            queue.pop(0)

        while queue and arr[queue[-1]] < arr[i]:
            queue.pop()

        queue.append(i)

        if i >= m - 1:
            maxArr.append(arr[queue[0]])

    return maxArr
    
while True:
    # Ввод данных
    n = int(input("Размер массива: "))
    line = input()
    arr = line.split()
    m = int(input("Размер окна: "))

    # Проверки на верность ввода
    if (n < 1 or n > 10^5 or m < 1 or m > n or len(arr) != n):
        print("Ошибка ввода")
    else:
        print(maxInWinN2 (arr, n, m))
        print("\n")