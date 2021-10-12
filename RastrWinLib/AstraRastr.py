# -*- coding: utf-8 -*-
# COM ИНТЕРФЕЙСЫ ПРОГРАММЫ RASTR
# Объект Rastr
# Это основной объект в astra.dll.
# При работе во встроенных макросах он уже создан,
# при работе во внешней среде – должен создаваться обычным образом,
# например, в Python:
from win32com.client import Dispatch, WithEvents


class RastrEvents:
    """
    Метод Onprot - выводит сообщения написанные: rastr.Printp("Сообщение из Printp")
    Метод OnLog
    """

    def OnLog(self, code, level, id, name, index, description, formName):
        # print(f"[{code}] {description}")
        # self.file.write(f"[{code}=info] {description}")
        if code == 2:
            print(f"[{'Error'}] {description}")
        elif code == 3:
            print(f"[{'Warning'}] {description}")
        elif code == 4:
            print(f"[{'Lightbulb'}] {description}")
        elif code == 5:
            print(f"[{'Info'}] {description}")
        else:
            print(f"[{code}] {description}")

    def Onprot(self, message):
        print(message)


RASTR = Dispatch('Astra.Rastr')
WithEvents(RASTR, RastrEvents)
