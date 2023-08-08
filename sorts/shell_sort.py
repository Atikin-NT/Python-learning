
def shell_sort(list):
    distance = len(list) // 2
    while distance > 0:
        for i in range(distance, len(list)):
            tmp = list[i]
            j = i
            while j >= distance and list[j - distance] > tmp:
                list[j] = list[j - distance]
                j -= distance
            list[j] = tmp
        
        distance //= 2
    return list

if __name__ == '__main__':
    list = [44, 16, 83, 7, 67, 21, 34, 45, 10]
    shell_sort(list)
    print(list)

