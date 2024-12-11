class TreeNode:
     def __init__(self, key):
         self.key = key
         self.left = None
         self.right = None

    def build_tree(n, data):
         nodes = []
         for i in range(n):
             key, left, right = data[i]
             node = TreeNode(key)
             nodes.append(node)
             if left != -1:
                 node.left = None # Изначально устанавливаем в None
             if right != -1:
                 node.right = None # Изначально устанавливаем в None

         # Теперь создание связи между узлами
         for i in range(n):
             if data[i][1] != -1: # Если есть левый сын
                nodes[i].left = nodes[data[i][1]]
             if data[i][2] != -1: # Если есть правый сын
                 nodes[i].right = nodes[data[i][2]]
            return nodes[0] if n > 0 else None

    def in_order(node, result):
         if node:
             in_order(node.left, result)
             result.append(node.key)
             in_order(node.right, result)
    def pre_order(node, result):
         if node:
             result.append(node.key)
             pre_order(node.left, result)
             pre_order(node.right, result)
    def post_order(node, result):
         if node:
             post_order(node.left, result)
             post_order(node.right, result)
             result.append(node.key)

# Ввод данных
n = int(input("Введите количество вершин: "))
data = []
for i in range(n):
     entry = list(map(int, input().strip().split()))
     data.append(entry)
# Построение дерева
root = build_tree(n, data)
# Результаты обходов
in_order_result = []
pre_order_result = []
post_order_result = []
# Выполнение обходов
in_order(root, in_order_result)
pre_order(root, pre_order_result)
post_order(root, post_order_result)
# Вывод результатов
print("In-order:", ' '.join(map(str, in_order_result)))
print("Pre-order:", ' '.join(map(str, pre_order_result)))
print("Post-order:", ' '.join(map(str, post_order_result)))