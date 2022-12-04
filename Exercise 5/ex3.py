def binary_search(elements: list, x) -> bool:
    try:
        if len(elements) == 0:
            return False
        middle = len(elements) // 2
        if elements[middle] == x:
            return True
        elif elements[middle] < x:
            return binary_search(elements[middle + 1:], x)
        else:
            return binary_search(elements[:middle], x)
    except TypeError:
        return False

my_sorted_list = [1, 2, 5, 7, 8, 10, 20, 30, 41, 100]
print(binary_search(my_sorted_list, 1))
print(binary_search(my_sorted_list, 20))
print(binary_search(my_sorted_list, 21))
print(binary_search(my_sorted_list, "hello"))