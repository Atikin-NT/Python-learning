
def int_pol_search(list, item):
    idx0 = 0
    idxn = len(list) - 1
    while idx0 <= idxn and item >= list[idx0] and item <= list[idxn]:
        mid = idx0 + int(((float(idxn - idx0)/(list[idxn]-list[idx0]))*(item-list[idx0])))
        print(mid)
        if list[mid] == item:
            return True
        if list[mid] < item:
            idx0 = mid + 1
    return False

if __name__ == '__main__':
    list = [11, 12, 22, 33, 55, 90, 99]
    print(int_pol_search(list, 12))
    print(int_pol_search(list, 91))