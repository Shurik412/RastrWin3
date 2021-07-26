# -*- coding: utf-8 -*-
import re
from icecream import ic

string = '(ts[12721])&(ts[12719])&(ts[2096])&(ti[2097])&(ts[2098])&(ts[2168])&(ts[2091])&(ts[2090])' \
      '&(ts[2092])&(ts[13112])&(ts[13110])&(ts[13143])&(ts[13140])&(ts[3280])&(ts[2250])&(ts[696])' \
      '&(ts[698])&(ts[702])&(ts[697])&(ts[699])&(ts[703])&(ts[663])&(ts[665])&(ts[662])&(ts[664])' \
      '&(ts[5781])&(ts[5732])'




def sampling_from_string(string):
    list_t = []
    list_end = []
    list_str = []
    for index, i in enumerate(string):
        if i == 't':
            list_t.append(index)
        if i == ']':
            list_end.append(index + 1)
    # print(f'list_t={list_t}')
    # print(f'list_end={list_end}')
    for index_list_t, t in enumerate(list_t):
        num_str_list_end = list_end[index_list_t]
        ts_plus_str = string[t:num_str_list_end]
        list_str.append(ts_plus_str)
    return list_str


cell_ = '(ts[12721])&(ts[12719])&(ts[2096])&(ts[2097])&(ts[2098])&(ts[2168])&(ts[2091])&(ts[2090])' \
        '&(ts[2092])&(ts[13112])&(ts[13110])&(ts[13143])&(ts[13140])&(ts[3280])&(ts[2250])&(ts[696])' \
        '&(ts[698])&(ts[702])&(ts[697])&(ts[699])&(ts[703])&(ts[663])&(ts[665])&(ts[662])&(ts[664])' \
        '&(ts[5781])&(ts[5732])'
list_cell = list(map(int, re.findall(r"\[([+-]?\d+)\]", cell_)))  # \[(\d+)\]'
print(list_cell)

ll = sampling_from_string(string)

ic(ll)
