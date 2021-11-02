# -*- coding: utf-8 -*-
from RastrWin3.Tools.tools import DirectoryCheck

obj_dir = DirectoryCheck(name=r'test9.scn')

# print(obj_dir.get_name())
print(obj_dir.get_expansion())
print(obj_dir.get_full_name())