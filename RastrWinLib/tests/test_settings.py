# -*- coding: utf-8 -*-

from RastrWinLib.loading.load import load_file
from RastrWinLib.loading.shablon import shablon_file_dynamic, test_9_rst, shablon_file_ut_common
from RastrWinLib.settings.regim import set_regim
from RastrWinLib.settings.ut_common import set_ut_common
from RastrWinLib.settings.equivalence import set_com_ekviv
from RastrWinLib.settings.dynamic import set_dynamic
from RastrWinLib.loading.save import save_file

load_file(file_path=test_9_rst,
          shablon=shablon_file_dynamic)
load_file(shablon=shablon_file_ut_common)

# set_regim(switch_command_line=True)
# set_ut_common(switch_command_line=True)
# set_com_ekviv(switch_command_line=True)

set_dynamic(
        t_ras=5.0,
        h_int=0.01,
        h_min=0.01,
        h_max=0.01,
        h_out=0.01,
        mint='HH5',
        smint='КМ4',
        int_epsilon=0.0001,
        inform_on_step_change=0,
        tf=0.02,
        dEf=0.001,
        npf=10,
        valid='По умолчанию',
        dempfrec='S',
        corrT=0,
        is_demp='Да',
        frSXNtoY=0.3,
        SXNTolerance=0,
        SnapPath='c:\\tmp\\',
        MaxResultFiles=0,
        SnapTemplate='<count>.sna',
        SnapAutoLoad=1,
        SnapMaxCount=6,
        TripGeneratorOnSpeed=0,
        PickupDropout=0,
        RealtimeCSV=0,
        PeriodAngle=0,
        ResultFlowDirection=0,
        TreatWarningsAsErrors=0,
        EventProcess=0,
        switch_command_line=True)

save_file(file_path=r'C:\Users\Ohrimenko_AG\Desktop\Test_equiPy\test9_123.rst',
          shablon=shablon_file_dynamic)
