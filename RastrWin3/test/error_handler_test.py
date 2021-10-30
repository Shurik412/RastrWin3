from RastrWin3.Tools.error_handler import decor_error
from RastrWin3.AstraRastr import RASTR
from RastrWin3.Templates import directory_shabl
import pythoncom


@decor_error
def load(path):
    RASTR.Load(1, path, directory_shabl(rus_name_shabl='автоматика'))


load('3')
