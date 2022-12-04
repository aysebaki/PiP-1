def gen_range (start: int, stop:int, step:int =1) -> int:
    if (
        not isinstance(start, int)
        or not isinstance(stop, int)
        or not isinstance(step, int)
     ):
        raise TypeError
    if step == 0:
        raise ValueError
    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step

print(list(gen_range(0, 10)))
print(list(gen_range(0, 10, 3)))
print(list(gen_range(0, 10, -1)))
print(list(gen_range(10, 0)))
print(list(gen_range(10, 0, -2)))
print(list(gen_range(-10, -3, 2)))
print(list(gen_range(0.0, 10)))
print(list(gen_range(0, 10, 0)))


