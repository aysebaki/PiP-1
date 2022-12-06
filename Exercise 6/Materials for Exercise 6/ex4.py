import os

def chunks(path: str, size: int, **kwargs) -> str:
    if not os.path.isfile(path):
        raise ValueError
    if size < 1:
        raise ValueError
    with open (path, **kwargs) as f:
        while True:
            chunk = f.read(size)
            if not chunk:
                break
            yield chunk

for i, c in enumerate(chunks("ex1_data.txt", 25, mode="rb")):
    print(f"Chunk {i} = {c}")