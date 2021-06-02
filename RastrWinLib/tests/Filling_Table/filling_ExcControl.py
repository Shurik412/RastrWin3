# -*- coding: utf-8 -*-
from time import time, localtime, strftime
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.loading.load import load_file
from RastrWinLib.loading.save import save_file
from RastrWinLib.loading.shablon import Shabl
from RastrWinLib.FillingTable.ARV_Filling import filling_ExcControl
from RastrWinLib.tables.Dynamic.ExcControl import ExcControl

file_rst_dir = r'C:\Users\Ohrimenko_AG\Desktop\test_filling'
file_name = r'\test.rst'

load_file(rastr_win=RASTR,
          file_path=file_rst_dir + file_name,
          shabl=Shabl.shablon_file_dynamic)

load_file(rastr_win=RASTR,
          shabl=Shabl.shablon_file_automation)

table_ = RASTR.Tables(ExcControl.table)

start_time = time()

for i in range(0, 1000):
    table_.AddRow()
    filling_ExcControl(rastr_win=RASTR,
                       row_id=i,
                       sel=None,
                       sta=None,
                       Id=123456789,
                       Name=f'Генератор {i}',
                       ModelType=None,
                       Brand=None,
                       ForcerId=123456789,
                       CustomModel=None,
                       OELId=123465789,
                       PSSId=123456789,
                       UELId=123456789,
                       Trv=0.123456,
                       Tf=0.123456,
                       T1f=0.123456,
                       T2f=0.123456,
                       T1f1=0.123456,
                       T2f1=0.123456,
                       T3f1=0.123456,
                       T1if=0.123456,
                       T1if1=0.123456,
                       T2if1=0.123456,
                       T1u=0.123456,
                       T1u1=0.123456,
                       T2u1=0.123456,
                       Tbch=0.123456,
                       TINT=0.123456,
                       Ku=0.123456,
                       Ku1=0.123456,
                       Kf=0.123456,
                       Kf1=0.123456,
                       Kif1=0.123456,
                       K_cosfi=0.123456,
                       K_Ia=0.123456,
                       K_Ir=0.123456,
                       K_P=0.123456,
                       K_Q=0.123456,
                       K_Usd=0.123456,
                       Kiu=0.123456,
                       Kpi=0.123456,
                       KST=0.123456,
                       Kuf=0.123456,
                       Urv_max=0.123456,
                       Urv_min=0.123456,
                       dEqdt=0.123456,
                       dVdt=0.123456,
                       Uarv=0.123456,
                       Udop1=0.123456,
                       U11=0.123456,
                       U22=0.123456,
                       Alpha=0.123456,
                       dSudt=0.123456,
                       deltaF=0.123456,
                       switch_command_line=False)

time_calc = time() - start_time
print(f'Seconds: {"%.2f" % time_calc} [секунд]')

save_file(rastr_win=RASTR,
          file_path=file_rst_dir + '\\test2.rst',
          shabl=Shabl.shablon_file_dynamic)
