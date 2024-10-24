def treeHeight(parents):
    #массив, который хранит глубину каждой вершины дерева
    depth = [-1] * len(parents) + [0] # 0 - для учета корневой вершины

    def cntDepth(i): # рекурсивный расчет глубины вершины с индексом i
        if (depth[i] == -1):
            depth[i] = cntDepth(parents[i]) + 1
        return depth[i]

    return max(cntDepth(i) for i in range(len(parents))) #максимальное значение из вычисленных глубин.

# Входные данные
n = int(input("N = ")) # кол-во чисел
parents = list() # ввод родителей вершины
for i in range(n):
    parent = int(input())
    parents.append(parent)

#Выходные данные
print("Высота дерева: ")
print(treeHeight(parents))  