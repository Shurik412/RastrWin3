# -*- coding: utf-8 -*-

from RastrWinLib.AstraRastr import RASTR, RastrDoc
from RastrWinLib.tables.Dynamic.Generator import Generator, GeneratorsDoc
from RastrWinLib.tools.tools import Tools
from RastrWinLib.variables.variable_parametrs import Variable


def filling_generators(
        rastr_win=RASTR,
        row_id=None,
        sta=None,
        Num=None,
        Name=None,
        Node=None,
        ModelType=None,
        Brand=None,
        NumBrand=None,
        ExciterId=None,
        ARSId=None,
        Pnom=None,
        Ugnom=None,
        cosFi=None,
        Demp=None,
        Mj=None,
        xd1=None,
        xd=None,
        xq=None,
        xd2=None,
        xq2=None,
        td01=None,
        td02=None,
        tq02=None,
        xq1=None,
        xl=None,
        x2=None,
        x0=None,
        tq01=None,
        switch_command_line=False
):
    f"""
    {GeneratorsDoc.name_table}
    :param row_id: {GeneratorsDoc.row_id};
    :param rastr_win: {RastrDoc};
    :param sta: {GeneratorsDoc.sta};
    :param Num: {GeneratorsDoc.Num};
    :param Name: {GeneratorsDoc.Name};
    :param Node: {GeneratorsDoc.Node};
    :param ModelType: {GeneratorsDoc.ModelType};
    :param Brand: {GeneratorsDoc.Brand};
    :param NumBrand: {GeneratorsDoc.NumBrand};
    :param ExciterId: {GeneratorsDoc.ExciterId};
    :param ARSId: {GeneratorsDoc.ARSId};
    :param Pnom: {GeneratorsDoc.Pnom};
    :param Ugnom: {GeneratorsDoc.Ugnom};
    :param cosFi: {GeneratorsDoc.cosFi};
    :param Demp: {GeneratorsDoc.Demp};
    :param Mj: {GeneratorsDoc.Mj};
    :param xd1: {GeneratorsDoc.xd1};
    :param xd: {GeneratorsDoc.xd};
    :param xq: {GeneratorsDoc.xq};
    :param xd2: {GeneratorsDoc.xd2};
    :param xq2: {GeneratorsDoc.xq2};
    :param td01: {GeneratorsDoc.td01};
    :param td02: {GeneratorsDoc.td02};
    :param tq02: {GeneratorsDoc.tq02};
    :param xq1: {GeneratorsDoc.xq1};
    :param xl: {GeneratorsDoc.xl};
    :param x2: {GeneratorsDoc.x2};
    :param x0: {GeneratorsDoc.x0};
    :param tq01: {GeneratorsDoc.tq01};
    :param switch_command_line: {Tools.switch_command_line_doc}
    :return: 
    """
    variable_ = Variable(rastr_win=rastr_win)

    # ModelType
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.ModelType,
                               row_id=row_id,
                               value=ModelType)
    # Ugnom
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.Ugnom,
                               row_id=row_id,
                               value=Ugnom)
    # cosFi
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.cosFi,
                               row_id=row_id,
                               value=cosFi)
    # Demp
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.Demp,
                               row_id=row_id,
                               value=Demp)
    # Mj
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.Mj,
                               row_id=row_id,
                               value=Mj)
    # xd1
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.xd1,
                               row_id=row_id,
                               value=xd1)
    # xd
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.xd,
                               row_id=row_id,
                               value=xd)
    # xq
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.xq,
                               row_id=row_id,
                               value=xq)
    # xd2
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.xd2,
                               row_id=row_id,
                               value=xd2)
    # xq2
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.xq2,
                               row_id=row_id,
                               value=xq2)
    # td01
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.td01,
                               row_id=row_id,
                               value=td01)
    # td02
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.td02,
                               row_id=row_id,
                               value=td02)
    # tq02
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.tq02,
                               row_id=row_id,
                               value=tq02)
    # xq1
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.xq1,
                               row_id=row_id,
                               value=xq1)
    # xl
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.xl,
                               row_id=row_id,
                               value=xl)
    # x2
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.x2,
                               row_id=row_id,
                               value=x2)
    # x0
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.x0,
                               row_id=row_id,
                               value=x0)
    # tq01
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.tq01,
                               row_id=row_id,
                               value=tq01)
