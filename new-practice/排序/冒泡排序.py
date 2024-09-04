'''

冒泡排序：两两比较，每轮都会比出当前最大的

'''
from typing import List


def bubbleSort(arr: List[int]) -> List[int]:
    for i in range(len(arr)-1):
        for j in range(1, len(arr)-i):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr


def main():
    # 让用户输入一组数字，并将其转换为整数列表
    arr = list(map(int, input("请输入一组数字，用空格分隔: ").split()))

    print("排序前的数组:", arr)

    sorted_arr = bubbleSort(arr)

    print("排序后的数组:", sorted_arr)


if __name__ == "__main__":
    main()

