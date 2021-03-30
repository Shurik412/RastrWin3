' 2020-06-28 Изменения в удалении: делаем Vzd
' 2020-07-06 Изменения в установлении перетока в сечении
xxx = 1
nlog = 1
r=setlocale("en-us")
'Файл с корректирующими данными:
'settings="c:\!Расчеты\НВАЭС-2\Расчеты для ввода блока №7\Расчет Беларусь 2020\Настройки коррекции.xlsx"
'settings="c:\!Расчеты\НВАЭС-2\Расчеты для ввода блока №7\Модели из БРМ 19-20\Настройки коррекции.xlsx"
'settings="c:\!Расчеты\Воронежское ремонтное\РМ УКРАИНА\Экв\Настройки коррекции.xlsx"
settings="e:\Работа\Коррекция БРМ\Настройки коррекции.xlsx"

PMINMAX = 0
typfile = ".rg2"
'typfile = ".rst"

Dim ishdir, fin_dir, rg2_shabl, sec_shabl, grf_shabl, anc_shabl, sec_need, grf_need, anc_need,ncorrect,col,oldvalue,newvalue
Dim filename(1000), corr_settings(1000), newfilename(1000), new_sec_name(1000), new_grf_name(1000), new_anc_name(1000)
Dim sec_name(1000), grf_name(1000),anc_name(1000),savef(1000),setiav
Dim rayony(10,9999),terr(10,9999),obyedin(10,9999),genr(10,9999)
Dim nsecbal,secbal(10,20), nutnode, nvybut, nareaut, utnode(10000,10), vybut(100,10),areaut(100,10),kshag,tcom_regim

setiav = 0
Call GetSettings

r=setlocale("ru-ru")
Set fso1 = createobject ("scripting.filesystemobject")
nowdate = date()

If FSO1.FolderExists(fin_dir) Then
	n = 1
	while FSO1.FolderExists(fin_dir & "_" & n)
		n = n + 1
	wend
	fin_dir = fin_dir & "_" & n
end if

'msgbox nowdate
'msgbox fin_dir
fso1.createfolder fin_dir
fin_dir = fin_dir & "\"
rrr = 1
'Файл настроек:
'settings="f:\работа\КуАЭС-2\Модели КуАЭС-2\20161028\НА\Настройки коррекции 2023.xlsx"
Set ExLog = CreateObject("Excel.Application")
ExLog.Visible = 1
ExLog.Workbooks.Add
'Excel.ScreenUpdating = False
ExLog.EnableEvents = False
r = setlocale("ru-ru")
ExLog.ActiveWorkbook.SaveAs fin_dir & "лог -" & "_" & nowdate & "_" & Hour(Now()) & "h" & Minute(Now()) & "m.xlsx", 51
r = setlocale("en-us")
Call writelog "!","Открыт с наборами корректирующих данных: " & settings
Call writelog ""," =========================================="
Set t = CreateObject("Astra.Rastr")
for ifile = 1 to ncorrect
    Call writelog "!!!", ifile
    Set ExcelSet = CreateObject("Excel.Application")
    ExcelSet.Workbooks.open ishdir & corr_settings(ifile)
    ExcelSet.Visible = 1
    'ExcelSet.ScreenUpdating = False
    ExcelSet.EnableEvents = False
    Call writelog ""," =========================================="
    Call writelog "!!!","Открыт с корректирующими данными: " & corr_settings(ifile)
    Call writelog ""," =========================================="
    if filename(ifile) <> "bez izmeneniya fayla!" then
        t.Load 1, (ishdir & filename(ifile) & typfile), rg2_shabl
        Call writelog "!","Открыт файл rg2: " & filename(ifile)
        if sec_need > 0 and sec_name(ifile) <> "" then
            t.Load 1, (ishdir & sec_name(ifile) & ".sch"), sec_shabl
            Call writelog "!","Открыт файл sec: " & sec_name(ifile)
            set sec = t.tables("sechen")
            set grline = t.tables("grline")
        end if
        if grf_need > 0 and grf_name(ifile) <> "" then
            t.Load 1, (ishdir & grf_name(ifile) & ".grf"), grf_shabl
            Call writelog "!","Открыт файл grf: " & grf_name(ifile)
        end if
        if anc_need > 0 and anc_name(ifile) <> "" then
            t.Load 1, (ishdir & anc_name(ifile) & ".anc"), anc_shabl
            Call writelog "!","Открыт файл anc: " & anc_name(ifile)
            set anc = t.tables("ancapf")
            set anc2 = t.tables("Ancapf2")
        end if
    end if
    t.LogEnable=False ' блокировка вывода в протокол
    set vet=t.tables("vetv")
    set uzl=t.tables("node")
    set gen=t.tables("Generator")
    set git=t.tables("graphikIT")
    set pq=t.tables("graphik2")
    set sxn=t.tables("polin")
    set ray=t.tables("area")
    set ray2=t.tables("area2")
    't.Tables("com_regim").Cols("neb_p").z(0)=0.001
    't.Tables("com_regim").Cols("it_max").z(0)=100
    kod = t.rgm ("p") 'почему-то не использовалось
    if kod = 0 then Call writelog "!","Исходный расчет режима успешный"
    if kod <> 0 then Call writelog "!!!","!!! Исходный расчет режима неуспешнай!!!"
    needtodel = 0'
    '=========================== change ===============================
	On Error Resume Next
	oooo0 = ExcelSet.Worksheets("change").cells(3,1).value
 	If Err.Number = 0 Then
        t.RenumWP=True
        nvetch=0
        for i2=3 to 999999
            if ExcelSet.Worksheets("change").cells(i2,5).value<>"" then
                ip=ExcelSet.Worksheets("change").cells(i2,5).value
                iq=ExcelSet.Worksheets("change").cells(i2,6).value
                np=ExcelSet.Worksheets("change").cells(i2,7).value
                if np="" then np=0
                vet.SetSel("ip="&ip&"&iq="&iq&"&np="&np)
                ivet=vet.findnextsel(-1)
                if ivet<>-1 then
                    ipnew=ExcelSet.Worksheets("change").cells(i2,8).value
                    iqnew=ExcelSet.Worksheets("change").cells(i2,9).value
                    npnew=ExcelSet.Worksheets("change").cells(i2,10).value
                    nvetch=nvetch+1
                    if ip<>ipnew then
                        vet.cols("ip").z(ivet)=ipnew
                        Call writelog "ip="&ipnew&"&iq="&iqnew&"&np="&npnew,"Измененo начало ветви: "& ip	&" на "& ipnew
                    end if
                    if iq<>iqnew then
                        vet.cols("iq").z(ivet)=iqnew
                        writelog "ip="&ipnew&"&iq="&iqnew&"&np="&npnew,"Изменен конец ветви: "& iq	&" на "& iqnew
                    end if
                    if np<>npnew then
                        vet.cols("np").z(ivet)=npnew
                        Call writelog "ip="&ipnew&"&iq="&iqnew&"&np="&npnew,"Изменен номер параллельности ветви: "& np	&" на "& npnew
                    end if
                else
                    Call writelog "ip="&ip&"&iq="&iq&"&np="&np,"Не найдена ветвь с ip="&ip&"&iq="&iq&"&np="&np
                end if
	        else
		        exit for
	        end if
        next
        if nvetch>0 then Call writelog "!","Изменено ключей ветвей: " & nvetch
        'Nodes keys changing
        nuzlch=0
        for i2=3 to 999999
            if ExcelSet.Worksheets("change").cells(i2,1).value<>"" then
                ny=ExcelSet.Worksheets("change").cells(i2,1).value
                nynew=ExcelSet.Worksheets("change").cells(i2,2).value
                uzl.SetSel("ny="&nynew)
                iuzl = uzl.findnextsel(-1)
                if iuzl<0 then
                    uzl.SetSel("ny=" & ny)
                    iuzl = uzl.findnextsel(-1)
                    if iuzl<>-1 then
                        if ny<>nynew then
                            nuzlch = nuzlch + 1
                            uzl.cols("ny").z(iuzl) = nynew
                            writelog "ny=" & nynew,"Изменен номер узла: " & ny	& " на " & nynew
                        end if
                    else
                        writelog "!!!","Не найден узел с ny=" & ny
                    end if
                else
                    writelog "!!!","Уже существует узел с ny=" & nynew
                end if
            else
                exit for
            end if
        next
        if nuzlch>0 then writelog "!","Изменено ключей узлов: "& nuzlch
        'generator keys changing
        nuzlch=0

for i2=3 to 99999
	if ExcelSet.Worksheets("change").cells(i2,13).value<>"" then
		ny=ExcelSet.Worksheets("change").cells(i2,13).value
		nynew=ExcelSet.Worksheets("change").cells(i2,14).value
		gen.SetSel("Num="&nynew)
		iuzl=gen.findnextsel(-1)
		if iuzl<0 then
			gen.SetSel("Num="&ny)
			iuzl=gen.findnextsel(-1)
			if iuzl<>-1 then
				if ny<>nynew then
					nuzlch=nuzlch+1
					gen.cols("Num").z(iuzl)=nynew
					writelog "Num="&nynew,"Изменен номер генератора: "& ny	&" на "& nynew
				end if

			else
				writelog "!!!","Не найден генератор № "&ny
			end if
		else
			writelog "!!!","Уже существует генератор № "&nynew
		end if
	else
		exit for
	end if
next
if nuzlch>0 then writelog "!","Изменено ключей генераторов: "& nuzlch
'generator PQ keys changing
nuzlch=0
for i2=3 to 99999
	if ExcelSet.Worksheets("change").cells(i2,17).value<>"" then
		ny=ExcelSet.Worksheets("change").cells(i2,17).value
		nynew=ExcelSet.Worksheets("change").cells(i2,18).value
		pq.SetSel("Num="&nynew)
		iuzl=pq.findnextsel(-1)
		if iuzl<0 then
			pq.SetSel("Num="&ny)
			iuzl=pq.findnextsel(-1)
			if iuzl<>-1 then
				if ny<>nynew then
					nuzlch=nuzlch+1
					pq.cols("Num").calc(nynew)
					writelog "Num="&nynew,"Изменена зависимость P(Q) генератора №"& ny	&" на "& nynew
				end if

			else
				writelog "!!!","Не найдена зависимость P(Q) генератора № "&ny
			end if
		else
			writelog "!!!","Уже существует зависимость P(Q) генератора № "&nynew
		end if
	else
		exit for
	end if
next
if nuzlch>0 then writelog "!","Изменено ключей зависимости P(Q) генератора: "& nuzlch
'Изменение номеров СХН
nuzlch=0
for i2=3 to 99999
	if ExcelSet.Worksheets("change").cells(i2,24).value<>"" then
		ny=ExcelSet.Worksheets("change").cells(i2,24).value
		nynew=ExcelSet.Worksheets("change").cells(i2,25).value
		sxn.SetSel("nsx="&nynew)
		iuzl=sxn.findnextsel(-1)
		if iuzl<0 then
			sxn.SetSel("nsx="&ny)
			iuzl=sxn.findnextsel(-1)
			if iuzl<>-1 then
				if ny<>nynew then
					nuzlch=nuzlch+1
					sxn.cols("nsx").calc(nynew)
					writelog "nsx="&nynew,"Изменена зависимость СХН № "& ny	&" на "& nynew
				end if
			else
				writelog "!!!","Не найдена зависимость СХН № "&ny
			end if
		else
			writelog "!!!","Уже существует зависимость СХН № "&nynew
		end if
	else
		exit for
	end if
next
if nuzlch>0 then writelog "!","Изменено ключей зависимости СХН: "& nuzlch
'Изменение номеров Iдоп(t)
nuzlch=0
for i2=3 to 99999
	if ExcelSet.Worksheets("change").cells(i2,31).value<>"" then
		ny=ExcelSet.Worksheets("change").cells(i2,31).value
		nynew=ExcelSet.Worksheets("change").cells(i2,32).value
		git.SetSel("Num="&nynew)
		iuzl=git.findnextsel(-1)
		if iuzl<0 then
			git.SetSel("Num="&ny)
			iuzl=git.findnextsel(-1)
			if iuzl<>-1 then
				if ny<>nynew then
					nuzlch=nuzlch+1
					git.cols("Num").calc(nynew)
					writelog "Num="&nynew,"Изменена зависимость Iдоп(t) № "& ny	&" на "& nynew
				end if
			else
				writelog "!!!","Не найдена зависимость Iдоп(t) № "&ny
			end if
		else
			writelog "!!!","Уже существует зависимость Iдоп(t) № "&nynew
		end if
	else
		exit for
	end if
next
if nuzlch>0 then writelog "!","Изменено ключей зависимости Iдоп(t): "& nuzlch
'Изменение номеров районов
nuzlch=0
for i2=3 to 99999
	if ExcelSet.Worksheets("change").cells(i2,34).value<>"" then
		ny=ExcelSet.Worksheets("change").cells(i2,34).value
		nynew=ExcelSet.Worksheets("change").cells(i2,35).value
		ray.SetSel("na="&nynew)
		iuzl=ray.findnextsel(-1)
		if iuzl<0 then
			ray.SetSel("na="&ny)
			iuzl=ray.findnextsel(-1)
			if iuzl<>-1 then
				if ny<>nynew then
					nuzlch=nuzlch+1
					ray.cols("na").calc(nynew)
					writelog "na="&nynew,"Изменен район № "& ny	&" на "& nynew
				end if
			else
				writelog "!!!","Не найден район № "&ny
			end if
		else
			writelog "!!!","Уже существует район № "&nynew
		end if
	else
		exit for
	end if
next

