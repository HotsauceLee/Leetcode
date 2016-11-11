def insertion(input):
    for i in range(1, len(input)):
        while i > 0 and input[i] < input[i - 1]:
            input[i], input[i - 1] = input[i - 1], input[i]
            i -= 1

test_case1 = [5,4,3,2,1]
insertion(test_case1)
print test_case1

test_case2 = []
insertion(test_case2)
print test_case2

test_case3 = [1]
insertion(test_case3)
print test_case3

test_case4 = [2,1]
insertion(test_case4)
print test_case4

test_case5 = [2,1,4,3,5]
insertion(test_case5)
print test_case5

