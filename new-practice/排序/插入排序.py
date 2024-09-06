'''

插入排序：将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。

从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）

'''


def insertionSort1(arr: list[int]) -> list[int]:
    for j in range(1, len(arr)):
        temp = arr[j]
        for i in range(j - 1, -1, -1):
            if arr[i] > temp:
                arr[i+1] = arr[i]
                if i == 0:
                    arr[i] = temp
            elif arr[i] <= temp:
                arr[i+1] = temp
                break
    return arr


def insertionSort(arr: list[int]) -> list[int]:
    for j in range(1, len(arr)):
        temp = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > temp:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = temp
    return arr



if __name__ == '__main__':
    print(insertionSort([3,2,4,3,8,1,0,3,6,9,5,6]))