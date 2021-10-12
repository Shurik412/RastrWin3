# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, request

from RastrWinLib.Calculation.regim import SteadyState
from RastrWinLib.Getting.get import GettingParameter
from RastrWinLib.tables.Node.node import Node
from load_file_rastr import load_file_rgm
from RastrWinLib.AstraRastr import RASTR

get_object = GettingParameter(rastr_win=RASTR)
rgm_object = SteadyState(rastr_win=RASTR, switch_command_line=True)

load_file_rgm()

app = Flask(__name__)


@app.route('/')
def index():
    u_kalininska_aes = get_object.get_cell_param(table=Node.table,
                                                 column=Node.vras,
                                                 key='ny=51700101')
    regime()
    bootloader()
    return render_template("GrafRegimCentr.v.2.2.html", u_kalininska_aes='%.0f' % u_kalininska_aes)


@app.route("/", methods=['GET', 'POST'])
def regime():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('regime') == 'regime':
            # pass
            print("regime")
        else:
            # pass # unknown
            return render_template("GrafRegimCentr.v.2.2.html")
    elif request.method == 'GET':
        rgm_object.rgm()
    return render_template("GrafRegimCentr.v.2.2.html")


@app.route("/", methods=['GET', 'POST'])
def bootloader():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('bootloader') == 'bootloader':
            # pass
            print("bootloader")
        else:
            # pass # unknown
            return render_template("GrafRegimCentr.v.2.2.html")
    elif request.method == 'GET':
        load_file_rgm()
    return render_template("GrafRegimCentr.v.2.2.html")


if __name__ == '__main__':
    app.run(debug=True)
