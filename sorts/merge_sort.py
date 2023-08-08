
def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        merge_sort(left)
        merge_sort(right)

        a, b, c = (0, 0, 0)
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                list[c] = left[a]
                a += 1
            else:
                list[c] = right[b]
                b += 1
            c += 1
        while a < len(left):
            list[c] = left[a]
            a += 1
            c += 1
        while b < len(right):
            list[c] = right[b]
            b += 1
            c += 1
        return list

if __name__ == '__main__':
    list = [44, 16, 83, 7, 67, 21, 34, 45, 10]
    merge_sort(list)
    print(list)
