# -*- coding: utf-8 -*-
#
#
#

node_table = 'node'
node_attributes_list = ['sel', 'sta', 'tip', 'ny', 'name', 'uhom', 'na', ]
node_attributes_dict = {'sel': 'sel'}
node_attributes = {
    'sel': '"О" Отметка узла',
    'sta': '"S" Состояние узла',
    'tip': '"Тип" Тип узла',
    'ny': '"Номер" Номер узла',
    'name': '"Название" Название узла',
    'uhom': '"U_ном" Номинальное напряжение',
}

vetv_table = 'vetv'
vetv_attributes_list = ['sel', 'sta', 'tip', 'ip', 'iq', 'name', 'na', ]
vetv_attributes = {
    'sel': '"О" Отметка ветви',
    'sta': '"S" Состояние ветви',
    'tip': '"Тип" Тип ветви',
    'ip': '"N_нач" Номер начала',
    'iq': '"N_кон" Номер конца',
    'name': '"Название" Название ветви'
}

generator_table = 'Generator'
generator_attributes_list = ['sel', 'sta', 'Num', 'Name', 'Node', 'P', 'Q', ]
generator_attributes = {
    'sel': '"О" Отметка генератора',
    'sta': '"S" Состояние генератора',
    'Num': '"N агр" Номер генератора',
    'Name': '"Название" Название генератора',
    'Node': '"N узла" Номер узла'
}

com_cxema_table = 'com_cxema'
com_cxema_attributes_list = ['ny', 'nv', 'na', 'ny_o', 'nv_o', 'nby', 'ngen', 'ntran', 'nlep', 'nvikl', 'pg', 'pn',
                             'dp', 'pby', 'dpsh', 'dv_min', 'dv_max', 'nt_max', 'max_it', 'nl_nax', 'max_il', ]
com_cxema_attributes = {
    'ny': 'Узлов: (Ny)',
    'nv': 'Ветвей: (Nv)',
    'na': 'Районов: (Na)',
    'ny_o': 'Число отключенных узлов: (Ny_откл)',
    'nv_o': 'Число отключенных ветвей: (Nv_откл)',
    'nby': 'Число балансир. узлов : (N_бу)',
    'ngen': 'Число узлов с заданн. V: (N_ген)',
    'ntran': 'Число трансформаторов : (N_Тр)',
    'nlep': 'Число ЛЭП : (N_ЛЭП)',
    'nvikl': 'Число выключателей : (N_выкл.)',
    'pg': 'P_ген: (Pg)',
    'pn': 'P_наг: (Pn)',
    'dp': 'Потери P (переменные): (dP)',
    'pby': 'P_баланс. узла: (P_бу)',
    'dpsh': 'Постоянные Потери : (dP_пост)',
    'dv_min': 'Минимальное отклонение V (%) (dV_min)',
    'dv_max': 'Максимальное отклонение V (%) (dV_max)',
    'nt_max': 'Число перегруженных тр-ров (по I_доп) (I_тр)',
    'max_it': 'Макс загрузка по току ТР (%) (I/I_доп-тр)',
    'nl_nax': 'Число перегруженных ЛЭП (по I_доп) (I_лэп)',
    'max_il': 'Макс загрузка по току ЛЭП (%) (I/I_доп-лэп)'
}

com_ekviv_table = 'com_ekviv'
com_ekviv_attributes_list = ['selekv', 'met_ekv', 'tip_ekv', 'ekvgen', 'tip_gen', 'kfc_x', 'pot_gen', 'kpn', 'tip_sxn',
                             'smart', 'zmax', 'otm_n', ]
com_ekviv_attributes = {
    'selekv': 'Отмеченные узлы: (Отмеч)',
    'met_ekv': 'Метод эквивалентирования (Мет Экв)',
    'tip_ekv': 'Тип эквивалентирования (Тип Экв)',
    'ekvgen': 'Эквивалент узлов с фикс V (фиксV)',
    'tip_gen': 'Тип эквивалентирования генераторов (Тип Ген)',
    'kfc_x': 'Коэффициент для Xg_ген (К_X_ Ген)',
    'pot_gen': 'Учет потерь при разносе генерации: (dP_Ген)',
    'kpn': 'Доля нагрузки, пересчитываемая в шунт (d_наг)',
    'tip_sxn': 'Учитывать СХН при эквивалентировании (СХН)',
    'smart': '"Умное" эквивалентирование : (Smart)',
    'zmax': 'Удаление ветвей с сопротивлением большим: (Z_max)',
    'otm_n': 'Отмечать узлы после эквивалентирования (Отм)',
}

