# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "Возбудитель IEEE" RastrWin3

from RastrWinLib.ActionsObject.Variable import Variable
from RastrWinLib.AstraRastr import RASTR


def filling_DFWIEEE421(
        rastr_win=RASTR,
        row_id: int = None,
        sel: bool = None,
        sta: bool = None,
        Id: int = None,
        Name: str = None,
        ModelType: str = None,
        Brand: str = None,
        CustomModel: str = None,
        UELId: int = None,
        UELPos: str = None,
        OELId: int = None,
        OELPos: str = None,
        PSSId: int = None,
        PSSPos: str = None,
        Te: float = None,
        Ta: float = None,
        Tk: float = None,
        Tj: float = None,
        Th: float = None,
        Tm: float = None,
        Tc: float = None,
        Tc1: float = None,
        Tc2: float = None,
        Tb: float = None,
        Tb1: float = None,
        Tb2: float = None,
        Trh: float = None,
        Tdr: float = None,
        Tf: float = None,
        Tf2: float = None,
        Tf3: float = None,
        Tub1: float = None,
        Tub2: float = None,
        Tuc1: float = None,
        Tob1: float = None,
        Toc1: float = None,
        Toc2: float = None,
        Tob2: float = None,
        Tr: float = None,
        TINT: float = None,
        Ke: float = None,
        Ka: float = None,
        Kia: float = None,
        Kf: float = None,
        Kf1: float = None,
        Kf2: float = None,
        Kof: float = None,
        K1f: float = None,
        Kfw: float = None,
        Kv: float = None,
        Kp: float = None,
        Kpa: float = None,
        Kpr: float = None,
        Kir: float = None,
        Kdr: float = None,
        Kc: float = None,
        Kc1: float = None,
        Kc2: float = None,
        Kcf: float = None,
        Kd: float = None,
        Kb: float = None,
        Kh: float = None,
        Khf: float = None,
        Kr: float = None,
        Kn: float = None,
        Klv: float = None,
        Kl: float = None,
        Klr: float = None,
        Klo: float = None,
        Ki: float = None,
        Ki2: float = None,
        Kif: float = None,
        Kif1: float = None,
        Kg: float = None,
        Km: float = None,
        Ku: float = None,
        Ku1: float = None,
        KST: float = None,
        Se1: float = None,
        Se2: float = None,
        Efd1: float = None,
        Efd2: float = None,
        Efdn: float = None,
        Ve1: float = None,
        Ve2: float = None,
        Aex: float = None,
        Bex: float = None,
        SW1: float = None,
        SW2: float = None,
        Vemin: float = None,
        Vrmax: float = None,
        Vrmin: float = None,
        Vfemax: float = None,
        Vimax: float = None,
        Vimin: float = None,
        Vamax: float = None,
        Vamin: float = None,
        Vlv: float = None,
        Vmmax: float = None,
        Vmmin: float = None,
        Vhmax: float = None,
        Vfelim: float = None,
        VBmax: float = None,
        VGmax: float = None,
        VfwMax: float = None,
        VfwMin: float = None,
        Vlim1: float = None,
        Vlim2: float = None,
        VpidMax: float = None,
        VpidMin: float = None,
        Ilr: float = None,
        Theta: float = None,
        Ifmax: float = None,
        Ifth: float = None,
        VB2max: float = None,
        Xl: float = None,
        Rc: float = None,
        Xc: float = None,
        TRFout: float = None,
        Samovozb: float = None,
        RPQlim: float = None,
        RIFlim: float = None,
        switch_command_line: bool = False
):
    """
    Функция filling_DFWIEEE421 - вносит изменения в таблицу "Возбудители IEEE".

    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param row_id: Порядковый номер в таблице: возвращается функцией FindNexSel;
    :param sel: Отметка [O];
    :param sta: Состояние возбудителя [S];
    :param Id: Номер возбудителя [N взб];
    :param Name: Название возбудителя [Название];
    :param ModelType: Модель возбудителя [Модель];
    :param Brand: Марка возбудителя [Марка];
    :param CustomModel: Модель в конструкторе [Конструктор];
    :param UELId: Номер ОМВ [N ОМВ];
    :param UELPos: Точка подключения ОМВ [Точка ОМВ];
    :param OELId: Номер БОР [N БОР];
    :param OELPos: Точка подключения БОР [Точка БОР];
    :param PSSId: Номер системного стабилизатора [N стаб];
    :param PSSPos: Точка подключения стабилизатора [Точка стаб];
    :param Te: Постоянная времени возбудителя [Te];
    :param Ta: Постоянная времени регулятора напряжения [Ta];
    :param Tk: Постоянная времени инерционно-форсирующего звена регулятора (AC6A) [Tk];
    :param Tj: Постоянная времени ограничителя тока возбуждения (AC6A) [Tj];
    :param Th: Постоянная времени ограничителя тока возбуждения (AC6A) [Th];
    :param Tm: Постоянная времени внутреннего каскада [Tm];
    :param Tc: Постоянная времени регулятора напряжения [Tc];
    :param Tc1: Постоянная времени регулятора напряжения [Tc1];
    :param Tc2: Постоянная времени основного канала [Tc2];
    :param Tb: Постоянная времени регулятора напряжения [Tb];
    :param Tb1: Постоянная времени регулятора напряжения [Tb1];
    :param Tb2: Постоянная времени основного канала [Tb2];
    :param Trh: Постоянная времени перемещения реостата (DC3A) [Trh];
    :param Tdr: Постоянная времени дифференциального канала [Tdr];
    :param Tf: Постоянная времени обратной связи cтабилизации [Tf];
    :param Tf2: Постоянная времени звена обратной связи (AC5C) [Tf2];
    :param Tf3: Постоянная времени звена обратной связи (AC5C) [Tf3];
    :param Tub1: Постоянная времени канала UEL [Tub1];
    :param Tub2: Постоянная времени канала UEL [Tub2];
    :param Tuc1: Постоянная времени канала UEL [Tuc1];
    :param Tob1: Постоянная времени канала OEL [Tob1];
    :param Toc1: Постоянная времени канала OEL [Toc1];
    :param Toc2: Постоянная времени канала OEL [Toc2];
    :param Tob2: Постоянная времени канала OEL [Tob2];
    :param Tr: Постоянная времени датчика напряжения [Tr];
    :param TINT: Постоянная времени интегратора в канале регулирования по отклонению напряжения генератора [TINT];
    :param Ke: Коэффициент обратной связи возбудителя [Ke];
    :param Ka: Коэффициент усиления регулятора напряжения [Ka];
    :param Kia: Интегральный коэффициент усиления [Kia];
    :param Kf: Коэффициент обратной связи cтабилизации [Kf];
    :param Kf1: Коэффициент стабилизирующей обратной связи [Kf1];
    :param Kf2: Коэффициент стабилизирующей обратной связи [Kf2];
    :param Kof: Коэффициент усиления в канале по отклонению частоты напряжения генератора [K0f];
    :param K1f: Коэффициент стабилизирующей обратной связи [Kf1];
    :param Kfw: Коэффициент ШИМ-преобразователя [Kfw];
    :param Kv: Интервал переключения контактов (DC3A) [Kv];
    :param Kp: Коэффициент усиления по напряжению на выводах [Kp];
    :param Kpa: Пропорциональный коэффициент усиления [Kpa];
    :param Kpr: Пропорциональный коэффициент усиления [Kpr];
    :param Kir: Интегральный коэффициент усиления [Kir];
    :param Kdr: Дифференциальный  коэффициент усиления [Kdr];
    :param Kc: Коэффициент нагрузки выпрямителя [Kc];
    :param Kc1: Коэффициент нагрузки системы питания [Kc1];
    :param Kc2: Коэффициент нагрузки системы питания по току [Kc2];
    :param Kcf: Постоянная времени охлаждения [Kcf];
    :param Kd: Коэффициент демагнетизации [Kd];
    :param Kb: Коэффициент усиления [Kb];
    :param Kh: Коэффициент ОС по току (AC2C)/Коэффициент усиления ограничителя (AC6A) [Kh];
    :param Khf: Постоянная времени обратной время?токовой характеристики [Khf];
    :param Kr: Коэффициент ОС питания регулятора (AC3A)/Усиления ST5B/Питания (AC7C) [Kr];
    :param Kn: Переключаемый коэффициент стабилизирующей ОС (AC3A) [Kn];
    :param Klv: Коэффициент системы ограничения минмального возбуждения (AC3A) [Klv];
    :param Kl: Коэффициент усиления ограничения по напряжению на выводах (AC7C) [Kl];
    :param Klr: Коэффициент усиления ограничителя возбуждения [Klr];
    :param Klo: Коэффициент регулирования устройства ОМВ [Klo];
    :param Ki: Коэффициент усиления по току статора [Ki];
    :param Ki2: Коэффициент системы питания по току [Ki2];
    :param Kif: Коэффициент усиления контура отрицательной обратной связи (ООС) по току возбуждения [Kif];
    :param Kif1: Коэффициент регулирования по производной тока ротора [Kif1];
    :param Kg: Коэффициент усиления обратной связи [Kg];
    :param Km: Коэффициент усиления внутреннего каскада [Km];
    :param Ku: Коэффициент регулирования по отклонению напряжения [Ku];
    :param Ku1: Коэффициент регулирования по производной напряжения [Ku1];
    :param KST: Статизм по реактивной мощности [KST];
    :param Se1: Se первой точки кривой насыщения [Se1];
    :param Se2: Se второй точки кривой насыщения [Se2];
    :param Efd1: Efd первой точки кривой насыщения [Efd1];
    :param Efd2: Efd второй точки кривой насыщения [Efd2];
    :param Efdn: Порог переключения коэффициентов стабилизирующей ОС (AC3A) [Efdn];
    :param Ve1: Ve первой точки кривой насыщения [Ve1];
    :param Ve2: Ve второй точки кривой насыщения [Ve2];
    :param Aex: Коэффициент кривой насыщения вращающегося возбудителя [Aex];
    :param Bex: Коэффициент кривой насыщения вращающегося возбудителя [Bex];
    :param SW1: Переключатель SW1 [SW1];
    :param SW2: Переключатель SW2 [SW2];
    :param Vemin: Минимальное напряжение возбудителя [Vemin];
    :param Vrmax: Ограничение регулятора возбуждения [Vrmax];
    :param Vrmin: Ограничение регулятора возбуждения [Vrmin];
    :param Vfemax: Максимальное напряжение возбудителя [Vfemax];
    :param Vimax: Максимальное ограничение входа регулятора [Vimax];
    :param Vimin: Минимальное ограничение входа регулятора [Vimin];
    :param Vamax: Максимальное регулятора напряжения [Vamax];
    :param Vamin: Минимальное ограничение регулятора напряжения [Vamin];
    :param Vlv: Порог системы ограничения минмального возбуждения (AC3A) [Vlv];
    :param Vmmax: Максимальное ограничение усилителя [Vmmax];
    :param Vmmin: Минимальное ограничение усилителя [Vmmin];
    :param Vhmax: Ограничение сигнала обратной связи (AC6A) [Vhmax];
    :param Vfelim: Уставка ограничителя минимального возбуждения [Vfelim];
    :param VBmax: Ограничение источника питания [VBmax];
    :param VGmax: Ограничение обратной связи [VGmax];
    :param VfwMax: Максимальное ограничение ШИМ-преобразователя [VfwMax];
    :param VfwMin: Минимальное ограничение ШИМ-преобразователя [VfwMin];
    :param Vlim1: Порог ШИМ-преобразователя [Vlim1];
    :param Vlim2: Порог ШИМ-преобразователя [Vlim2];
    :param VpidMax: Максимальное ограничение ПИД-регулятора [VpidMax];
    :param VpidMin: Минимальное ограничение ПИД-регулятора [VpidMin];
    :param Ilr: Уставка ограничителя перевозбуждения [Ilr];
    :param Theta: Коэффициент усиления по току статора [Theta];
    :param Ifmax: Уставка максимального тока возбуждения [Ifmax];
    :param Ifth: Уставка теплового ограничения по току возбуждения [Ifth];
    :param VB2max: Ограничение источника питания по току [VB2max];
    :param Xl: Сопротивление источника питания [Xl];
    :param Rc: R компенсации [Rc];
    :param Xc: X компенсации [Xc];
    :param TRFout: Блокировка работы релейной форсировки [TRFout];
    :param Samovozb: Параметр, определяющий тип системы возбуждения (зависимая/независимая) [Samovozb];
    :param RPQlim: Блокировка работы устройства ОМВ [RPQlim];
    :param RIFlim: Блокировка работы устройства БОР [RIFlim];
    :param switch_command_line: True/False - вывод сообщений в протокол;
    :return: Noting return.
    """
    variable_ = Variable(rastr_win=rastr_win)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.sel,
                                       row_id=row_id,
                                       value=sel)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.sta,
                                       row_id=row_id,
                                       value=sta)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Id,
                                       row_id=row_id,
                                       value=Id)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Name,
                                       row_id=row_id,
                                       value=Name)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.ModelType,
                                       row_id=row_id,
                                       value=ModelType)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Brand,
                                       row_id=row_id,
                                       value=Brand)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.CustomModel,
                                       row_id=row_id,
                                       value=CustomModel)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.UELId,
                                       row_id=row_id,
                                       value=UELId)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.UELPos,
                                       row_id=row_id,
                                       value=UELPos)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.OELId,
                                       row_id=row_id,
                                       value=OELId)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.OELPos,
                                       row_id=row_id,
                                       value=OELPos)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.PSSId,
                                       row_id=row_id,
                                       value=PSSId)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.PSSPos,
                                       row_id=row_id,
                                       value=PSSPos)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Te,
                                       row_id=row_id,
                                       value=Te)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Ta,
                                       row_id=row_id,
                                       value=Ta)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Tk,
                                       row_id=row_id,
                                       value=Tk)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Tj,
                                       row_id=row_id,
                                       value=Tj)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Th,
                                       row_id=row_id,
                                       value=Th)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Tm,
                                       row_id=row_id,
                                       value=Tm)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Tc,
                                       row_id=row_id,
                                       value=Tc)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Tc1,
                                       row_id=row_id,
                                       value=Tc1)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Tc2,
                                       row_id=row_id,
                                       value=Tc2)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Tb,
                                       row_id=row_id,
                                       value=Tb)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Tb1,
                                       row_id=row_id,
                                       value=Tb1)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Tb2,
                                       row_id=row_id,
                                       value=Tb2)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Trh,
                                       row_id=row_id,
                                       value=Trh)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Tdr,
                                       row_id=row_id,
                                       value=Tdr)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Tf,
                                       row_id=row_id,
                                       value=Tf)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Tf2,
                                       row_id=row_id,
                                       value=Tf2)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Tf3,
                                       row_id=row_id,
                                       value=Tf3)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Tub1,
                                       row_id=row_id,
                                       value=Tub1)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Tub2,
                                       row_id=row_id,
                                       value=Tub2)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Tuc1,
                                       row_id=row_id,
                                       value=Tuc1)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Tob1,
                                       row_id=row_id,
                                       value=Tob1)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Toc1,
                                       row_id=row_id,
                                       value=Toc1)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Toc2,
                                       row_id=row_id,
                                       value=Toc2)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Tob2,
                                       row_id=row_id,
                                       value=Tob2)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Tr,
                                       row_id=row_id,
                                       value=Tr)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.TINT,
                                       row_id=row_id,
                                       value=TINT)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Ke,
                                       row_id=row_id,
                                       value=Ke)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Ka,
                                       row_id=row_id,
                                       value=Ka)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kia,
                                       row_id=row_id,
                                       value=Kia)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kf,
                                       row_id=row_id,
                                       value=Kf)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kf1,
                                       row_id=row_id,
                                       value=Kf1)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kf2,
                                       row_id=row_id,
                                       value=Kf2)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kof,
                                       row_id=row_id,
                                       value=Kof)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.K1f,
                                       row_id=row_id,
                                       value=K1f)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kfw,
                                       row_id=row_id,
                                       value=Kfw)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kv,
                                       row_id=row_id,
                                       value=Kv)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kp,
                                       row_id=row_id,
                                       value=Kp)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kpa,
                                       row_id=row_id,
                                       value=Kpa)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kpr,
                                       row_id=row_id,
                                       value=Kpr)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kir,
                                       row_id=row_id,
                                       value=Kir)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kpa,
                                       row_id=row_id,
                                       value=Kpa)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kpr,
                                       row_id=row_id,
                                       value=Kpr)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kir,
                                       row_id=row_id,
                                       value=Kir)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kdr,
                                       row_id=row_id,
                                       value=Kdr)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kc,
                                       row_id=row_id,
                                       value=Kc)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kc1,
                                       row_id=row_id,
                                       value=Kc1)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kc2,
                                       row_id=row_id,
                                       value=Kc2)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kcf,
                                       row_id=row_id,
                                       value=Kcf)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kd,
                                       row_id=row_id,
                                       value=Kd)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kb,
                                       row_id=row_id,
                                       value=Kb)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kh,
                                       row_id=row_id,
                                       value=Kh)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Khf,
                                       row_id=row_id,
                                       value=Khf)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kr,
                                       row_id=row_id,
                                       value=Kr)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kn,
                                       row_id=row_id,
                                       value=Kn)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Klv,
                                       row_id=row_id,
                                       value=Klv)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kl,
                                       row_id=row_id,
                                       value=Kl)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Klr,
                                       row_id=row_id,
                                       value=Klr)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Klo,
                                       row_id=row_id,
                                       value=Klo)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Ki,
                                       row_id=row_id,
                                       value=Ki)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Ki2,
                                       row_id=row_id,
                                       value=Ki2)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Klo,
                                       row_id=row_id,
                                       value=Klo)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Ki,
                                       row_id=row_id,
                                       value=Ki)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Ki2,
                                       row_id=row_id,
                                       value=Ki2)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kif,
                                       row_id=row_id,
                                       value=Kif)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kif1,
                                       row_id=row_id,
                                       value=Kif1)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kg,
                                       row_id=row_id,
                                       value=Kg)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Km,
                                       row_id=row_id,
                                       value=Km)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Ku,
                                       row_id=row_id,
                                       value=Ku)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Ku1,
                                       row_id=row_id,
                                       value=Ku1)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.KST,
                                       row_id=row_id,
                                       value=KST)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Se1,
                                       row_id=row_id,
                                       value=Se1)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Se2,
                                       row_id=row_id,
                                       value=Se2)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Efd1,
                                       row_id=row_id,
                                       value=Efd1)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Efd2,
                                       row_id=row_id,
                                       value=Efd2)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Efdn,
                                       row_id=row_id,
                                       value=Efdn)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Ve1,
                                       row_id=row_id,
                                       value=Ve1)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Ve2,
                                       row_id=row_id,
                                       value=Ve2)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Aex,
                                       row_id=row_id,
                                       value=Aex)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Bex,
                                       row_id=row_id,
                                       value=Bex)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.SW1,
                                       row_id=row_id,
                                       value=SW1)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.SW2,
                                       row_id=row_id,
                                       value=SW2)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Vemin,
                                       row_id=row_id,
                                       value=Vemin)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Vrmax,
                                       row_id=row_id,
                                       value=Vrmax)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Vrmin,
                                       row_id=row_id,
                                       value=Vrmin)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Vfemax,
                                       row_id=row_id,
                                       value=Vfemax)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Vimax,
                                       row_id=row_id,
                                       value=Vimax)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Vimin,
                                       row_id=row_id,
                                       value=Vimin)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Vamax,
                                       row_id=row_id,
                                       value=Vamax)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Vamin,
                                       row_id=row_id,
                                       value=Vamin)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Vlv,
                                       row_id=row_id,
                                       value=Vlv)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Vmmax,
                                       row_id=row_id,
                                       value=Vmmax)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Vmmin,
                                       row_id=row_id,
                                       value=Vmmin)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Vhmax,
                                       row_id=row_id,
                                       value=Vhmax)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Vhmax,
                                       row_id=row_id,
                                       value=Vfelim)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.VBmax,
                                       row_id=row_id,
                                       value=VBmax)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.VGmax,
                                       row_id=row_id,
                                       value=VGmax)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.VfwMax,
                                       row_id=row_id,
                                       value=VfwMax)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.VfwMin,
                                       row_id=row_id,
                                       value=VfwMin)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Vlim1,
                                       row_id=row_id,
                                       value=Vlim1)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Vlim2,
                                       row_id=row_id,
                                       value=Vlim2)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.VpidMax,
                                       row_id=row_id,
                                       value=VpidMax)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.VpidMin,
                                       row_id=row_id,
                                       value=VpidMin)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Ilr,
                                       row_id=row_id,
                                       value=Ilr)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Theta,
                                       row_id=row_id,
                                       value=Theta)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Ifmax,
                                       row_id=row_id,
                                       value=Ifmax)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Ifth,
                                       row_id=row_id,
                                       value=Ifth)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.VB2max,
                                       row_id=row_id,
                                       value=VB2max)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Xl,
                                       row_id=row_id,
                                       value=Xl)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Rc,
                                       row_id=row_id,
                                       value=Rc)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Xc,
                                       row_id=row_id,
                                       value=Xc)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.TRFout,
                                       row_id=row_id,
                                       value=TRFout)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Samovozb,
                                       row_id=row_id,
                                       value=Samovozb)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.RPQlim,
                                       row_id=row_id,
                                       value=RPQlim)

    variable_.make_changes_filling_row(table=DFWIEEE421.table,
                                       column=DFWIEEE421.RIFlim,
                                       row_id=row_id,
                                       value=RIFlim)


