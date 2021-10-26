from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.operation.Get import GettingParameter
from RastrWinLib.Tables.Dynamic.Generator import Generator
from RastrWinLib.Tables.Node.node import Node
from RastrWinLib.Tables.Vetv.vetv import Vetv
from RastrWinLib.operation.Variable import FindNextSel, FindNextSel_ROW
from RastrWinLib.operation.Variable import Variable
from RastrWinLib.operation.Selection import selection


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


def equivalent_gen(viborka, u_min=170, u_max=250):
    vetv = RASTR.Tables(Vetv.table)
    node = RASTR.Tables(Node.table)
    getObj = GettingParameter(rastr_win=RASTR)
    varObj = Variable(rastr_win=RASTR)
    findNextSelNodeObj = FindNextSel(rastr_win=RASTR, table=Node.table)
    findNextSelGenObj = FindNextSel(rastr_win=RASTR, table=Generator.table)
    findNextSelVetvObj = FindNextSel(rastr_win=RASTR, table=Vetv.table)
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
                j_vetv = findNextSelVetvObj.row(key=f'({Vetv.ip}={ny})|({Vetv.iq}={ny})')
                while j_vetv != (-1):
                    tip_vetv = getObj.get_cell_row(table=Vetv.table,
                                                   column=Vetv.tip,
                                                   row_id=j_vetv)
                    if tip_vetv == 1:
                        v_ip = getObj.get_cell_row(table=Vetv.table,
                                                   column=Vetv.v_ip,
                                                   row_id=j_vetv)
                        v_iq = getObj.get_cell_row(table=Vetv.table,
                                                   column=Vetv.v_iq,
                                                   row_id=j_vetv)
                        if (v_ip > u_min and v_iq < u_max) or (v_ip < u_min and v_iq > u_max):
                            varObj.make_changes_row(table=Node.table, column=Node.sel, row_id=j, value=0)
                    j_vetv = vetv.FindNextSel(j_vetv)
            else:
                j_vetv_2 = findNextSelVetvObj.row(key=f'({Vetv.ip}={ny})|({Vetv.iq}={ny})')
                while j_vetv_2 != (-1):
                    tip_vetv_2 = getObj.get_cell_row(table=Vetv.table,
                                                     column=Vetv.tip,
                                                     row_id=j_vetv_2)
                    if tip_vetv_2 == 1:
                        v_ip_2 = getObj.get_cell_row(table=Vetv.table,
                                                     column=Vetv.v_ip,
                                                     row_id=j_vetv_2)

                        v_iq_2 = getObj.get_cell_row(table=Vetv.table,
                                                     column=Vetv.v_iq,
                                                     row_id=j_vetv_2)

                        if (v_ip_2 > u_min and v_iq_2 < u_max) or (v_ip_2 < u_min and v_iq_2 > u_max):
                            varObj.make_changes_row(table=Node.table,
                                                    column=Node.sel,
                                                    row_id=j,
                                                    value=0)

                    j_vetv_2 = vetv.FindNextSel(j_vetv_2)

            node.SetSel(viborka)
            j = node.FindNextSel(j)


