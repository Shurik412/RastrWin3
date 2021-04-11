from RastrWin.settings.regim import SetRegim
from RastrWin.settings.dynamic import SetDynamic
from RastrWin.settings.alt_unit import AltUnit
from RastrWin.settings.equivalence import SetEkviv
from RastrWin.settings.ut_common import UtCommon
from RastrWin.AstraRastr import RASTR
from RastrWin.loading.load import LoadRUSTab
from RastrWin.loading.shablon import shablon_dynamic, shablon_scenario
from RastrWin.loading.save import save_file

load_f = LoadRUSTab(rastr_win=RASTR, shablon=shablon_dynamic, switch_command_line=True)
load_f.load(file_path='')

SetEkviv(rastr_win=RASTR).set(selekv=0,
                              met_ekv=0,
                              tip_ekv=0,
                              ekvgen=0,
                              tip_gen=1,
                              kfc_x='',
                              pot_gen=0,
                              kpn='',
                              tip_sxn=0,
                              smart=0,
                              zmax=1000,
                              otm_n=0)

SetRegim(rastr_win=RASTR).set(neb_p=1.0,
                              it_max=500,
                              start=0,
                              flot=1,
                              dv_min=0.5,
                              dv_max=2.0,
                              dd_max=5157,
                              status=0,
                              rr=0,
                              wt='',
                              gen_p=0,
                              method=0,
                              method_ogr=0,
                              print_mode=0,
                              qmax=0,
                              min_x='',
                              calc_tr=0,
                              nag_p=0,
                              rem_breaker=0,
                              gram=0,
                              ctrl_baza=0,
                              itz='',
                              itz_ogr_max='',
                              itz_ogr_min='',
                              min_nodes_in_island='')

SetDynamic(rastr_win=RASTR).set(t_ras=5.0,
                                h_int=0.01,
                                h_min=0.01,
                                h_max=0.01,
                                h_out=0.01,
                                mint=0,
                                smint=0)

SetEkviv(rastr_win=RASTR).set(selekv=0,
                              met_ekv=0,
                              tip_sxn=0,
                              ekvgen=0,
                              tip_gen=1,
                              smart=0,
                              zmax=1000,
                              otm_n=0,
                              kfc_x='')

UtCommon(rastr_win=RASTR).set(maxs=5,
                              maxv=2,
                              maxd=2,
                              maxa=10,
                              iter=100,
                              tip=0,
                              f_ots=0,
                              add_d=0,
                              ekstr=0,
                              kfc=1.0)

save_file(rastr_win=RASTR, file_path='')
