""""

def insertionSort(n):
    for i in range(1, len(n)):
        key = n[i]
        j = i - 1
        while j >= 0 and key < n[j]:
            n[j + 1] = n[j]
            j -= 1
        n[j + 1] = key


# testa koden
n = [2, 3, 12, 17, 20]
insertionSort(n)
for i in range(len(n)):
    print("% a" % n[i])
"""


def bubbleSort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# testa koden
arr = [88, 69, 50, 90, 20, 14, 2]
bubbleSort(arr)
print("Sorterad array är: ")
for i in range(len(arr)):
    print("% d" % arr[i])
