# # -*- coding: utf-8 -*-
#
# from contextlib import contextmanager
#
#
# # @contextmanager
# # def managed_file(name, text):
# #     global f
# #     try:
# #         f = open(name, 'w')
# #         yield f.write(f'{text}\n')
# #     finally:
# #         f.close()
#
# @contextmanager
# def text_msg(name, text):
#     def managed_file(name):
#         global f
#         try:
#             f = open(name, 'w')
#             yield f
#         finally:
#             f.close()
#
#     with managed_file(name) as f:
#         f.write(f'{text}\n')
#
#
# # with managed_file('hello.txt', 'sdfsdfsdfsdf') as f:
#
# # managed_file('hello.txt', '11111111')
#
# text_msg('g.txt', 'sadasdasda111')
# text_msg('g.txt', '22222')
#
#
# class Indenter:
#     def __init__(self):
#         self.level = 0
#
#     def __enter__(self):
#         self.level += 1
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.level -= 1
#
#     def print(self, text):
#         print(' ' * self.level + text)
#
# # with Indenter() as indent:
# #     indent.print('привет!')
# #     with indent:
# #         indent.print('здорово')
# #         with indent:
# #             indent.print('бонжур')
# #             indent.print('эй')


def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper


@uppercase
def greet():
    return 'Привет!'


print(greet())

