'''

选择排序：在未排序中找最小的，放到前面，以此类推

'''


def selectionSort(arr: list[int]) -> list[int]:
    for i in range(len(arr)-1):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if minIndex != i:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


if __name__ == '__main__':
    print(selectionSort([3,2,4,5,6]))

