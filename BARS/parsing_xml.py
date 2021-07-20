# -*- coding: utf-8 -*-
import re
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.utils import get_column_interval, column_index_from_string
from icecream import ic
from xml.etree.ElementTree import parse, Element
from lxml import etree


def parseBookXML(xmlFile):
    with open(xmlFile) as fobj:
        xml = fobj.read()
    root = etree.fromstring(xml)
    for book in root.getchildren():
        for elem in book.getchildren():
            if book.tag == "SHEMA":
                print(elem.tag + ' => ' + elem.taxt)


# doc = parse(r'C:\Users\Ohrimenko_AG\Desktop\05_ модель от 19_07 sktc tok ter.xml')
#
# for item in doc.iterfind('cn-smzu-main.oducn.so.MDP3/SHEMA/'):
#     potr = item.findtext('POTR')
#     gen = item.findtext('GEN')
#     ic(potr)
#     ic(gen)

if __name__ == "__main__":
    parseBookXML(r'C:\Users\Ohrimenko_AG\Desktop\05_ модель от 19_07 sktc tok ter.xml')
