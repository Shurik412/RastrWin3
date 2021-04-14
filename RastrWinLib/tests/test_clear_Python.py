# -*- coding: utf-8 -*-

from contextlib import contextmanager


@contextmanager
def managed_file(name):
    global f
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()


with managed_file('hello.txt') as f:
    f.write('Привет 1\n')
    f.write('Привет 2')


class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print(' ' * self.level + text)


with Indenter() as indent:
    indent.print('привет!')
    with indent:
        indent.print('здорово')
        with indent:
            indent.print('бонжур')
            indent.print('эй')
