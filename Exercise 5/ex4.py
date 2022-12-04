def flatten (nested: list) -> list:
    result = []
    for element in nested:
        if isinstance(element, list):
            result.extend(flatten(element))
        else:
            result.append(element)
    return result

print(flatten([1, 2,[4,[8, 9,[11, 12], 10], 5],3,[6,7]]))
print(flatten([[]]))
print(flatten([[], [], [1], [], [1, [], [4,5, [[[6]]], 2, 3]]]))