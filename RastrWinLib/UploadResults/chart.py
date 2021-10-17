# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


class Plot:
    def __init__(self, title: str = 'График'):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlabel('Ось Х')
        self.ax.set_ylabel('Ось Y')
        self.ax.grid()
        #  Устанавливаем интервал основных делений:
        self.ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
        #  Устанавливаем интервал вспомогательных делений:
        self.ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
        #  Тоже самое проделываем с делениями на оси "y":
        self.ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
        self.ax.yaxis.set_minor_locator(ticker.MultipleLocator(2.5))
        self.ax.set_title(title)

    def settings_plot(self, axis_x, axis_y,
                      line_name_legend: str = 'Line1',
                      line_style: str = '-',
                      line_width: float = 3,
                      line_color: str = 'black'):
        self.ax = plt.plot(axis_x, axis_y,
                           linestyle=line_style,
                           linewidth=line_width,
                           color=line_color,
                           label=line_name_legend)
        plt.legend()

    def show_plot(self):
        plt.show()


if __name__ == '__main__':
    import numpy as np

    x_ = np.linspace(-5, 5, 100)
    y_ = 2 * x_

    pl = Plot()
    pl.settings_plot(axis_x=x_, axis_y=y_)
    pl.settings_plot(x_ * 1.05, y_ * 2.05, line_color='red', line_width=1.5, line_name_legend='line 2')
    pl.show_plot()
