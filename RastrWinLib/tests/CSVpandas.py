# -*- coding: utf-8 -*-
import csv

list_ = []

with open(file=r'C:\Users\Ohrimenko_AG\Desktop\TestCSV\23.csv') as f:
    reader = csv.reader(f, delimiter=';')
    for index, row in enumerate(reader):
        print(f'{index} -> {row}')
        list_.append(row)


print(list_[1])
