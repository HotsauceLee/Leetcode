# O(n^2)
def bubble(input):
    idx = len(input) - 1
    while idx > 0:
        for i in range(idx):
            if input[i] > input[i + 1]:
                input[i], input[i + 1] = input[i + 1], input[i]

        idx -= 1

test_case1 = [5,4,3,2,1]
bubble(test_case1)
print test_case1

test_case2 = []
bubble(test_case2)
print test_case2

test_case3 = [1]
bubble(test_case3)
print test_case3

test_case4 = [2,1]
bubble(test_case4)
print test_case4

test_case5 = [2,1,4,3,5]
bubble(test_case5)
print test_case5

