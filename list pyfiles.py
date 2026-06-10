import os
def list_python_files(folder):
    py_files = []
    for file in os.listdir(folder):
        if file.endswith(".py"):
            py_files.append(file)
    return py_fil