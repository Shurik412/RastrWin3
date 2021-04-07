# -*- coding: utf-8 -*-

from R_modules.Tables_Parametrs.Tables_and_parametrs import table_name_com_ekviv, table_com_ekviv, table_name_com_regim, \
    table_com_regim, table_com_dynamics, table_name_com_dynamics
from R_modules.variables.variable_parametrs import VariableDefRowId
from R_modules.object_rastr import RASTR


class SetEkviv(VariableDefRowId):
    """
    Класс выставляет параметров настройки "Эквивалент"
    selekv=0 => Отмеченные узлы:
    met_ekv=0 => Метод эквивалентирования
    tip_ekv=0 => Тип эквивалентирования
    ekvgen=0 => Эквивалент узлов с фикс V
    tip_gen=1 => Тип эквивалентирования генераторов
    kfc_x='' => Коэффициент для Xg_ген
    pot_gen=0 => Учет потерь при разносе генерации:
    kpn='' => Доля нагрузки, пересчитываемая в шунт
    tip_sxn=0 => Учитывать СХН при эквивалентировании
    smart=0 => "Умное" эквивалентирование :
    zmax=1000 => Удаление ветвей с сопротивлением большим:
    otm_n=0 => Отмечать узлы после эквивалентирования
    """

    def __init__(self, rastr_win=RASTR, table=table_name_com_ekviv):
        self.rastr_win = rastr_win
        self.list_key = []
        for key in table_com_ekviv.keys():
            self.list_key.append(key)
        VariableDefRowId.__init__(self, rastr_win=rastr_win, table=table, switch_command_line=True)

    def set(self,
            selekv=0,
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
            otm_n=0):
        VariableDefRowId.make_changes(self, column=self.list_key[0], row_id=0, value=selekv)
        VariableDefRowId.make_changes(self, column=self.list_key[1], row_id=0, value=met_ekv)
        VariableDefRowId.make_changes(self, column=self.list_key[2], row_id=0, value=tip_ekv)
        VariableDefRowId.make_changes(self, column=self.list_key[3], row_id=0, value=ekvgen)
        VariableDefRowId.make_changes(self, column=self.list_key[4], row_id=0, value=tip_gen)
        VariableDefRowId.make_changes(self, column=self.list_key[5], row_id=0, value=kfc_x)
        VariableDefRowId.make_changes(self, column=self.list_key[6], row_id=0, value=pot_gen)
        VariableDefRowId.make_changes(self, column=self.list_key[7], row_id=0, value=kpn)
        VariableDefRowId.make_changes(self, column=self.list_key[8], row_id=0, value=tip_sxn)
        VariableDefRowId.make_changes(self, column=self.list_key[9], row_id=0, value=smart)
        VariableDefRowId.make_changes(self, column=self.list_key[10], row_id=0, value=zmax)
        VariableDefRowId.make_changes(self, column=self.list_key[11], row_id=0, value=otm_n)


