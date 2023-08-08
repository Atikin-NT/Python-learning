
def linear_search(list, item):
    index = 0
    while index < len(list):
        if list[index] == item:
            return True
        index += 1
    return False

if __name__ == '__main__':
    list = [12, 33, 11, 99, 22, 55, 90]
    print(linear_search(list, 12))
    print(linear_search(list, 91))