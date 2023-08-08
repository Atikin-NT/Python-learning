
def binary_search(list, item):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == item:
            return True
        else:
            if item < list[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return False

if __name__ == '__main__':
    list = [11, 12, 22, 33, 55, 90, 99]
    print(binary_search(list, 12))
    print(binary_search(list, 91))