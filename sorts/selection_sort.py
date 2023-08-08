
def selection_sort(list):
    for i in range(len(list) - 1, 0, -1):
        max_index = 0
        for j in range(0, i + 1):
            if list[j] > list[max_index]:
                max_index = j
        list[i], list[max_index] = list[max_index], list[i]
    return list

if __name__ == '__main__':
    list = [44, 16, 83, 7, 67, 21, 34, 45, 10]
    selection_sort(list)
    print(list)

