# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.Getting.get import GettingParameter
from RastrWinLib.Tables.Dynamic.Generator import Generator
from RastrWinLib.Tables.Node.node import Node
from RastrWinLib.Tables.Vetv.vetv import Vetv
from RastrWinLib.Variables.group_correction import GroupCorr
from RastrWinLib.Variables.variable_parametrs import Variable, FindNextSel


def delete_switches(viborka):
    node = RASTR.Tables(Node.table)
    vetv = RASTR.Tables(Vetv.table)
    generator = RASTR.Tables(Generator.table)

    groupCorrVetvGroupidObj = GroupCorr(rastr_win=RASTR,
                                        table=Vetv.table,
                                        column=Vetv.groupid)

    findNextSelNodeObj = FindNextSel(rastr_win=RASTR,
                                     table=Node.table)

    variableObj = Variable(rastr_win=RASTR,
                           switch_command_line=False)

    gettingParameterObj = GettingParameter(rastr_win=RASTR)

    node.SetSel(viborka)
    node.Cols(Node.sel).Calc("1")

    k = findNextSelNodeObj.row(key='iq.sel=1 & ip.sel=0 &!sta')
    while k != (-1):
        iq1 = gettingParameterObj.get_cell_row(table=Vetv.table,
                                               column=Vetv.iq,
                                               row_id=k)
        k2 = findNextSelNodeObj.row(key=f'{Node.ny}={iq1}')
        if k2 != (-1):
            variableObj.make_changes_row(table=Node.table,
                                         column=Node.sel,
                                         row_id=k2,
                                         value=0)
        k = vetv.FindNextSel(k)

    k = findNextSelNodeObj.row(key='iq.sel=0 & ip.sel=1 & !sta')
    while k != (-1):
        ip1 = gettingParameterObj.get_cell_row(table=Vetv.table,
                                               column=Vetv.ip,
                                               row_id=k)
        k2 = findNextSelNodeObj.row(key=f'{Node.ny}={ip1}')
        if k2 != (-1):
            variableObj.make_changes_row(table=Node.table,
                                         column=Node.sel,
                                         row_id=k2,
                                         value=0)
        k = vetv.FindNextSel(k)

    k = findNextSelNodeObj.row(key='(iq.sel=1 & ip.sel=0)|(ip.sel=1 & iq.sel=0) & tip=2')
    while k != (-1):
        iq1 = gettingParameterObj.get_cell_row(table=Vetv.table,
                                               column=Vetv.iq,
                                               row_id=k)
        k2 = findNextSelNodeObj.row(key=f'{Node.ny}={iq1}')
        if k2 != (-1):
            variableObj.make_changes_row(table=Node.table,
                                         column=Node.sel,
                                         row_id=k2,
                                         value=0)
        ip1 = gettingParameterObj.get_cell_row(table=Vetv.table,
                                               column=Vetv.ip,
                                               row_id=k2)
        k2 = findNextSelNodeObj.row(key=f'{Node.ny}={ip1}')
        if k2 != (-1):
            variableObj.make_changes_row(table=Node.table,
                                         column=Node.sel,
                                         row_id=k2,
                                         value=0)

        k = findNextSelNodeObj.row(key='(iq.sel=1 &ip.sel=0) | (ip.sel=1 &iq.sel=0) & tip=2')

    viborka_in_bsh = '(iq.bsh>0 & ip.bsh=0) | (ip.bsh>0 & iq.bsh=0) | (iq.bshr>0 & ip.bshr=0) | (ip.bshr>0 & iq.bshr=0)| ip.sel=0 | iq.sel=0)'

    groupCorrVetvGroupidObj.calc(key='1',
                                 formula='0')

    groupCorrVetvGroupidObj.calc(key=viborka_in_bsh,
                                 formula='1')
    nvet = 0
    flvykl = 0
    for povet in range(0, 10000):
        ivet = findNextSelNodeObj.row(
            key='x<0.01 & x>-0.01 & r<0.005 & r>=0 & (ktr=0 | ktr=1) & !sta & groupid!=1 & b<0.000005')
        if ivet == -1:
            break
        ip = gettingParameterObj.get_cell_row(table=Vetv.table,
                                              column=Vetv.ip,
                                              row_id=ivet)
        iq = gettingParameterObj.get_cell_row(table=Vetv.table,
                                              column=Vetv.iq,
                                              row_id=ivet)

        if ip > iq:
            ny = iq
            ndel = ip
        else:
            ny = ip
            ndel = iq

        ndny = 0
        ndndel = 0



