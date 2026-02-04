def binary_search(list, item):
    first = 0
    last = len(list) - 1
    found = False
    while (first <= last and not found):
        mid = (first + last) // 2
        if list[mid] == item:
            found = True
        else:
            if item < list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

numList = [4, 12, 7, 45, 52, 64, 71, 84, 27, 72]
print('List has the items: ', numList)
searchNum = int(input("Enter a number to search for: "))
found = binary_search(numList, searchNum)
if found == True:
    print(searchNum, "is present in the list")
else:
    print(searchNum, "is not present in the list")