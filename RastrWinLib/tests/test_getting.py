from RastrWinLib.getting.get import GettingParameter
from RastrWinLib.getting.get import get_param
from RastrWinLib.loading.load import load_file
from RastrWinLib.loading.shablon import shablon_file_dynamic
import RastrWinLib.tables.Dynamic.ExcControl as ExcControl
from RastrWinLib.AstraRastr import RASTR

file = r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst'
load_file(file_path=file,
          shablon=shablon_file_dynamic)