if nuzlch>0 then writelog "!","Изменено номеров районов: "& nuzlch
'Изменение номеров территорий
nuzlch=0
for i2=3 to 99999
	if ExcelSet.Worksheets("change").cells(i2,38).value<>"" then
		ny=ExcelSet.Worksheets("change").cells(i2,38).value
		nynew=ExcelSet.Worksheets("change").cells(i2,39).value
		ray2.SetSel("npa="&nynew)
		iuzl=ray2.findnextsel(-1)
		if iuzl<0 then
			ray2.SetSel("npa="&ny)
			iuzl=ray2.findnextsel(-1)
			if iuzl<>-1 then
				if ny<>nynew then
					nuzlch=nuzlch+1
					ray2.cols("npa").calc(nynew)
					writelog "npa="&nynew,"Изменена территория № "& ny	&" на "& nynew
				end if
			else
				writelog "!!!","Не найдена территория № "&ny
			end if
		else
			writelog "!!!","Уже существует территория № "&nynew
		end if
	else
		exit for
	end if
next
if nuzlch>0 then writelog "!","Изменено номеров территорий: "& nuzlch
'Изменение номеров сечений
if sec_need>0 and sec_name(ifile)<>"" then
nuzlch=0
for i2=3 to 99999
	if ExcelSet.Worksheets("change").cells(i2,20).value<>"" then
		ny=ExcelSet.Worksheets("change").cells(i2,20).value
		nynew=ExcelSet.Worksheets("change").cells(i2,21).value
		sec.SetSel("ns="&nynew)
		iuzl=ray.findnextsel(-1)
		if iuzl<0 then
			sec.SetSel("ns="&ny)
			iuzl=sec.findnextsel(-1)
			if iuzl<>-1 then
				if ny<>nynew then
					nuzlch=nuzlch+1
					sec.cols("ns").calc(nynew)
					writelog "ns="&nynew,"Изменен номер сечения "& ny	&" на "& nynew
				end if
			else
				writelog "!!!","Не найдено сечение № "&ny
			end if
		else
			writelog "!!!","Уже существует сечение № "&nynew
		end if
	else
		exit for
	end if
next
if nuzlch>0 then writelog "!","Изменено номеров сечений: "& nuzlch
end if
'Изменение номеров таблицы анцапф
if anc_need>0 and anc_name(ifile)<>"" then
nuzlch=0
for i2=3 to 99999
	if ExcelSet.Worksheets("change").cells(i2,27).value<>"" then
		ny=ExcelSet.Worksheets("change").cells(i2,27).value
		nynew=ExcelSet.Worksheets("change").cells(i2,28).value
		anc.SetSel("nbd="&nynew)
		iuzl=anc.findnextsel(-1)
		if iuzl<0 then
			anc.SetSel("nbd="&ny)
			iuzl=anc.findnextsel(-1)
			if iuzl<>-1 then
				if ny<>nynew then
					nuzlch=nuzlch+1
					anc.cols("nbd").calc(nynew)
					writelog "nbd="&nynew,"Изменен номер в таблице анцапф "& ny	&" на "& nynew
				end if
			else
				writelog "!!!","Не найден номер в таблице анцапф № "&ny
			end if
		else
			writelog "!!!","Уже существует номер в таблице анцапф № "&nynew
		end if
	else
		exit for
	end if
next
if nuzlch>0 then writelog "!","Изменено номеров в таблице анцапф: "& nuzlch
end if
t.RenumWP=False
else
writelog "!","Вкладка изменения ключей отсутствует!!!"
end if
'=========================== vetv ===============================
On Error Resume Next
	oooo0=ExcelSet.Worksheets("vetv").cells(3,1).value
	fffff=Err.Number
 	If fffff = 0 Then
nvet=0
for i2=3 to 999999
	if ExcelSet.Worksheets("vetv").cells(i2,1).value<>"" then
		nvet=nvet+1
		ip=ExcelSet.Worksheets("vetv").cells(i2,1).value
		iq=ExcelSet.Worksheets("vetv").cells(i2,2).value
		np=ExcelSet.Worksheets("vetv").cells(i2,3).value
		if np="" then np=0
		vybornotvyb=0
		If ExcelSet.Worksheets("vetv").cells(i2,4).value=66666 or ExcelSet.Worksheets("vetv").cells(i2,4).value=77777 Then
			vyborka=ip
			vybornotvyb=1
		else
			vyborka="ip="&ip&"&iq="&iq&"&np="&np
		end if
		vet.SetSel(vyborka)'&")|(iq="&ip&"&ip="&iq&"&np="&np&")"
		vetcount=vet.count
		ivet=vet.findnextsel(-1)
		if ivet<>-1 then
			if ExcelSet.Worksheets("vetv").cells(i2,4).value=666 or ExcelSet.Worksheets("vetv").cells(i2,4).value=66666 then
				vet.delrows
				if vetcount=1 then
					writelog vyborka,"Ветвь "&vyborka&" удалена!!!"
				else
					writelog vyborka,vetcount&" ветвей по выборке: "&vyborka&" удалены!!!"
				end if
			else
				while ivet<>-1
					if vybornotvyb=1 then
						ip=vet.cols("ip").zn(ivet)
						iq=vet.cols("iq").zn(ivet)
						np=vet.cols("np").zn(ivet)
					end if
					for i3=5 to 100
						if ExcelSet.Worksheets("vetv").cells(2,i3).value<>"" then

							col=ExcelSet.Worksheets("vetv").cells(2,i3).value
							if col<>"name" then
								oldvalue=vet.cols(col).zn(ivet)
								newvalue=ExcelSet.Worksheets("vetv").cells(i2,i3).value
								'if col="sta" then msgbox "SSSS "&"ip="&ip&"&iq="&iq&"&np="&np &": " &	col&"  oldvalue ="&oldvalue	&"  newvalue = "&newvalue
								if col="dname" then
									if oldvalue<>newvalue  then
										vet.cols(col).zn(ivet)=newvalue
										writelog vyborka,"Изменен параметр ветви "&"ip="&ip&"&iq="&iq&"&np="&np &": " &	col&":  стар.="& oldvalue&"  нов.= "&newvalue
									end if
								else
									if newvalue="" then newvalue=0
									if oldvalue<>newvalue  then
										if (col="r" or col="x" or col="b" or col="g") then
											if abs(newvalue-oldvalue)>=0.005  then
												vet.cols(col).zn(ivet)=newvalue
												writelog vyborka,"Изменен параметр ветви "&"ip="&ip&"&iq="&iq&"&np="&np &": " &	col&":  стар.="& oldvalue&"  нов.= "&newvalue
											end if
										else
											if col="ktr" then
												if abs(newvalue-oldvalue)>=0.0001 then
													vet.cols(col).zn(ivet)=newvalue
													writelog vyborka,"Изменен параметр ветви "&"ip="&ip&"&iq="&iq&"&np="&np &": " &	col&":  стар.="& oldvalue&"  нов.= "&newvalue
												end if
											else
												vet.cols(col).zn(ivet)=newvalue
												writelog vyborka,"Изменен параметр ветви "&"ip="&ip&"&iq="&iq&"&np="&np &": " &	col&":  стар.="& oldvalue&"  нов.= "&newvalue
											end if
										end if
									end if
								end if
							end if
						else
							exit for
						end if
					next
					ivet=vet.findnextsel(ivet)
				wend
			end if
		else
			if ExcelSet.Worksheets("vetv").cells(i2,4).value=666 or ExcelSet.Worksheets("vetv").cells(i2,4).value=66666 then
				Call writelog "!!!","Ветвь (ветви) для удаления " & vyborka & " не существует!!! "
			else
				If ExcelSet.Worksheets("vetv").cells(i2,4).value=77777 Then
					Call writelog "!!!","Ветви по выборке: " & vyborka & " не существуют!!! "
				else
					Call writelog vyborka,"Новая Ветвь " & "ip=" & ip & "&iq=" & iq & "&np=" & np & " создана!!! "
					ivet=0
					vet.insrow ivet
					vet.cols("ip").z(ivet)=ip
					vet.cols("iq").z(ivet)=iq
					vet.cols("np").z(ivet)=np
					for i3=5 to 100
						if ExcelSet.Worksheets("vetv").cells(2,i3).value <> "" then
							col=ExcelSet.Worksheets("vetv").cells(2,i3).value
							if vet.cols(col).zn(ivet)<>ExcelSet.Worksheets("vetv").cells(i2,i3).value and col <> "name" then
								vet.cols(col).zn(ivet)=ExcelSet.Worksheets("vetv").cells(i2,i3).value
								'writelog "!","Добавлен параметр новой ветви "&"ip="&ip&"&iq="&iq&"&np="&np &": " &	col
							end if
						else
							exit for
						end if
					next
				end if
			end if
		end if
	else
		exit for
	end if
next
    Call writelog "!","Изменено ветвей: "& nvet
		else
			Call writelog "!","Вкладка изменения ветвей отсутствует!!!"
		end if
'=========================== node ===============================
On Error Resume Next
oooo0=ExcelSet.Worksheets("node").cells(3,1).value
If Err.Number = 0 Then
nuzl=0
for i2=3 to 999999
	if ExcelSet.Worksheets("node").cells(i2,1).value<>"" then
		nuzl=nuzl+1
		ny=ExcelSet.Worksheets("node").cells(i2,1).value
		vybornotvyb=0
		If ExcelSet.Worksheets("node").cells(i2,2).value=66666 or ExcelSet.Worksheets("node").cells(i2,2).value=77777 Then
			vyborka=ny
			vybornotvyb=1
		else
			vyborka="ny="&ny
		end if
		uzl.SetSel(vyborka)
		iuzl=uzl.findnextsel(-1)
		if iuzl<>-1 then
			if ExcelSet.Worksheets("node").cells(i2,2).value=666 or ExcelSet.Worksheets("node").cells(i2,2).value=66666 then
				uzl.delrows
				Call writelog vyborka, " Узел "& vyborka & " удален!!!"
			else
			   if ExcelSet.Worksheets("node").cells(i2,2).value<>77777 then
				for i3=3 to 100
					if ExcelSet.Worksheets("node").cells(2,i3).value<>"" then
						col=ExcelSet.Worksheets("node").cells(2,i3).value
						oldvalue=uzl.cols(col).zn(iuzl)
						newvalue=ExcelSet.Worksheets("node").cells(i2,i3).value
						if newvalue="" and col<>"name" then newvalue=0
						if oldvalue<>newvalue then
							if (col="pn" or col="qn" or col="pg" or col="qg" or col="qmin" or col="qmax" or col="vzd" or col="bsh") then
								if abs(newvalue-oldvalue)>=0.1  then
									uzl.cols(col).zn(iuzl)=newvalue
									Call writelog "ny="&ny,"Изменен параметр узла "&"ny="&ny&" параметр "&col	&":  стар.="& oldvalue&"  нов.= "&newvalue
								end if
							else
								uzl.cols(col).zn(iuzl)=newvalue
								Call writelog "ny=" & ny,"Изменен параметр узла " & "ny=" & ny & " параметр " & col	& ":  стар.=" & oldvalue&"  нов.= "&newvalue
							end if
						end if
					else
						exit for
					end if
				next
			    else
			    	for i3=3 to 100
					if ExcelSet.Worksheets("node").cells(2,i3).value<>"" then
						col=ExcelSet.Worksheets("node").cells(2,i3).value
						newvalue=ExcelSet.Worksheets("node").cells(i2,i3).value
						if newvalue="" then newvalue=0
						if col<>"name" then uzl.cols(col).calc(newvalue)
						Call writelog vyborka,"Изменен параметрs узлs vyborka=" & vyborka & " параметр " & col & "  нов.zn= " & newvalue
					else
						exit for
					end if
				next
			    end if
			end if
		else
			if ExcelSet.Worksheets("node").cells(i2,2).value=666 then
				writelog "ny="&ny,"Узел для удаления "&"ny="&ny&" не существует!!!"
			else
				writelog "ny="&ny,"Новый Узел "&"ny="&ny&" создан!!! "
				iuzl=0
				uzl.insrow iuzl
				uzl.cols("ny").z(iuzl)=ny
				for i3=3 to 100
					if ExcelSet.Worksheets("node").cells(2,i3).value<>"" then
						col=ExcelSet.Worksheets("node").cells(2,i3).value
						if uzl.cols(col).zn(iuzl)<>ExcelSet.Worksheets("node").cells(i2,i3).value then
							uzl.cols(col).zn(iuzl)=ExcelSet.Worksheets("node").cells(i2,i3).value
							'writelog "Добавлен параметр нового узла "&"ny="&ny&" параметр "&	col
						end if
					else
						exit for
					end if
				next
			end if
		end if
	else
		exit for
	end if
next
    writelog "!","Изменено узлов: "& nuzl
		else
			writelog "!","Вкладка изменения узлов отсутствует!!!"
		end if
'=========================== I ===============================
	On Error Resume Next
	oooo0=ExcelSet.Worksheets("I").cells(3,1).value
 	If Err.Number = 0 Then
