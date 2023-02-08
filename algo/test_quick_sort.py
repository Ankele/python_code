
# -*- coding:utf-8 -*-


def quick_sort(li):
    n = len(li)
    if n < 2:
        return
    _quick_sort(li, 0, n-1)


def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and tmp <= li[right]:
            right -= 1
        li[left] = li[right]
        while left < right and tmp > li[left]:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left


def _quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        _quick_sort(li, left, mid-1)
        _quick_sort(li, mid+1, right)


def main():
    # li = [5, 3, 2, 7, 9, 1, 8, 4, 6]
    # quick_sort(li)
    # print li
    import random
    li = list(range(100))
    random.shuffle(li)
    print li
    quick_sort(li)
    print li


if __name__ == '__main__':
    main()

