def parent(num):
    # print("Printing from the parent() function.")

    def first_child():
        return "Printing from the first_child() function."

    def second_child():
        return "Printing from the second_child() function."

    # print(first_child())
    # print(second_child())

    try:
        assert num==10

        print('---------')
        return first_child

    except AssertionError:
        print('---------')
        return second_child

foo=parent(10)

bar=parent(11)


print(foo())

print(bar())


