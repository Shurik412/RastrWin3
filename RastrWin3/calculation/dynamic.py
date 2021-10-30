# -*- coding: utf-8 -*-
from RastrWin3.AstraRastr import RASTR
from RastrWin3.Settings.dynamic import GetSettingsDynamic, VariableSettingsDynamic
from RastrWin3.Tools.tools import TableOutput


class Dynamic(VariableSettingsDynamic, GetSettingsDynamic):
    """
    Расчет Электро Механических Переходных Процессов (ЭМехПП)
    """

    def __init__(self, rastr_win=RASTR,
                 calc_time: float = 1.0,
                 snap_max_count: int = 1,
                 switch_command_line: bool = False):
        """
        Функции для расчтета ЭМПП доступны в интерфейсе IFWDynamic.
        Интерфейс может быть получен с помощью свойства IRastr.FWDynamic.
        :param rastr_win: COM - объект Rastr.Astra (win32com);
        :param calc_time: время расчета ЭМПП;
        :param snap_max_count: макс. число сохраняемых файлов *.sna с результатами;
        :param switch_command_line: True/False - вывод сообщений в протокол.
        """
        super().__init__()
        self.rastr_win = rastr_win
        self.calc_time = calc_time
        self.snap_max_count = snap_max_count
        self.switch_command_line = switch_command_line

        self.FWDynamic = self.rastr_win.FWDynamic()
        self.TimeReached = self.FWDynamic.TimeReached  # Вывод времени, достигнутого в расчете

        if self.snap_max_count == 1.0:
            VariableSettingsDynamic.SnapMaxCount(self, value=self.snap_max_count)
        else:
            print(f'snap_max_count больше 1.0 => {GetSettingsDynamic.SnapMaxCount(self)}')

    def __bool__(self):
        return self.switch_command_line

    def change_calc_time(self):
        VariableSettingsDynamic.Tras(self, value=self.calc_time)

    def change_snap_max_count(self):
        VariableSettingsDynamic.SnapMaxCount(self, value=self.snap_max_count)

    def run(self):
        self.FWDynamic.Run()
        if self.switch_command_line:
            self.messageResult()

    def messageResult(self):
        ResultMessage = self.FWDynamic.ResultMessage  # Вывод сообщения о результатах расчета
        pt = TableOutput(fieldName=['Описание', 'Параметр'])
        pt.row_add(['Время расчета для динамики', f'{GetSettingsDynamic.Tras(self)} cек.'])
        pt.row_add(['Сообщение о результатх расчета ЭМПП', ResultMessage])
        if ResultMessage == '':
            pt.row_add(['Расчет завершен успешно, потери синхронизма не выявлено.', ''])
        elif ResultMessage == 0:
            pt.row_add(['Расчет завершен успешно, потери синхронизма не выявлено.', ''])
        elif ResultMessage == 1:
            pt.row_add(['Выявлено превышение угла по ветви значения 180°.', ''])
        elif ResultMessage == 2:
            pt.row_add(['Выявлено превышение угла по сопротивлению генератора значения 180°.', ''])
        elif ResultMessage == 4:
            pt.row_add(['Выявлено превышение допустимой скорости вращения одного или нескольких генераторов.'
                        'Допустимая скорость вращения задается уставкой автомата безопасности в настройках динамики.',
                        ''])
        pt.show(title_table="Расчет ЭМПП")
        return ResultMessage
