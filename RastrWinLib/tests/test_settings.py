from RastrWinLib.loading.load import load_file
from RastrWinLib.loading.shablon import shablon_file_dynamic, test_9_rst
from RastrWinLib.settings.regim import set_regim

load_file(file_path=test_9_rst,
          shablon=shablon_file_dynamic)

set_regim(switch_command_line=False)
