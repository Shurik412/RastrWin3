# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "Возбудитель (ИД)" RastrWin3

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.Dynamic.DFWIEEE421 import DFWIEEE421, DFWIEEE421_Description
from RastrWinLib.variables.variable_parametrs import Variable


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
        UELId: str = None,
        UELPos: str = None,
        OELId: str = None,
        OELPos: str = None,
        PSSId: str = None,
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

    :param rastr_win:
    :param row_id:
    :param sel:
    :param sta:
    :param Id:
    :param Name:
    :param ModelType:
    :param Brand:
    :param CustomModel:
    :param UELId:
    :param UELPos:
    :param OELId:
    :param OELPos:
    :param PSSId:
    :param PSSPos:
    :param Te:
    :param Ta:
    :param Tk:
    :param Tj:
    :param Th:
    :param Tm:
    :param Tc:
    :param Tc1:
    :param Tc2:
    :param Tb:
    :param Tb1:
    :param Tb2:
    :param Trh:
    :param Tdr:
    :param Tf:
    :param Tf2:
    :param Tf3:
    :param Tub1:
    :param Tub2:
    :param Tuc1:
    :param Tob1:
    :param Toc1:
    :param Toc2:
    :param Tob2:
    :param Tr:
    :param TINT:
    :param Ke:
    :param Ka:
    :param Kia:
    :param Kf:
    :param Kf1:
    :param Kf2:
    :param Kof:
    :param K1f:
    :param Kfw:
    :param Kv:
    :param Kp:
    :param Kpa:
    :param Kpr:
    :param Kir:
    :param Kdr:
    :param Kc:
    :param Kc1:
    :param Kc2:
    :param Kcf:
    :param Kd:
    :param Kb:
    :param Kh:
    :param Khf:
    :param Kr:
    :param Kn:
    :param Klv:
    :param Kl:
    :param Klr:
    :param Klo:
    :param Ki:
    :param Ki2:
    :param Kif:
    :param Kif1:
    :param Kg:
    :param Km:
    :param Ku:
    :param Ku1:
    :param KST:
    :param Se1:
    :param Se2:
    :param Efd1:
    :param Efd2:
    :param Efdn:
    :param Ve1:
    :param Ve2:
    :param Aex:
    :param Bex:
    :param SW1:
    :param SW2:
    :param Vemin:
    :param Vrmax:
    :param Vrmin:
    :param Vfemax:
    :param Vimax:
    :param Vimin:
    :param Vamax:
    :param Vamin:
    :param Vlv:
    :param Vmmax:
    :param Vmmin:
    :param Vhmax:
    :param Vfelim:
    :param VBmax:
    :param VGmax:
    :param VfwMax:
    :param VfwMin:
    :param Vlim1:
    :param Vlim2:
    :param VpidMax:
    :param VpidMin:
    :param Ilr:
    :param Theta:
    :param Ifmax:
    :param Ifth:
    :param VB2max:
    :param Xl:
    :param Rc:
    :param Xc:
    :param TRFout:
    :param Samovozb:
    :param RPQlim:
    :param RIFlim:
    :param switch_command_line:
    :return:
    """
    variable_ = Variable(rastr_win=rastr_win)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.sel,
                               row_id=row_id,
                               value=sel)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.sta,
                               row_id=row_id,
                               value=sta)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Id,
                               row_id=row_id,
                               value=Id)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Name,
                               row_id=row_id,
                               value=Name)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.ModelType,
                               row_id=row_id,
                               value=ModelType)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Brand,
                               row_id=row_id,
                               value=Brand)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.CustomModel,
                               row_id=row_id,
                               value=CustomModel)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.UELId,
                               row_id=row_id,
                               value=UELId)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.UELPos,
                               row_id=row_id,
                               value=UELPos)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.OELId,
                               row_id=row_id,
                               value=OELId)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.OELPos,
                               row_id=row_id,
                               value=OELPos)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.PSSId,
                               row_id=row_id,
                               value=PSSId)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.PSSPos,
                               row_id=row_id,
                               value=PSSPos)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Te,
                               row_id=row_id,
                               value=Te)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Ta,
                               row_id=row_id,
                               value=Ta)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Tk,
                               row_id=row_id,
                               value=Tk)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Tj,
                               row_id=row_id,
                               value=Tj)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Th,
                               row_id=row_id,
                               value=Th)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Tm,
                               row_id=row_id,
                               value=Tm)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Tc,
                               row_id=row_id,
                               value=Tc)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Tc1,
                               row_id=row_id,
                               value=Tc1)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Tc2,
                               row_id=row_id,
                               value=Tc2)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Tb,
                               row_id=row_id,
                               value=Tb)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Tb1,
                               row_id=row_id,
                               value=Tb1)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Tb2,
                               row_id=row_id,
                               value=Tb2)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Trh,
                               row_id=row_id,
                               value=Trh)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Tdr,
                               row_id=row_id,
                               value=Tdr)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Tf,
                               row_id=row_id,
                               value=Tf)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Tf2,
                               row_id=row_id,
                               value=Tf2)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Tf3,
                               row_id=row_id,
                               value=Tf3)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Tub1,
                               row_id=row_id,
                               value=Tub1)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Tub2,
                               row_id=row_id,
                               value=Tub2)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Tuc1,
                               row_id=row_id,
                               value=Tuc1)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Tob1,
                               row_id=row_id,
                               value=Tob1)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Toc1,
                               row_id=row_id,
                               value=Toc1)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Toc2,
                               row_id=row_id,
                               value=Toc2)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Tob2,
                               row_id=row_id,
                               value=Tob2)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Tr,
                               row_id=row_id,
                               value=Tr)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.TINT,
                               row_id=row_id,
                               value=TINT)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Ke,
                               row_id=row_id,
                               value=Ke)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Ka,
                               row_id=row_id,
                               value=Ka)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kia,
                               row_id=row_id,
                               value=Kia)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kf,
                               row_id=row_id,
                               value=Kf)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kf1,
                               row_id=row_id,
                               value=Kf1)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kf2,
                               row_id=row_id,
                               value=Kf2)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kof,
                               row_id=row_id,
                               value=Kof)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.K1f,
                               row_id=row_id,
                               value=K1f)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kfw,
                               row_id=row_id,
                               value=Kfw)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kv,
                               row_id=row_id,
                               value=Kv)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kp,
                               row_id=row_id,
                               value=Kp)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kpa,
                               row_id=row_id,
                               value=Kpa)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kpr,
                               row_id=row_id,
                               value=Kpr)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kir,
                               row_id=row_id,
                               value=Kir)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kpa,
                               row_id=row_id,
                               value=Kpa)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kpr,
                               row_id=row_id,
                               value=Kpr)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kir,
                               row_id=row_id,
                               value=Kir)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kdr,
                               row_id=row_id,
                               value=Kdr)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kc,
                               row_id=row_id,
                               value=Kc)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kc1,
                               row_id=row_id,
                               value=Kc1)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kc2,
                               row_id=row_id,
                               value=Kc2)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kcf,
                               row_id=row_id,
                               value=Kcf)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kd,
                               row_id=row_id,
                               value=Kd)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kb,
                               row_id=row_id,
                               value=Kb)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kh,
                               row_id=row_id,
                               value=Kh)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Khf,
                               row_id=row_id,
                               value=Khf)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kr,
                               row_id=row_id,
                               value=Kr)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kn,
                               row_id=row_id,
                               value=Kn)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Klv,
                               row_id=row_id,
                               value=Klv)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kl,
                               row_id=row_id,
                               value=Kl)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Klr,
                               row_id=row_id,
                               value=Klr)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Klo,
                               row_id=row_id,
                               value=Klo)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Ki,
                               row_id=row_id,
                               value=Ki)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Ki2,
                               row_id=row_id,
                               value=Ki2)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Klo,
                               row_id=row_id,
                               value=Klo)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Ki,
                               row_id=row_id,
                               value=Ki)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Ki2,
                               row_id=row_id,
                               value=Ki2)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kif,
                               row_id=row_id,
                               value=Kif)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kif1,
                               row_id=row_id,
                               value=Kif1)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Kg,
                               row_id=row_id,
                               value=Kg)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Km,
                               row_id=row_id,
                               value=Km)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Ku,
                               row_id=row_id,
                               value=Ku)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Ku1,
                               row_id=row_id,
                               value=Ku1)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.KST,
                               row_id=row_id,
                               value=KST)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Se1,
                               row_id=row_id,
                               value=Se1)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Se2,
                               row_id=row_id,
                               value=Se2)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Efd1,
                               row_id=row_id,
                               value=Efd1)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Efd2,
                               row_id=row_id,
                               value=Efd2)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Efdn,
                               row_id=row_id,
                               value=Efdn)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Ve1,
                               row_id=row_id,
                               value=Ve1)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Ve2,
                               row_id=row_id,
                               value=Ve2)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Aex,
                               row_id=row_id,
                               value=Aex)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Bex,
                               row_id=row_id,
                               value=Bex)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.SW1,
                               row_id=row_id,
                               value=SW1)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.SW2,
                               row_id=row_id,
                               value=SW2)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Vemin,
                               row_id=row_id,
                               value=Vemin)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Vrmax,
                               row_id=row_id,
                               value=Vrmax)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Vrmin,
                               row_id=row_id,
                               value=Vrmin)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Vfemax,
                               row_id=row_id,
                               value=Vfemax)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Vimax,
                               row_id=row_id,
                               value=Vimax)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Vimin,
                               row_id=row_id,
                               value=Vimin)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Vamax,
                               row_id=row_id,
                               value=Vamax)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Vamin,
                               row_id=row_id,
                               value=Vamin)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Vlv,
                               row_id=row_id,
                               value=Vlv)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Vmmax,
                               row_id=row_id,
                               value=Vmmax)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Vmmin,
                               row_id=row_id,
                               value=Vmmin)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Vhmax,
                               row_id=row_id,
                               value=Vhmax)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Vhmax,
                               row_id=row_id,
                               value=Vfelim)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.VBmax,
                               row_id=row_id,
                               value=VBmax)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.VGmax,
                               row_id=row_id,
                               value=VGmax)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.VfwMax,
                               row_id=row_id,
                               value=VfwMax)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.VfwMin,
                               row_id=row_id,
                               value=VfwMin)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Vlim1,
                               row_id=row_id,
                               value=Vlim1)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Vlim2,
                               row_id=row_id,
                               value=Vlim2)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.VpidMax,
                               row_id=row_id,
                               value=VpidMax)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.VpidMin,
                               row_id=row_id,
                               value=VpidMin)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Ilr,
                               row_id=row_id,
                               value=Ilr)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Theta,
                               row_id=row_id,
                               value=Theta)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Ifmax,
                               row_id=row_id,
                               value=Ifmax)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Ifth,
                               row_id=row_id,
                               value=Ifth)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.VB2max,
                               row_id=row_id,
                               value=VB2max)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Xl,
                               row_id=row_id,
                               value=Xl)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Rc,
                               row_id=row_id,
                               value=Rc)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Xc,
                               row_id=row_id,
                               value=Xc)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.TRFout,
                               row_id=row_id,
                               value=TRFout)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.Samovozb,
                               row_id=row_id,
                               value=Samovozb)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.RPQlim,
                               row_id=row_id,
                               value=RPQlim)

    variable_.make_changes_row(table=DFWIEEE421.table,
                               column=DFWIEEE421.RIFlim,
                               row_id=row_id,
                               value=RIFlim)