def delete_generation_switch():
    findNextSelNode = FindNextSel(table=Node.table,
                                  rastr_win=RASTR)
    findNextSelNodeROW = FindNextSel_ROW(rastr_win=RASTR,
                                         table=Node.table)
    findNextSelGen = FindNextSel(table=Generator.table,
                                 rastr_win=RASTR)
    findNextSelGenROW = FindNextSel_ROW(rastr_win=RASTR,
                                        table=Generator.table)
    vetv = RASTR.Tables(Vetv.table)
    gen = RASTR.Tables(Generator.table)
    selection(switch_command_line=True)
    getObj = GettingParameter(rastr_win=RASTR)
    variableObj = Variable(rastr_win=RASTR)
    k1 = findNextSelNode.row(key='')

    while k1 != (-1):
        ny1 = getObj.get_cell_row(table=Node.table,
                                  column=Node.ny,
                                  row_id=k1)

        vetv.SetSel(f'({Vetv.ip}={ny1})|({Vetv.iq}={ny1})')

        if vetv.Count == 1:
            vetv.SetSel(f"x<1 & (tip=0 | tip=2) & ((ip={ny1})|(iq={ny1}))")
            if vetv.Count == 1:
                vetv.SetSel(f'x<1 & (tip=0 | tip=2) & ((ip={ny1})|(iq={ny1}))')
                k3 = vetv.FindNextSel(-1)
                if k3 != (-1):
                    ip_k3 = getObj.get_cell_row(table=Vetv.table,
                                                column=Vetv.ip,
                                                row_id=k3)
                    if ip_k3 == ny1:
                        ny2 = getObj.get_cell_row(table=Vetv.table,
                                                  column=Vetv.iq,
                                                  row_id=k3)
                    else:
                        ny2 = getObj.get_cell_row(table=Vetv.table,
                                                  column=Vetv.ip,
                                                  row_id=k3)

                    k2 = findNextSelGen.row(key=f'{Generator.Node}={ny1}')
                    if k2 != (-1):
                        k4 = findNextSelNode.row(key=f'{Node}={ny1}')

                        if k4 != (-1):
                            pn_k1 = getObj.get_cell_row(table=Node.table,
                                                        column=Node.pn,
                                                        row_id=k1)

                            variableObj.make_changes_row(table=Node.table,
                                                         column=Node.pn,
                                                         row_id=k4,
                                                         value=(pn_k1 + pn_k1))

                            qn_k1 = getObj.get_cell_row(table=Node.table,
                                                        column=Node.qn,
                                                        row_id=k1)
                            variableObj.make_changes_row(table=Node.table,
                                                         column=Node.qn,
                                                         row_id=k4,
                                                         value=(qn_k1 + qn_k1))

                            vzd_k1 = getObj.get_cell_row(table=Node.table,
                                                         column=Node.vzd,
                                                         row_id=k1)
                            variableObj.make_changes_row(table=Node.table,
                                                         column=Node.vzd,
                                                         row_id=k4,
                                                         value=vzd_k1)

                            exist_load_k1 = getObj.get_cell_row(table=Node.table,
                                                                column=Node.exist_load,
                                                                row_id=k1)
                            variableObj.make_changes_row(table=Node.table,
                                                         column=Node.exist_load,
                                                         row_id=k4,
                                                         value=exist_load_k1)

                            exist_gen_k1 = getObj.get_cell_row(table=Node.table,
                                                               column=Node.exist_gen,
                                                               row_id=k1)
                            variableObj.make_changes_row(table=Node.table,
                                                         column=Node.exist_gen,
                                                         row_id=k4,
                                                         value=exist_gen_k1)

                            pn_max_k1 = getObj.get_cell_row(table=Node.table,
                                                            column=Node.pn_max,
                                                            row_id=k1)
                            pn_max_k4 = getObj.get_cell_row(table=Node.table,
                                                            column=Node.pn_max,
                                                            row_id=k4)
                            variableObj.make_changes_row(table=Node.table,
                                                         column=Node.pn_max,
                                                         row_id=k4,
                                                         value=pn_max_k1 + pn_max_k4)

                            if pn_max_k4 >= pn_max_k1:
                                pn_min_k1 = getObj.get_cell_row(table=Node.table,
                                                                column=Node.pn_min,
                                                                row_id=k1)

                                variableObj.make_changes_row(table=Node.table,
                                                             column=Node.pn_min,
                                                             row_id=k4,
                                                             value=pn_min_k1)

                            variableObj.make_changes_row(table=Node.table,
                                                         column=Node.sel,
                                                         row_id=k1,
                                                         value=1)

                            variableObj.make_changes_row(table=Vetv.table,
                                                         column=Vetv.sel,
                                                         row_id=k3,
                                                         value=1)
                            k2 = findNextSelGen.row(key=f'{Generator.Node}={ny}')
                            while k2 != (-1):
                                variableObj.make_changes_row(table=Generator.table,
                                                             column=Generator.Node,
                                                             row_id=k2,
                                                             value=ny2)
                                k2 = gen.FindNextSel(k2)

        k1 = findNextSelNodeROW.row(key='',
                                    row_=k1)
