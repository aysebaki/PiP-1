def clip(*values, min_=0, max_=1) -> list:
    arr = list()
    for x in values:
        if x < min_:
            arr.append(min_)
        elif x > max_:
            arr.append(max_)
        else:
            arr.append(x)
    return arr

print(clip())
print(clip(1, 2, 0.1, 0))
print(clip(-1, 0.5))
print(clip(-1, 0.5, min_=2))
print(clip(-1, 0.5, max_=0.3))
print(clip(-1, 0.5, min_=2, max_=3))