com_regim_table = 'com_regim'
com_regim_attributes_list = ['neb_p', 'it_max', 'start', 'flot', 'dv_min', 'dv_max', 'dd_max', 'status', 'rr', 'wt',
                             'gen_p', 'method', 'method_ogr', 'print_mode', 'qmax', 'min_x', 'calc_tr', 'nag_p',
                             'rem_breaker', 'gram', 'ctrl_baza', 'itz', 'itz_ogr_max', 'itz_ogr_min',
                             'min_nodes_in_island', ]
com_regim_attributes = {
    'neb_p': 'Точность расчета (dP)',
    'it_max': 'Максимальное число итераций (It)',
    'start': 'Стартовый алгоритм (Start)',
    'flot': 'Плоский старт (Пл.старт)',
    'dv_min': 'Мин. допустимое снижение V (dV-)',
    'dv_max': 'Макс. допустимое превышение V (dV+)',
    'dd_max': 'Макс. допустимый угол по связи (dDelta)',
    'status': 'Состояние расчета режима (Статус)',
    'rr': 'Учет частоты: (W)',
    'wt': 'Отклонение частоты (dF)',
    'gen_p': 'Пересчитывать P/Q узла по P ген (Ген->P)',
    'method': 'Метод Расчета (Метод)',
    'method_ogr': 'Метод учета ограничений Q (Метод учета ограничений Q)',
    'print_mode': 'Уровень печати (Печать)',
    'qmax': 'Точный метод расчета Qmax (Qmax)',
    'min_x': 'Сопротивление выключателя (ое на 10-6) (Min_X)',
    'calc_tr': 'Пересчет АТ/3х обм. трансформаторов (Транс.)',
    'nag_p': 'Пересчитывать (P/Q) нагрузки узла по ВРДО (Наг->P)',
    'rem_breaker': 'Удаление выключателей из схемы: (Выкл)',
    'gram': 'Пересчет мощности генератора по ГРАМ: (Грам)',
    'ctrl_baza': 'Автоматическое создание БУ (БУ)',
    'itz': 'Стартовый метод: число итераций (Z_it)',
    'itz_ogr_max': 'Стартовый метод: Учет Qmax с итерации (Z_it_max)',
    'itz_ogr_min': 'Стартовый метод: Учет Qmin с итерации (Z_it_min)',
    'min_nodes_in_island': 'Минимальное число узлов в острове (Min_nodes)'
}

com_dynamics_table = 'com_dynamics'
com_dynamics_attributes_list = ['Tras', 'Hint', 'Hmin', 'Hmax', 'Hout', 'Mint', 'SMint', 'IntEpsilon',
                                'InformOnStepChange', 'Tf', 'dEf', 'Npf', 'Valid', 'dempfrec', 'corrT', 'IsDemp',
                                'frSXNtoY', 'SXNTolerance', 'SnapPath', 'MaxResultFiles', 'SnapTemplate',
                                'SnapAutoLoad', 'SnapMaxCount', 'TripGeneratorOnSpeed', 'PickupDropout', 'RealtimeCSV',
                                'PeriodAngle', 'ResultFlowDirection', 'TreatWarningsAsErrors', 'EventProcess', ]
