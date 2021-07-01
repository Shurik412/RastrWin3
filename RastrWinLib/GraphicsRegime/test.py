# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, request

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.calculation.regim import SteadyState
from RastrWinLib.getting.get import GettingParameter
from RastrWinLib.tables.Node.node import Node
from load_file_rastr import load_file_rgm


app = Flask(__name__)


@app.route('/')
def contact():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Do Something':
            pass  # do something
        elif request.form['submit_button'] == 'Do Something Else':
            pass  # do something else
        else:
            pass  # unknown
    elif request.method == 'GET':
        form='gett'
        return render_template('test.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
