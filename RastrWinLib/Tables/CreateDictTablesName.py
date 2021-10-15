# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR


sb = RASTR.SubstServer
substId = sb.TypeIdByName("Substation")

print(
    substId
)