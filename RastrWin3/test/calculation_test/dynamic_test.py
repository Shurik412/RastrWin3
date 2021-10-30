from RastrWin3.Load import load_file
from RastrWin3.AstraRastr import RASTR
from RastrWin3.calculation.dynamic import Dynamic

load_file(rastr_win=RASTR,
          path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.scn',
          shabl='сценарий',
          switch_command_line=True)

load_file(rastr_win=RASTR,
          path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst',
          shabl='динамика',
          switch_command_line=True)

calc = Dynamic(rastr_win=RASTR,
               calc_time=11.5,
               snap_max_count=1,
               switch_command_line=True)

calc.change_calc_time()
calc.change_snap_max_count()
calc.run()