if __name__ == '__main__':
    from RastrWinLib.AstraRastr import RASTR
    from RastrWinLib.Tables.Dynamic.DFWIEEE421 import DFWIEEE421
    from RastrWinLib.Load import load_file
    from RastrWinLib.Save import save_file

    load_file(rastr_win=RASTR,
              path_file=r'C:\Users\Ohrimenko_AG\Desktop\test_filling\test.rst',
              shabl='динамика')

    load_file(rastr_win=RASTR,
              path_file='',
              shabl='автоматика')

    table_ = RASTR.Tables(DFWIEEE421.table)

    for i in range(0, 1000):
        table_.AddRow()
        filling_DFWIEEE421(
            rastr_win=RASTR,
            row_id=i,
            sel=None,
            sta=None,
            Id=123456789,
            Name=f'Генератор {i}',
            ModelType=None,
            Brand=None,
            CustomModel=None,
            UELId=123456789,
            UELPos=None,
            OELId=123456789,
            OELPos=None,
            PSSId=123456789,
            PSSPos=None,
            Te=0.123465,
            Ta=0.123465,
            Tk=0.123465,
            Tm=0.123465,
            Tc=0.123465,
            Tc1=0.123465,
            Tc2=0.123465,
            Tb=0.123465,
            Tb1=0.123465,
            Tb2=0.123465,
            Trh=0.123465,
            Tdr=0.123465,
            Tf=0.123465,
            Tf2=0.123465,
            Tf3=0.123465,
            Tub1=0.123465,
            Tub2=0.123465,
            Tuc1=0.123465,
            Tob1=0.123465,
            Toc1=0.123465,
            Toc2=0.123465,
            Tob2=0.123465,
            Tr=0.123465,
            TINT=0.123465,
            Ke=0.123465,
            Ka=0.123465,
            Kia=0.123465,
            Kf=0.123465,
            Kf1=0.123465,
            Kf2=0.123465,
            Kof=0.123465,
            K1f=0.123465,
            Kfw=0.123465,
            Kv=0.123465,
            Kp=0.123465,
            Kpa=0.123465,
            Kpr=0.123465,
            Kir=0.123465,
            Kdr=0.123465,
            Kc=0.123465,
            Kc1=0.123465,
            Kc2=0.123465,
            Kcf=0.123465,
            Kd=0.123465,
            Kb=0.123465,
            Kh=0.123465,
            Khf=0.123465,
            Kr=0.123465,
            Kn=0.123465,
            Klv=0.123465,
            Kl=0.123465,
            Klr=0.123465,
            Klo=0.123465,
            Ki=0.123465,
            Ki2=0.123465,
            Kif=0.123465,
            Kif1=0.123465,
            Kg=0.123465,
            Km=0.123465,
            Ku=0.123465,
            Ku1=0.123465,
            KST=0.123465,
            Se1=0.123465,
            Se2=0.123465,
            Efd1=0.123465,
            Efd2=0.123465,
            Efdn=0.123465,
            Ve1=0.123465,
            Ve2=0.123465,
            Aex=0.123465,
            Bex=0.123465,
            SW1=0.123465,
            SW2=0.123465,
            Vemin=0.123465,
            Vrmax=0.123465,
            Vrmin=0.123465,
            Vfemax=0.123465,
            Vimax=0.123465,
            Vimin=0.123465,
            Vamax=0.123465,
            Vamin=0.123465,
            Vlv=0.123465,
            Vmmax=0.123465,
            Vmmin=0.123465,
            Vhmax=0.123465,
            Vfelim=0.123465,
            VBmax=0.123465,
            VGmax=0.123465,
            VfwMax=0.123465,
            VfwMin=0.123465,
            Vlim1=0.123465,
            Vlim2=0.123465,
            VpidMax=0.123465,
            VpidMin=0.123465,
            Ilr=0.123465,
            Theta=0.123465,
            Ifmax=0.123465,
            Ifth=0.123465,
            VB2max=0.123465,
            Xl=0.123465,
            Rc=0.123465,
            Xc=0.123465,
            TRFout=0.123465,
            Samovozb=0.123465,
            RPQlim=0.123465,
            RIFlim=0.123465,
            switch_command_line=False)

    save_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Desktop\test_filling\test234.rst',
              shabl=Shabl.shablon_file_dynamic)
