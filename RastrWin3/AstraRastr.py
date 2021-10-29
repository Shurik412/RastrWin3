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

    @staticmethod
    def OnLog(code, level, id, name, index, description, formName) -> None:
        if code == 2:
            print('[Error]', description)
        elif code == 3:
            print('[Warning]', description)
        elif code == 4:
            print('[Lightbulb]', description)
        elif code == 5:
            print('[Info]', description)
        else:
            print([code, description])

    @staticmethod
    def Onprot(message: str) -> None:
        print(message)


RASTR = Dispatch('Astra.Rastr')
WithEvents(RASTR, RastrEvents)
