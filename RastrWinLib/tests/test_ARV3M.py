from RastrWinLib.CustomModels.ARV3M.ARV3M import change_parameters, getting
from RastrWinLib.loading.load import load_file
from RastrWinLib.loading.save import save_file
from RastrWinLib.loading.shablon import shablon_file_dynamic

file = r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst'
file_save = r'C:\Users\Ohrimenko_AG\Desktop\test9.rst'

load_file(file_path=file,
          shablon=shablon_file_dynamic)

getting(Id=1320)

save_file(file_path=file_save,
          shablon=shablon_file_dynamic)
