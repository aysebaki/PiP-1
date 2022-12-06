def read_numbers(path: str) -> list:
    result = []
    with open(path) as f:
        for line in f:
            for token in line.split():
                try:
                    result.append(int(token))
                except ValueError:
                    try:
                        result.append(float(token))
                    except ValueError:
                        pass
    return result

read_numbers("ex1_data.txt")

print(read_numbers("ex1_data.txt"))
