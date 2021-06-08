# -*- coding: utf-8 -*-
from time import time, localtime, strftime

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.Settings.com_dynamics import ComDynamics
from RastrWinLib.tools.tools import Tools
from RastrWinLib.variables.variable_parametrs import Variable
from win32com.client import Dispatch, WithEvents, constants


class RastrEvents:
    """
    Метод Onprot - выводит сообщения написанные: rastr.Printp("Сообщение из Printp")
    Метод OnLog
    """

    def OnLog(self, code, level, id, name, index, description, formName):
        print(f"[{code}] {description}")

    def Onprot(self, message):
        print(message)


class Dynamic:

    def __init__(self, rastr_win=RASTR,
                 calc_time: float = 1.0,
                 snap_max_count=1,
                 switch_command_line=False):
        f"""
        Функции для расчтета ЭМПП доступны в интерфейсе IFWDynamic.
        Интерфейс может быть получен с помощью свойства IRastr.FWDynamic.
        :param rastr_win: ;
        :param calc_time: время расчета ЭМПП;
        :param snap_max_count:  
        :param switch_command_line: ;
        """

        self.rastr_win = rastr_win
        self.calc_time = calc_time
        self.snap_max_count = snap_max_count
        self.FWDynamic = self.rastr_win.FWDynamic()
        self.TimeReached = self.FWDynamic.TimeReached  # Вывод времени, достигнутого в расчете
        self.switch_command_line = switch_command_line

        if self.snap_max_count == 1.0:
            snap_max_count = Variable(rastr_win=self.rastr_win,
                                      switch_command_line=self.switch_command_line)
            snap_max_count.make_changes_row(table=ComDynamics.table,
                                            column=ComDynamics.SnapMaxCount,
                                            row_id=0,
                                            value=self.snap_max_count)
        else:
            print(f'snap_max_count больше 1.0 => {self.snap_max_count}')

    def change_calc_time(self):
        settlement_time = Variable(rastr_win=self.rastr_win,
                                   switch_command_line=True)

        settlement_time.make_changes_row(table=ComDynamics.table,
                                         column=ComDynamics.Tras,
                                         row_id=0,
                                         value=self.calc_time)

    def change_snap_max_count(self):
        snap_max_count = Variable(rastr_win=self.rastr_win,
                                  switch_command_line=True)

        snap_max_count.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.SnapMaxCount,
                                        row_id=0,
                                        value=self.snap_max_count)

    def run(self):
        if self.switch_command_line is not False:
            start_time = time()
        else:
            start_time = 0
        print(Tools.separator_grid)
        print(f'Запуск расчета ЭМПП:')
        self.FWDynamic.Run()
        ResultMessage = self.FWDynamic.ResultMessage  # Вывод сообщения о результатах расчета
        if self.switch_command_line is not False:
            settlement_time = self.rastr_win.Tables(ComDynamics.table).Cols(ComDynamics.Tras).Z(0)
            print(f'\tВремя расчета (T_расч): {float(settlement_time)}')
            print(f'\tСообщение о результатх расчета ЭМПП: {ResultMessage}')
            if ResultMessage == '':
                print('\t\tРасчет завершен успешно, потери синхронизма не выявлено.')
            elif ResultMessage == 0:
                print('\t\tРасчет завершен успешно, потери синхронизма не выявлено.')
            elif ResultMessage == 1:
                print('\t\tВыявлено превышение угла по ветви значения 180°.')
            elif ResultMessage == 2:
                print('\t\tВыявлено превышение угла по сопротивлению генератора значения 180°.')
            elif ResultMessage == 4:
                print('\t\tВыявлено превышение допустимой скорости вращения одного или нескольких генераторов.\n'
                      '\t\tДопустимая скорость вращения задается уставкой автомата безопасности в настройках динамики.')
        if self.switch_command_line is not False:
            time_calc = time() - start_time
            print(
                f'\tВремя расчета ЭМПП: {strftime("M: %M [минут] S: %S [секунд]", localtime(time_calc))}'
                f' (Seconds: {"%.2f" % time_calc} [секунд])')
        print(Tools.separator_grid)
        return ResultMessage


if __name__ == '__main__':
    from RastrWinLib.loading.load import load_file
    from RastrWinLib.loading.shablon import Shabl
    from RastrWinLib.AstraRastr import RASTR

    load_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst',
              shabl=Shabl.shablon_file_dynamic)

    load_file(rastr_win=RASTR)

    calc = Dynamic(rastr_win=RASTR)

    calc.run()