ni=0
for i2=3 to 999999
	if ExcelSet.Worksheets("I").cells(i2,1).value<>"" then
		ni=ni+1
		ip=ExcelSet.Worksheets("I").cells(i2,1).value
		iq=ExcelSet.Worksheets("I").cells(i2,2).value
		np=ExcelSet.Worksheets("I").cells(i2,3).value
		if np="" then np=0
		vet.SetSel("(ip="&ip&"&iq="&iq&"&np="&np&")|(iq="&ip&"&ip="&iq&"&np="&np&")")
		ivet=vet.findnextsel(-1)
		if ivet<>-1 then
			if setiav=0 then
				for i3=6 to 9
						col=ExcelSet.Worksheets("I").cells(2,i3).value
						newvalue=ExcelSet.Worksheets("I").cells(i2,i3).value
						oldvalue=vet.cols(col).zn(ivet)
						if newvalue<>oldvalue then
							vet.cols(col).zn(ivet)=ExcelSet.Worksheets("I").cells(i2,i3).value
							writelog "ip="&ip&"&iq="&iq&"&np="&np,"Изменен параметр ветви "&"ip="&ip&"&iq="&iq&"&np="&np &": " &	col&":  стар.="& oldvalue&"  нов.= "&newvalue
						end if
				next
			else
						col=ExcelSet.Worksheets("I").cells(2,6).value
						newvalue=ExcelSet.Worksheets("I").cells(i2,6).value
						oldvalue=vet.cols(col).zn(ivet)
						if newvalue<>oldvalue then
							vet.cols(col).zn(ivet)=ExcelSet.Worksheets("I").cells(i2,i3).value
							writelog "ip="&ip&"&iq="&iq&"&np="&np,"Изменен параметр ветви "&"ip="&ip&"&iq="&iq&"&np="&np &": " &	col&":  стар.="& oldvalue&"  нов.= "&newvalue
						end if
				for i3=10 to 12
						col=ExcelSet.Worksheets("I").cells(2,i3-setiav).value
						newvalue=ExcelSet.Worksheets("I").cells(i2,i3).value
						if newvalue="" or newvalue=0 then newvalue=ExcelSet.Worksheets("I").cells(i2,i3-setiav).value
						oldvalue=vet.cols(col).zn(ivet)
						if newvalue<>oldvalue then
							vet.cols(col).zn(ivet)=ExcelSet.Worksheets("I").cells(i2,i3).value
							writelog "ip="&ip&"&iq="&iq&"&np="&np,"Изменен параметр ветви "&"ip="&ip&"&iq="&iq&"&np="&np &": " &	col&":  стар.="& oldvalue&"  нов.= "&newvalue
						end if
				next
			end if
		else
			writelog "!!!","Ветви для изменения токов "&"ip="&ip&"&iq="&iq&"&np="&np &" не существует!!! "
		end if
	else
		exit for
	end if
next
    writelog "!","Изменено токов: "& ni
		else
			writelog "!","Вкладка изменения токов отсутствует!!!"
		end if
'=========================== n_it ===============================
	On Error Resume Next
	oooo0=ExcelSet.Worksheets("n_it").cells(3,1).value
 	If Err.Number = 0 Then
nit=0
for i2=3 to 99999
	if ExcelSet.Worksheets("n_it").cells(i2,1).value<>"" then
		nit=nit+1
		Num=ExcelSet.Worksheets("n_it").cells(i2,1).value
		Tc=ExcelSet.Worksheets("n_it").cells(i2,2).value
		if Tc="" then Tc=0
		git.SetSel("Num="&Num&"&Tc="&Tc)
		ivet=git.findnextsel(-1)
		if ivet<>-1 then
			if ExcelSet.Worksheets("n_it").cells(i2,3).value=666 then
				git.delrows
				writelog "Num="&Num&"&Tc="&Tc,"Удален параметр I доп (t)  Num="&Num&" Tc="&Tc
			else
						col=ExcelSet.Worksheets("n_it").cells(2,4).value
						newvalue=ExcelSet.Worksheets("n_it").cells(i2,4).value
						oldvalue=git.cols(col).zn(ivet)
						if git.cols(col).zn(ivet)<>ExcelSet.Worksheets("n_it").cells(i2,4).value then
							git.cols(col).zn(ivet)=ExcelSet.Worksheets("n_it").cells(i2,4).value
							writelog "Num="&Num&"&Tc="&Tc,"Изменен параметр I доп (t)  Num="&Num&" Tc="&Tc&" параметр "&col&":  стар.="& oldvalue&"  нов.= "&newvalue
						end if
			end if
		else
			if ExcelSet.Worksheets("n_it").cells(i2,3).value=666 then
				writelog "!!!","I доп (t) для удаления  "&"Num="&Num&"&Tc="&Tc &" не существует!!! "
			else
				writelog "Num="&Num&"&Tc="&Tc,"Новый I доп (t) "&"Num="&Num&"&Tc="&Tc &" создан!!! "
				ivet=0
				git.insrow ivet
				git.cols("Num").z(ivet)=Num
				git.cols("Tc").z(ivet)=Tc
						col=ExcelSet.Worksheets("n_it").cells(2,4).value
						if git.cols(col).zn(ivet)<>ExcelSet.Worksheets("n_it").cells(i2,4).value then
							git.cols(col).zn(ivet)=ExcelSet.Worksheets("n_it").cells(i2,4).value
							'writelog "!","Добавлен I доп (t)  Num="&Num&" Tc="&Tc&" параметр "&col
						end if
			end if
		end if
	else
		exit for
	end if
next
    writelog "!","Изменено зависимостей I доп (t) : "& nit
		else
			writelog "!","Вкладка изменения токовых зависимостей отсутствует!!!"
		end if
'=========================== gen ===============================
	On Error Resume Next
	oooo0=ExcelSet.Worksheets("gen").cells(3,1).value
 	If Err.Number = 0 Then
ng=0
for i2=3 to 99999
	if ExcelSet.Worksheets("gen").cells(i2,1).value<>"" then
		ng=ng+1
		Num=ExcelSet.Worksheets("gen").cells(i2,1).value
		gen.SetSel("Num="&Num)
		iuzl=gen.findnextsel(-1)
		if iuzl<>-1 then
			if ExcelSet.Worksheets("gen").cells(i2,2).value=666 then
				gen.delrows
				writelog "Num="&Num,"Генератор "&"Num="&Num&" удален!!!"
			else
				for i3=3 to 100
					if ExcelSet.Worksheets("gen").cells(2,i3).value<>"" then
						col=ExcelSet.Worksheets("gen").cells(2,i3).value
						oldvalue=gen.cols(col).zn(iuzl)
						newvalue=ExcelSet.Worksheets("gen").cells(i2,i3).value
						if oldvalue<>newvalue then
							gen.cols(col).zn(iuzl)=ExcelSet.Worksheets("gen").cells(i2,i3).value
							writelog "Num="&Num,"Изменен параметр генератора "&"Num="&Num&" параметр "&	col	&":  стар.="& oldvalue&"  нов.= "&newvalue
						end if
					else
						exit for
					end if
				next
			end if
		else
			if ExcelSet.Worksheets("gen").cells(i2,2).value=666 then
				writelog "!!!","генератор для удаления  "&"Num="&Num&" не существует!!! "
			else
				writelog "Num="&Num,"Новый генератор с Num="&Num&" создан!!! "
				iuzl=0
				gen.insrow iuzl
				gen.cols("Num").z(iuzl)=Num
				for i3=3 to 100
					if ExcelSet.Worksheets("gen").cells(2,i3).value<>"" then
						col=ExcelSet.Worksheets("gen").cells(2,i3).value
						newvalue=ExcelSet.Worksheets("gen").cells(i2,i3).value
						gen.cols(col).zn(iuzl)=ExcelSet.Worksheets("gen").cells(i2,i3).value
						'writelog "!","Добавлен параметр нового генератора "&"Num="&Num&" параметр "&	col&"  oldvalue ="& oldvalue&"  newvalue = "&newvalue
					else
						exit for
					end if
				next
			end if
		end if
	else
		exit for
	end if
next
    writelog "!","Изменено генераторов: "& ng
		else
			writelog "!","Вкладка изменения генераторов отсутствует!!!"
		end if
'=========================== PQ ===============================
	On Error Resume Next
	oooo0=ExcelSet.Worksheets("PQ").cells(2,1).value
 	If Err.Number = 0 Then
npq=0
for i2=3 to 99999
	if ExcelSet.Worksheets("PQ").cells(i2,1).value<>"" then
		npq=npq+1
		Num=ExcelSet.Worksheets("PQ").cells(i2,1).value
		P=ExcelSet.Worksheets("PQ").cells(i2,2).value
		if P="" then P=0
		pq.SetSel("Num="&Num&"&P="&P)
		ivet=pq.findnextsel(-1)
		if ivet<>-1 then
			if ExcelSet.Worksheets("PQ").cells(i2,3).value=666 then
				pq.delrows
				writelog "Num="&Num&"&P="&P,"Удален элемент PQ-диаграммы  Num="&Num&" P="&P
			else
				for i3=4 to 5
					if ExcelSet.Worksheets("PQ").cells(2,i3).value<>"" then
						col=ExcelSet.Worksheets("PQ").cells(2,i3).value
						if pq.cols(col).z(ivet)<>ExcelSet.Worksheets("PQ").cells(i2,i3).value then
							pq.cols(col).z(ivet)=ExcelSet.Worksheets("PQ").cells(i2,i3).value
							writelog "Num="&Num&" P="&P,"Изменен параметр PQ  Num="&Num&" P="&P&" параметр "&col&":  стар.="& oldvalue&"  нов.= "&newvalue
						end if
					end if
				next
			end if
		else
			if ExcelSet.Worksheets("PQ").cells(i2,3).value=666 then
				writelog "!!!","PQ для удаления  "&"Num="&Num&"&P="&P &" не существует!!! "
			else
				writelog "Num="&Num&" P="&P,"Новый PQ Num="&Num&"&P="&P &" создан!!! "
				ivet=0
				pq.insrow ivet
				pq.cols("Num").z(ivet)=Num
				pq.cols("P").z(ivet)=P
				for i3=4 to 5
					if ExcelSet.Worksheets("PQ").cells(2,i3).value<>"" then
						col=ExcelSet.Worksheets("PQ").cells(2,i3).value
						pq.cols(col).z(ivet)=ExcelSet.Worksheets("PQ").cells(i2,i3).value
						'writelog "!","Новый параметр PQ  Num="&Num&" P="&P&" параметр "&col
					end if
				next
			end if
		end if
	else
		exit for
	end if
next
 writelog "!","Изменено зависимостей PQ : "& npq
		else
			writelog "!","Вкладка изменения мощностных зависимостей отсутствует!!!"
		end if
'==========================================  - СХН -  ===========================================
	On Error Resume Next
	oooo0=ExcelSet.Worksheets("sxn").cells(3,1).value
 	If Err.Number = 0 Then
nsxn=0
for i2=3 to 99999
	if ExcelSet.Worksheets("sxn").cells(i2,1).value<>"" then
		nsxn=nsxn+1
		nsx=ExcelSet.Worksheets("sxn").cells(i2,1).value
		sxn.SetSel("nsx="&nsx)
		isxn=sxn.findnextsel(-1)
		if isxn<>-1 then
			if ExcelSet.Worksheets("sxn").cells(i2,2).value=666 then
				sxn.delrows
				writelog "nsx="&nsx,"Удалена СХН nsx="&nsx
			else
				for i3=3 to 30
					if ExcelSet.Worksheets("sxn").cells(2,i3).value<>"" then
						col=ExcelSet.Worksheets("sxn").cells(2,i3).value
						oldvalue=sxn.cols(col).zn(isxn)
						newvalue=ExcelSet.Worksheets("sxn").cells(i2,i3).value
						if oldvalue<>newvalue then
							sxn.cols(col).zn(isxn)=ExcelSet.Worksheets("sxn").cells(i2,i3).value
							writelog "nsx="&nsx,"Изменен параметр СХН "&"nsx="&nsx&" параметр "&	col	&":  стар.="& oldvalue&"  нов.= "&newvalue
						end if
					else
						exit for
					end if
				next
			end if
		else
			if ExcelSet.Worksheets("sxn").cells(i2,2).value=666 then
				writelog "!!!","СХН для удаления  "&"nsx="&nsx&" не существует!!! "
			else
				writelog "nsx="&nsx,"Новая СХН с nsx="&nsx&" создана!!! "
				isxn=0
				sxn.insrow isxn
				sxn.cols("nsx").z(isxn)=nsx
				for i3=3 to 30
					if ExcelSet.Worksheets("sxn").cells(2,i3).value<>"" then
						col=ExcelSet.Worksheets("sxn").cells(2,i3).value
						newvalue=ExcelSet.Worksheets("sxn").cells(i2,i3).value

						sxn.cols(col).zn(isxn)=ExcelSet.Worksheets("sxn").cells(i2,i3).value
						'writelog "!","Добавлен параметр нового генератора "&"Num="&Num&" параметр "&	col&"  oldvalue ="& oldvalue&"  newvalue = "&newvalue

					else
						exit for
					end if
				next
			end if
		end if
	else
		exit for
	end if
next
writelog "!","Изменено СХН: "& nsxn
		else
			writelog "!","Вкладка изменения СХН отсутствует!!!"
		end if

'==========================================  - Районы -  ===========================================
	On Error Resume Next
	oooo0=ExcelSet.Worksheets("area").cells(3,1).value
 	If Err.Number = 0 Then

narea=0
for i2=3 to 99999
	if ExcelSet.Worksheets("area").cells(i2,1).value<>"" then
		narea=narea+1
		na=ExcelSet.Worksheets("area").cells(i2,1).value
		ray.SetSel("na="&na)
		ina=ray.findnextsel(-1)
		if ina<>-1 then
			if ExcelSet.Worksheets("area").cells(i2,2).value=666 then
				ray.delrows
				writelog "na="&na,"Удален из таблицы район na="&na
			else
				if ExcelSet.Worksheets("area").cells(i2,2).value=66666 or ExcelSet.Worksheets("area").cells(i2,2).value=77777 or ExcelSet.Worksheets("area").cells(i2,2).value=66677 then
					needtodel=1
					if ExcelSet.Worksheets("area").cells(i2,2).value=66666 then uzl.SetSel("na="&na)
					if ExcelSet.Worksheets("area").cells(i2,2).value=77777 then uzl.SetSel("na!="&na)
					if ExcelSet.Worksheets("area").cells(i2,2).value=66677 then
						vybbbb=ExcelSet.Worksheets("area").cells(i2,4).value
						if vybbbb<>"" then uzl.SetSel(vybbbb&"&na="&na) else uzl.SetSel("na="&na)
					end if
					uzl.cols("muskod").calc(66666)
					if ExcelSet.Worksheets("area").cells(i2,2).value=66677 and vybbbb<>"" then
						writelog vybbbb&"&na!="&na,"Удален район na="&na&" по выборке="&vybbbb
					else
						writelog "na="&na,"Удален совсем район na="&na
					end if
				else
					for i3=3 to 30
						if ExcelSet.Worksheets("area").cells(2,i3).value<>"" then
							col=ExcelSet.Worksheets("area").cells(2,i3).value
							oldvalue=ray.cols(col).zn(ina)
							newvalue=ExcelSet.Worksheets("area").cells(i2,i3).value
							if oldvalue<>newvalue then
								ray.cols(col).zn(ina)=ExcelSet.Worksheets("area").cells(i2,i3).value
								writelog "na="&na,"Изменен параметр района "&"na="&na&", параметр "&	col	&":  стар.="& oldvalue&"  нов.= "&newvalue
							end if
						else
							exit for
						end if
					next
				end if
			end if
		else
			if ExcelSet.Worksheets("area").cells(i2,2).value=666 then
				writelog "!!!","Район для удаления  "&"na="&na&" не существует!!! "
			else
				writelog "na="&na,"Новый район na="&na&" создан!!! "
				ina=0

				ray.insrow ina

				ray.cols("na").z(ina)=na

				for i3=3 to 30
					if ExcelSet.Worksheets("area").cells(2,i3).value<>"" then
						col=ExcelSet.Worksheets("area").cells(2,i3).value
						newvalue=ExcelSet.Worksheets("area").cells(i2,i3).value

						ray.cols(col).zn(ina)=ExcelSet.Worksheets("area").cells(i2,i3).value
					else
						exit for
					end if
				next
			end if
		end if
	else
		exit for
	end if
