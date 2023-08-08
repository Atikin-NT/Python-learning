
def bubble_sort(list):
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

if __name__ == '__main__':
    list = [44, 16, 83, 7, 67, 21, 34, 45, 10]
    bubble_sort(list)
    print(list)
