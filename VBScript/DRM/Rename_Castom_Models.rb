r=setlocale("en-us")
rrr=1

set t=RASTR

'Задать ссылку для пользовательских устройств
Link = "C:\RastrWin3\CustomModels\"    ' -  ПРИМЕР: "C:\RastrWin3\CustomModels\"

'spComDynamic("SnapPath").Z(0)= "D:\Результаты Rustab"

'1.----------AC8B--------------------
t.Tables("CustomDeviceMap").delrows
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(0)="1"
t.Tables("CustomDeviceMap").Cols("Module").z(0)= Link +"dll\AC8B"
t.Tables("CustomDeviceMap").Cols("Name").z(0)="AC8B"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(0)="DFWIEEE421"
t.Tables("CustomDeviceMap").Cols("Tag").z(0)="Exciter"
t.Tables("CustomDeviceMap").Cols("LinkList").z(0)="Generator"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(0)=" "

'2.----------ARV_REM--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(1)="2"
t.Tables("CustomDeviceMap").Cols("Module").z(1)=Link +"dll\ARV-REM simp"
t.Tables("CustomDeviceMap").Cols("Name").z(1)="ARV-REM simp"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(1)="ExcControl"
t.Tables("CustomDeviceMap").Cols("Tag").z(1)="ExcControl"
t.Tables("CustomDeviceMap").Cols("LinkList").z(1)="Exciter"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(1)=" "

'3.----------ARV2M--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(2)="3"
t.Tables("CustomDeviceMap").Cols("Module").z(2)=Link +"dll\AVR-2M_res"
t.Tables("CustomDeviceMap").Cols("Name").z(2)="AVR-2M_res"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(2)="ExcControl"
t.Tables("CustomDeviceMap").Cols("Tag").z(2)="ExcControl"
t.Tables("CustomDeviceMap").Cols("LinkList").z(2)="Exciter"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(2)=" "

'4.----------ARV-3MTK--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(3)="4"
t.Tables("CustomDeviceMap").Cols("Module").z(3)=Link +"dll\AVR-3M_res"
t.Tables("CustomDeviceMap").Cols("Name").z(3)="AVR-3M_res"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(3)="ExcControl"
t.Tables("CustomDeviceMap").Cols("Tag").z(3)="ExcControl"
t.Tables("CustomDeviceMap").Cols("LinkList").z(3)="Exciter"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(3)=" "

'5.----------ARV-4M--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(4)="5"
t.Tables("CustomDeviceMap").Cols("Module").z(4)=Link +"dll\AVR-4M_res"
t.Tables("CustomDeviceMap").Cols("Name").z(4)="AVR-4M_res"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(4)="ExcControl"
t.Tables("CustomDeviceMap").Cols("Tag").z(4)="ExcControl"
t.Tables("CustomDeviceMap").Cols("LinkList").z(4)="Exciter"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(4)=" "

'6.----------ARVNL--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(5)="6"
t.Tables("CustomDeviceMap").Cols("Module").z(5)=Link +"dll\ARVNL_sts simp"
t.Tables("CustomDeviceMap").Cols("Name").z(5)="ARVNL_sts simp"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(5)="ExcControl"
t.Tables("CustomDeviceMap").Cols("Tag").z(5)="ExcControl"
t.Tables("CustomDeviceMap").Cols("LinkList").z(5)="Exciter"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(5)=" "

'7.----------ARVSDE--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(6)="7"
t.Tables("CustomDeviceMap").Cols("Module").z(6)=Link +"dll\ARVSDE simp"
t.Tables("CustomDeviceMap").Cols("Name").z(6)="ARVSDE simp"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(6)="ExcControl"
t.Tables("CustomDeviceMap").Cols("Tag").z(6)="ExcControl"
t.Tables("CustomDeviceMap").Cols("LinkList").z(6)="Exciter"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(6)=" "