com_dynamics_attributes = {
    'Tras': 'Время расчета (Tras)',
    'Hint': 'Начальный шаг интегрирования (H_инт)',
    'Hmin': 'Минимальный шаг интегрирования (H_мин)',
    'Hmax': 'Максимальный шаг интегрирования (H_макс)',
    'Hout': 'Шаг печати (H_печ)',
    'Mint': 'Основной метод интегрирования (Осн.Метод)',
    'SMint': 'Стартовый метод интегрирования (Старт.Метод)',
    'IntEpsilon': 'Точность шага интегрирования (dInt)',
    'InformOnStepChange': 'Информировать об изменении шага (Выводить шаг)',
    'Tf': 'Постоянная сглаживания угловой скорости (частоты) узла (Tf)',
    'dEf': 'Точность балансировки эдс при учете явнополюсности (dEf)',
    'Npf': 'Макс число пересчетов УР на шаге при учете явнополюсности (Ит)',
    'Valid': 'Контроль входных параметров (Контр.)',
    'dempfrec': 'Демпфирование в уравнениях движения (Демпф)',
    'corrT': 'Корректировать Т в парковских моделях (Корр Т)',
    'IsDemp': 'Учет демп. момента в моделях с демп контурами (Уч Демп)',
    'frSXNtoY': 'Напряжения перехода с СХН на шунт (V_минСХРН)',
    'SXNTolerance': 'Допустимый небаланс СХН (SXNTol)',
    'SnapPath': 'Выходной каталог файлов результатов (Кат. результатов)',
    'MaxResultFiles': 'Максимальное кол-во файлов результатов (Макс. файлов)',
    'SnapTemplate': 'Шаблон имени выходного файла (Шаблон имени)',
    'SnapAutoLoad': 'Автозагрузка последнего результата (Автозагрузка)',
    'SnapMaxCount': 'Максимальное кол-во слотов результатов (Макс. рез-тов)',
    'TripGeneratorOnSpeed': 'Отключать генератор при превышении скорости % (Уставка автоматов безопасности)',
    'PickupDropout': 'Информировать о пуске/возврате автоматики (Информировать о пуске/возврате автоматики)',
    'RealtimeCSV': 'Выводить контролируемые величины в CSV (Выводить контролируемые величины в CSV)',
    'PeriodAngle': 'Отображать углы в диапазоне +/-180 (Отображать углы в диапазоне +/-180)',
    'ResultFlowDirection': 'Положительное направление результатов (Положительное направление результатов)',
    'TreatWarningsAsErrors': 'Считать предупреждения ошибками (Предупреждение=Ошибка)',
    'EventProcess': 'Метод обработки дискретных изменений (Дискретные изменения)'
}

alt_unit_table = 'AltUnit'
alt_unit_attributes_list = ['Active', 'Unit', 'Alt', 'Formula', 'Prec', 'Tabl', ]
alt_unit_attributes = {
    'Active': 'Активизация альтернативной ЕИ (A)',
    'Unit': 'Основная Единица Измерения (ЕИ)',
    'Alt': 'Альтернативная Единица Измерения (Альт ЕИ)',
    'Formula': 'Формула для преобразования (Формула)',
    'Prec': 'Точность отображение Альт ЕИ (Точность)',
    'Tabl': 'Ограничитель по таблице (Табл)',
}

ut_common_table = 'ut_common'
ut_common_attributes_list = ['maxs', 'maxv', 'maxd', 'maxa', 'iter', 'tip', 'f_ots', 'add_d', 'ekstr', 'kfc', 'sum_kfc',
                             'ds', 'it', 'Status', 'KorrT', 'KorrPer', 'KorrVib', 'enable_contr', 'dis_v_contr',
                             'dis_p_contr', 'dis_i_contr', 'ss_calc', 'criterion', 'no_crit_d_ba', 'no_crit_d_coa',
                             'no_crit_d_ga', 'save_files_filter', 'save_files_path', 'stop_u_n', 'dyn_find_pred', ]
ut_common_attributes = {
    'maxs': 'Точность P (Pmax)',
    'maxv': 'Точность V (Vmax)',
    'maxd': 'Точность угла (Dmax)',
    'maxa': 'Точность P района (Amax)',
    'iter': 'Макс число итераций (Imax)',
    'tip': 'Тип утяжеления (Тип)',
    'f_ots': 'Формировать описания контр. величин: (ФормКВ:)',
    'add_d': 'Добавлять значения контр. величин после шага (ДобКЗ)',
    'ekstr': 'Поиск экстремума по контролируемым величинам (Экстремум)',
    'kfc': 'Текущий шаг (Шаг)',
    'sum_kfc': 'Сумарный шаг (Шаг_Сумм)',
    'ds': 'Деление шага (ДелШаг)',
    'it': 'Текущая итерация (Итер)',
    'Status': 'Состояние утяжеления (Статус)',
    'KorrT': 'коррекция по температуре: температура, Гр. (KorrT)',
    'KorrPer': 'коррекция по температуре: перегрузка % (KorrPer)',
    'KorrVib': 'коррекция по температуре: выборка (KorrVib)',
    'enable_contr': 'Включить контроль всех ограничений U,P,I (Включить контр. U,P,I)',
    'dis_v_contr': 'Отключить контроль всех ограничений по напряжению U (Откл контр. U)',
    'dis_p_contr': 'Отключить контроль всех ограничений по мощности P (Откл контр. P)',
    'dis_i_contr': 'Отключить контроль всех ограничений по току I (Откл контр. I)',
    'ss_calc': 'Как расчитывать УР при утяжелении (Расчет УР)',
    'criterion': 'Критерий устойчивости (Критерий)',
    'no_crit_d_ba': 'Динамика:не учет критерия разворота угла по ЛЭП (Нет критерия: угол по ЛЭП)',
    'no_crit_d_coa': 'Динамика:не учет критерия угла генератора и COA (Нет критерия: угол по Генератору)',
    'no_crit_d_ga': 'Динамика:не учет критерия срабатывания автомата безопасности генератора '
                    '(Нет критерия: автомат безопасности ген.)',
    'save_files_filter': 'Критерий сохранения файлов (Критерий)',
    'save_files_path': 'Папка для сохранения файлов результатов (Путь)',
    'stop_u_n': 'Остановить при переходе к устойчивому/неустойчивому (Остановить)',
    'dyn_find_pred': 'Динамика: поиск предела (Динамика: поиск предела)',
}