class SetRegim(VariableDefRowId):
    """
    Класс выставляет параметров настройки "Общие параметры режима"


    """

    def __init__(self, rastr_win=RASTR, table=table_name_com_regim, switch_command_line=False):
        self.rastr_win = rastr_win
        self.list_key = []
        for key in table_com_regim.keys():
            self.list_key.append(key)
        self.switch_command_line = switch_command_line

        VariableDefRowId.__init__(self, rastr_win=rastr_win, table=table, switch_command_line=switch_command_line)

    def set(self,
            neb_p=1.000,
            it_max=500,
            start=0,
            flot=1,
            dv_min=0.5,
            dv_max=2.000,
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
            min_nodes_in_island=''):
        VariableDefRowId.make_changes(self, column=self.list_key[0], row_id=0, value=float(neb_p))
        VariableDefRowId.make_changes(self, column=self.list_key[1], row_id=0, value=it_max)
        VariableDefRowId.make_changes(self, column=self.list_key[2], row_id=0, value=start)
        VariableDefRowId.make_changes(self, column=self.list_key[3], row_id=0, value=flot)
        VariableDefRowId.make_changes(self, column=self.list_key[4], row_id=0, value=float(dv_min))
        VariableDefRowId.make_changes(self, column=self.list_key[5], row_id=0, value=float(dv_max))
        VariableDefRowId.make_changes(self, column=self.list_key[6], row_id=0, value=dd_max)
        VariableDefRowId.make_changes(self, column=self.list_key[7], row_id=0, value=status)
        VariableDefRowId.make_changes(self, column=self.list_key[8], row_id=0, value=rr)
        VariableDefRowId.make_changes(self, column=self.list_key[9], row_id=0, value=wt)
        VariableDefRowId.make_changes(self, column=self.list_key[10], row_id=0, value=gen_p)
        VariableDefRowId.make_changes(self, column=self.list_key[11], row_id=0, value=method)
        VariableDefRowId.make_changes(self, column=self.list_key[12], row_id=0, value=method_ogr)
        VariableDefRowId.make_changes(self, column=self.list_key[13], row_id=0, value=print_mode)
        VariableDefRowId.make_changes(self, column=self.list_key[14], row_id=0, value=qmax)
        VariableDefRowId.make_changes(self, column=self.list_key[15], row_id=0, value=min_x)
        VariableDefRowId.make_changes(self, column=self.list_key[16], row_id=0, value=calc_tr)
        VariableDefRowId.make_changes(self, column=self.list_key[17], row_id=0, value=nag_p)
        VariableDefRowId.make_changes(self, column=self.list_key[18], row_id=0, value=rem_breaker)
        VariableDefRowId.make_changes(self, column=self.list_key[19], row_id=0, value=gram)
        VariableDefRowId.make_changes(self, column=self.list_key[20], row_id=0, value=ctrl_baza)
        VariableDefRowId.make_changes(self, column=self.list_key[21], row_id=0, value=itz)
        VariableDefRowId.make_changes(self, column=self.list_key[22], row_id=0, value=itz_ogr_max)
        VariableDefRowId.make_changes(self, column=self.list_key[23], row_id=0, value=itz_ogr_min)
        VariableDefRowId.make_changes(self, column=self.list_key[24], row_id=0, value=min_nodes_in_island)


