
def insert_sort(list):
    for i in range(1, len(list)):
        j = i-1
        element_next = list[i]
        while (list[j] > element_next) and (j >= 0):
            list[j+1] = list[j]
            j -= 1
        list[j+1] = element_next
    return list

if __name__ == '__main__':
    list = [44, 16, 83, 7, 67, 21, 34, 45, 10]
    insert_sort(list)
    print(list)

