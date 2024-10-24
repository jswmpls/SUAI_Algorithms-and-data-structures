class workWithStack:
    def __init__(self, max_size): # инициализируем экземпляр класса.
        self.stack = [] #основной стек
        self.max_stack = [] #макс значение
        self.min_stack = [] #мин значение
        self.sum_stack = [] #сумма
        self.max_size = max_size #макс размер

    def push(self, number):
        # Если текущий размер стека равен максимальному, выводится сообщение и выполнение прекращается
        if len(self.stack) >= self.max_size:
            print("Достигнуто максимальное значение стека")
            return
        
        self.stack.append(number)
        
        # Обновление max_stack
        # Если max_stack не пуст, добавляется максимальное значение между number и верхним элементом max_stack
        if self.max_stack:
            self.max_stack.append(max(number, self.max_stack[-1]))
        else:
            self.max_stack.append(number)
        
        # Обновление min_stack
        # Если min_stack не пуст, добавляется минимальное значение между number и верхним элементом min_stack
        if self.min_stack:
            self.min_stack.append(min(number, self.min_stack[-1]))
        else:
            self.min_stack.append(number)
        
        # Обновление sum_stack (храним текущую сумму)   
        current_sum = self.sum_stack[-1] + number if self.sum_stack else number
        self.sum_stack.append(current_sum)

    def pop(self):
        if not self.stack:
            return

        self.stack.pop()
        self.max_stack.pop()
        self.min_stack.pop()
        self.sum_stack.pop()

    def max(self):
        if not self.stack:
            return
        print(self.max_stack[-1])

    def min(self):
        if not self.stack:
            return
        print(self.min_stack[-1])

    def avg(self):
        if not self.stack:
            return
        print(self.sum_stack[-1] / len(self.stack))



stack = workWithStack(int(input("Максимальный размер стека: ")))
q = int(input("Число запросов: "))

for i in range(q):
    command = input().split()
    if command[0] == 'push':
        stack.push(int(command[1]))
    elif command[0] == 'pop':
        stack.pop()
    elif command[0] == 'max':
        stack.max()
    elif command[0] == 'min':
        stack.min()
    elif command[0] == 'avg':
        stack.avg()