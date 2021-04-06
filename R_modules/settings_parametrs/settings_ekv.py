# -*- coding: utf-8 -*-

from R_modules.Tables_Parametrs.Tables_and_parametrs import table_name_com_ekviv, table_com_ekviv
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
