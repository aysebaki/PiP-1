import os

def get_abs_paths(root_path: str, ext_filter: str = None) -> list:
    if not os.path.isdir(root_path):
        raise ValueError
    if ext_filter is not None and not ext_filter.startswith("."):
        raise ValueError
    result = []
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if ext_filter is None or file.endswith(ext_filter):
                result.append(os.path.join(root, file))
    return sorted(result)