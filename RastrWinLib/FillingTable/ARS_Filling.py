# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "Турбины (ИД)" RastrWin3

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.Dynamic.ARS import ARS, ARS_Description
from RastrWinLib.variables.variable_parametrs import Variable


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

    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param row_id: Порядковый номер в таблице Генераторы(ИД): возвращается функцией FindNexSel;
    :param sel: Отметка;
    :param sta: Состояние турбины/регулятора скорости;
    :param Id: Номер турбины/регулятора скорости;
    :param Name: Название турбины/регулятора скорости;
    :param ModelType: Модель турбины/регулятора скорости;
    :param CustomModel: Модель в конструкторе;
    :param Brand: Марка турбины/регулятора скорости;
    :param GovernorId: Номер регулятора скорости турбины;
    :param ao: Постоянная времени на открытие;
    :param az: Постоянная времени на закрытие;
    :param otmin: Минимальная мощность турбины;
    :param otmax: Максимальная мощность турбины;
    :param strs: Статизм регулятора скорости турбины;
    :param zn: Зона нечувствительности;
    :param dpo: Доля участия паровых объемов в суммарной мощности турбины;
    :param Thp: Постоянная времени ЦВД;
    :param Trlp: Постоянная времени ЦНД и промперегрева;
    :param Tw: Временя изменения скорости воды от 0 до ном;
    :param pt: Мощность турбины;
    :param Mu: Положение регулирующего клапана;
    :param Psteam: Давление пара;
    :param Mupo: Паровые объемы;
    :param tpo: Постоянная времени паровых объемов;
    :param switch_command_line: вывод сообщений в протокол;
    :return:
    """
    variable_ = Variable(rastr_win=rastr_win)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.sel,
                               row_id=row_id,
                               value=sel)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.sta,
                               row_id=row_id,
                               value=sta)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.Id,
                               row_id=row_id,
                               value=Id)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.Name,
                               row_id=row_id,
                               value=Name)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.ModelType,
                               row_id=row_id,
                               value=ModelType)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.CustomModel,
                               row_id=row_id,
                               value=CustomModel)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.Brand,
                               row_id=row_id,
                               value=Brand)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.GovernorId,
                               row_id=row_id,
                               value=GovernorId)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.ao,
                               row_id=row_id,
                               value=ao)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.az,
                               row_id=row_id,
                               value=az)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.otmin,
                               row_id=row_id,
                               value=otmin)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.otmax,
                               row_id=row_id,
                               value=otmax)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.strs,
                               row_id=row_id,
                               value=strs)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.zn,
                               row_id=row_id,
                               value=zn)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.dpo,
                               row_id=row_id,
                               value=dpo)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.Thp,
                               row_id=row_id,
                               value=Thp)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.Trlp,
                               row_id=row_id,
                               value=Trlp)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.Tw,
                               row_id=row_id,
                               value=Tw)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.pt,
                               row_id=row_id,
                               value=pt)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.Mu,
                               row_id=row_id,
                               value=Mu)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.Psteam,
                               row_id=row_id,
                               value=Psteam)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.Mupo,
                               row_id=row_id,
                               value=Mupo)

    variable_.make_changes_row(table=ARS.table,
                               column=ARS.tpo,
                               row_id=row_id,
                               value=tpo)
