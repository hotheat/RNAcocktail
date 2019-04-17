import time
import argparse
import os


def log(*args, **kwargs):
    format = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    print(dt, *args, **kwargs)


def mkdir(path):
    path = path.strip().rstrip("\\")
    file_exist = os.path.exists(path)
    if not file_exist:
        os.makedirs(path)
        return True
    else:
        return False


def load_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        read_file = f.read()
    return read_file


def get_arg():
    parse = argparse.ArgumentParser(
        description='Choose the running step of each section', )
    parse.add_argument("-s", dest="start", help="which step to run in each section", default=0, type=int)
    arg = parse.parse_args().__dict__
    return arg


class RaiseException(Exception):
    pass