'8.----------ARVSDS--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(7)="8"
t.Tables("CustomDeviceMap").Cols("Module").z(7)=Link +"dll\ARVSDS"
t.Tables("CustomDeviceMap").Cols("Name").z(7)="ARVSDS"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(7)="ExcControl"
t.Tables("CustomDeviceMap").Cols("Tag").z(7)="ExcControl"
t.Tables("CustomDeviceMap").Cols("LinkList").z(7)="Exciter"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(7)=" "

'9.----------ARVSG--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(8)="9"
t.Tables("CustomDeviceMap").Cols("Module").z(8)=Link +"dll\ARVSG_sts simp"
t.Tables("CustomDeviceMap").Cols("Name").z(8)="ARVSG_sts simp"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(8)="ExcControl"
t.Tables("CustomDeviceMap").Cols("Tag").z(8)="ExcControl"
t.Tables("CustomDeviceMap").Cols("LinkList").z(8)="Exciter"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(8)=" "

'10.----------AVR2--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(9)="10"
t.Tables("CustomDeviceMap").Cols("Module").z(9)=Link +"dll\AVR-2"
t.Tables("CustomDeviceMap").Cols("Name").z(9)="AVR-2"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(9)="ExcControl"
t.Tables("CustomDeviceMap").Cols("Tag").z(9)="ExcControl"
t.Tables("CustomDeviceMap").Cols("LinkList").z(9)="Exciter"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(9)=" "

'11.----------AVR-2_br--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(10)="11"
t.Tables("CustomDeviceMap").Cols("Module").z(10)=Link +"dll\AVR-2_br"
t.Tables("CustomDeviceMap").Cols("Name").z(10)="AVR-2_br"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(10)="ExcControl"
t.Tables("CustomDeviceMap").Cols("Tag").z(10)="ExcControl"
t.Tables("CustomDeviceMap").Cols("LinkList").z(10)="Exciter"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(10)=" "

'12.----------DECS--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(11)="12"
t.Tables("CustomDeviceMap").Cols("Module").z(11)=Link +"dll\DECS simp"
t.Tables("CustomDeviceMap").Cols("Name").z(11)="DECS simp"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(11)="DFWIEEE421"
t.Tables("CustomDeviceMap").Cols("Tag").z(11)="Exciter"
t.Tables("CustomDeviceMap").Cols("LinkList").z(11)="Generator"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(11)=" "

'13.----------EAA--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(12)="13"
t.Tables("CustomDeviceMap").Cols("Module").z(12)=Link +"dll\EAA"
t.Tables("CustomDeviceMap").Cols("Name").z(12)="EAA"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(12)="ExcControl"
t.Tables("CustomDeviceMap").Cols("Tag").z(12)="ExcControl"
t.Tables("CustomDeviceMap").Cols("LinkList").z(12)="Exciter"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(12)=" "

'14.----------EX2100--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(13)="14"
t.Tables("CustomDeviceMap").Cols("Module").z(13)=Link +"dll\EX2100 simp"
t.Tables("CustomDeviceMap").Cols("Name").z(13)="EX2100 simp"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(13)="DFWIEEE421"
t.Tables("CustomDeviceMap").Cols("Tag").z(13)="Exciter"
t.Tables("CustomDeviceMap").Cols("LinkList").z(13)="Generator"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(13)="DFWIEEE421PSS13"

'15.----------EX2100br--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(14)="15"
t.Tables("CustomDeviceMap").Cols("Module").z(14)=Link +"dll\EX2100br simp"
t.Tables("CustomDeviceMap").Cols("Name").z(14)="EX2100br simp"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(14)="DFWIEEE421"
t.Tables("CustomDeviceMap").Cols("Tag").z(14)="Exciter"
t.Tables("CustomDeviceMap").Cols("LinkList").z(14)="Generator"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(14)=" "

'16.----------K0SUR2--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(15)="16"
t.Tables("CustomDeviceMap").Cols("Module").z(15)=Link +"dll\K0SUR2"
t.Tables("CustomDeviceMap").Cols("Name").z(15)="K0SUR2"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(15)="ExcControl"
t.Tables("CustomDeviceMap").Cols("Tag").z(15)="ExcControl"
t.Tables("CustomDeviceMap").Cols("LinkList").z(15)="Exciter"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(15)=" "