next
writelog "!","Изменено районов: "& narea
		else
			writelog "!","Вкладка изменения районов отсутствует!!!"
		end if
'============================== - Территории - ==============================================
	On Error Resume Next
	oooo0=ExcelSet.Worksheets("area2").cells(3,1).value
 	If Err.Number = 0 Then

narea=0
for i2=3 to 99999
	if ExcelSet.Worksheets("area2").cells(i2,1).value<>"" then
		narea=narea+1
		na=ExcelSet.Worksheets("area2").cells(i2,1).value
		ray2.SetSel("npa="&na)
		ina=ray2.findnextsel(-1)
		if ina<>-1 then
			if ExcelSet.Worksheets("area2").cells(i2,2).value=666 then
				ray2.delrows
				writelog "npa="&na,"Удалена из таблицы территория npa="&na
			else
				if ExcelSet.Worksheets("area2").cells(i2,2).value=66666 then
					needtodel=1
					uzl.SetSel("npa="&na)
					uzl.cols("muskod").calc(66666)
					writelog "npa="&na,"Удалена совсем территория npa="&na
				else
					for i3=3 to 30
						if ExcelSet.Worksheets("area2").cells(2,i3).value<>"" then
							col=ExcelSet.Worksheets("area2").cells(2,i3).value
							oldvalue=ray2.cols(col).zn(ina)
							newvalue=ExcelSet.Worksheets("area2").cells(i2,i3).value
							if oldvalue<>newvalue then
								ray2.cols(col).zn(ina)=ExcelSet.Worksheets("area").cells(i2,i3).value
								writelog "npa="&na,"Изменен параметр территории "&"npa="&na&", параметр "&	col	&":  стар.="& oldvalue&"  нов.= "&newvalue
							end if
						else
							exit for
						end if
					next
				end if
			end if
		else
			if ExcelSet.Worksheets("area2").cells(i2,2).value=666 then
				writelog "!!!","Территория для удаления  "&"npa="&na&" не существует!!! "
			else
				writelog "npa="&na,"Новая территория npa="&na&" создана!!! "
				ina=0
				ray2.insrow ina
				ray2.cols("npa").z(ina)=na
				for i3=3 to 30
					if ExcelSet.Worksheets("area2").cells(2,i3).value<>"" then
						col=ExcelSet.Worksheets("area2").cells(2,i3).value
						newvalue=ExcelSet.Worksheets("area2").cells(i2,i3).value
						ray2.cols(col).zn(ina)=ExcelSet.Worksheets("area2").cells(i2,i3).value
					else
						exit for
					end if
				next
			end if
		end if
	else
		exit for
    	end if
next
    writelog "!","Изменено территорий: "& narea
		else
			writelog "!","Вкладка изменения территорий отсутствует!!!"
		end if
'============================== - Сечения - ==============================================
			if sec_need>0 and sec_name(ifile)<>"" then
	On Error Resume Next
	oooo0=ExcelSet.Worksheets("sech").cells(3,1).value
 	If Err.Number = 0 Then
narea=0
for i2=3 to 99999
	if ExcelSet.Worksheets("sech").cells(i2,1).value<>"" then
		narea=narea+1
		na=ExcelSet.Worksheets("sech").cells(i2,1).value
		sec.SetSel("ns="&na)
		ina=sec.findnextsel(-1)
		if ina<>-1 then
			if ExcelSet.Worksheets("sech").cells(i2,2).value=666 then
				sec.delrows
				writelog "ns="&na,"Удалено сечение "&"ns="&na
			else
				for i3=3 to 30
					if ExcelSet.Worksheets("sech").cells(2,i3).value<>"" then
						col=ExcelSet.Worksheets("sech").cells(2,i3).value
						oldvalue=sec.cols(col).zn(ina)
						newvalue=ExcelSet.Worksheets("sech").cells(i2,i3).value
						if oldvalue<>newvalue then
							sec.cols(col).zn(ina)=ExcelSet.Worksheets("sech").cells(i2,i3).value
							writelog "ns="&na,"Изменен параметр сечения "&"ns="&na&", параметр "&	col	&":  стар.="& oldvalue&"  нов.= "&newvalue
						end if
					else
						exit for
					end if
				next
			end if
		else
			if ExcelSet.Worksheets("sech").cells(i2,2).value=666 then
				writelog "!!!","Сечение для удаления  ns="&na&" не существует!!! "
			else
				writelog "ns="&na,"Новое сечение ns="&na&" создано!!! "
				ina=0
				sec.insrow ina
				sec.cols("ns").z(ina)=na
				for i3=3 to 30
					if ExcelSet.Worksheets("sech").cells(2,i3).value<>"" then
						col=ExcelSet.Worksheets("sech").cells(2,i3).value
						newvalue=ExcelSet.Worksheets("sech").cells(i2,i3).value
						sec.cols(col).zn(ina)=ExcelSet.Worksheets("sech").cells(i2,i3).value
					else
						exit for
					end if
				next
			end if
		end if
	else
		exit for
	end if
next
    writelog "!","Изменено сечений: "& narea
		else
			writelog "!","Вкладка изменения сечений отсутствует!!!"
		end if
'============================== - Группы линий сечений - ==============================================
	On Error Resume Next
	oooo0=ExcelSet.Worksheets("grline").cells(3,1).value
 	If Err.Number = 0 Then
npq=0
for i2=3 to 99999
	if ExcelSet.Worksheets("grline").cells(i2,1).value<>"" then
		npq=npq+1
		ns=ExcelSet.Worksheets("grline").cells(i2,1).value
		ip=ExcelSet.Worksheets("grline").cells(i2,2).value
		iq=ExcelSet.Worksheets("grline").cells(i2,3).value
		grline.SetSel("ns="&ns&"&ip="&ip&"&iq="&iq)
		ivet=grline.findnextsel(-1)
		if ivet<>-1 then
			if ExcelSet.Worksheets("grline").cells(i2,4).value=666 then
				grline.delrows
				writelog "ns="&ns&"&ip="&ip&"&iq="&iq,"Удален элемент Группы линий сечений  ns="&ns&"&ip="&ip&"&iq="&iq
			else
				for i3=5 to 30
					if ExcelSet.Worksheets("grline").cells(2,i3).value<>"" then
						col=ExcelSet.Worksheets("grline").cells(2,i3).value
						if grline.cols(col).z(ivet)<>ExcelSet.Worksheets("grline").cells(i2,i3).value then
							grline.cols(col).z(ivet)=ExcelSet.Worksheets("grline").cells(i2,i3).value
							writelog "ns="&ns&"&ip="&ip&"&iq="&iq,"Изменен параметр Группы линий сечений  ns="&ns&"&ip="&ip&"&iq="&iq&": "&	col	&":  стар.="& oldvalue&"  нов.= "&newvalue
						end if
					end if
				next
			end if
		else
			if ExcelSet.Worksheets("grline").cells(i2,4).value=666 then
				writelog "!!!","Группа линий сечений для удаления   ns="&ns&"&ip="&ip&"&iq="&iq		 &" не существует!!! "
			else
				writelog "ns="&ns&"&ip="&ip&"&iq="&iq,"Новая Группа линий сечений ns="&ns&"&ip="&ip&"&iq="&iq	&" создан!!! "
				ivet=0
				grline.insrow ivet
				grline.cols("ns").z(ivet)=ns
				grline.cols("ip").z(ivet)=ip
				grline.cols("iq").z(ivet)=iq
				for i3=5 to 30
					if ExcelSet.Worksheets("grline").cells(2,i3).value<>"" then
						col=ExcelSet.Worksheets("grline").cells(2,i3).value
						grline.cols(col).z(ivet)=ExcelSet.Worksheets("grline").cells(i2,i3).value
						'writelog "!","Новый параметр PQ  Num="&Num&" P="&P&" параметр "&col
					end if
				next
			end if
		end if
	else
		exit for
	end if
next
    writelog "!","Изменено Групп линий сечений : "& npq
		else
			writelog "!","Вкладка изменения сечений отсутствует!!!"
		end if
		end if
'============================== - Анцапфы - ==============================================
			if anc_need>0 and anc_name(ifile)<>"" then
	On Error Resume Next
	oooo0=ExcelSet.Worksheets("anc").cells(3,1).value
 	If Err.Number = 0 Then
narea=0
for i2=3 to 99999
	if ExcelSet.Worksheets("anc").cells(i2,1).value<>"" then
		narea=narea+1
		na=ExcelSet.Worksheets("anc").cells(i2,1).value
		anc.SetSel("nbd="&na)
		ina=anc.findnextsel(-1)
		if ina<>-1 then
			if ExcelSet.Worksheets("anc").cells(i2,2).value=666 then
				anc.delrows
				writelog "nbd="&na,"Удалены анцапфы с nbd="&na
			else
				for i3=3 to 30
					if ExcelSet.Worksheets("anc").cells(2,i3).value<>"" then
						col=ExcelSet.Worksheets("anc").cells(2,i3).value
						oldvalue=anc.cols(col).zn(ina)
						newvalue=ExcelSet.Worksheets("anc").cells(i2,i3).value
						if oldvalue<>newvalue then
							anc.cols(col).zn(ina)=ExcelSet.Worksheets("anc").cells(i2,i3).value
							writelog "nbd="&na,"Изменен параметр анцапфы nbd="&na&", параметр "&	col	&":  стар.="& oldvalue&"  нов.= "&newvalue
						end if
					else
						exit for
					end if
				next
			end if
		else
			if ExcelSet.Worksheets("anc").cells(i2,2).value=666 then
				writelog "!!!","Анцапфы для удаления  nbd="&na&" не существует!!! "
			else
				writelog "nbd="&na,"Новые анцапфы nbd="&na&" создан!!! "
				ina=0
				anc.insrow ina
				anc.cols("nbd").z(ina)=na
				for i3=3 to 30
					if ExcelSet.Worksheets("anc").cells(2,i3).value<>"" then
						col=ExcelSet.Worksheets("anc").cells(2,i3).value
						newvalue=ExcelSet.Worksheets("anc").cells(i2,i3).value
    					anc.cols(col).zn(ina)=ExcelSet.Worksheets("anc").cells(i2,i3).value
					else
						exit for
					end if
				next
			end if
		end if
	else
		exit for
	end if
next
    Call writelog "!","Изменено анцапф: "& narea
		else
			Call writelog "!","Вкладка изменения анцапф отсутствует!!!"
		end if
'============================== - Анцапфы БД- ==============================================
	On Error Resume Next
	oooo0=ExcelSet.Worksheets("anc2").cells(3,1).value
 	If Err.Number = 0 Then
npq=0
for i2=3 to 99999
	if ExcelSet.Worksheets("anc2").cells(i2,1).value<>"" then
		npq=npq+1
		Num=ExcelSet.Worksheets("anc2").cells(i2,1).value
		An1=ExcelSet.Worksheets("anc2").cells(i2,2).value
		An2=ExcelSet.Worksheets("anc2").cells(i2,3).value
		An3=ExcelSet.Worksheets("anc2").cells(i2,4).value
		anc2.SetSel("Num="&Num&"&An1="&An1&"&An2="&An2&"&An3="&An3)
		ivet=anc2.findnextsel(-1)
		if ivet<>-1 then
			if ExcelSet.Worksheets("anc2").cells(i2,5).value=666 then
				anc2.delrows
				writelog "Num="&Num&"&An1="&An1&"&An2="&An2&"&An3="&An3,"Удален элемент Анцапфы БД Num="&Num&"&An1="&An1&"&An2="&An2&"&An3="&An3&": "&	col	&":  стар.="& oldvalue&"  нов.= "&newvalue
			else
				for i3=6 to 100
					if ExcelSet.Worksheets("anc2").cells(2,i3).value<>"" then
						col=ExcelSet.Worksheets("anc2").cells(2,i3).value
						if anc2.cols(col).z(ivet)<>ExcelSet.Worksheets("anc2").cells(i2,i3).value then
							anc2.cols(col).z(ivet)=ExcelSet.Worksheets("anc2").cells(i2,i3).value
							writelog "Num="&Num&"&An1="&An1&"&An2="&An2&"&An3="&An3,"Изменен параметр Анцапфы БД Num="&Num&"&An1="&An1&"&An2="&An2&"&An3="&An3
						end if
					end if
				next
			end if
		else
			if ExcelSet.Worksheets("anc2").cells(i2,5).value=666 then
				writelog "!!!","Анцапфа БД для удаления  Num="&Num&"&An1="&An1&"&An2="&An2&"&An3="&An3	 &" не существует!!! "
			else
				writelog "Num="&Num&"&An1="&An1&"&An2="&An2&"&An3="&An3,"Новая Анцапфа БД Num="&Num&"&An1="&An1&"&An2="&An2&"&An3="&An3	&" создана!!! "
				ivet=0
				anc2.insrow ivet
				anc2.cols("Num").z(ivet)=Num
				anc2.cols("An1").z(ivet)=An1
				anc2.cols("An2").z(ivet)=An2
				anc2.cols("An3").z(ivet)=An3
				for i3=6 to 100
					if ExcelSet.Worksheets("anc2").cells(2,i3).value<>"" then
						col=ExcelSet.Worksheets("anc2").cells(2,i3).value
						anc2.cols(col).z(ivet)=ExcelSet.Worksheets("anc2").cells(i2,i3).value
						'writelog "!","Новый параметр PQ  Num="&Num&" P="&P&" параметр "&col
					end if
				next
			end if
		end if
	else
		exit for
	end if
