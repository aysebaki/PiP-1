def sort(elements: list, ascending: bool = True) -> list:
    for x in range(len(elements)):
        for y in range(len(elements) - 1):
            if ascending:
                if elements[y] > elements[y + 1]:
                   elements[y], elements[y + 1] = elements[j + 1], elements[y]
            else:
                if elements[y] < elements[y + 1]:
                   elements[y], elements[y + 1] = elements[y +1],elements[j]

