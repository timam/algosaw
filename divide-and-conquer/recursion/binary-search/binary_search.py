def binary_search(alist, key):

    if len(alist) > 0:

        mid = len(alist) // 2

        if alist[mid] == key:
            return True

        if key < alist[mid]:
            return binary_search(alist[:mid], key)

        if key > alist[mid]:
            return binary_search(alist[mid+1:], key)

    else:
        return False


print(binary_search([10, 20, 30, 40], 20))

print(binary_search([10, 20, 30, 40, 50], 11))