class SetDynamic(VariableDefRowId):
    """
    Класс выставляет параметров настройки "Общие данные для расчета динамики"
    """

    def __init__(self, rastr_win=RASTR, table=table_name_com_dynamics, switch_command_line=False):
        self.rastr_win = rastr_win
        self.list_key = []
        for key in table_com_dynamics.keys():
            self.list_key.append(key)
        self.switch_command_line = switch_command_line
        VariableDefRowId.__init__(self, rastr_win=rastr_win, table=table, switch_command_line=switch_command_line)

    def set(self,
            t_ras=5,
            h_int=0.01,
            h_min=0.01,
            h_max=0.01,
            h_out=0.01,
            mint=0,
            smint=0,
            int_epsilon=0.0001,
            inform_on_step_change=0,
            tf=0.02,
            dEf=0.001,
            npf=10,
            valid=0,
            dempfrec=0,
            corrT=0,
            is_demp=0,
            frSXNtoY=0.3,
            SXNTolerance='',
            SnapPath='c:\\tmp\\',
            MaxResultFiles='',
            SnapTemplate='<count>.sna',
            SnapAutoLoad=1,
            SnapMaxCount=6,
            TripGeneratorOnSpeed='',
            PickupDropout=0,
            RealtimeCSV=0,
            PeriodAngle=0,
            ResultFlowDirection=0,
            TreatWarningsAsErrors=0,
            EventProcess=0):

        VariableDefRowId.make_changes(self, column=self.list_key[0], row_id=0, value=float(t_ras))
        VariableDefRowId.make_changes(self, column=self.list_key[1], row_id=0, value=float(h_int))
        VariableDefRowId.make_changes(self, column=self.list_key[2], row_id=0, value=float(h_min))
        VariableDefRowId.make_changes(self, column=self.list_key[3], row_id=0, value=float(h_max))
        VariableDefRowId.make_changes(self, column=self.list_key[4], row_id=0, value=float(h_out))
        VariableDefRowId.make_changes(self, column=self.list_key[5], row_id=0, value=int(mint))
        VariableDefRowId.make_changes(self, column=self.list_key[6], row_id=0, value=int(smint))
        VariableDefRowId.make_changes(self, column=self.list_key[7], row_id=0, value=float(int_epsilon))
        VariableDefRowId.make_changes(self, column=self.list_key[8], row_id=0, value=float(inform_on_step_change))
        VariableDefRowId.make_changes(self, column=self.list_key[9], row_id=0, value=float(tf))
        VariableDefRowId.make_changes(self, column=self.list_key[10], row_id=0, value=float(dEf))
        VariableDefRowId.make_changes(self, column=self.list_key[11], row_id=0, value=float(npf))
        VariableDefRowId.make_changes(self, column=self.list_key[12], row_id=0, value=float(valid))
        VariableDefRowId.make_changes(self, column=self.list_key[13], row_id=0, value=float(dempfrec))
        VariableDefRowId.make_changes(self, column=self.list_key[14], row_id=0, value=float(corrT))
        VariableDefRowId.make_changes(self, column=self.list_key[15], row_id=0, value=float(is_demp))
        VariableDefRowId.make_changes(self, column=self.list_key[16], row_id=0, value=float(frSXNtoY))
        VariableDefRowId.make_changes(self, column=self.list_key[17], row_id=0, value=float(SXNTolerance))
        VariableDefRowId.make_changes(self, column=self.list_key[18], row_id=0, value=str(SnapPath))
        VariableDefRowId.make_changes(self, column=self.list_key[19], row_id=0, value=float(MaxResultFiles))
        VariableDefRowId.make_changes(self, column=self.list_key[20], row_id=0, value=str(SnapTemplate))
        VariableDefRowId.make_changes(self, column=self.list_key[21], row_id=0, value=float(SnapAutoLoad))
        VariableDefRowId.make_changes(self, column=self.list_key[22], row_id=0, value=float(SnapMaxCount))
        VariableDefRowId.make_changes(self, column=self.list_key[23], row_id=0, value=float(TripGeneratorOnSpeed))
        VariableDefRowId.make_changes(self, column=self.list_key[24], row_id=0, value=float(PickupDropout))
        VariableDefRowId.make_changes(self, column=self.list_key[25], row_id=0, value=float(RealtimeCSV))
        VariableDefRowId.make_changes(self, column=self.list_key[26], row_id=0, value=float(PeriodAngle))
        VariableDefRowId.make_changes(self, column=self.list_key[27], row_id=0, value=float(ResultFlowDirection))
        VariableDefRowId.make_changes(self, column=self.list_key[28], row_id=0, value=float(TreatWarningsAsErrors))
        VariableDefRowId.make_changes(self, column=self.list_key[29], row_id=0, value=float(EventProcess))


if __name__ == '__main__':
    # import win32com.client
    from R_modules.load_and_save_file.load_file_rastrwin import load_file
    from R_modules.load_and_save_file.shablons_dir import shablon_file_regime
    from R_modules.load_and_save_file.shablons_dir import test_195_rg
    from R_modules.object_rastr import RASTR
    from R_modules.load_and_save_file.save_file_rastrwin import save_file

    # rastr = win32com.client.Dispatch('Astra.Rastr')
    load_file(rastr_win=RASTR, file_path=test_195_rg, shablon=shablon_file_regime)
    set = SetEkviv(rastr_win=RASTR)
    set.set(selekv=1,
            smart=1,
            zmax=85)
    save_file(rastr_win=RASTR, file_path=r'C:\Users\Ohrimenko_AG\Desktop\65\t.rg2', shablon=shablon_file_regime,
              switch_command_line=True)