next
    writelog "!","Изменено Анцапф БД : "& npq
		else
			writelog "!","Вкладка изменения Анцапфы БД отсутствует!!!"
		end if
		end if
'============================== - Удаление всего и вся- ==============================================
if needtodel=1 then
	vet.SetSel(1)
	vet.cols("groupid").calc(0)
	uzl.SetSel("muskod!=66666")
	uzl.cols("muskod").calc(0)
	vet.SetSel("ip.muskod=66666&iq.muskod!=66666&!sta")'!sta Выбираем все пограничные неотключенные ветви с началом в удал районе
	vet.cols("groupid").calc(1)
	vet.SetSel("groupid=1")
	ivet=vet.findnextsel(-1)
	for iiii=0 to 99999
		if ivet=-1 then exit for
		nyost=vet.cols("ip").zn(ivet)' Узел, который остается
		uzl.SetSel("ny="&nyost)
		iuzl=uzl.findnextsel(-1)' Убзел, который остается из удаляемого района
		if uzl.cols("muskod").zn(iuzl)=66666 then
			uzl.cols("pn").zn(iuzl)=0
			uzl.cols("qn").zn(iuzl)=0
			uzl.cols("pg").zn(iuzl)=-vet.cols("pl_ip").zn(ivet)
            ' 2020-06-28 делаем Vzd
			'uzl.cols("qg").zn(iuzl)=-vet.cols("ql_ip").zn(ivet)
            uzl.cols("vzd").zn(iuzl)=uzl.cols("vras").zn(iuzl)
            uzl.cols("qmin").zn(iuzl)=-10*uzl.cols("uhom").zn(iuzl)
            uzl.cols("qmax").zn(iuzl)=10*uzl.cols("uhom").zn(iuzl)
		else' Узел в удал районе, который остается и был обработан muskod=1

			uzl.cols("pg").zn(iuzl)=uzl.cols("pg").zn(iuzl)-vet.cols("pl_ip").zn(ivet)
			' 2020-06-28 uzl.cols("qg").zn(iuzl)=uzl.cols("qg").zn(iuzl)-vet.cols("ql_ip").zn(ivet)
		end if
		uzl.cols("muskod").zn(iuzl)=1' Узел в удал районе, который остается и был обработан muskod=1
		ivet=vet.findnextsel(ivet)
	next


	vet.SetSel("!sta&ip.muskod!=66666&ip.muskod!=1&(iq.muskod=66666|iq.muskod=1)")'!sta Выбираем все пограничные неотключенные ветви с концом в удал районе
	vet.cols("groupid").calc(2)
	vet.SetSel("groupid=2")

	ivet=vet.findnextsel(-1)
	for iiii=0 to 99999
		if ivet=-1 then exit for
		nyost=vet.cols("iq").zn(ivet)
		uzl.SetSel("ny="&nyost)
		iuzl=uzl.findnextsel(-1)
		if uzl.cols("muskod").zn(iuzl)=66666 then
			uzl.cols("pn").zn(iuzl)=0
			uzl.cols("qn").zn(iuzl)=0
			uzl.cols("pg").zn(iuzl)=vet.cols("pl_iq").zn(ivet)
			' 2020-06-28 делаем Vzd uzl.cols("qg").zn(iuzl)=vet.cols("ql_iq").zn(ivet)
            uzl.cols("vzd").zn(iuzl)=uzl.cols("vras").zn(iuzl)
            uzl.cols("qmin").zn(iuzl)=-10*uzl.cols("uhom").zn(iuzl)
            uzl.cols("qmax").zn(iuzl)=10*uzl.cols("uhom").zn(iuzl)
		else' Узел в удал районе, который остается и был обработан muskod=1

			uzl.cols("pg").zn(iuzl)=uzl.cols("pg").zn(iuzl)+vet.cols("pl_iq").zn(ivet)
			' 2020-06-28 делаем Vzd uzl.cols("qg").zn(iuzl)=uzl.cols("qg").zn(iuzl)+vet.cols("ql_iq").zn(ivet)
		end if
		uzl.cols("muskod").zn(iuzl)=1' Узел в удал районе, который остается и был обработан muskod=1
		ivet=vet.findnextsel(ivet)
	next
	gen.SetSel(1)
	gen.cols("Pgconst").calc(0)
	for igen=0 to gen.count-1
		ny=gen.cols("Node").zn(igen)
		msk=t.Calc("val","node","muskod","ny="&ny)  ' Удаляем генераторы, узлы которых удаляются
		if msk=66666 then gen.cols("Pgconst").zn(igen)=1
	next
	gen.SetSel("Pgconst=1")
	gen.delrows
	'vet.SetSel("(ip.muskod=66666|ip.muskod=1)&(iq.muskod=66666|iq.muskod=1)")
	vet.SetSel("(ip.muskod=66666&iq.muskod=66666)|(ip.muskod=66666&iq.muskod=1)|(ip.muskod=1&iq.muskod=66666)|(sta&(ip.muskod=66666|iq.muskod=66666))")
	vet.delrows
	uzl.SetSel("muskod=66666")
	uzl.delrows
end if
'============================== - Изменение балансов - ==============================================
	On Error Resume Next
	oooo0=ExcelSet.Worksheets("corr_bal").cells(2,1).value
 	If Err.Number = 0 Then
nray=0
ngenr=0
nterr=0
nob=0
basenode=0
for i2=3 to 9999
	if ExcelSet.Worksheets("corr_bal").cells(i2,1).value<>"" then
		if ExcelSet.Worksheets("corr_bal").cells(i2,2).value="area" then
			if ExcelSet.Worksheets("corr_bal").cells(i2,3).value="pg" then
				ngenr=ngenr+1
				genr(0,ngenr)=ExcelSet.Worksheets("corr_bal").cells(i2,1).value'номер района
				genr(1,ngenr)=ExcelSet.Worksheets("corr_bal").cells(i2,3).value'ключ
				genr(2,ngenr)=ExcelSet.Worksheets("corr_bal").cells(i2,4).value'выборка
				genr(3,ngenr)=ExcelSet.Worksheets("corr_bal").cells(i2,5).value'новое значение
			else
				nray=nray+1
				rayony(0,nray)=ExcelSet.Worksheets("corr_bal").cells(i2,1).value'номер района
				rayony(1,nray)=ExcelSet.Worksheets("corr_bal").cells(i2,3).value'ключ
				rayony(2,nray)=ExcelSet.Worksheets("corr_bal").cells(i2,4).value'выборка
				rayony(3,nray)=ExcelSet.Worksheets("corr_bal").cells(i2,5).value'новое значение
			end if
		end if
		if ExcelSet.Worksheets("corr_bal").cells(i2,2).value="area2" then
			nterr=nterr+1
			terr(0,nterr)=ExcelSet.Worksheets("corr_bal").cells(i2,1).value
			terr(1,nterr)=ExcelSet.Worksheets("corr_bal").cells(i2,3).value
			terr(2,nterr)=ExcelSet.Worksheets("corr_bal").cells(i2,4).value
			terr(3,nterr)=ExcelSet.Worksheets("corr_bal").cells(i2,5).value
			'terr(5,nterr)=1
		end if
		if ExcelSet.Worksheets("corr_bal").cells(i2,2).value="darea" then
			nob=nob+1
			obyedin(0,nob)=ExcelSet.Worksheets("corr_bal").cells(i2,1).value
			obyedin(1,nob)=ExcelSet.Worksheets("corr_bal").cells(i2,3).value
			obyedin(2,nob)=ExcelSet.Worksheets("corr_bal").cells(i2,4).value
			obyedin(3,nob)=ExcelSet.Worksheets("corr_bal").cells(i2,5).value
			'obyedin(5,nob)=1
		end if
		if ExcelSet.Worksheets("corr_bal").cells(i2,2).value="base" then
			nybase=ExcelSet.Worksheets("corr_bal").cells(i2,1).value
			vybbase=ExcelSet.Worksheets("corr_bal").cells(i2,4).value
			valnewbase=ExcelSet.Worksheets("corr_bal").cells(i2,5).value
			basenode=1
		end if
	else
		exit for
	end if
next
kod=t.rgm("pс")
if basenode=1 then tipbase=t.Calc("val","node","tip","ny="&nybase)
'msgbox " basenode="&basenode&" tipbase="&tipbase
if basenode=1 and tipbase<>0 then basenode=0
if basenode=1 then valnowbase=t.Calc("val","node","pg","ny="&nybase)
'msgbox " basenode="&basenode&" valnowbase="&valnowbase
if basenode=1 then
	sumpnforbase=t.Calc("sum","node","pn","!sta&pn>0&"&vybbase)
	if sumpnforbase>100 then
		del1=1+(valnewbase-valnowbase)/sumpnforbase
		uzl.SetSel("!sta&pn>1&"&vybbase)
		uzl.Cols("pn").Calc("pn*"&del1)
		uzl.Cols("qn").Calc("qn*"&del1)
	end if
	kod=t.rgm("pс")
end if
if sumpnforbase<100 then basenode=0
' terr - ===================================================================================================
sumpn=0
for i = 1 to 4
	maxneb=0
	for i1 = 1 to nterr
		terr(5,i1)=t.Calc("val","area2",terr(1,i1),"npa="&terr(0,i1))
		if abs(terr(5,i1)-terr(3,i1))>maxneb then maxneb=abs(terr(5,i1)-terr(3,i1))
	next
	if maxneb<1 and kod=0 then exit for
	for i1 = 1 to nterr
		if terr(1,i1)="pop" or terr(1,i1)="pn" or terr(1,i1)="vnp" then
			terr(4,i1)=t.Calc("sum","node","pn","!sta&pn>0&npa="&terr(0,i1)&"&"&terr(2,i1))
    'msgbox "terr: "&terr(0,i1)&"  -0; "&terr(1,i1)&"  -1;"&terr(2,i1)&"  -2;"&terr(3,i1)&"  -3; "&terr(4,i1)&"  -4; "&terr(5,i1)&"  -5"
    writelog i&"; kod="&kod&"; basenode="&basenode,"terr: "&terr(0,i1)&"  -0; "&terr(1,i1)&"  -1;"&terr(2,i1)&"  -2;"&terr(3,i1)&"  -3; "&terr(4,i1)&"  -4; "&terr(5,i1)&"  -5"
			if terr(1,i1)="pop" or terr(1,i1)="pn" then
				deltapn=terr(3,i1)-terr(5,i1)
			end if
			if terr(1,i1)="vnp" then
				deltapn=terr(5,i1)-terr(3,i1)
			end if
			if deltapn>500 then deltapn=500
			if deltapn<-500 then deltapn=-500
			if deltapn>-0.5 and deltapn<0 then deltapn=-0.5
			if deltapn<0.5 and deltapn>0 then deltapn=0.5
			if terr(4,i1)<0.5 and terr(4,i1)>-0.5 then terr(4,i1)=0.5
			sumpn=sumpn+deltapn
			if (sumpn<4000 and sumpn>-4000) or (sumpn<-4000 and deltapn>0) or (sumpn>4000 and deltapn<0) or basenode=1 then
				del=1+deltapn/terr(4,i1)
				if del<0.001 then del=0.001
				uzl.SetSel("!sta&pn>0&npa="&terr(0,i1)&"&"&terr(2,i1))
				uzl.Cols("pn").Calc("pn*"&del)
				uzl.Cols("qn").Calc("qn*"&del)
			end if
		end if
	next
	kod=t.rgm("pс")
	if basenode=1 then
		sumpnforbase=t.Calc("sum","node","pn","!sta&pn>0&"&vybbase)
		valnowbase=t.Calc("val","node","pg","ny="&nybase)
		del1=1+(valnewbase-valnowbase)/sumpnforbase
		uzl.SetSel("!sta&pn>1&"&vybbase)
		uzl.Cols("pn").Calc("pn*"&del1)
		uzl.Cols("qn").Calc("qn*"&del1)
		kod=t.rgm("pс")
	end if
