from RastrWinLib.loading.load import load_file
from RastrWinLib.loading.shablon import shablon_file_dynamic, test_9_rst, shablon_file_ut_common
from RastrWinLib.settings.regim import set_regim
from RastrWinLib.settings.ut_common import set_ut_common
from RastrWinLib.settings.equivalence import set_com_ekviv

load_file(file_path=test_9_rst,
          shablon=shablon_file_dynamic)
load_file(shablon=shablon_file_ut_common)

set_regim(switch_command_line=True)
set_ut_common(switch_command_line=True)
set_com_ekviv(switch_command_line=True)