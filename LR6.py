def sift_down(arr, n, i, swaps):
     smallest = i
     left = 2 * i + 1
     right = 2 * i + 2
     if left < n and arr[left] < arr[smallest]:
         smallest = left
     if right < n and arr[right] < arr[smallest]:
         smallest = right
     if smallest != i:
         arr[i], arr[smallest] = arr[smallest], arr[i]
         swaps.append((i, smallest))
         sift_down(arr, n, smallest, swaps)
def build_min_heap(arr):
     n = len(arr)
     swaps = []
     for i in range(n // 2 - 1, -1, -1):
         sift_down(arr, n, i, swaps)
     return swaps

while True:
     try:
         arr = list(map(int, input("Введите массив чисел: ").strip().split()))
         swaps = build_min_heap(arr)
         print(len(swaps))
         for i, j in swaps:
             print(i, j)
     except ValueError:
         print("Ошибка ввода. Попробуйте снова.")