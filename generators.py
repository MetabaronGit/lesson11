import os


def find_names(target_string, dir_path):
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            if target_string in filename:
                yield os.path.join(dirpath, filename)


def open_files(names):
    for name in names:
        yield open(name)


def read_file(files):
    for file in files:
        for line in file:
            yield line


def extract_lines(target, lines):
    for line in lines:
        if target in line:
            yield line


# lines = extract_lines('python', read_file(open_files(find_names('.txt', '/home/user/PythonBeginner'))))
# print(next(lines))
# print(next(lines))
# print(next(lines))

a = find_names('.txt', os.getcwd())
print(next(a))
