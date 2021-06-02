# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "Возбудитель DECS-400" RastrWin3

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.Dynamic.DECS_400 import DFWDECS400, DFWDECS400_Description
from RastrWinLib.variables.variable_parametrs import Variable


def filling_DECS400(
        rastr_win=RASTR,
        row_id: int = None,
        sel: bool = None,
        sta: bool = None,
        Id: int = None,
        Name: str = None,
        ModelType: str = None,
        Brand: str = None,
        CustomModel: str = None,
        PSSId: int = None,
        UELId: int = None,
        OELId: int = None,
        ForcerId: int = None,
        Xl: float = None,
        DRP: float = None,
        VrMin: float = None,
        VrMax: float = None,
        VmMax: float = None,
        VmMin: float = None,
        VbMax: float = None,
        Kc: float = None,
        Kp: float = None,
        Kpm: float = None,
        Kpr: float = None,
        Kir: float = None,
        Kpd: float = None,
        Ta: float = None,
        Td: float = None,
        Tr: float = None,
        SelfExc: float = None,
        Del: float = None,
        switch_command_line: bool = False
):
    """

    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param row_id:
    :param sel:
    :param sta:
    :param Id: Номер возбудителя [N взб];
    :param Name: Название возбудителя [Название];
    :param ModelType: Модель возбудителя [Модель];
    :param Brand: Марка возбудителя [Марка];
    :param CustomModel: Модель в конструкторе [Конструктор];
    :param PSSId: Номер системного стабилизатора [N стаб];
    :param UELId: Номер ОМВ [N ОМВ];
    :param OELId: Номер БОР [N БОР];
    :param ForcerId: Номер РФ [N РФ];
    :param Xl: Потери в выпрямителе [Xl];
    :param DRP: Статизм [DRP];
    :param VrMin: Минимальное ограничение потери напряжения (? цитата НИИПТ) [VrMin];
    :param VrMax: Максимальное ограничение потери напряжения (? цитата НИИПТ) [VrMax];
    :param VmMax: Максимальное ограничение тока контроллера [VmMax];
    :param VmMin: Минимальное ограничение тока контроллера [VmMin];
    :param VbMax: Максимальное напряжение возбудителя [VbMax];
    :param Kc: Коэффициент усиления [Kc];
    :param Kp: Коэффициент усиления [Kp];
    :param Kpm: Коэффициент усиления [Kpm];
    :param Kpr: Пропорциональный коэффициент усиления [Kpr];
    :param Kir: Интегральный коэффициент усиления [Kir];
    :param Kpd: Дифференциальный коэффициент усиления [Kpd];
    :param Ta: Постоянная времени тиристорного моста [Ta];
    :param Td: Постоянная времени дифференциального канала [Td];
    :param Tr: Постоянная времени фильтров [Tr];
    :param SelfExc: Самовозбуждение [CB];
    :param Del: Самовозбуждение [Del];
    :param switch_command_line: вывод сообщений в протокол;
    :return:
    """
    variable_ = Variable(rastr_win=rastr_win)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.sel,
                                       row_id=row_id,
                                       value=sel)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.sta,
                                       row_id=row_id,
                                       value=sta)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.Id,
                                       row_id=row_id,
                                       value=Id)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.Name,
                                       row_id=row_id,
                                       value=Name)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.ModelType,
                                       row_id=row_id,
                                       value=ModelType)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.Brand,
                                       row_id=row_id,
                                       value=Brand)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.CustomModel,
                                       row_id=row_id,
                                       value=CustomModel)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.PSSId,
                                       row_id=row_id,
                                       value=PSSId)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.UELId,
                                       row_id=row_id,
                                       value=UELId)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.OELId,
                                       row_id=row_id,
                                       value=OELId)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.ForcerId,
                                       row_id=row_id,
                                       value=ForcerId)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.Xl,
                                       row_id=row_id,
                                       value=Xl)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.DRP,
                                       row_id=row_id,
                                       value=DRP)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.VrMin,
                                       row_id=row_id,
                                       value=VrMin)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.VrMax,
                                       row_id=row_id,
                                       value=VrMax)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.VmMax,
                                       row_id=row_id,
                                       value=VmMax)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.VmMin,
                                       row_id=row_id,
                                       value=VmMin)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.VbMax,
                                       row_id=row_id,
                                       value=VbMax)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.Kc,
                                       row_id=row_id,
                                       value=Kc)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.Kp,
                                       row_id=row_id,
                                       value=Kp)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.Kpm,
                                       row_id=row_id,
                                       value=Kpm)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.Kpr,
                                       row_id=row_id,
                                       value=Kpr)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.Kir,
                                       row_id=row_id,
                                       value=Kir)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.Kpd,
                                       row_id=row_id,
                                       value=Kpd)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.Ta,
                                       row_id=row_id,
                                       value=Ta)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.Td,
                                       row_id=row_id,
                                       value=Td)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.Tr,
                                       row_id=row_id,
                                       value=Tr)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.SelfExc,
                                       row_id=row_id,
                                       value=SelfExc)

    variable_.make_changes_filling_row(table=DFWDECS400.table,
                                       column=DFWDECS400.Del,
                                       row_id=row_id,
                                       value=Del)


if __name__ == '__main__':
    from RastrWinLib.AstraRastr import RASTR
    from RastrWinLib.loading.load import load_file
    from RastrWinLib.loading.save import save_file
    from RastrWinLib.loading.shablon import Shabl
    from RastrWinLib.tables.Dynamic.DECS_400 import DFWDECS400

    load_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Desktop\test_filling\test.rst',
              shabl=Shabl.shablon_file_dynamic)

    load_file(rastr_win=RASTR,
              shabl=Shabl.shablon_file_automation)

    table_ = RASTR.Tables(DFWDECS400.table)

    for i in range(0, 10):
        table_.AddRow()
        filling_DECS400(
            rastr_win=RASTR,
            row_id=i,
            sel=None,
            sta=None,
            Id=123456789,
            Name=f'Генератор {i}',
            ModelType=None,
            Brand=None,
            CustomModel=None,
            PSSId=123456789,
            UELId=123456789,
            OELId=123456879,
            ForcerId=123456798,
            Xl=0.123456,
            DRP=0.123456,
            VrMin=0.123456,
            VrMax=0.123456,
            VmMax=0.123456,
            VmMin=0.123456,
            VbMax=0.123456,
            Kc=0.123456,
            Kp=0.123456,
            Kpm=0.123456,
            Kpr=0.123456,
            Kir=0.123456,
            Kpd=0.123456,
            Ta=0.123456,
            Td=0.123456,
            Tr=0.123456,
            SelfExc=0.123456,
            Del=0.123456,
            switch_command_line=False)

    save_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Desktop\test_filling\test23.rst',
              shabl=Shabl.shablon_file_dynamic)
