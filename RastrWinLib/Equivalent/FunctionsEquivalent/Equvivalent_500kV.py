from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.getting.get import GettingParameter
from RastrWinLib.tables.Dynamic.Generator import Generator
from RastrWinLib.tables.Node.node import Node
from RastrWinLib.tables.Vetv.vetv import Vetv
from RastrWinLib.variables.variable_parametrs import FindNextSel
from RastrWinLib.variables.variable_parametrs import Variable


def equvivalent(viborka, u_min=430, u_max=580):
    vetv = RASTR.Tables(Vetv.table)
    variableObj = Variable(rastr_win=RASTR,
                           switch_command_line=False)

    getParamObj = GettingParameter(rastr_win=RASTR)

    findNextSelNodeObj = FindNextSel(rastr_win=RASTR,
                                     table=Node.table)

    findNextSelVetvObj = FindNextSel(rastr_win=RASTR,
                                     table=Vetv.table)

    findNextSelGenObj = FindNextSel(rastr_win=RASTR,
                                    table=Generator.table)

    j = findNextSelNodeObj.row(key=f'{viborka}')

    while j != (-1):
        ny = getParamObj.get_cell_row(table=Node.table,
                                      column=Node.ny,
                                      row_id=j)

        tip_node = getParamObj.get_cell_row(table=Node.table,
                                            column=Node.tip,
                                            row_id=j)

        # uhom = getParamObj.get_cell_row(table=Node.table,
        #                                 column=Node.uhom,
        #                                 row_id=j)

        if tip_node > 1:
            j_gen = findNextSelGenObj.row(key=f'{Generator.Node}.{Node.ny}={ny}')

            if j_gen != (-1):
                j_vetv = findNextSelVetvObj.row(key=f'({Vetv.ip}={ny})|({Vetv.iq}=ny)')

                while j_vetv != (-1):
                    tip_vetv = getParamObj.get_cell_row(table=Vetv.table,
                                                        column=Vetv.tip,
                                                        row_id=j_vetv)
                    if tip_vetv == 1:
                        v_ip = getParamObj.get_cell_row(table=Vetv.table,
                                                        column=Vetv.v_ip,
                                                        row_id=j_vetv)
                        v_iq = getParamObj.get_cell_row(table=Vetv.table,
                                                        column=Vetv.v_iq,
                                                        row_id=j_vetv)
                        if (v_ip > u_min and v_iq < u_max) or (v_ip < u_min and v_iq > u_max):
                            variableObj.make_changes_row(table=Node.table,
                                                         column=Node.sel,
                                                         row_id=j,
                                                         value=0)
                    j_vetv = vetv.FindNextSel(j_vetv)
            else:
                j_vetv_2 = findNextSelVetvObj.row(key=f'({Vetv.ip}={ny})|({Vetv.iq}={ny})')
                while j_vetv_2 != (-1):
                    tip_vetv_2 = getParamObj.get_cell_row(table=Vetv.table,
                                                          column=Vetv.tip,
                                                          row_id=j_vetv_2)
                    if tip_vetv_2 == 1:
                        v_ip_2 = getParamObj.get_cell_row(table=Vetv.table,
                                                          column=Vetv.v_ip,
                                                          row_id=j_vetv_2)

                        v_iq_2 = getParamObj.get_cell_row(table=Vetv.table,
                                                          column=Vetv.v_iq,
                                                          row_id=j_vetv_2)
                        if (v_ip_2 > u_min and v_iq_2 < u_max) or (v_ip_2 < u_min and v_iq_2 > u_max):
                            variableObj.make_changes_row(table=Node.table,
                                                         column=Node.sel,
                                                         row_id=j,
                                                         value=0)
                    j_vetv_2 = vetv.FindNextSel(j_vetv_2)

            j = findNextSelNodeObj.row(key=vyborka_gen)


def equivalent_gen(viborka):
    vetv = RASTR.Tables(Vetv.table)
    node = RASTR.Tables(Node.table)
    getObj = GettingParameter(rastr_win=RASTR)
    findNextSelNodeObj = FindNextSel(rastr_win=RASTR, table=Node.table)
    findNextSelGenObj = FindNextSel(rastr_win=RASTR, table=Generator.table)
    node.SetSel(viborka)
    node.Cols(Node.sel).Calc('1')
    j = findNextSelObj.row(key=viborka)
    while j != (-1):
        ny = getObj.get_cell_row(table=Node.table,
                                 column=Node.ny,
                                 row_id=j)

        tip_node = getObj.get_cell_row(table=Node.table,
                                       column=Node.tip,
                                       row_id=j)

        uhom = getObj.get_cell_row(table=Node.table,
                                   column=Node.uhom,
                                   row_id=j)

        if tip_node > 1:
            j_gen = findNextSelGenObj.row(key=f'{Node.table}.{Node.ny}={ny}')
            if j_gen != (-1):

