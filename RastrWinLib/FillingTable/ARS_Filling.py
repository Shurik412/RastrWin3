# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "Турбины (ИД)" RastrWin3

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.Tables.Dynamic.ARS import ARS, ARS_Description
from RastrWinLib.Variables.variable_parametrs import Variable


def filling_ARS(
        rastr_win=RASTR,
        row_id: int = None,
        sel: bool = None,
        sta: bool = None,
        Id: int = None,
        Name: str = None,
        ModelType: str = None,
        CustomModel: str = None,
        Brand: str = None,
        GovernorId: int = None,
        ao: float = None,
        az: float = None,
        otmin: float = None,
        otmax: float = None,
        strs: float = None,
        zn: float = None,
        dpo: float = None,
        Thp: float = None,
        Trlp: float = None,
        Tw: float = None,
        pt: float = None,
        Mu: float = None,
        Psteam: float = None,
        Mupo: float = None,
        tpo: float = None,
        switch_command_line: bool = False
):
    """
    Функция filling_ARS - заполняет или вносит изменения в заданные переметры таблицы "".

    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param row_id: Порядковый номер в таблице Турбина(ИД): возвращается функцией FindNexSel;
    :param sel: Отметка [O];
    :param sta: Состояние турбины/регулятора скорости [S];
    :param Id: Номер турбины/регулятора скорости [N турб];
    :param Name: Название турбины/регулятора скорости [Название];
    :param ModelType: Модель турбины/регулятора скорости [Модель];
    :param CustomModel: Модель в конструкторе [Конструктор];
    :param Brand: Марка турбины/регулятора скорости [Марка];
    :param GovernorId: Номер регулятора скорости турбины [N АРС];
    :param ao: Постоянная времени на открытие [T_откр];
    :param az: Постоянная времени на закрытие [T_закр];
    :param otmin: Минимальная мощность турбины [Pt_min];
    :param otmax: Максимальная мощность турбины [Pt_max];
    :param strs: Статизм регулятора скорости турбины [Статизм];
    :param zn: Зона нечувствительности [З_неч];
    :param dpo: Доля участия паровых объемов в суммарной мощности турбины [Д_по];
    :param Thp: Постоянная времени ЦВД [Тцвд];
    :param Trlp: Постоянная времени ЦНД и промперегрева [Тцнд];
    :param Tw: Временя изменения скорости воды от 0 до ном [Твод];
    :param pt: Мощность турбины [P_т];
    :param Mu: Положение регулирующего клапана [Mu];
    :param Psteam: Давление пара [Pпара];
    :param Mupo: Паровые объемы [ПО];
    :param tpo: Постоянная времени паровых объемов [Т_по];
    :param switch_command_line: True/False - вывод сообщений в протокол;
    :return: Noting return.
    """
    variable_ = Variable(rastr_win=rastr_win)

    variable_.make_changes_filling_row(table=ARS.table,
                                       column=ARS.sel,
                                       row_id=row_id,
                                       value=sel)

    variable_.make_changes_filling_row(table=ARS.table,
                                       column=ARS.sta,
                                       row_id=row_id,
                                       value=sta)

    variable_.make_changes_filling_row(table=ARS.table,
                                       column=ARS.Id,
                                       row_id=row_id,
                                       value=Id)

    variable_.make_changes_filling_row(table=ARS.table,
                                       column=ARS.Name,
                                       row_id=row_id,
                                       value=Name)

    variable_.make_changes_filling_row(table=ARS.table,
                                       column=ARS.ModelType,
                                       row_id=row_id,
                                       value=ModelType)

    variable_.make_changes_filling_row(table=ARS.table,
                                       column=ARS.CustomModel,
                                       row_id=row_id,
                                       value=CustomModel)

    variable_.make_changes_filling_row(table=ARS.table,
                                       column=ARS.Brand,
                                       row_id=row_id,
                                       value=Brand)

    variable_.make_changes_filling_row(table=ARS.table,
                                       column=ARS.GovernorId,
                                       row_id=row_id,
                                       value=GovernorId)

    variable_.make_changes_filling_row(table=ARS.table,
                                       column=ARS.ao,
                                       row_id=row_id,
                                       value=ao)

    variable_.make_changes_filling_row(table=ARS.table,
                                       column=ARS.az,
                                       row_id=row_id,
                                       value=az)

    variable_.make_changes_filling_row(table=ARS.table,
                                       column=ARS.otmin,
                                       row_id=row_id,
                                       value=otmin)

    variable_.make_changes_filling_row(table=ARS.table,
                                       column=ARS.otmax,
                                       row_id=row_id,
                                       value=otmax)

    variable_.make_changes_filling_row(table=ARS.table,
                                       column=ARS.strs,
                                       row_id=row_id,
                                       value=strs)

    variable_.make_changes_filling_row(table=ARS.table,
                                       column=ARS.zn,
                                       row_id=row_id,
                                       value=zn)

    variable_.make_changes_filling_row(table=ARS.table,
                                       column=ARS.dpo,
                                       row_id=row_id,
                                       value=dpo)

    variable_.make_changes_filling_row(table=ARS.table,
                                       column=ARS.Thp,
                                       row_id=row_id,
                                       value=Thp)

    variable_.make_changes_filling_row(table=ARS.table,
                                       column=ARS.Trlp,
                                       row_id=row_id,
                                       value=Trlp)

    variable_.make_changes_filling_row(table=ARS.table,
                                       column=ARS.Tw,
                                       row_id=row_id,
                                       value=Tw)

    variable_.make_changes_filling_row(table=ARS.table,
                                       column=ARS.pt,
                                       row_id=row_id,
                                       value=pt)

    variable_.make_changes_filling_row(table=ARS.table,
                                       column=ARS.Mu,
                                       row_id=row_id,
                                       value=Mu)

    variable_.make_changes_filling_row(table=ARS.table,
                                       column=ARS.Psteam,
                                       row_id=row_id,
                                       value=Psteam)

    variable_.make_changes_filling_row(table=ARS.table,
                                       column=ARS.Mupo,
                                       row_id=row_id,
                                       value=Mupo)

    variable_.make_changes_filling_row(table=ARS.table,
                                       column=ARS.tpo,
                                       row_id=row_id,
                                       value=tpo)


