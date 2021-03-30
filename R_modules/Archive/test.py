# # list = [1, 2, 3]
# # dict_1 = {1: ['ip1', 'iq1', 'np1'],
# #           2: ['ip2', 'iq2', 'np2'],
# #           3: ['ip3', 'iq3', 'np3']}
# #
# # for i in list:
# #     print(f'Значения: {dict_1[i]}')
# #     print(f'Значения списков: {dict_1[i][0]}')
# #     print(f'Значения списков: {dict_1[i][1]}')
# #     print(f'Значения списков: {dict_1[i][2]}')
#
#
# # dict_1 = {1: [['ip1', 'name_ip1'], 'iq1', 'np1'],
# #           2: [['ip2', 'name_ip2'], 'iq2', 'np2'],
# #           3: [['ip3', 'name_ip3'], 'iq3', 'np3']}
# # list = len(dict_1)
# # print((list))
#
# dict_scn = {1: ['ip1', 'iq1', 'np1', '1.scn', 'Лист_расч 1'],
#             2: ['ip2', 'iq2', 'np2', '2.scn', 'Лист_расч 2'],
#             3: ['ip3', 'iq3', 'np3', '3.scn', 'Лист_расч 3'],
#             4: ['ip4', 'iq4', 'np4', '4.scn', 'Лист_расч 4'],
#             5: ['ip5', 'iq5', 'np5', '5.scn', 'Лист_расч 5'],
#             6: ['ip6', 'iq6', 'np6', '6.scn', 'Лист_расч 6']}
# max_count_dict_scn = len(dict_scn)
#
#
# print(dict_scn[1][4])
#
#
# for i in dict_1:
#     print(f't={t}')
#     print(i)
#     print(f'Индекс: ')
#     print(f'Значения словаря: {dict_1[i]}')
#     print(f'\t- значения списков: {dict_1[i][list.index(i)]}')
#     print(f'\t\t<{dict_1[i][0][0]} - {dict_1[i][0][1]}>')


# import re
# from icecream import ic
#
# d = 'S dfsdf.scn'
# p = re.compile(r"""(?P<name>[0-9а-яА-ЯёЁa-zA-Z])[.](?P<expansion>([s][c][n]))""", re.I | re.X)
#
# r = p.search(d)
# # ic(r.group("name"))
# ic(r)
# t = re.Match
# ic(r.group("expansion"))
# # ic(r.group("expansion"))
#

# list_coordinates_of_graphs = [('B2', 'S2', 'AJ2'),
#                               ('B36', 'S36', 'AJ36'),
#                               ('B70', 'S70', 'AJ70'),
#                               ('B104', 'S104', 'AJ104')]

import pydantic

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'J.D.'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, 3],
}

user = User(**external_data)
print(user.friends)

from pydantic import ValidationError

try:
    User(signup_ts='broken', friends=[1, 2, 'not number'])
except ValidationError as e:
    print(e.json())