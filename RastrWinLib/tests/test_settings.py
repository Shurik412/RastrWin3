from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.loading.load import LoadRUSTab
from RastrWinLib.loading.save import save_file
from RastrWinLib.loading.shablon import shablon_dynamic
from RastrWinLib.settings.dynamic import SetDynamic
from RastrWinLib.settings.equivalence import SetEkviv
from RastrWinLib.settings.regim import SetRegim
from RastrWinLib.settings.ut_common import UtCommon

load_f = LoadRUSTab(rastr_win=RASTR, shablon=shablon_dynamic, switch_command_line=True)
load_f.load(file_path='')


save_file(rastr_win=RASTR, file_path='')
