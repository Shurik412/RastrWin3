# -*- coding: utf-8 -*-
# COM ИНТЕРФЕЙСЫ ПРОГРАММЫ RASTR
# Объект Rastr
# Это основной объект в astra.dll.
# При работе во встроенных макросах он уже создан,
# при работе во внешней среде – должен создаваться обычным образом,
# например, в Python:
import win32com.client

RASTR = win32com.client.Dispatch('Astra.Rastr')
