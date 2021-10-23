# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


class Plot:
    def __init__(self, title: str = 'График',
                 x_major_locator: int = 1, x_minor_locator: float = 0.5,
                 y_major_locator: int = 5, y_minor_locator: float = 2.5,
                 enable_axis_x_fission_regulation: bool = False,
                 enable_axis_y_fission_regulation: bool = False):
        """

        :param title:
        :param x_major_locator:
        :param x_minor_locator:
        :param y_major_locator:
        :param y_minor_locator:
        :param enable_axis_x_fission_regulation:
        :param enable_axis_y_fission_regulation:
        """
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlabel('Ось Х')
        self.ax.set_ylabel('Ось Y')
        self.ax.grid()
        if enable_axis_x_fission_regulation:
            #  Устанавливаем интервал основных делений:
            self.ax.xaxis.set_major_locator(ticker.MultipleLocator(x_major_locator))
            #  Устанавливаем интервал вспомогательных делений:
            self.ax.xaxis.set_minor_locator(ticker.MultipleLocator(x_minor_locator))

        if enable_axis_y_fission_regulation:
            self.ax.yaxis.set_major_locator(ticker.MultipleLocator(y_major_locator))
            self.ax.yaxis.set_minor_locator(ticker.MultipleLocator(y_minor_locator))
        self.ax.set_title(title)

    def settings_plot(self, axis_x, axis_y,
                      line_name_legend: str = 'Line1',
                      line_style: str = '-',
                      line_width: float = 3,
                      line_color: str = 'black'):
        """

        :param axis_x:
        :param axis_y:
        :param line_name_legend:
        :param line_style:
        :param line_width:
        :param line_color:
        :return:
        """
        self.ax = plt.plot(axis_x, axis_y,
                           linestyle=line_style,
                           linewidth=line_width,
                           color=line_color,
                           label=line_name_legend)
        plt.legend()

    def subplot(self, title_one: str, title_two: str,
                axis_x_one, axis_y_one,
                axis_x_two, axis_y_two):

        ax_1 = self.fig.add_subplot(1, 2, 1)
        ax_2 = self.fig.add_subplot(1, 2, 2)

        ax_1.set(title=title_one, xticks=axis_x_one, yticks=axis_y_one)
        ax_2.set(title=title_two, xticks=axis_x_two, yticks=axis_y_two)

    def show_plot(self):
        """

        :return:
        """
        plt.show()


if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    x_ = np.linspace(-5, 5, 100)
    y_ = 2 * x_
    #
    # pl = Plot()
    # # pl.settings_plot(axis_x=x_, axis_y=y_)
    # # pl.settings_plot(x_ * 1.05, y_ * 2.05, line_color='red', line_width=1.5, line_name_legend='line 2')
    #
    # pl.subplot(title_one='Ti1', title_two='Ti2',
    #            axis_x_one=x_, axis_y_one=y_,
    #            axis_x_two=x_, axis_y_two=y_)
    #
    # pl.show_plot()

    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib.cbook as cbook


    # create two subplots with the shared x and y axes
    fig, (ax1, ax2) = plt.subplots(1, 2)

    ax1.plot(x_, y_, lw=3)
    ax2.plot(x_, y_, lw=2)

    for ax in ax1, ax2:
        ax.grid(True)

    ax1.set_ylabel('price')
    ax2.set_ylabel('price')

    # for label in ax2.get_yticklabels():
    #     label.set_visible(False)

    fig.suptitle('Google (GOOG) daily closing price')
    fig.autofmt_xdate()
    plt.show()