'17.----------Prismic--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(16)="17"
t.Tables("CustomDeviceMap").Cols("Module").z(16)=Link +"dll\Prismic"
t.Tables("CustomDeviceMap").Cols("Name").z(16)="Prismic"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(16)="DFWIEEE421"
t.Tables("CustomDeviceMap").Cols("Tag").z(16)="Exciter"
t.Tables("CustomDeviceMap").Cols("LinkList").z(16)="Generator"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(16)=" "


'18.----------Semipol--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(17)="18"
t.Tables("CustomDeviceMap").Cols("Module").z(17)=Link +"dll\Semipol"
t.Tables("CustomDeviceMap").Cols("Name").z(17)="Semipol"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(17)="DFWIEEE421"
t.Tables("CustomDeviceMap").Cols("Tag").z(17)="Exciter"
t.Tables("CustomDeviceMap").Cols("LinkList").z(17)="Generator"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(17)="DFWIEEE421PSS13"

'19.----------Semipol_PSS--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(18)="19"
t.Tables("CustomDeviceMap").Cols("Module").z(18)=Link +"dll\Semipol"
t.Tables("CustomDeviceMap").Cols("Name").z(18)="Semipol_PSS"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(18)="DFWIEEE421PSS13"
t.Tables("CustomDeviceMap").Cols("Tag").z(18)="PSS"
t.Tables("CustomDeviceMap").Cols("LinkList").z(18)="DFWIEEE421"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(18)=" "


'20.----------THYNE_4--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(19)="20"
t.Tables("CustomDeviceMap").Cols("Module").z(19)=Link +"dll\THYNE_4"
t.Tables("CustomDeviceMap").Cols("Name").z(19)="THYNE_4"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(19)="DFWIEEE421"
t.Tables("CustomDeviceMap").Cols("Tag").z(19)="Exciter"
t.Tables("CustomDeviceMap").Cols("LinkList").z(19)="Generator"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(19)=" "

'21.----------U5001--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(20)="21"
t.Tables("CustomDeviceMap").Cols("Module").z(20)=Link +"dll\U5000"
t.Tables("CustomDeviceMap").Cols("Name").z(20)="U5000"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(20)="DFWIEEE421"
t.Tables("CustomDeviceMap").Cols("Tag").z(20)="Exciter"
t.Tables("CustomDeviceMap").Cols("LinkList").z(20)="Generator"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(20)=" "

'22.----------u6800--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(21)="22"
t.Tables("CustomDeviceMap").Cols("Module").z(21)=Link +"dll\U6800 simp"
t.Tables("CustomDeviceMap").Cols("Name").z(21)="U6800 simp"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(21)="DFWIEEE421"
t.Tables("CustomDeviceMap").Cols("Tag").z(21)="Exciter"
t.Tables("CustomDeviceMap").Cols("LinkList").z(21)="Generator"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(21)="DFWIEEE421PSS4B"

'23.----------Hydrot--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(22)="23"
t.Tables("CustomDeviceMap").Cols("Module").z(22)=Link +"dll\Hydrot"
t.Tables("CustomDeviceMap").Cols("Name").z(22)="Hydrot"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(22)="ARS"
t.Tables("CustomDeviceMap").Cols("Tag").z(22)="ARS"
t.Tables("CustomDeviceMap").Cols("LinkList").z(22)="Generator"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(22)=" "

'24.----------BESSCH--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(23)="24"
t.Tables("CustomDeviceMap").Cols("Module").z(23)=Link +"dll\BESSCH"
t.Tables("CustomDeviceMap").Cols("Name").z(23)="BESSCH"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(23)="Exciter"
t.Tables("CustomDeviceMap").Cols("Tag").z(23)="Exciter"
t.Tables("CustomDeviceMap").Cols("LinkList").z(23)="Generator"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(23)=" "