if __name__ == '__main__':
    from RastrWinLib.loading.load import load_file
    from RastrWinLib.loading.save import save_file
    from RastrWinLib.loading.shablon import Shabl
    from RastrWinLib.Tables.Dynamic.ARS import ARS
    from RastrWinLib.AstraRastr import RASTR

    load_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Desktop\test_filling\test.rst',
              shabl=Shabl.shablon_file_dynamic)

    load_file(rastr_win=RASTR,
              shabl=Shabl.shablon_file_automation)

    table_ = RASTR.Tables(ARS.table)

    for i in range(0, 10):
        table_.AddRow()
        filling_ARS(rastr_win=RASTR,
                    row_id=i,
                    sel=None,
                    sta=None,
                    Id=123456789,
                    Name=f'Генератор {i}',
                    ModelType=None,
                    CustomModel=None,
                    Brand=None,
                    GovernorId=12345679,
                    ao=0.123456789,
                    az=0.123456789,
                    otmin=0.123456789,
                    otmax=0.123456789,
                    strs=0.123456789,
                    zn=0.123456789,
                    dpo=0.123456789,
                    Thp=0.123456789,
                    Trlp=0.123456789,
                    Tw=0.123456789,
                    pt=0.123456789,
                    Mu=0.123456789,
                    Psteam=0.123456789,
                    Mupo=0.123456789,
                    tpo=0.123456789,
                    switch_command_line=False)

    save_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Desktop\test_filling\test22.rst',
              shabl=Shabl.shablon_file_dynamic)
