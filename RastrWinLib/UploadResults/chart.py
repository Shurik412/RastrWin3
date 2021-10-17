# -*- coding: utf-8 -*-
from prettytable import PrettyTable

from RastrWinLib.ActionsObject.Variable import FindNextSelection
from RastrWinLib.AstraRastr import RASTR
import matplotlib.pyplot as plt
import numpy as np


class Plot:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlabel('Ось Х')
        self.ax.set_ylabel('Ось Y')
        self.ax.grid()

    def settings_plot(self, x, y):
        ax = plt.plot(x, y,
                      linestyle='-',
                      linewidth=4,
                      color='darkblue')

    def show_plot(self):
        plt.show()


if __name__ == '__main__':
    x = np.linspace(-5, 5, 100)
    y = 2 * x

    pl = Plot()
    pl.settings_plot(x, y)
    # pl.settings_plot(x * 1.05, y * 1.05)
    pl.show_plot()
