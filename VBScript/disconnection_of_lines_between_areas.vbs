r=setlocale("en-us")
rrr=1

set t=RASTR
set vet=t.tables("vetv")
set uzl=t.tables("node")
set ray=t.tables("area")
set gen=t.tables("Generator")
set pqd=t.Tables("graphik2")
set graphikIT=t.Tables("graphikIT")
set area=t.Tables("area")
set area2=t.Tables("area2")
set darea=t.Tables("darea")
set polin=t.Tables("polin")

vet.cols("sel").calc("0")
uzl.cols("sel").calc("0")

'uzl.SetSel("(na=801 | na=803 | na=804 | na=805 | na=806 | na=807 | na=813 | na=817 | na=819 | na=820 | na=402 | na=403 | na=404 | na=405 | na=407 | na=408 | na=409 | na=529 | na=513 | na=510 | na=517 | na=532 | na=511 | na=526 | na=515 | na=517 | na=523 | na=519| na=521 | na=518 | na=527 | na=532 | na=527 | na=532 | na=524 | na=526 | na=516)")
uzl.SetSel("(na=518)")

uzl.cols("sel").calc("1")

uzl.SetSel("")
vet.SetSel("")

vet.SetSel("iq.sel=1 &ip.sel=0")
vet.cols("sta").calc(1)

vet.SetSel("iq.sel=0 &ip.sel=1")
vet.cols("sta").calc(1)

vet.cols("sel").calc("0")
uzl.cols("sel").calc("0")
