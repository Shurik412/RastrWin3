# -*- coding: utf-8 -*-
from win32com.client import Dispatch, WithEvents, constants


# COM event handlers
class RastrEvents:
    def OnLog(self, code, level, id, name, index, description, formName):
        print("[%d] %s" % (code, description))

    def Onprot(self, message):
        print(message)


def runAstra():
    rastr = Dispatch("Astra.Rastr")
    WithEvents(rastr, RastrEvents)
    rastr.Load(constants.RG_ADD, r"C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\cx195.rg2", "")
    rastr.rgm("p")
    rastr.Printp("Сообщение из Printp")


if __name__ == '__main__':
    runAstra()
