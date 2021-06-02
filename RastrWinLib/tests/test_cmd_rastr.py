import win32com.client
from RastrWinLib.loading.load import load_file
from RastrWinLib.loading.shablon import Shabl

RASTR = win32com.client.Dispatch('Astra.Rastr')
RASTR_ = win32com.client.Dispatch('Rastr_')


def Rastr_OnLog(code, description):
    print(code[0])
    # print(f'[ERROR] {description}')
    # print(f'[ERROR] {description}')
    # print(f'[ERROR] {description}')
    # print(f'[WARNING] {description}')
    # print(f'[MESSAGE] {description}')
    # print(f'[INFO] {description}')


load_file(rastr_win=RASTR,
          shabl=Shabl.shablon_file_regime,
          file_path=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\cx195.rg2')

RASTR.Rgm('')