area_table = 'area'
area_attributes_list = ['na', 'name', 'no', 'pg', 'pn', 'dp', 'pop', 'vnp', 'Tc', 'pn_min', 'pn_max', 'pg_min',
                        'pg_max', ]
area_attributes = {
    'na': 'Номер района (Nр-н)',
    'name': 'Название района (Район)',
    'no': 'Номер объединения (Nоб)',
    'pg': 'Генерация P (Pген)',
    'pn': 'Нагрузка P (Pнаг)',
    'dp': 'Потери P (Dp)',
    'pop': 'Потребление P (Pпотр)',
    'vnp': 'Внешний переток P (Pвн)',
    'Tc': 'Температура (Tc)',
    'pn_min': 'Минимум нагрузки, МВт (Pн мин)',
    'pn_max': 'Максимум нагрузки, МВт (Pн max)',
    'pg_min': 'Минимум генерации, МВт (Pг мин)',
    'pg_max': 'Максимум генерации, МВт (Pг max)',
}

DFWAutoActionScn = 'DFWAutoActionScn'
DFWAutoActionScn_attributes_list = ['State', 'Id', 'ParentId', 'Type', 'Name', 'Formula', 'ObjectClass', 'ObjectProp',
                                    'ObjectKey', 'OutputMode', 'RunsCount', 'TimeStart', 'DT', 'Tag', ]
DFWAutoActionScn_attributes = {
    'State': 'Действие активно (Сост)',
    'Id': 'Номер действия (N)',
    'ParentId': 'Номер группы (N группы)',
    'Type': 'Тип действия (Тип)',
    'Name': 'Название (Название)',
    'Formula': 'Формула (Формула)',
    'ObjectClass': 'Тип объекта (Тип объекта)',
    'ObjectProp': 'Свойство объекта (Свойство объекта)',
    'ObjectKey': 'Ключ объекта (Ключ объекта)',
    'OutputMode': 'Режим выхода (Режим)',
    'RunsCount': 'Количество срабатываний (N сраб)',
    'TimeStart': 'Время начала действия упрощенного сценария (Время начала)',
    'DT': 'Длительность действия упрощенного сценария (Длительность)',
    'Tag': 'Тэг упрощенного сценария (Тэг)',
}

DFWAutoLogicScn = 'DFWAutoLogicScn'
DFWAutoLogicScn_attributes_list = ['Id', 'Name', 'ParentId', 'Type', 'Formula', 'Actions', 'Delay', 'UnitStarters',
                                   'UnitConstants', 'UnitActions', 'OutputMode', ]
DFWAutoLogicScn_attributes = {
    'Id': 'Номер элемента логики (N)',
    'Name': 'Название (Название)',
    'ParentId': 'Номер модуля (N модуля)',
    'Type': 'Тип логики (Тип)',
    'Formula': 'Формула (Формула)',
    'Actions': 'Список действий элемента (Действия)',
    'Delay': 'Выдержка времени (Выдержка)',
    'UnitStarters': 'Список ПО модуля (ПО мод)',
    'UnitConstants': 'Список констант модуля (Const мод)',
    'UnitActions': 'Список действий модуля (Дейст мод)',
    'OutputMode': 'Режим выхода (Режим)',
}
