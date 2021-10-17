# -*- coding: utf-8 -*-
from openpyxl.chart import Reference, Series, ScatterChart


class ChartExcel:
    def __init__(self, work_sheet,
                 chart_obj=ScatterChart(),
                 chart_title='График',
                 x_axis_title='Ось Х', y_axis_title='Ось Y',
                 width_chart=15, height_chart=7.5,
                 switch_command_line=False):
        """
        Класс создания графика по двум осям XY

        :param work_sheet: рабочий лист;
        :param chart_obj: объект
        :param chart_title: название графика;
        :param x_axis_title: название оси Х;
        :param y_axis_title: название оси Y;
        :param width_chart: ширина графика;
        :param height_chart: высота графика;
        :param switch_command_line: True/False - вывод сообщений в протокол.
        """
        self.work_sheet = work_sheet
        self.chart_obj = chart_obj
        self.chart_obj.title = chart_title
        self.chart_obj.x_axis.title = x_axis_title
        self.chart_obj.y_axis.title = y_axis_title
        chart_obj.width = float(width_chart)
        chart_obj.height = float(height_chart)
        self.switch_command_line = switch_command_line
        if switch_command_line is not False:
            print(f'Создан объект графика с названием "{chart_title}", на листе {work_sheet}:')

    def add_line_chart(self,
                       min_col_x,
                       min_row_x,
                       max_row_x,
                       min_col_y,
                       min_row_y,
                       max_row_y,
                       title_from_data_ch=True,
                       title_ch=None,
                       width_line_pt=None):
        """
        Метод для добавления кривой в график.

        :param min_col_x: минмальная колонка (столбец) для оси Х;
        :param min_row_x: минмальная строка для оси Х;
        :param max_row_x: максимальный столбец для оси Х;
        :param min_col_y: минимальная колонка для оси Y;
        :param min_row_y: минимальная строка для оси Y;
        :param max_row_y: максимальная строка для оси Y;
        :param title_from_data_ch:
        :param title_ch: название графика;
        :param width_line_pt:
        :return:
        """

        if title_from_data_ch is not True:
            min_row_y = min_row_y + 1

        x_values = Reference(self.work_sheet,
                             min_col=min_col_x,
                             min_row=min_row_x,
                             max_row=max_row_x,
                             range_string=None)

        y_values = Reference(self.work_sheet,
                             min_col=min_col_y,
                             min_row=min_row_y,
                             max_row=max_row_y,
                             range_string=None)

        series_xy = Series(y_values,
                           x_values,
                           title_from_data=title_from_data_ch,
                           title=title_ch)

        if width_line_pt is not None:
            series_xy.graphicalProperties.line.width = 12700 * width_line_pt  # 12700 width in EMUs

        self.chart_obj.series.append(series_xy)

        if self.switch_command_line is not False:
            print(f'\t- добавлена линия (кривая) на график;')

    def print_chart(self, cell_print_chart='A10'):
        self.work_sheet.add_chart(self.chart_obj, cell_print_chart)
        if self.switch_command_line is not False:
            print(f'\t\t- график выведен на лист {self.work_sheet}, в ячейку {cell_print_chart}.')


class ChartExcelOtherSheet:
    """
    legend_position: позиция легенды на графике
        - r - справа, l - слева, t - сверху , b - снизу.
    """

    def __init__(self,
                 work_sheet,
                 work_book,
                 chart_obj=ScatterChart(),
                 chart_title='График',
                 x_axis_title='Ось Х', y_axis_title='Ось Y',
                 width_chart=15, height_chart=7.5,
                 legend_position='r',
                 x_axis_min=None, x_axis_max=None,
                 y_axis_min=None, y_axis_max=None,
                 switch_command_line=False):
        """

        :param work_sheet: рабочий лист;
        :param work_book: рабочая книга Excel;
        :param chart_obj: объект
        :param chart_title: название графика;
        :param x_axis_title: название оси Х;
        :param y_axis_title: название оси Y;
        :param width_chart: ширина графика;
        :param height_chart: высота графика;
        :param legend_position: расположение легенды на графике;
        :param x_axis_min: минимальная
        :param x_axis_max:
        :param y_axis_min:
        :param y_axis_max:
        :param switch_command_line: True/False - выводит сообщения в протокол;
        """
        self.work_book = work_book
        self.work_sheet = work_sheet
        self.chart_obj = chart_obj
        self.chart_obj.title = chart_title
        self.chart_obj.x_axis.title = x_axis_title
        self.chart_obj.y_axis.title = y_axis_title
        chart_obj.width = float(width_chart)
        chart_obj.height = float(height_chart)
        self.switch_command_line = switch_command_line
        self.chart_obj.legend.position = str(legend_position)
        self.chart_obj.x_axis.scaling.min = x_axis_min
        self.chart_obj.x_axis.scaling.max = x_axis_max
        self.chart_obj.y_axis.scaling.min = y_axis_min
        self.chart_obj.y_axis.scaling.max = y_axis_max

        if switch_command_line is not False:
            print(f'Создан объект графика с названием "{chart_title}", на листе {work_sheet}:')

    def add_line_chart(self,
                       min_col_x,
                       min_row_x,
                       max_row_x,
                       min_col_y,
                       min_row_y,
                       max_row_y,
                       work_sheet_other=None,
                       title_from_data_ch=True,
                       title_ch=None,
                       width_line_pt=None):
        """


        :param min_col_x: минимальная колонка X;
        :param min_row_x: минимальная строка Х;
        :param max_row_x: максимальная строка Х;
        :param min_col_y: минимальная колонка Y;
        :param min_row_y: минимальная строка Y;
        :param max_row_y: максимальная строка Y;
        :param work_sheet_other:  другой рабочий лист;
        :param title_from_data_ch:
        :param title_ch:
        :param width_line_pt:
        :return:
        """
        if work_sheet_other is None:
            work_sheet_other_ = self.work_sheet
        else:
            work_sheet_other_ = self.work_book[work_sheet_other]

        if title_from_data_ch is not True:
            min_row_y = min_row_y + 1

        x_values = Reference(worksheet=work_sheet_other_,
                             min_col=min_col_x,
                             min_row=min_row_x,
                             max_row=max_row_x,
                             range_string=None)

        y_values = Reference(worksheet=work_sheet_other_,
                             min_col=min_col_y,
                             min_row=min_row_y,
                             max_row=max_row_y,
                             range_string=None)

        series_xy = Series(y_values, x_values,
                           title_from_data=title_from_data_ch,
                           title=title_ch)

        # series_xy.graphicalProperties.line.solidFill = "00AAAA"
        # series_xy.graphicalProperties.line.dashStyle = "sysDot"
        if width_line_pt is not None:
            series_xy.graphicalProperties.line.width = 12700 * width_line_pt  # 12700 width in EMUs

        self.chart_obj.series.append(series_xy)

        if self.switch_command_line is not False:
            print(f'\t- добавлена линия (кривая) на график;')

    def print_chart(self, cell_print_chart='A10'):
        """

        :param cell_print_chart:
        :return:
        """
        self.work_sheet.add_chart(self.chart_obj, cell_print_chart)
        if self.switch_command_line is not False:
            print(f'\t\t- график выведен на лист {self.work_sheet}, в ячейку {cell_print_chart}.')
