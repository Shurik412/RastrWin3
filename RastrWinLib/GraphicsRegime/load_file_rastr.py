# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.loading.load import load_file
from RastrWinLib.loading.shablon import Shabl


def load_file_rgm():
    load_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Desktop\БРМ 2021 версия 4\БРМ лето 2020 МАКСИМУМ_4.rg2',
              shabl=Shabl.shablon_file_regime)

    load_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Desktop\БРМ 2021 версия 4\Сечения Центр_4.sch',
              shabl=Shabl.shablon_file_sch)
