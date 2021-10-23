# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, join
import os


def file_extensions(path_file: str, extensions: str):
    only_files = [f for f in listdir(path_file) if isfile(join(path_file, f))]
    for file in only_files:
        file_name, file_extension = os.path.splitext(file)
        if file_extension == extensions:
            return file_name, file_extension
        else:
            file_name = 'Нет данных!'
            return file_name
