def merge_sort(input):
    if not input:
        return 
    if len(input) <= 1:
        return input

    mid = len(input)//2
    l = merge_sort(input[:mid])
    r = merge_sort(input[mid:])
    
    return merge(l, r)


def merge(list1, list2):
    if not list1 and not list2:
        return None
    if not list1:
        return list2
    if not list2:
        return list1

    result = []
    idx1 = 0
    idx2 = 0
    while idx1 < len(list1) and idx2 < len(list2):
        if list1[idx1] < list2[idx2]:
            result.append(list1[idx1])
            idx1 += 1
        else:
            result.append(list2[idx2])
            idx2 += 1

    if idx1 >= len(list1):
        result += list2[idx2:]
    if idx2 >= len(list2):
        result += list1[idx1:]

    return result

list1 = [1,3,5,7,9]
list2 = [2,4,6,8,10]
list3 = [2,4,11,12,13]

print merge(list1, list2)
print merge(list1, list3)

input1 = [5,4,3,2,1]
input2 = [1,3,2,4,15,9,7,6]

print merge_sort(input1)
print merge_sort(input2)
