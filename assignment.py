def read_file(file_path: str) -> str:
    f = open(file_path, "r")
    res = ""
    for i in f:
        res += str(i)
    f.close()
    return res
    raise NotImplementedError()


def write_file(file_path: str, content: str) -> None:
    f = open(file_path, "a")
    f.write(str(content))
    f.close()
    return None
    raise NotImplementedError()

def list_files_in_directory(directory_path: str) -> list:
    import os
    res = os.listdir(directory_path)
    return res
    raise NotImplementedError()


def generate_numbers(n: int) -> iter:
    temp = []
    for i in range(0, n):
        temp.append(i)
    return iter(temp)
    raise NotImplementedError()


def use_function_from_module(module_name: str, function_name: str, *args) -> any:
    import importlib
    module = importlib.import_module(module_name)
    func = getattr(module, function_name)
    return func(*args)
    raise NotImplementedError()
