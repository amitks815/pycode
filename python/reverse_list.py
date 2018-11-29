def reverseGroup(input, k):
    # set starting index at 0
    start = 0
    result = []
    while (start < len(input)):

        if len(input[start:]) < k:
            result = result + list(reversed(input[start:]))
            break

        # select current group of size of k
        # reverse it and concatenate
        result = result + list(reversed(input[start:start + k]))
        start = start + k
    print(result)


# Driver program
if __name__ == "__main__":
    input = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 5
    reverseGroup(input, k)


# l=[1,2,3,4,5,6,7,]
#
# a=[x for x in reversed(l)]
# print(a)