next
' rayony - ===================================================================================================
sumpn=0
for i = 1 to 5
	maxneb=0
	for i1 = 1 to nray
		rayony(5,i1)=t.Calc("val","area",rayony(1,i1),"na="&rayony(0,i1))
		genr(5,i1)=t.Calc("val","area",genr(1,i1),"na="&genr(0,i1))
		if abs(rayony(5,i1)-rayony(3,i1))>maxneb then maxneb=abs(rayony(5,i1)-rayony(3,i1))
		if abs(genr(5,i1)-genr(3,i1))>maxneb then maxneb=abs(genr(5,i1)-genr(3,i1))
	next
	if maxneb<1 and kod=0 then exit for
	for i1 = 1 to nray
		if rayony(1,i1)="pop" or rayony(1,i1)="pn" or rayony(1,i1)="vnp" then
			rayony(4,i1)=t.Calc("sum","node","pn","!sta&pn>0&na="&rayony(0,i1)&"&"&rayony(2,i1))
    'msgbox "rayony: "&rayony(0,i1)&"  -0; "&rayony(1,i1)&"  -1;"&rayony(2,i1)&"  -2;"&rayony(3,i1)&"  -3; "&rayony(4,i1)&"  -4; "&rayony(5,i1)&"  -5"
    writelog i&"; kod="&kod&"; basenode="&basenode,"rayony: "&rayony(0,i1)&"  -0; "&rayony(1,i1)&"  -1;"&rayony(2,i1)&"  -2;"&rayony(3,i1)&"  -3; "&rayony(4,i1)&"  -4; "&rayony(5,i1)&"  -5"
			if rayony(1,i1)="pop" or rayony(1,i1)="pn" then
				deltapn=rayony(3,i1)-rayony(5,i1)
			end if
			if rayony(1,i1)="vnp" then
				deltapn=rayony(5,i1)-rayony(3,i1)
			end if
			if deltapn>500 then deltapn=500
			if deltapn<-500 then deltapn=-500
			if deltapn>-0.5 and deltapn<0 then deltapn=-0.5
			if deltapn<0.5 and deltapn>0 then deltapn=0.5
			if rayony(4,i1)<0.5 and rayony(4,i1)>-0.5 then rayony(4,i1)=0.5
			sumpn=sumpn+deltapn
			if (sumpn<4000 and sumpn>-4000) or (sumpn<-4000 and deltapn>0) or (sumpn>4000 and deltapn<0) or basenode=1 then
				del=1+deltapn/rayony(4,i1)
				if del<0.001 then del=0.001
				uzl.SetSel("!sta&pn>0&na="&rayony(0,i1)&"&"&rayony(2,i1))
				uzl.Cols("pn").Calc("pn*"&del)
				uzl.Cols("qn").Calc("qn*"&del)
			end if
		end if
	next
	for i1 = 1 to ngenr
		if genr(1,i1)="pg" then
			qqqq1=t.Calc("sum","node","pg","tip!=0&!sta&pg>0&na="&genr(0,i1)&"&"&genr(2,i1))
			qqqq2=t.Calc("sum","node","pg","tip!=0&!sta&pg<0&na="&genr(0,i1)&"&"&genr(2,i1))
			genr(4,i1)=qqqq1-qqqq2
    'msgbox "tip!=0&!sta&pg>0&na="&genr(0,i1)&"&"&genr(2,i1)
    'msgbox genr(0,i1)&"  "&qqqq1&"  "&qqqq2&"  "&genr(4,i1)

    'msgbox "rayony: "&rayony(0,i1)&"  -0; "&rayony(1,i1)&"  -1;"&rayony(2,i1)&"  -2;"&rayony(3,i1)&"  -3; "&rayony(4,i1)&"  -4; "&rayony(5,i1)&"  -5"
    writelog i&"; kod="&kod&"; basenode="&basenode,"genr: "&genr(0,i1)&"  -0; "&genr(1,i1)&"  -1;"&genr(2,i1)&"  -2;"&genr(3,i1)&"  -3; "&genr(4,i1)&"  -4; "&genr(5,i1)&"  -5"
			if genr(1,i1)="pg" then
				deltapn=genr(3,i1)-genr(5,i1)
			end if
			'if genr(1,i1)="vnp" then
				'deltapn=genr(5,i1)-genr(3,i1)
			'end if
			if deltapn>900 then deltapn=900
			if deltapn<-900 then deltapn=-900
			if deltapn>-0.5 and deltapn<0 then deltapn=-0.5
			if deltapn<0.5 and deltapn>-0.0001 then deltapn=0.5
			if genr(4,i1)<0.5 and genr(4,i1)>0 then genr(4,i1)=0.5
			if genr(4,i1)<0 and genr(4,i1)>-0.5 then genr(4,i1)=-0.5
			sumpn=sumpn-deltapn
			'if (sumpn<4000 and sumpn>-4000) or (sumpn<-4000 and deltapn>0) or (sumpn>4000 and deltapn<0) or basenode=1 then
				del=deltapn/genr(4,i1)
                'writelog i,"deltapn="&deltapn & " del="&del
				'if del<0.0001 and del>-0.0000001 then del=0.0001
				'if del<0 and del>-0.0001 then del=-0.0001
				uzl.SetSel("tip!=0&!sta&pg>0&na="&genr(0,i1)&"&"&genr(2,i1))
				uzl.Cols("pg").Calc(del&"*pg+pg")
				uzl.Cols("qg").Calc("qg+abs(qg)*"&del)
				uzl.SetSel("tip!=0&!sta&pg<0&na="&genr(0,i1)&"&"&genr(2,i1))
				uzl.Cols("pg").Calc("pg*(1-"&del&")")
				'uzl.Cols("pg").Calc("pg*(1+0.0255)")
				uzl.Cols("qg").Calc("qg+abs(qg)*"&del)
			'end if
		end if
	next
	kod=t.rgm("pс")
	if basenode=1 then
		sumpnforbase=t.Calc("sum","node","pn","!sta&pn>0&"&vybbase)
		valnowbase=t.Calc("val","node","pg","ny="&nybase)
		del1=1+(valnewbase-valnowbase)/sumpnforbase
		uzl.SetSel("!sta&pn>1&"&vybbase)
		uzl.Cols("pn").Calc("pn*"&del1)
		uzl.Cols("qn").Calc("qn*"&del1)
		kod=t.rgm("pс")
	end if
next
' obyedin - ===================================================================================================
sumpn=0
for i = 1 to 8
	maxneb=0
	for i1 = 1 to nob
		obyedin(5,i1)=t.Calc("val","darea",obyedin(1,i1),"no="&obyedin(0,i1))
		if abs(obyedin(5,i1)-obyedin(3,i1))>maxneb then maxneb=abs(obyedin(5,i1)-obyedin(3,i1))
	next
	if maxneb<1 and kod=0 then exit for
	for i1 = 1 to nob
		if obyedin(1,i1)="pp" or obyedin(1,i1)="pvn" then
			obyedin(4,i1)=t.Calc("sum","node","pn","!sta&pn>0&na_no="&obyedin(0,i1)&"&"&obyedin(2,i1))
            'msgbox "obyedin: "&obyedin(0,i1)&"  -0; "&obyedin(1,i1)&"  -1;"&obyedin(2,i1)&"  -2;"&obyedin(3,i1)&"  -3; "&obyedin(4,i1)&"  -4; "&obyedin(5,i1)&"  -5"
            writelog i&"; kod="&kod&"; basenode="&basenode,"obyedin: "&obyedin(0,i1)&"  -0; "&obyedin(1,i1)&"  -1;"&obyedin(2,i1)&"  -2;"&obyedin(3,i1)&"  -3; "&obyedin(4,i1)&"  -4; "&obyedin(5,i1)&"  -5"
			if obyedin(1,i1)="pp" then
				deltapn=obyedin(3,i1)-obyedin(5,i1)
			end if
			if obyedin(1,i1)="pvn" then
				deltapn=obyedin(5,i1)-obyedin(3,i1)
			end if
			if deltapn>1000 then deltapn=1000
			if deltapn<-1000 then deltapn=-1000
			if deltapn>-0.5 and deltapn<0 then deltapn=-0.5
			if deltapn<0.5 and deltapn>0 then deltapn=0.5
			if obyedin(4,i1)<0.5 and obyedin(4,i1)>-0.5 then obyedin(4,i1)=0.5
			sumpn=sumpn+deltapn
			if (sumpn<4000 and sumpn>-4000) or (sumpn<-4000 and deltapn>0) or (sumpn>4000 and deltapn<0) or basenode=1 then
				del=1+deltapn/obyedin(4,i1)
				if del<0.001 then del=0.001
				uzl.SetSel("!sta&pn>0&na_no="&obyedin(0,i1)&"&"&obyedin(2,i1))
				uzl.Cols("pn").Calc("pn*"&del)
				uzl.Cols("qn").Calc("qn*"&del)
			end if
		end if
	next
	kod=t.rgm("pс")
	if basenode=1 then
		sumpnforbase=t.Calc("sum","node","pn","!sta&pn>0&"&vybbase)
		valnowbase=t.Calc("val","node","pg","ny="&nybase)
		del1=1+(valnewbase-valnowbase)/sumpnforbase
		uzl.SetSel("!sta&pn>1&"&vybbase)
		uzl.Cols("pn").Calc("pn*"&del1)
		uzl.Cols("qn").Calc("qn*"&del1)
		kod=t.rgm("pс")
	end if
next
		else
			writelog "!","Вкладка изменения балансов отсутствует!!!"
		end if
kod1=t.rgm ("p")
'============================== - Изменение балансов сечения - ==============================================
	On Error Resume Next
	oooo0=ExcelSet.Worksheets("sec_bal").cells(2,1).value
 	If Err.Number = 0 Then
nsecbal=0
ntracks=0
for i2=2 to 2 'одно сечение - одна траектория!
		if ExcelSet.Worksheets("sec_bal").cells(i2,1).value="" then exit for
		nsecbal=nsecbal+1
		secbal(1,nsecbal)=ExcelSet.Worksheets("sec_bal").cells(i2,1).value ' ns
		secbal(2,nsecbal)=ExcelSet.Worksheets("sec_bal").cells(i2,2).value ' name
		'trtrtr=ExcelSet.Worksheets("sec_bal").cells(i2,3).value ' track
		if nsecbal=1 then
			ntracks=ntracks+1
			secbal(3,nsecbal)=ExcelSet.Worksheets("sec_bal").cells(i2,3).value ' track
		end if
		secbal(4,nsecbal)=ExcelSet.Worksheets("sec_bal").cells(i2,4).value ' newvalue
		secbal(5,nsecbal)=ExcelSet.Worksheets("sec_bal").cells(i2,5).value ' stepsum
next
if nsecbal<>0 then
	nutnode=0
	nvybut=0
	nareaut=0
	track=secbal(3,nsecbal)
	for i2=0 to 10000
		if ExcelSet.Worksheets(track).cells(i2+2,2).value<>"" then
			if ExcelSet.Worksheets(track).cells(i2+2,1).value="" or ExcelSet.Worksheets(track).cells(i2+2,1).value="ny" then
				nutnode=nutnode+1
				utnode(nutnode,0)=ExcelSet.Worksheets(track).cells(i2+2,2).value
				utnode(nutnode,1)=ExcelSet.Worksheets(track).cells(i2+2,4).value
				utnode(nutnode,2)=ExcelSet.Worksheets(track).cells(i2+2,5).value
				utnode(nutnode,3)=ExcelSet.Worksheets(track).cells(i2+2,6).value
				utnode(nutnode,4)=ExcelSet.Worksheets(track).cells(i2+2,7).value
				utnode(nutnode,5)=ExcelSet.Worksheets(track).cells(i2+2,8).value
				utnode(nutnode,6)=ExcelSet.Worksheets(track).cells(i2+2,9).value
				utnode(nutnode,7)=ExcelSet.Worksheets(track).cells(i2+2,10).value
				Call writelog "utnode-0 №" & nutnode, utnode(nutnode,0)
			end if
			if ExcelSet.Worksheets(track).cells(i2+2,1).value="vyb" then
				nvybut=nvybut+1
				vybut(nvybut,0)=ExcelSet.Worksheets(track).cells(i2+2,3).value
				vybut(nvybut,1)=ExcelSet.Worksheets(track).cells(i2+2,4).value
				vybut(nvybut,2)=ExcelSet.Worksheets(track).cells(i2+2,5).value
				vybut(nvybut,3)=ExcelSet.Worksheets(track).cells(i2+2,6).value
				vybut(nvybut,4)=ExcelSet.Worksheets(track).cells(i2+2,7).value
				vybut(nvybut,5)=ExcelSet.Worksheets(track).cells(i2+2,8).value
				vybut(nvybut,6)=ExcelSet.Worksheets(track).cells(i2+2,9).value
				vybut(nvybut,7)=ExcelSet.Worksheets(track).cells(i2+2,10).value
				Call writelog "vybut-0 №"&nvybut,vybut(nvybut,0)
			end if
			if ExcelSet.Worksheets(track).cells(i2+2,1).value="area" then
				nareaut=nareaut+1
				if ExcelSet.Worksheets(track).cells(i2+2,2).value="" then
					areaut(nareaut,0)=ExcelSet.Worksheets(track).cells(i2+2,3).value
				else
					areaut(nareaut,0)=ExcelSet.Worksheets(track).cells(i2+2,3).value&"&na="&ExcelSet.Worksheets(track).cells(i2+2,2).value
				end if
				areaut(nareaut,1)=ExcelSet.Worksheets(track).cells(i2+2,4).value
				areaut(nareaut,2)=ExcelSet.Worksheets(track).cells(i2+2,5).value
				areaut(nareaut,3)=ExcelSet.Worksheets(track).cells(i2+2,6).value
				areaut(nareaut,4)=ExcelSet.Worksheets(track).cells(i2+2,7).value
				areaut(nareaut,5)=ExcelSet.Worksheets(track).cells(i2+2,8).value
				areaut(nareaut,6)=ExcelSet.Worksheets(track).cells(i2+2,9).value
				areaut(nareaut,7)=ExcelSet.Worksheets(track).cells(i2+2,10).value
				Call writelog "areaut-0 №" & nareaut,areaut(nareaut,0)
			end if
		else
			exit for
		end if
	next
	Call generatorset
	Call set_sec
end if
else
    Call writelog "!","Вкладка изменения перетоков в сечениях отсутствует!!!"
end if
'==============================
ExcelSet.Quit
if savef(ifile)=1 then
	t.Save fin_dir&newfilename(ifile)&typfile,rg2_shabl
	writelog "!","Сохранен в папку: "&fin_dir&"  файл rg2: "&newfilename(ifile)&typfile
    'msgbox "sec_need="&sec_need&" sec_name(ifile)="&sec_name(ifile)
	if sec_need=1 and sec_name(ifile)<>"" then
		t.Save fin_dir&new_sec_name(ifile)&".sch",sec_shabl
		writelog "!","Сохранен в папку: "&fin_dir&"  файл sch: "&new_sec_name(ifile)&".sch"
	end if
	if grf_need=1 and grf_name(ifile)<>"" then
		t.Save fin_dir&new_grf_name(ifile)&".grf",grf_shabl
		writelog "!","Сохранен в папку: "&fin_dir&"  файл grf: "&new_grf_name(ifile)&".grf"
	end if
	if anc_need=1 and anc_name(ifile)<>"" then
		t.Save fin_dir&new_anc_name(ifile)&".anc",anc_shabl
		writelog "!","Сохранен в папку: "&fin_dir&"  файл anc: "&new_anc_name(ifile)&".anc"
	end if
