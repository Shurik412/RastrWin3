# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "АРВ(ИД)" RastrWin3

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.Dynamic.ExcControl import ExcControl, ExcControlDescription
from RastrWinLib.variables.variable_parametrs import Variable


def filling_ExcControl(
        rastr_win=RASTR,
        row_id: int = None,
        sel: bool = None,
        sta: bool = None,
        Id: int = None,
        Name: str = None,
        ModelType: str = None,
        Brand: str = None,
        ForcerId: str = None,
        CustomModel: str = None,
        OELId: str = None,
        PSSId: str = None,
        UELId: str = None,
        Trv: float = None,
        Tf: float = None,
        T1f: float = None,
        T2f: float = None,
        T1f1: float = None,
        T2f1: float = None,
        T3f1: float = None,
        T1if: float = None,
        T1if1: float = None,
        T2if1: float = None,
        T1u: float = None,
        T1u1: float = None,
        T2u1: float = None,
        Tbch: float = None,
        TINT: float = None,
        Ku: float = None,
        Ku1: float = None,
        Kf: float = None,
        Kf1: float = None,
        Kif1: float = None,
        K_cosfi: float = None,
        K_Ia: float = None,
        K_Ir: float = None,
        K_P: float = None,
        K_Q: float = None,
        K_Usd: float = None,
        Kiu: float = None,
        Kpi: float = None,
        KST: float = None,
        Kuf: float = None,
        Urv_max: float = None,
        Urv_min: float = None,
        dEqdt: float = None,
        dVdt: float = None,
        Uarv: float = None,
        Udop1: float = None,
        U11: float = None,
        U22: float = None,
        Alpha: float = None,
        dSudt: float = None,
        deltaF: float = None,
        switch_command_line: bool = False):
    """

    :param row_id:
    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param sel:
    :param sta:
    :param Id:
    :param Name:
    :param ModelType:
    :param Brand:
    :param ForcerId:
    :param CustomModel:
    :param OELId:
    :param PSSId:
    :param UELId:
    :param Trv:
    :param Tf:
    :param T1f:
    :param T2f:
    :param T1f1:
    :param T2f1:
    :param T3f1:
    :param T1if:
    :param T1if1:
    :param T2if1:
    :param T1u:
    :param T1u1:
    :param T2u1:
    :param Tbch:
    :param TINT:
    :param Ku:
    :param Ku1:
    :param Kf:
    :param Kf1:
    :param Kif1:
    :param K_cosfi:
    :param K_Ia:
    :param K_Ir:
    :param K_P:
    :param K_Q:
    :param K_Usd:
    :param Kiu:
    :param Kpi:
    :param KST:
    :param Kuf:
    :param Urv_max:
    :param Urv_min:
    :param dEqdt:
    :param dVdt:
    :param Uarv:
    :param Udop1:
    :param U11:
    :param U22:
    :param Alpha:
    :param dSudt:
    :param deltaF:
    :param switch_command_line:
    :return:
    """
    variable_ = Variable(rastr_win=rastr_win)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.sel,
                               row_id=row_id,
                               value=sel)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.sta,
                               row_id=row_id,
                               value=sta)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.Id,
                               row_id=row_id,
                               value=Id)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.Name,
                               row_id=row_id,
                               value=Name)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.ModelType,
                               row_id=row_id,
                               value=ModelType)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.Brand,
                               row_id=row_id,
                               value=Brand)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.ForcerId,
                               row_id=row_id,
                               value=ForcerId)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.CustomModel,
                               row_id=row_id,
                               value=CustomModel)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.OELId,
                               row_id=row_id,
                               value=OELId)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.PSSId,
                               row_id=row_id,
                               value=PSSId)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.UELId,
                               row_id=row_id,
                               value=UELId)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.Trv,
                               row_id=row_id,
                               value=Trv)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.Tf,
                               row_id=row_id,
                               value=Tf)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.T1f,
                               row_id=row_id,
                               value=T1f)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.T2f,
                               row_id=row_id,
                               value=T2f)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.T1f1,
                               row_id=row_id,
                               value=T1f1)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.T2f1,
                               row_id=row_id,
                               value=T2f1)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.T3f1,
                               row_id=row_id,
                               value=T3f1)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.T1if,
                               row_id=row_id,
                               value=T1if)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.T1if1,
                               row_id=row_id,
                               value=T1if1)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.T2if1,
                               row_id=row_id,
                               value=T2if1)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.T1u,
                               row_id=row_id,
                               value=T1u)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.T1u1,
                               row_id=row_id,
                               value=T1u1)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.T2u1,
                               row_id=row_id,
                               value=T2u1)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.Tbch,
                               row_id=row_id,
                               value=Tbch)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.TINT,
                               row_id=row_id,
                               value=TINT)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.Ku,
                               row_id=row_id,
                               value=Ku)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.Ku1,
                               row_id=row_id,
                               value=Ku1)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.Kf,
                               row_id=row_id,
                               value=Kf)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.Kf1,
                               row_id=row_id,
                               value=Kf1)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.Kif1,
                               row_id=row_id,
                               value=Kif1)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.K_cosfi,
                               row_id=row_id,
                               value=K_cosfi)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.K_Ia,
                               row_id=row_id,
                               value=K_Ia)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.K_Ir,
                               row_id=row_id,
                               value=K_Ir)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.K_P,
                               row_id=row_id,
                               value=K_P)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.K_Q,
                               row_id=row_id,
                               value=K_Q)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.K_Usd,
                               row_id=row_id,
                               value=K_Usd)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.Kiu,
                               row_id=row_id,
                               value=Kiu)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.Kpi,
                               row_id=row_id,
                               value=Kpi)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.KST,
                               row_id=row_id,
                               value=KST)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.Kuf,
                               row_id=row_id,
                               value=Kuf)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.Urv_max,
                               row_id=row_id,
                               value=Urv_max)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.Urv_min,
                               row_id=row_id,
                               value=Urv_min)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.dEqdt,
                               row_id=row_id,
                               value=dEqdt)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.dVdt,
                               row_id=row_id,
                               value=dVdt)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.Uarv,
                               row_id=row_id,
                               value=Uarv)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.Udop1,
                               row_id=row_id,
                               value=Udop1)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.U11,
                               row_id=row_id,
                               value=U11)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.U22,
                               row_id=row_id,
                               value=U22)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.Alpha,
                               row_id=row_id,
                               value=Alpha)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.dSudt,
                               row_id=row_id,
                               value=dSudt)

    variable_.make_changes_row(table=ExcControl.table,
                               column=ExcControl.deltaF,
                               row_id=row_id,
                               value=deltaF)
