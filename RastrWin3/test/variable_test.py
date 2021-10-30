from RastrWin3.AstraRastr import RASTR
from RastrWin3.Load import load_file
import pythoncom
from RastrWin3.Tools.error_handler import error_load_file
from RastrWin3.ActionsObject.variable import Variable
import pywintypes
from RastrWin3.Templates import directory_shabl

#
# def decor_error(func):
#     def wrapper(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#         except pythoncom.com_error as error:
#             hr, msg, exc, arg = error.args
#             print(hr)  # -2147352567
#             print(msg)  # Ошибка.
#             print(exc)  # (0, 'Astra.Rastr.1', 'Ошибка открытия файла asd2 ', None, 0, -2147467259)
#             print(arg)  # None
#     return wrapper


#
# load_file(rastr_win=RASTR,
#           path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.scn',
#           shabl='сценарий',
#           switch_command_line=False)
#
# load_file(rastr_win=RASTR,
#           path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst',
#           shabl='динамика',
#           switch_command_line=False)

# find = FindNextSelection(rastr_win=RASTR,
#                          table="com_dynamics")
#
# tras = RASTR.Tables("com_dynamics").Cols("Tras").Z(0)
# print(f'tras={tras}')
# var = Variable(rastr_win=RASTR, switch_command_line=False)

@error_load_file
def load(path):
    RASTR.Load(1, path, directory_shabl(rus_name_shabl='автоматика'))


load(path='')

# @decor_error
# def variable_str():
#     var.make_changes_row(table='com_dynamic', column='Tras', row=0, value=1.25)
#
# load_ = LoadRastr(rastr=RASTR)
#
# @decor_error
# def lod():
#     load_.load(path='asd')
# #
# lod()
# v = variable_str()
# print(v)

# try:
#     var = Variable(rastr_win=RASTR, switch_command_line=False)
#     var.make_changes_row(table='com_dynamic', column='Tras', row=0, value=1.25)
# except pythoncom.com_error as error:
#     print(error)
#     # print(type(vars(error)))
#     # print(vars(error)['hresult'])
#     # # print(vars(error)['strerror'])
#     # print(vars(error)['excepinfo'][0])
#     # print(vars(error)['excepinfo'][1])
#     print(vars(error)['excepinfo'][2].split(',')[1])
#     # print(vars(error)['excepinfo'][3])
#     # print(vars(error)['excepinfo'][4])
#     # print(vars(error)['argerror'])
#     # print(type(error.args))
#     # 'hr, msg, exc, arg = error.args
#
# tras = RASTR.Tables("com_dynamics").Cols("Tras").Z(0)
# print(f'tras={tras}')