end if
next
ExLog.ActiveWorkbook.Save
ExLog.Quit
msgbox "Корректировка закончена!!!"
'============================================= writelog =====================================================
sub writelog (vyborrka,logsign)
	ExLog.Worksheets(1).cells(nlog,1).value=time()
	ExLog.Worksheets(1).cells(nlog,2).value=vyborrka
	ExLog.Worksheets(1).cells(nlog,3).value=logsign
	if  vyborrka<>"!" and vyborrka<>"!!!" and vyborrka<>"" then
		ExLog.Worksheets(1).cells(nlog,4).value=col
		ExLog.Worksheets(1).cells(nlog,5).value=oldvalue
		ExLog.Worksheets(1).cells(nlog,6).value=newvalue
	end if
	nlog=nlog+1
end sub
'============================================= GetSettings =====================================================
Sub GetSettings
    Set ExcelSet = CreateObject("Excel.Application")
        ExcelSet.Workbooks.open settings
        ExcelSet.Visible = 1
        ExcelSet.ScreenUpdating = False
        ExcelSet.EnableEvents = False
    for i2=2 to 20
		if ExcelSet.Worksheets("set").cells(i2,1).value="" then exit for
		buf=ExcelSet.Worksheets("set").cells(i2,1).value
		if buf="ishdir" then ishdir=ExcelSet.Worksheets("set").cells(i2,2).value
		if buf="fin_dir" then fin_dir=ExcelSet.Worksheets("set").cells(i2,2).value
		if buf="sec_shabl" then sec_shabl=ExcelSet.Worksheets("set").cells(i2,2).value
		if buf="rg2_shabl" then rg2_shabl=ExcelSet.Worksheets("set").cells(i2,2).value
		if buf="grf_shabl" then grf_shabl=ExcelSet.Worksheets("set").cells(i2,2).value
		if buf="anc_shabl" then anc_shabl=ExcelSet.Worksheets("set").cells(i2,2).value
		if buf="sec_need" then sec_need=ExcelSet.Worksheets("set").cells(i2,2).value
		if buf="grf_need" then grf_need=ExcelSet.Worksheets("set").cells(i2,2).value
		if buf="anc_need" then anc_need=ExcelSet.Worksheets("set").cells(i2,2).value
		if buf="setiav" then
			setiav=ExcelSet.Worksheets("set").cells(i2,2).value
			if setiav>0 then setiav=3 else setiav=0
		end if
    next
    ncorrect=0
    isamenames=0
    for i2=2 to 1000
		if ExcelSet.Worksheets("files").cells(i2,2).value="" then exit for
		ncorrect=ncorrect+1
		filename(ncorrect)=ExcelSet.Worksheets("files").cells(i2,1).value
		if filename(1)="" then
			msgbox "Ошибка! Нет имени исходного файла!"
			ncorrect=-1
			exit sub
		end if
		savef(ncorrect)=1
		corr_settings(ncorrect)=ExcelSet.Worksheets("files").cells(i2,2).value
		if filename(ncorrect)="" then
			filename(ncorrect)="bez izmeneniya fayla!"
			newfilename(ncorrect)=newfilename(ncorrect-1)
			sec_name(ncorrect)=sec_name(ncorrect-1)
			grf_name(ncorrect)=grf_name(ncorrect-1)
			anc_name(ncorrect)=anc_name(ncorrect-1)
			new_sec_name(ncorrect)=new_sec_name(ncorrect-1)
			new_grf_name(ncorrect)=new_grf_name(ncorrect-1)
			new_anc_name(ncorrect)=new_anc_name(ncorrect-1)
			savef(ncorrect-1)=0
		else
			newfilename(ncorrect)=ExcelSet.Worksheets("files").cells(i2,3).value
			if newfilename(ncorrect)="" then
				 newfilename(ncorrect)=filename(ncorrect)&"_"&nowdate&"_"&Hour(Now())&"h"&Minute(Now())&"m"
			end if

			for iii=1 to ncorrect-1
				if newfilename(ncorrect)=newfilename(iii) then
					isamenames=isamenames+1
					newfilename(ncorrect)=newfilename(ncorrect)&"_"&isamenames
					exit for
				end if
			next
			if sec_need>0 then
				sec_name(ncorrect)=ExcelSet.Worksheets("files").cells(i2,4).value
				new_sec_name(ncorrect)=ExcelSet.Worksheets("files").cells(i2,7).value
				if new_sec_name(ncorrect)="" then
					 new_sec_name(ncorrect)=sec_name(ncorrect)&"_"&nowdate&"_"&Hour(Now())&"h"&Minute(Now())&"m"
				end if
				for iii=1 to ncorrect-1
					if new_sec_name(ncorrect)=new_sec_name(iii) then
						isamenames=isamenames+1
						new_sec_name(ncorrect)=new_sec_name(ncorrect)&"_"&isamenames
						exit for
					end if
				next
			end if
			if grf_need>0 then
				grf_name(ncorrect)=ExcelSet.Worksheets("files").cells(i2,5).value
				new_grf_name(ncorrect)=ExcelSet.Worksheets("files").cells(i2,8).value
				if new_grf_name(ncorrect)="" then
					 new_grf_name(ncorrect)=grf_name(ncorrect)&"_"&nowdate&"_"&Hour(Now())&"h"&Minute(Now())&"m"
				end if
				for iii=1 to ncorrect-1
					if new_grf_name(ncorrect)=new_grf_name(iii) then
						isamenames=isamenames+1
						new_grf_name(ncorrect)=new_grf_name(ncorrect)&"_"&isamenames
						exit for
					end if
				next
			end if
			if anc_need>0 then
				anc_name(ncorrect)=ExcelSet.Worksheets("files").cells(i2,6).value
				new_anc_name(ncorrect)=ExcelSet.Worksheets("files").cells(i2,9).value
				if new_anc_name(ncorrect)="" then
					 new_anc_name(ncorrect)=anc_name(ncorrect)&"_"&nowdate&"_"&Hour(Now())&"h"&Minute(Now())&"m"
				end if
				for iii=1 to ncorrect-1
					if new_anc_name(ncorrect)=new_anc_name(iii) then
						isamenames=isamenames+1
						new_anc_name(ncorrect)=new_anc_name(ncorrect)&"_"&isamenames
						exit for
					end if
				next
			end if
		end if
    next
    ExcelSet.Quit
end sub

