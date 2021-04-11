# -*- coding: utf-8 -*-
from RastrWinLib.variables.variable_parametrs import VariableRowId
from RastrWinLib.AstraRastr import RASTR
from time import time, localtime, strftime


class Dynamic:
    """
    Функции для расчтета ЭМПП доступны в интерфейсе IFWDynamic. Интерфейс может быть
    получен с помощью свойства IRastr.FWDynamic.
    TimeReached - Вывод времени, достигнутого в расчете
    ResultMessage - Вывод сообщения о результатах расчета
    switch_result = False
    """

    def __init__(self, rastr_win=RASTR, calc_time=1, snap_max_count=1, switch_command_line=False):
        self.rastr_win = rastr_win
        self.calc_time = calc_time
        self.snap_max_count = snap_max_count
        self.FWDynamic = self.rastr_win.FWDynamic()
        self.TimeReached = self.FWDynamic.TimeReached       # Вывод времени, достигнутого в расчете
        self.ResultMessage = self.FWDynamic.ResultMessage   # Вывод сообщения о результатах расчета
        self.switch_command_line = switch_command_line

    def change_calc_time(self):
        settlement_time = VariableRowId(rastr_win=self.rastr_win, table='com_dynamics', column='Tras', row_id=0,
                                        switch_command_line=True)
        settlement_time.make_changes(value=self.calc_time)

    def change_snap_max_count(self):
        snap_max_count = VariableRowId(rastr_win=self.rastr_win, table='com_dynamics', column='SnapMaxCount', row_id=0,
                                       switch_command_line=True)
        snap_max_count.make_changes(value=self.snap_max_count)

    def run(self):
        if self.switch_command_line is not False:
            start_time = time()
        else:
            start_time = 0
        print(f'Запуск расчета ЭМПП:')
        self.FWDynamic.Run()
        if self.switch_command_line is not False:
            settlement_time = self.rastr_win.Tables('com_dynamics').Cols('Tras').Z(0)
            print(f'\tВремя расчета (T_расч): {float(settlement_time)}')
            print(f'\tСообщение о результатх расчета ЭМПП: {self.ResultMessage}')
            if self.ResultMessage == '':
                print('\t\tРасчет завершен успешно, потери синхронизма не выявлено.')
            elif self.ResultMessage == 0:
                print('\t\tРасчет завершен успешно, потери синхронизма не выявлено.')
            elif self.ResultMessage == 1:
                print('\t\tВыявлено превышение угла по ветви значения 180°.')
            elif self.ResultMessage == 2:
                print('\t\tВыявлено превышение угла по сопротивлению генератора значения 180°.')
            elif self.ResultMessage == 4:
                print('\t\tВыявлено превышение допустимой скорости вращения одного или нескольких генераторов.\n'
                      '\t\tДопустимая скорость вращения задается уставкой автомата безопасности в настройках динамики.')
        if self.switch_command_line is not False:
            time_calc = time() - start_time
            print(
                f'\tВремя расчета ЭМПП: {strftime("M: %M [минут] S: %S [секунд]", localtime(time_calc))} (Seconds: {"%.2f" % (time_calc)} [секунд])')