'25.----------K0SUR2_br--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(24)="25"
t.Tables("CustomDeviceMap").Cols("Module").z(24)=Link +"dll\Kosur2bsv"
t.Tables("CustomDeviceMap").Cols("Name").z(24)="Kosur2bsv"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(24)="ExcControl"
t.Tables("CustomDeviceMap").Cols("Tag").z(24)="ExcControl"
t.Tables("CustomDeviceMap").Cols("LinkList").z(24)="Exciter"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(24)=" "

'26.----------gglite--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(25)="26"
t.Tables("CustomDeviceMap").Cols("Module").z(25)=Link +"dll\gglite"
t.Tables("CustomDeviceMap").Cols("Name").z(25)="gglite"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(25)="ARS"
t.Tables("CustomDeviceMap").Cols("Tag").z(25)="ARS"
t.Tables("CustomDeviceMap").Cols("LinkList").z(25)="Generator"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(25)=" "

'27.----------Alstom2--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(26)="27"
t.Tables("CustomDeviceMap").Cols("Module").z(26)=Link +"dll\Alstom2 simp"
t.Tables("CustomDeviceMap").Cols("Name").z(26)="Alstom2 simp"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(26)="DFWIEEE421"
t.Tables("CustomDeviceMap").Cols("Tag").z(26)="Exciter"
t.Tables("CustomDeviceMap").Cols("LinkList").z(26)="Generator"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(26)="DFWIEEE421PSS13"

'28.----------Alstom2_PSS--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(27)="28"
t.Tables("CustomDeviceMap").Cols("Module").z(27)=Link +"dll\Alstom2_PSS"
t.Tables("CustomDeviceMap").Cols("Name").z(27)="Alstom2_PSS"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(27)="DFWIEEE421PSS13"
t.Tables("CustomDeviceMap").Cols("Tag").z(27)="PSS"
t.Tables("CustomDeviceMap").Cols("LinkList").z(27)="DFWIEEE421"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(27)=" "

'29.----------Thyripol--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(28)="29"
t.Tables("CustomDeviceMap").Cols("Module").z(28)=Link +"dll\Thyripol6RV simp"
t.Tables("CustomDeviceMap").Cols("Name").z(28)="Thyripol6RV simp"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(28)="DFWIEEE421"
t.Tables("CustomDeviceMap").Cols("Tag").z(28)="Exciter"
t.Tables("CustomDeviceMap").Cols("LinkList").z(28)="Generator"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(28)="DFWIEEE421PSS13"

'30.----------Thyripol PSS--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(29)="30"
t.Tables("CustomDeviceMap").Cols("Module").z(29)=Link +"dll\ThyrPSS6RV"
t.Tables("CustomDeviceMap").Cols("Name").z(29)="ThyrPSS6RV"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(29)="DFWIEEE421PSS13"
t.Tables("CustomDeviceMap").Cols("Tag").z(29)="PSS"
t.Tables("CustomDeviceMap").Cols("LinkList").z(29)="DFWIEEE421"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(29)=" "

'31.----------Tyr0--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(30)="31"
t.Tables("CustomDeviceMap").Cols("Module").z(30)=Link +"dll\Tyr0"
t.Tables("CustomDeviceMap").Cols("Name").z(30)="Tyr0"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(30)="Exciter"
t.Tables("CustomDeviceMap").Cols("Tag").z(30)="Exciter"
t.Tables("CustomDeviceMap").Cols("LinkList").z(30)="Generator"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(30)=" "

'32.----------BSV--------------------
t.Tables("CustomDeviceMap").AddRow
t.Tables("CustomDeviceMap").Cols("Id").z(31)="32"
t.Tables("CustomDeviceMap").Cols("Module").z(31)=Link +"dll\BSV"
t.Tables("CustomDeviceMap").Cols("Name").z(31)="BSV"
t.Tables("CustomDeviceMap").Cols("InstanceTable").z(31)="Exciter"
t.Tables("CustomDeviceMap").Cols("Tag").z(31)="Exciter"
t.Tables("CustomDeviceMap").Cols("LinkList").z(31)="Generator"
t.Tables("CustomDeviceMap").Cols("SiblingLinkList").z(31)=" "