'=======================================- generatorset -==============================================
Sub generatorset()
    't.Tables("com_regim").Cols("gen_p").z(0)=0'генераторы остаются, но ...
    kod1=t.rgm ("p")
    pg_plus=0
	pg_minus=0
	dpg_plus=0
	dpg_minus=0
    'nutnode=nutnode0
    stepsum=secbal(5,nsecbal)
	for ivybut=1 to nvybut
        uzl.setsel(vybut(ivybut,0))
		iuzl=uzl.findnextsel(-1)
        while iuzl<>-1
		    nutnode=nutnode+1
			utnode(nutnode,0)=uzl.Cols("ny").z(iuzl)
			utnode(nutnode,1)=vybut(ivybut,1)
			utnode(nutnode,2)=vybut(ivybut,2)
			utnode(nutnode,3)=vybut(ivybut,3)
			utnode(nutnode,4)=vybut(ivybut,4)
			utnode(nutnode,5)=vybut(ivybut,5)
			utnode(nutnode,6)=vybut(ivybut,6)
			utnode(nutnode,7)=vybut(ivybut,7)
			iuzl=uzl.findnextsel(iuzl)
		wend
	next
	for iareaut=1 to nareaut
    	'if (areaut(iareaut,1)<>"+" and areaut(iareaut,1)<>"-") or (areaut(iareaut,6)<>"+" and areaut(iareaut,6)<>"-") then
		pnsumut=t.calc("sum","node","pn",areaut(iareaut,0))
		pgsumut=t.calc("sum","node","pg",areaut(iareaut,0))
		'msgbox areaut(iareaut,0)&"&(pn<>0&pg<>0)"&"-"&areaut(iareaut,1)
		writelog areaut(iareaut,0)&"areaut-0 №"&iareaut,areaut(iareaut,0)
        writelog areaut(iareaut,0)&"pnsumut №"&iareaut,pnsumut
		writelog areaut(iareaut,0)&"pgsumut №"&iareaut,pgsumut
		uzl.setsel(areaut(iareaut,0)&"&(pn!=0|pg!=0)")
		iuzl=uzl.findnextsel(-1)
        while iuzl<>-1
            'msgbox iuzl
			nutnode=nutnode+1
			utnode(nutnode,0)=uzl.Cols("ny").z(iuzl)
			utnode(nutnode,1)=0
			utnode(nutnode,6)=0
            'if nutnode>980 then msgbox nutnode&" - "&utnode(nutnode,0)
			'msgbox utnode(nutnode,0)&" - "&utnode(nutnode,1)&" - "&utnode(nutnode,6)
			if uzl.Cols("pg").z(iuzl) <> 0 then
			    if (areaut(iareaut,1) <> "+" and areaut(iareaut,1) <> "-") then
						utnode(nutnode,1)=areaut(iareaut,1)*uzl.Cols("pg").z(iuzl)/pgsumut
						if uzl.Cols("vzd").z(iuzl)=0 or uzl.Cols("vzd").z(iuzl)="" then
							if areaut(iareaut,2) = "" then
								powerkoef=uzl.Cols("qg").z(iuzl)/uzl.Cols("pg").z(iuzl)
								if powerkoef<=0.9 and powerkoef>=0.2 then utnode(nutnode,2)=utnode(nutnode,1)*powerkoef
								if powerkoef>0.9 then utnode(nutnode,2)=utnode(nutnode,1)*0.9
								if powerkoef<0.2 then utnode(nutnode,2)=utnode(nutnode,1)*0.2
							else
								utnode(nutnode,2)=areaut(iareaut,2)*uzl.Cols("pg").z(iuzl)/pgsumut
							end if
						else
							if areaut(iareaut,3)="" then
								powerkoef=uzl.Cols("qmin").z(iuzl)/uzl.Cols("pg").z(iuzl)
								if powerkoef<=0.2 and powerkoef>=-0.9 then utnode(nutnode,3)=utnode(nutnode,1)*powerkoef
								if powerkoef>0.2 then utnode(nutnode,3)=utnode(nutnode,1)*0.2
								if powerkoef<-0.9 then utnode(nutnode,3)=utnode(nutnode,1)*(-0.9)
							else
								if areaut(iareaut,3)=-9999 then
									uzl.Cols("qmin").z(iuzl)=-9999
									utnode(nutnode,3)=0
								else
									utnode(nutnode,3)=areaut(iareaut,3)*uzl.Cols("pg").z(iuzl)/pgsumut
								end if
							end if
							if areaut(iareaut,4)="" then
								powerkoef=uzl.Cols("qmax").z(iuzl)/uzl.Cols("pg").z(iuzl)
								if powerkoef<=0.9 and powerkoef>=0.2 then utnode(nutnode,4)=utnode(nutnode,1)*powerkoef
								if powerkoef>0.9 then utnode(nutnode,4)=utnode(nutnode,1)*0.9
								if powerkoef<0.2 then utnode(nutnode,4)=utnode(nutnode,1)*0.2
							else
								if areaut(iareaut,4)=9999 then
									uzl.Cols("qmax").z(iuzl)=9999
									utnode(nutnode,4)=0
								else
									utnode(nutnode,4)=areaut(iareaut,4)*uzl.Cols("pg").z(iuzl)/pgsumut
								end if
							end if
							if areaut(iareaut,5)<>"" then
								utnode(nutnode,5)=areaut(iareaut,5)
								'*uzl.Cols("vzd").z(iuzl)/100
							end if
						end if
					else
						utnode(nutnode,1)=areaut(iareaut,1)
						if uzl.Cols("vzd").z(iuzl)<>0 and uzl.Cols("vzd").z(iuzl)<>"" then
							if areaut(iareaut,5)<>"" then utnode(nutnode,5)=areaut(iareaut,5)
							if areaut(iareaut,3)=-9999 then
								uzl.Cols("qmin").z(iuzl)=-9999
								utnode(nutnode,3)=0
							end if
							if areaut(iareaut,4)=9999 then
								uzl.Cols("qmax").z(iuzl)=9999
								utnode(nutnode,4)=0
							end if
						end if
					end if
				end if
				if uzl.Cols("pn").z(iuzl)<>0 then
					if (areaut(iareaut,6)<> "+" and areaut(iareaut,6)<>"-") then
						utnode(nutnode,6)=areaut(iareaut,6)*uzl.Cols("pn").z(iuzl)/pnsumut
						if areaut(iareaut,7)="" then
							powerkoef=uzl.Cols("qn").z(iuzl)/uzl.Cols("pn").z(iuzl)
							utnode(nutnode,7)=utnode(nutnode,6)*powerkoef
						else
							utnode(nutnode,7)=areaut(iareaut,7)*uzl.Cols("pn").z(iuzl)/pnsumut
						end if
					else
						utnode(nutnode,6)=areaut(iareaut,6)
						if areaut(iareaut,7)="" or areaut(iareaut,7)=0 then utnode(nutnode,7)=areaut(iareaut,7)
					end if
                end if
                'msgbox utnode(nutnode,0)&" - "&utnode(nutnode,1)&" - "&utnode(nutnode,6)
				'if (utnode(nutnode,1)=0) and (utnode(nutnode,6)=0)then nutnode=nutnode-1
				iuzl=uzl.findnextsel(iuzl)
				wend
			'end if
		next
		for iutnode=1 to nutnode
			uzl.setsel("ny="&utnode(iutnode,0))
			iuzl=uzl.findnextsel(-1)
			if utnode(iutnode,1)<>"+" and utnode(iutnode,1)<>"-"  then
				if utnode(iutnode,1)>0 then
					dpg_plus=dpg_plus+utnode(iutnode,1)
				end if
				if utnode(iutnode,1)<0 then
					dpg_minus=dpg_minus+utnode(iutnode,1)
				end if
			end if
			if utnode(iutnode,6)<>"+" and utnode(iutnode,6)<>"-"  then
				if utnode(iutnode,6)<0 then
					dpg_plus=dpg_plus-utnode(iutnode,6)
				end if
				if utnode(iutnode,6)>0 then
					dpg_minus=dpg_minus+utnode(iutnode,6)
				end if
			end if
		next
		for iutnode=1 to nutnode
			uzl.setsel("ny="&utnode(iutnode,0))
			iuzl=uzl.findnextsel(-1)
			if utnode(iutnode,1)="+" then
					pg_plus=pg_plus+uzl.Cols("pg").z(iuzl)
			end if
			if utnode(iutnode,1)="-"   then
					pg_minus=pg_minus+uzl.Cols("pg").z(iuzl)
			end if
			if  utnode(iutnode,6)="-"  then
					pg_plus=pg_plus+uzl.Cols("pn").z(iuzl)
			end if
			if utnode(iutnode,6)="+" then
					pg_minus=pg_minus+uzl.Cols("pn").z(iuzl)
			end if
		next
		dpg_plus=stepsum-dpg_plus
		dpg_minus=stepsum-dpg_minus
		if dpg_plus<0 then
			writelog dpg_plus, "Превышено положительное приращение по траектории!!!"
			dpg_minus=dpg_minus-dpg_plus
			dpg_plus=0
		end if
		if dpg_minus<0 then
			writelog dpg_minus,  "Превышено отрицательное приращение по траектории!!!"
			dpg_minus=0
		end if
		for iutnode=1 to nutnode
			uzl.setsel("ny="&utnode(iutnode,0))
			iuzl=uzl.findnextsel(-1)
			if utnode(iutnode,1)="+" then
				utnode(iutnode,1)=dpg_plus*uzl.Cols("pg").z(iuzl)/pg_plus
			end if
			if utnode(iutnode,1)="-" then
				utnode(iutnode,1)=-dpg_minus*uzl.Cols("pg").z(iuzl)/pg_minus
			end if
			if utnode(iutnode,6)="-" then
				utnode(iutnode,6)=-dpg_plus*uzl.Cols("pn").z(iuzl)/pg_plus
			end if
			if utnode(iutnode,6)="+" then
				utnode(iutnode,6)=+dpg_minus*uzl.Cols("pn").z(iuzl)/pg_minus
			end if
			if utnode(iutnode,1)<>"" and utnode(iutnode,1)<>0 then
    			if uzl.Cols("vzd").z(iuzl)=0 or uzl.Cols("vzd").z(iuzl)="" then
				if utnode(iutnode,2)="" then
					powerkoef=uzl.Cols("qg").z(iuzl)/uzl.Cols("pg").z(iuzl)
					if powerkoef<=0.9 and powerkoef>=0.2 then utnode(iutnode,2)=utnode(iutnode,1)*powerkoef
					if powerkoef>0.9 then utnode(iutnode,2)=utnode(iutnode,1)*0.9
					if powerkoef<0.2 then utnode(iutnode,2)=utnode(iutnode,1)*0.2
				end if
			else
				if utnode(iutnode,3)="" then
					powerkoef=uzl.Cols("qmin").z(iuzl)/uzl.Cols("pg").z(iuzl)
					if powerkoef<=0.2 and powerkoef>=-0.9 then utnode(iutnode,3)=utnode(iutnode,1)*powerkoef
					if powerkoef>0.2 then utnode(iutnode,3)=utnode(iutnode,1)*0.2
					if powerkoef<-0.9 then utnode(iutnode,3)=utnode(iutnode,1)*(-0.9)
				else
					if utnode(iutnode,3)=-9999 then
						uzl.Cols("qmin").z(iuzl)=-9999
						utnode(iutnode,3)=0
					end if
				end if
				if utnode(iutnode,4)="" then
					powerkoef=uzl.Cols("qmax").z(iuzl)/uzl.Cols("pg").z(iuzl)
					if powerkoef<=0.9 and powerkoef>=0.2 then utnode(iutnode,4)=utnode(iutnode,1)*powerkoef
					if powerkoef>0.9 then utnode(iutnode,4)=utnode(iutnode,1)*0.9
					if powerkoef<0.2 then utnode(iutnode,4)=utnode(iutnode,1)*0.2
				else
					if utnode(iutnode,4)=9999 then
						uzl.Cols("qmax").z(iuzl)=9999
						utnode(iutnode,4)=0
					end if
				end if
				if utnode(iutnode,5)<>"" then
					utnode(iutnode,5)=utnode(iutnode,5)*uzl.Cols("vzd").z(iuzl)/100
				end if
			end if
        end if
			if utnode(iutnode,7)="" and (utnode(iutnode,6)<>"" and utnode(iutnode,6)<>0) then
				powerkoef=uzl.Cols("qn").z(iuzl)/uzl.Cols("pn").z(iuzl)
				utnode(iutnode,7)=utnode(iutnode,6)*powerkoef
			end if
    next
		'if isetgen<21 then
			'if gettrack=1 then
				't.newfile utshabl
				'set uttable =  t.tables("ut_node")
			'end if
			for iutnode=1 to nutnode
				utnode(iutnode,9)=-1 ' Добавление генератора одного... Если больше - кривая трактория...
				gen.SetSel("!sta&P>0&Node="&utnode(iutnode,0))
				igenn=gen.findnextsel(-1)
				if igenn<>-1 then
					if gen.Count=1 then
						utnode(iutnode,9)=igenn
					else
						maxgenpovyb=t.calc("max","Generator","P","!sta&P>0&Node="&utnode(iutnode,0))
						gen.SetSel("!sta&P="&maxgenpovyb&"&Node="&utnode(iutnode,0))
						igenn=gen.findnextsel(-1)
						if igenn<>-1 then utnode(iutnode,9)=igenn
					end if
				end if
				Call writelog "utnode # "&iutnode&",0)",utnode(iutnode,0)&" ; "&utnode(iutnode,1)&"  ; "&utnode(iutnode,2)&"  ; "&utnode(iutnode,3)&"  ; "&utnode(iutnode,4)&"  ; "&utnode(iutnode,5)&"  ; "&utnode(iutnode,6)&"  ; "&utnode(iutnode,7)&"  ; "&utnode(iutnode,9)
				'if gettrack=1 then
					'uttable.AddRow
					'uttable.Cols("ny").z(iutnode)=utnode(iutnode,0)
					'uttable.Cols("pg").z(iutnode)=utnode(iutnode,1)
					'uttable.Cols("qg").z(iutnode)=utnode(iutnode,2)
					'uttable.Cols("qmin").z(iutnode)=utnode(iutnode,3)
					'uttable.Cols("qmax").z(iutnode)=utnode(iutnode,4)
					'uttable.Cols("vzd").z(iutnode)=utnode(iutnode,5)
					'uttable.Cols("pn").z(iutnode)=utnode(iutnode,6)
					'uttable.Cols("qn").z(iutnode)=utnode(iutnode,7)
					'if iutnode=nutnode then
					'	t.Save ishdir&"траектория "&name&Hour(Now())&"h"&Minute(Now())&"m"&Second(Now())&"s"&".ut2",utshabl
					'end if
				'end if
			next
		'end if
    'isetgen=isetgen+1
    tcom_regim=t.Tables("com_regim").Cols("gen_p").z(0)
End Sub
'============================================   set_sec  ==============================================================
Sub set_sec()
    kod1=t.rgm ("p")
    psech1=t.calc("val", "sechen", "psech", "ns=" & secbal(1, nsecbal)) ' sechen - табл. сечение, psech - мощность в сечении, ns- номер сечения, val -
    kshag=-0.2
    Call Pgplus()
    for iut=0 to 100
    	if kod1=0 then kod=t.rgm ("z")
	    if kod<>0 then kod=t.rgm ("p")
    	psech=t.calc("val", "sechen", "psech", "ns=" & secbal(1,nsecbal))
        Call writelog iut,"kshag= " & kshag
        Call writelog iut,"psech1= " & psech1
        Call writelog iut,"psech= " & psech
        Call writelog iut,"kod1= " & kod1
        Call writelog iut,"kod= " & kod
        if abs(psech-secbal(4,nsecbal))<0.5 and kod=0 then exit for
        if abs(psech-secbal(4,nsecbal))<2 and kod=0 and iut>4 then exit for
        if abs(psech-secbal(4,nsecbal))<10 and kod=0 and iut>10 then exit for
        if abs(psech-secbal(4,nsecbal))<30 and kod=0 and iut>18 then exit for
        if abs(psech-secbal(4,nsecbal))<60 and kod=0 and iut>22 then exit for
        if abs(psech-secbal(4,nsecbal))<120 and kod=0 and iut>24 then exit for
        if abs(psech-secbal(4,nsecbal))<200 and kod=0 and iut>26 then exit for
        'if abs(psech-secbal(4,nsecbal))<800 and kod=0 and iut>30 then exit for
        if abs(psech-secbal(4,nsecbal))<abs(psech1-secbal(4,nsecbal)) and kod=0 and kod1=0 and iut>28 then exit for
        if kod=0 and iut>45 then exit for
        if kod <>0 then
            if kod1=0 then delshag=-0.45
            if kod1<>0 then delshag=0.95
        else
            if kod1<>0 then
                delshag=0.45
		    else
                if abs(psech-psech1)>0.001 then delshag=(secbal(4,nsecbal)-psech)/(psech-psech1) else delshag=0.8
                if delshag>5 then delshag=5
                if delshag<-5 then delshag=-5
                if delshag>-0.01 and delshag<0 then delshag=-0.01
                if delshag>0 and delshag<0.01 then delshag=0.01
		    end if
	    end if
        kshag=kshag*delshag
        if kshag>-0.003 and kshag<0 then kshag=-0.003
        if kshag>0 and kshag<0.003 then kshag=0.003
        if kshag>4 then kshag=4
        if kshag<-4 then kshag=-4
	    psech1=psech
    	Call Pgplus()
	    kod1 = kod
    next
end sub
'===================================================================================================================
Sub Pgplus() 'добавлены все Генераторы (УР)
	for iutnode=1 to nutnode
		uzl.setsel("ny=" & utnode(iutnode,0))
		iuzl=uzl.findnextsel(-1)
		'Call writelog "utnode # "&iutnode,"utnode(iutnode,0)=" & utnode(iutnode,0)
		uzl.Cols("pg").z(iuzl)=uzl.Cols("pg").z(iuzl)+utnode(iutnode,1)*kshag
		uzl.Cols("qg").z(iuzl)=uzl.Cols("qg").z(iuzl)+utnode(iutnode,2)*kshag
		uzl.Cols("qmin").z(iuzl)=uzl.Cols("qmin").z(iuzl)+utnode(iutnode,3)*kshag
		uzl.Cols("qmax").z(iuzl)=uzl.Cols("qmax").z(iuzl)+utnode(iutnode,4)*kshag
		uzl.Cols("vzd").z(iuzl)=uzl.Cols("vzd").z(iuzl)+utnode(iutnode,5)*kshag
		uzl.Cols("pn").z(iuzl)=uzl.Cols("pn").z(iuzl)+utnode(iutnode,6)*kshag
		uzl.Cols("qn").z(iuzl)=uzl.Cols("qn").z(iuzl)+utnode(iutnode,7)*kshag
		if utnode(iutnode,9)<>-1 then
			if tcom_regim=0 or tcom_regim=2 then
				gen.cols("P").zn(utnode(iutnode,9))=gen.cols("P").zn(utnode(iutnode,9))+utnode(iutnode,1)*kshag
				if PMINMAX=1 then ' Пока выключен, может выходить за пределы
					if gen.cols("P").zn(utnode(iutnode,9))>gen.cols("Pmax").zn(utnode(iutnode,9)) then
						gen.cols("P").zn(utnode(iutnode,9))=gen.cols("Pmax").zn(utnode(iutnode,9))
					end if
					if gen.cols("P").zn(utnode(iutnode,9))<gen.cols("Pmin").zn(utnode(iutnode,9)) then
					    gen.cols("P").zn(utnode(iutnode,9))=gen.cols("Pmin").zn(utnode(iutnode,9))
					end if
				end if
				Call writelog "utnode # "&iutnode,"utnode-9=" & utnode(iutnode,9)&" utnode-0=" & utnode(iutnode,0)&"  gen.Node=" & gen.cols("Node").zn(utnode(iutnode,9))&"  gen.P=" & gen.cols("P").zn(utnode(iutnode,9))&" uzl.pg="&uzl.Cols("pg").z(iuzl)
			end if
			if tcom_regim=0 or tcom_regim=3 then
                if gen.cols("P").zn(utnode(iutnode,9))>gen.cols("Pmax").zn(utnode(iutnode,9)) then gen.cols("NumPQ").zn(utnode(iutnode,9))=0'Удаляем PQ характеристику
				if gen.cols("NumPQ").zn(utnode(iutnode,9))=0 then
                    gen.cols("Q").zn(utnode(iutnode,9))=gen.cols("Q").zn(utnode(iutnode,9))+utnode(iutnode,2)*kshag
                    gen.cols("Qmin").zn(utnode(iutnode,9))=gen.cols("Qmin").zn(utnode(iutnode,9))+utnode(iutnode,3)*kshag
                    gen.cols("Qmax").zn(utnode(iutnode,9))=gen.cols("Qmax").zn(utnode(iutnode,9))+utnode(iutnode,4)*kshag
                end if
		    end if
		else
		    Call writelog "utnode # "&iutnode,"utnode-9=" & utnode(iutnode,9)&" utnode-0=" & utnode(iutnode,0) & " uzl.pg="&uzl.Cols("pg").z(iuzl)
        end if
	next
    'sumshag=sumshag+kshag
End Sub