
Call Shkura()


'################################################################################################################################
Sub Raschet_Kves(branch,k_reverse)
	Set tnode  =  Rastr.Tables("node")
	Set n_uzla = tnode.Cols("ny")
	Set sta_uzla = tnode.Cols("sta")
	Set gen  =  Rastr.Tables("Generator")
	Set Pg_const = gen.Cols("Pgconst")
	Set Num_gen = gen.Cols("Num")
	Set Name_gen = gen.Cols("Name")
	Set Node_gen = gen.Cols("Node")
	Set Node_sta = gen.Cols("NodeState")
	Set P_gen = gen.Cols("P")
	Set sta_gen = gen.Cols("sta")
	Set Pmax_gen = gen.Cols("Pmax")
	Set Pmin_gen = gen.Cols("Pmin")
	Set tvetv = Rastr.Tables("vetv")

	sha_ut2 = "траектория утяжеления.ut2"
	prdir = Rastr.SEndCommandMain(3,"","",0) ' директория с Rastr
	shabl_ut2 = prdir & "SHABLON\" & sha_ut2

	'k_reverse - коэффициент разворота мощности для ветви, учитывает направление утяжеления
	dPgen = 10   'дельта генерации при определении весовых коэффициентов
	'задаем динамический массивы для хранения параметров траектории утяжеления
	'В столбцах хранятся:
	'0 позиция - N агр
	'1 позиция - K_ves
	'2 позиция - dP утяжеления
	'3 позиция - код действия: 0 - не участвует, 1- загрузить до максимума, 2 - включить, 3 - отключить
	redim traektory(3,1)
	'***********************************************
	'***********************************************
	tvetv.Setsel(branch)
	vetv_pos = tvetv.FindNextSel(-1)
	Pl_ip1 = Flow_Pip(vetv_pos)*k_reverse    'переток по контролируемой ветви в исходном режиме (в Растре для узла ip переток считается положительным при направлении к iq)

	'/////////////////////////////////////////////////////////////////////////////
	'Цикл по таблице ГЕНЕРАТОРЫ
	gen.Setsel("Num != 40100173 & ((Node.na = 510 & Pmax>9) | (Node.na >= 511 & Node.na <= 531 & Pmax >= 50) | (Node.na >= 201 & Node.na <= 409 & Pmax >= 145))")
	'gen.Setsel("(Node.na = 510&Pmax> = 10)|(Node.na> = 511&Node.na<531&Pmax> = 30)|(Node.na = 531&Pmax> = 10)|(Node.na> = 200&Node.na<500&Pmax> = 250)")
	str_traektory = 0 ' начальная строка в массиве траектории
	gen_pos = gen.FindNextSel(-1)
	While gen_pos<>(-1)
		K_ves_gen = 0
		kod_ut = 0   'код утяжеления в соответствии с описанием выше
		redim preserve traektory(3, str_traektory)
		'если генератор включен, добавляем к нему генерацию dPgen и контролируем изменение перетока (Pl_ip2-Pl_ip1)
		If sta_gen.Z(gen_pos) = 0 then
			dPgen_plus = Pmax_gen.Z(gen_pos) - P_gen.Z(gen_pos)         'величина, на которую можно увеличить генерацию
			'dPgen_minus = P_gen.Z(gen_pos)-Pmin_gen.Z(gen_pos)         'величина, на которую можно снизить генерацию не отключая сам генератор
			P_gen.Z(gen_pos) = P_gen.Z(gen_pos) + dPgen
			kod = rastr.rgm(kod_regima)
			If kod<>0 then 'если режим не сходится
				K_ves_gen = 0   'генератор не будет участвовать в траектории утяжеления
			else
				Pl_ip2 = Flow_Pip(vetv_pos) * k_reverse
				K_ves_gen = (Pl_ip2 - Pl_ip1)/dPgen
				'в соответствии с K_ves назначаем данному генератору код утяжеления
					If (K_ves_gen>0 and dPgen_plus>0) then
						kod_ut = 1
						traektory(2,str_traektory) =  dPgen_plus
					End If

					If (K_ves_gen > 0 and dPgen_plus <= 0) then
						kod_ut = 0
						traektory(2,str_traektory) =  0
					End If

					If K_ves_gen<0 then
						kod_ut = 3
						traektory(2,str_traektory) =  P_gen.Z(gen_pos)-dPgen            'P_gen.Z(gen_pos) - если отключаем генератор, dPgen_minus - если разгружаем до минимума
					End If
			End If
			traektory(0,str_traektory) =  Num_gen.Z(gen_pos)
			traektory(1,str_traektory) =  K_ves_gen
			P_gen.Z(gen_pos) = P_gen.Z(gen_pos)-dPgen             'возвращаем исходную генерацию
		End If
		'если генератор отключен, включаем его с генерацией Pmin и контролируем изменение перетока (Pl_ip2-Pl_ip1)
		If sta_gen.Z(gen_pos)<>0 then
			sta_uzla_0 = 0
			Pgen0 = P_gen.Z(gen_pos)   'исходная генерация, установленная для отключенного генератора
			uzel_gen = 0
			dPgen_plus = Pmax_gen.Z(gen_pos)-P_gen.Z(gen_pos)         'величина, на которую можно увеличить генерацию
			'dPgen_minus = P_gen.Z(gen_pos)-Pmin_gen.Z(gen_pos)       'величина, на которую можно снизить генерацию не отключая сам генератор
			sta_gen.Z(gen_pos) = 0
			uzel_gen = Node_gen.Z(gen_pos)                    		'узел, в который включен генератор
			'если узел генератора отключен, запоминаем его состояние, включаем его вместе с ветвями

			If Node_sta.Z(gen_pos)<>0 then
			   sta_uzla_0 = 1
			   HitGen uzel_gen 'если узел генератора выключен, включаем его с ветвями
			End If

			P_gen.Z(gen_pos) = Pmin_gen.Z(gen_pos)+dPgen
			kod = rastr.rgm(kod_regima)

			If kod<>0 then
				K_ves_gen = 0   'если режим при включении генератора на Pg_min не сошелся, он не будет участвовать в траектории утяжеления
			else
				Pl_ip2 = Flow_Pip(vetv_pos)*k_reverse
				K_ves_gen = (Pl_ip2-Pl_ip1)/(Pmin_gen.Z(gen_pos)+dPgen)

				If  K_ves_gen>0 then
					kod_ut = 2
					traektory(2,str_traektory) =  Pmax_gen.Z(gen_pos)
				End If

				If  K_ves_gen <= 0 then
					kod_ut = 0
					traektory(2,str_traektory) =  0
				End If
			End If
			traektory(0,str_traektory) =  Num_gen.Z(gen_pos)
			traektory(1,str_traektory) =  K_ves_gen
			P_gen.Z(gen_pos) = Pgen0  							'возвращаем исходное состояние генератора с нулевой генерацией
			sta_gen.Z(gen_pos) = 1
			'если исходное состояние узла было отключенным, то возвращаем его к тому же состоянию
			If sta_uzla_0 = 1 then
			   tnode.Setsel("ny = " & uzel_gen)      'поиск генераторного узла в таблице УЗЛЫ
			   uzel_pos = tnode.FindNextSel(-1)      'определение его позиции в таблице
			   sta_uzla.Z(uzel_pos) = 1              'возвращаем исходное состояние узла, к которому подключен генератор
			End If
		 End If
		traektory(3,str_traektory) =  kod_ut
		gen_pos = gen.FindNextSel(gen_pos)
		str_traektory = str_traektory + 1
	Wend
	rastr.rgm kod_regima
	'сортируем по убыванию модуля весовых коэффициентов
	Call BubbleSortKvesAbsDown(traektory, str_traektory-1)
	'Формируем таблицу траектории утяжеления МосРДУ
	Rastr.NewFile(shabl_ut2)
	Set trut = Rastr.Tables("Traektory_ut")
	' trut.SetSel("1")
	' trut.DelRows
	str_num = 0   'номер строки в таблице Трактория МосРДУ
	For i = 0 to str_traektory - 1
		If traektory(3,i)>0 then
			trut.AddRow
			trut.cols("Num").Z(str_num) = traektory(0,i)
			trut.cols("Kves").Z(str_num) = traektory(1,i)
			trut.cols("dPgen").Z(str_num) = traektory(2,i)
			trut.cols("kod_ut").Z(str_num) = traektory(3,i)
			str_num = str_num + 1
		End If
	next
	'Заполняем поле "Name" в созданной таблице
	For i = 0 to trut.size-1
		num_G = trut.Cols("Num").Z(i)
		gen.SetSel("Num = " & num_G)
		gen_pos = gen.FindNextSel(-1)
		If gen_pos<>-1 then trut.Cols("Name").Z(i) = gen.cols("Name").Z(gen_pos)
	next
	'стираем массив traektory
	Erase traektory
End Sub

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'функция определения перетока мощности в начале ветви
Function Flow_Pip(position)    'позиция ветви в таблице VETV
	Set tvetv = Rastr.Tables("vetv")
	Flow_Pip = tvetv.Cols("pl_ip").Z(position)'за положительное направление принято направление от шин в элемент
End Function

Function Flow_Piq(position)    'позиция ветви в таблице VETV
	Set tvetv = Rastr.Tables("vetv")
	Flow_Piq = tvetv.Cols("pl_iq").Z(position)      'за положительное направление принято направление от шин в элемент
End Function

Function Flow_P(position,control_P)    'позиция ветви в таблице VETV, место замера P
	If control_P = "ip" then Flow_P =  Flow_Pip(position)
	If control_P = "iq" then Flow_P =  Flow_Piq(position)
End Function

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'функция определения максимального тока по ветви
Function Flow_I(position)    'позиция ветви в таблице VETV
	Set tvetv = Rastr.Tables("vetv")
	Flow_I = max(tvetv.Cols("ib").Z(position),tvetv.Cols("ie").Z(position))*1000
End Function

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'подпрограмма включения узла с ветвями
Sub HitGen(uzel)
	Set tvetv = Rastr.Tables("vetv")
	Set tnode = Rastr.Tables("node")
	tnode.SetSel("ny = " & uzel)
	tnode.Cols("sta").calc("0")
	rastr.printp "включение узла №" & uzel
	tvetv.SetSel("ip = " & uzel & "|iq = " & uzel)
	tvetv.Cols("sta").Calc("0")
End sub

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'Подпрограмма сортировки методом пузырька по убыванию модуля
Sub BubbleSortKvesAbsDown(Arr, n)
	dim i,j,tmp
    For i = n-1 to 0 step -1
        For j = 0 to i
            If Abs(Arr(1,j)) <= Abs(Arr(1,j+1)) then
                Tmp = Arr(0,j)
                Arr(0,j) = Arr(0,j+1)
                Arr(0,j+1) = Tmp
                Tmp = Arr(1,j)
                Arr(1,j) = Arr(1,j+1)
                Arr(1,j+1) = Tmp
                Tmp = Arr(2,j)
                Arr(2,j) = Arr(2,j+1)
                Arr(2,j+1) = Tmp
                Tmp = Arr(3,j)
                Arr(3,j) = Arr(3,j+1)
                Arr(3,j+1) = Tmp
            End If
        next
    next
End Sub

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'Подпрограмма сортировки методом пузырька по возрастанию
Sub BubbleSortUp(Arr, n)
	dim i,j,tmp
    For i = n-1 to 0 step -1
        For j = 0 to i
            If Arr(1,j) >= Arr(1,j+1) then
                Tmp = Arr(0,j)
                Arr(0,j) = Arr(0,j+1)
                Arr(0,j+1) = Tmp
                Tmp = Arr(1,j)
                Arr(1,j) = Arr(1,j+1)
                Arr(1,j+1) = Tmp
                Tmp = Arr(2,j)
                Arr(2,j) = Arr(2,j+1)
                Arr(2,j+1) = Tmp
                Tmp = Arr(3,j)
                Arr(3,j) = Arr(3,j+1)
                Arr(3,j+1) = Tmp
            End If
        next
    next
End sub

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'Подпрограмма сортировки методом пузырька по убыванию
Sub BubbleSortDown(Arr, n)
	dim i,j,tmp
    For i = n-1 to 0 step -1
        For j = 0 to i
            If Arr(1,j) <= Arr(1,j+1) then
                Tmp = Arr(0,j)
                Arr(0,j) = Arr(0,j+1)
                Arr(0,j+1) = Tmp
                Tmp = Arr(1,j)
                Arr(1,j) = Arr(1,j+1)
                Arr(1,j+1) = Tmp
                Tmp = Arr(2,j)
                Arr(2,j) = Arr(2,j+1)
                Arr(2,j+1) = Tmp
                Tmp = Arr(3,j)
                Arr(3,j) = Arr(3,j+1)
                Arr(3,j+1) = Tmp
            End If
        next
    next
End sub

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'функция расчета суммы столбца заданного массива
Function Column_Sum(Arr, n, num) 'Arr - массив, n - число строк в массиве, num - столбец, в котором определяется сумма элементов
	dim i
	Column_Sum = 0
	For i = 0 to n
		Column_Sum = Column_Sum+Arr(num,i)
	next
End Function

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'функция поиска минимума среди двух значений
Function min(a,b)
	'dim a,b
	If a<= b then
		min = a
	else
		min = b
	End If
End Function

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'функция поиска максимума среди двух значений
Function max(a,b)
	'dim a,b
	If a >= b then
		max = a
	else
		max = b
	End If
End Function

'////////////////////////////////////////////////////
'функция определения мощности в балансирующем узле
Function Balance_P()
	'ny_bal = 10291049 'номер балансирующего узла (может измениться при очередном замере - поэтому ушли от этого)
	Set tnode = Rastr.Tables("node")
	tnode.SetSel("na = 102&tip = 0")
	'tnode.SetSel("ny = " & ny_bal)
	node_bal_pos = tnode.FindNextSel(-1)
	Balance_P = 0    'генерация в балансирующем узле
	Balance_P = tnode.Cols("pg").Z(node_bal_pos)
End Function

'/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'функция, выполянющая один шаг утяжеления с генератором N_agr, на выходе дает код успешности произведенного шага
Function shag_ut(N_agr, kod_d, U_control) 'kod_d - код действия с генератором: 10-загрузить до Pmax, 11-включить, 20-разгрузить до Pmin, 21-отключить
	If U_control = 1 then
		Call Control_U_500_750()  'запуск контроля напряжения в узлах 500-750 кВ сети ОЭС Центра
		Set tnode = Rastr.Tables("node")
		Set gen = Rastr.Tables("Generator")
		Set Num_gen = gen.Cols("Num")
		Set Node_gen = gen.Cols("Node")
		Set P_gen = gen.Cols("P")
		Set sta_gen = gen.Cols("sta")
		Set Pmax_gen = gen.Cols("Pmax")
		Set Pmin_gen = gen.Cols("Pmin")
		gen.Setsel("Num = " & N_agr)
		gen_pos = gen.FindNextSel(-1)
		P_gen0 = P_gen.Z(gen_pos)      'исходная генерация до осуществления шага утяжеления
		sta_gen0 = sta_gen.Z(gen_pos)  'исходное состояние генераторного узла до осуществления шага утяжеления
		Select Case kod_d
			Case 10
			   P_gen.Z(gen_pos) = Pmax_gen.Z(gen_pos)
			   rastr.printp "Загрузка до Pmax генератора №" & Num_gen.Z(gen_pos)
			Case 11
			   sta_gen.Z(gen_pos) = 0
			   P_gen.Z(gen_pos) = Pmax_gen.Z(gen_pos)
			   uzel_gen = Node_gen.Z(gen_pos)
			   tnode.Setsel("ny = " & uzel_gen)
			   uzel_pos = tnode.FindNextSel(-1)
			   sta_uzla0 = tnode.Cols("sta").Z(uzel_pos)   'исходное состояние узла в таблице УЗЛЫ до шага утяжеления
			   If tnode.Cols("sta").Z(uzel_pos)<>0 then HitGen uzel_gen
			   rastr.printp "Включение с мощностью Pmax генератора №" & Num_gen.Z(gen_pos)
			Case 20
			   P_gen.Z(gen_pos) = Pmin_gen.Z(gen_pos)
			Case 21
			sta_gen.Z(gen_pos) = 1
			rastr.printp "Отключение генератора №" & Num_gen.Z(gen_pos)
		End Select
		'расчет режима с учетом шага утяжеления
		shag_ut = rastr.rgm(kod_regima)  'код расчета режима
		If shag_ut<>0 then 'если режим разошелся возвращаемся к предыдущему состоянию
			rastr.printp "Режим на данном шаге утяжеления не сошелся - возврат к предыдущему шагу!"
			P_gen.Z(gen_pos) = P_gen0
			sta_gen.Z(gen_pos) = sta_gen0
			If sta_gen0<>0 then tnode.Cols("sta").Z(uzel_pos) = sta_uzla0
			ppp = rastr.rgm(kod_regima)
			If ppp<>0 then ppp = rastr.rgm("p")
			If ppp<>0 then rastr.printp "Режим не сошелся при откате назад"
		End If
        End If
End Function

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'********ПОДПРОГРАММА ПОИСКА ПРЕДЕЛЬНОГО РЕЖИМА*************************************************************************
'///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Sub Poisk_Ppred(branch,kQut,znch)  'контролируемая ветвь, направление утяжеления по Q, зона нечуствительности по Q для АТ
	Set tvetv = Rastr.Tables("vetv")
	tvetv.Setsel(branch)
	vetv_pos = tvetv.FindNextSel(-1)
	Set trut = Rastr.Tables("Traektory_ut")
	shag = 0
	ut_End = 0     'в траектории участвуют генераторы как на разгрузку, так и на загрузку - ut_End = 1 когда в траектории остануться только генераторы одной группы
	zapusk_Q = false   'флаг на запуск утяжеления по Q при помощи РПН
	'определяем направление утяжеления по генерации в балансирующем узле
	'Цикл утяжеления по условию
	Do While (shag < trut.Size and Abs(Balance_P()) <= 3000)
		rastr.printp "Переток P = " & Flow_Pip(vetv_pos)*(-1)
		Pbal = Balance_P()
		If ut_End = 1 then
			flag = 2
		else
			If Pbal <= (-100) then flag = 1
			If Pbal >= 100 then flag = 0
		End If
		'rastr.printp "Шаг №" & shag & ": баланс " & Balance_P(node_bal_pos)
		Select Case flag
			Case 0
				trut.SetSel("Uchastie = 0&kod_ut<3")
				ut_pos = trut.FindNextSel(-1)
				If ut_pos = (-1) then
					ut_End = 1
					Trans_Ut branch,kQut,znch,true,true    'ЗАПУСК НА УТЯЖЕЛЕНИЕ ПО Q ПУТЕМ ИЗМЕНЕНИЯ ПОЛОЖЕНИЯ РПН ТРАНСФОРМАТОРОВ
				else
					If trut.cols("kod_ut").Z(ut_pos) = 1 then kod_d = 10
					If trut.cols("kod_ut").Z(ut_pos) = 2 then kod_d = 11
					result = shag_ut(trut.cols("Num").Z(ut_pos), kod_d, 1)
					If result<>0 then
						rastr.printp "Режим не сходится!!! Пропускаем этот генератор"
						trut.cols("rashojdenie").Z(ut_pos) = 1
					End If
					trut.cols("Uchastie").Z(ut_pos) = 1
					trut.cols("n_shaga").Z(ut_pos) = shag
					shag = shag + 1
				End If

			Case 1
				trut.SetSel("Uchastie = 0 & kod_ut = 3")
				ut_pos = trut.FindNextSel(-1)
				If ut_pos = (-1) then
					ut_End = 1
					Trans_Ut branch,kQut,znch,true,true  'ЗАПУСК НА УТЯЖЕЛЕНИЕ ПО Q ПУТЕМ ИЗМЕНЕНИЯ ПОЛОЖЕНИЯ РПН ТРАНСФОРМАТОРОВ
				else
					If trut.cols("kod_ut").Z(ut_pos) = 3 then kod_d = 21
					result = shag_ut(trut.cols("Num").Z(ut_pos), kod_d, 1)
					If result<>0 then
						rastr.printp "Режим не сходится!!! Пропускаем этот генератор"
						trut.cols("rashojdenie").Z(ut_pos) = 1
					End If
					trut.cols("Uchastie").Z(ut_pos) = 1
					trut.cols("n_shaga").Z(ut_pos) = shag
					shag = shag + 1
				End If
			Case 2    'когда кончились генераторы одного направления утяжеления
				on Error Resume Next
				trut.SetSel("Uchastie = 0")
				ut_pos = trut.FindNextSel(-1)
				If trut.cols("kod_ut").Z(ut_pos) = 1 then kod_d = 10
				If trut.cols("kod_ut").Z(ut_pos) = 2 then kod_d = 11
				If trut.cols("kod_ut").Z(ut_pos) = 3 then kod_d = 21
				result = shag_ut(trut.cols("Num").Z(ut_pos), kod_d, 1)
				If result<>0 then
					rastr.printp "Режим не сходится при несбалансированном утяжелении"
					trut.cols("rashojdenie").Z(ut_pos) = 1
				End If
				trut.cols("Uchastie").Z(ut_pos) = 1
				trut.cols("n_shaga").Z(ut_pos) = shag
				shag = shag+1
			End Select
	'rastr.printp shag
	Loop
End Sub

'//////////////////////////////////////////////////////////////////////
Sub Control_U_500_750()
	Set tnode = Rastr.tables("node")
	tnode.SetSel("na >= 510 & na <= 532 & uhom >= 500 & bsh > 0 & vras < 0.8*uhom&sta = 0") 'выборка по  ОЭС Центра
	tnode.Cols("sta").Calc("1")
End Sub

'**********************************************************************************************************************
'Подпрограмма утяжеления по реактивной мощности при помощи РПН трансформаторов, входной параметр - контролируемая ветвь и направление утяжеления
Sub Trans_Ut(branch,k_reverse,zone_nch,option1,option2)  'option1 - расчет Kвес по Q, option2 - утяжеление по Q
	'zone_nch = 0.2      'зона нечуствительности - определяет порог выполнения условия по регулированию РПН трансформатора при изменении положения РПН на одну анцапфу

	sha_Ktves = "весовые коэффициенты трансформаторов.ves"
	sha_anc = "анцапфы.anc"
	prdir = Rastr.SEndCommandMain(3,"","",0) ' директория с Rastr
	shabl_ves = prdir & "SHABLON\" & sha_Ktves
	shabl_anc = prdir & "SHABLON\" & sha_anc
	'проверка загрузки файла с анцапфами
	proverka = false
	Set Tabs = Rastr.Tables
	For i = 0 to Tabs.Count-1
		If tabs(i).Name = "ancapf" then
			proverka = true
			j = i
		End If
	Next

	If ((not proverka) or (tabs(j).size = 0)) then
		msgbox "Не загружен файл анцапф! Срочно загрузите.",48,"Внимание!!!"
		file_anc = Rastr.SEndCommandMain(1,"Выберите файл с анцапфами","",0)
		If file_anc = "" then exit Sub
		Rastr.Load 1,file_anc,shabl_anc
	End If

	Rastr.rgm kod_regima

	redim trans_ves(4,1)                    'матрица весовых коэффициентов трансформаторов: 0-ip;1-iq;2-np;3-Kt_ves;4-anc0
	Set tvetv = Rastr.tables("vetv")
	Set tancapf = Rastr.tables("ancapf")
	tvetv.Setsel(branch)
	vetv_pos = tvetv.FindNextSel(-1)
	Ql_ip0 = tvetv.Cols("ql_ip").Z(vetv_pos)*k_reverse   'исходный переток Q в начале контролируемой ЛЭП

	If option1 then
		tvetv.Setsel("sel = 1")
		pos = tvetv.FindNextSel(-1)
		stroka_trans = 0
		While pos<>(-1)
			anc0 = tvetv.Cols("n_anc").Z(pos)          'текущее положение РПН на трансформаторе
			ktr0 = tvetv.Cols("ktr").Z(pos)            'текущий коэффициент трансформации трансформатора
			nomer_bd = tvetv.Cols("bd").Z(pos)
			redim preserve trans_ves(4,stroka_trans)
			'проверяем в каком положении стоит РПН: если не в крайнем максимальном, тогда переключаем на одну анцапфу вверх(с контролем изменения коэффициента трансформации) и контролируем наброс Q по исследуемой ветви
			If anc0 < Anc_max(nomer_bd) then              'если РПН не в крайнем максимальном положении, то добавляем одну отпайку
				do
					tvetv.Cols("n_anc").Z(pos) = tvetv.Cols("n_anc").Z(pos)+1    'если при добавлении одной отпайки коэффициент трансформации не меняется то добавляем еще до начала изменения
					'коэффициента трансформации(актуально для нейтральных положений)
					tvetv.Cols("n_anc").Calc("n_anc*1")
					ktr1 = tvetv.Cols("ktr").Z(pos)
				Loop While ktr1 = ktr0

				kod = Rastr.rgm(kod_regima)
				Ql_ip1 = tvetv.Cols("ql_ip").Z(vetv_pos)*k_reverse
				Kt_ves = (Ql_ip1-Ql_ip0)
				trans_ves(0,stroka_trans) = tvetv.Cols("ip").Z(pos)
				trans_ves(1,stroka_trans) = tvetv.Cols("iq").Z(pos)
				trans_ves(2,stroka_trans) = tvetv.Cols("np").Z(pos)
				trans_ves(3,stroka_trans) = Kt_ves
				trans_ves(4,stroka_trans) = anc0
			End If

			If anc0 = Anc_max(nomer_bd) then
				tvetv.Cols("n_anc").Z(pos) = anc0-1
				tvetv.Cols("n_anc").Calc("n_anc*1")
				kod = Rastr.rgm(kod_regima)
				If kod = 0 then
					Ql_ip1 = tvetv.Cols("ql_ip").Z(vetv_pos)*k_reverse
					Kt_ves = (Ql_ip1-Ql_ip0)*(-1)
					trans_ves(0,stroka_trans) = tvetv.Cols("ip").Z(pos)
					trans_ves(1,stroka_trans) = tvetv.Cols("iq").Z(pos)
					trans_ves(2,stroka_trans) = tvetv.Cols("np").Z(pos)
					trans_ves(3,stroka_trans) = Kt_ves
					trans_ves(4,stroka_trans) = anc0
				else
					tvetv.Cols("n_anc").Z(pos) = anc0
					tvetv.Cols("n_anc").Calc("n_anc*1")
					Kt_ves = 0  'трансформатор не участвует в утяжелении по Q
					trans_ves(0,stroka_trans) = tvetv.Cols("ip").Z(pos)
					trans_ves(1,stroka_trans) = tvetv.Cols("iq").Z(pos)
					trans_ves(2,stroka_trans) = tvetv.Cols("np").Z(pos)
					trans_ves(3,stroka_trans) = Kt_ves
					trans_ves(4,stroka_trans) = anc0
				End If
			End If
			tvetv.Cols("n_anc").Z(pos) = anc0
			tvetv.Cols("n_anc").Calc("n_anc*1")
			stroka_trans = stroka_trans+1
			pos = tvetv.FindNextSel(pos)
		Wend

		 'сортировка Kt_ves в порядке убывания модуля
		BubbleSortAbsDown trans_ves, stroka_trans-1

		 'Заполняем таблицу УТЯЖЕЛЕНИЕ ПО Q
		Rastr.NewFile(shabl_ves)

		Set transutQ = Rastr.Tables("TransUt")
		 'transutQ.SetSel("1")
		 'transutQ.DelRows
	    For i = 0 to stroka_trans-1
			transutQ.AddRow
			transutQ.Cols("ip").Z(i) = trans_ves(0,i)
			transutQ.Cols("iq").Z(i) = trans_ves(1,i)
			transutQ.Cols("np").Z(i) = trans_ves(2,i)
			transutQ.Cols("kt_ves").Z(i) = trans_ves(3,i)
			transutQ.Cols("anc0").Z(i) = trans_ves(4,i)
			tvetv.SetSel("ip = " & trans_ves(0,i) & "& iq = " & trans_ves(1,i) & "& np = " & trans_ves(2,i))
			j = tvetv.FindNextSel(-1)
			transutQ.Cols("name").Z(i) = tvetv.Cols("dname").Z(j)
		next
	End If

	Erase trans_ves

	If option2 then
	    'Применяем новые положения РПН согласно весовым коэффициентам из таблицы "Утяжеление по Q"
	    Set transutQ = Rastr.Tables("TransUt")
		transutQ.Cols("Uchastie").Calc("0")
		For i = 0 to transutQ.size-1
			tvetv.SetSel("ip = " & transutQ.Cols("ip").z(i) & "& iq = " & transutQ.Cols("iq").z(i) & "&  np = " & transutQ.Cols("np").z(i))
			pos_trans = tvetv.FindNextSel(-1)
			anc0 = tvetv.cols("n_anc").Z(pos_trans)   'запоминаем исходное положение РПН для возможности отката назад
			rastr.printp "Крутим " & tvetv.cols("dname").Z(pos_trans) & ".....n_anc исх = " & tvetv.cols("n_anc").Z(pos_trans)
			If transutQ.Cols("kt_ves").z(i)>zone_nch then 'если весовой коэффициент >зоны нечуствительности zone_nch тогда выставляем максимальное положение РПН
				tvetv.cols("n_anc").Z(pos_trans) = 50
				tvetv.cols("n_anc").calc("1*n_anc")
				kod = Rastr.rgm(kod_regima)
				If kod<>0 then        'если режим разошелся, возвращаем исходное положение РПН
					tvetv.cols("n_anc").Z(pos_trans) = anc0
					transutQ.Cols("Uchastie").Z(i) = false
				else
					tvetv.cols("groupid").Z(pos_trans) = 50
					transutQ.Cols("Uchastie").Z(i) = true
				End If
			End If
			If transutQ.Cols("kt_ves").z(i) < zone_nch*(-1) then 'если весовой коэффициент <0 тогда выставляем минимальное положение РПН
				tvetv.cols("n_anc").Z(pos_trans) = 1
				tvetv.cols("n_anc").calc("1*n_anc")
				kod = Rastr.rgm(kod_regima)
				If kod<>0 then        'если режим разошелся, возвращаем исходное положение РПН
					tvetv.cols("n_anc").Z(pos_trans) = anc0
				else
					tvetv.cols("groupid").Z(pos_trans) = 1
					transutQ.Cols("Uchastie").Z(i) = true
				End If
			End If
		next
	End If
End Sub


'********************************************************************************************************
'функция определения крайнего максимального положения РПН трансформатора в базе данных Анцапфы
Function Anc_max(nomer_bd)
	On Error Resume Next
	Set tancapf = Rastr.tables("ancapf")
	tancapf.SetSel("nbd = " & nomer_bd)
	pos_bd_anc = tancapf.FindNextSel(-1)
	Anc_max = tancapf.cols("n_anc1").Z(pos_bd_anc)+tancapf.cols("n_anc2").Z(pos_bd_anc)+tancapf.cols("n_anc3").Z(pos_bd_anc)+tancapf.cols("n_anc4").Z(pos_bd_anc)+tancapf.cols("n_anc5").Z(pos_bd_anc)+tancapf.cols("kne").Z(pos_bd_anc)
End Function

'************************************************************************************************************
'Подпрограмма выбора трансформаторов 220 кВ и выше в Московской ЭС с возможностью регулирования коэффициента трансформации под нагрузкой
Sub Trans_RPN()
	Set tvetv = rastr.tables("vetv")
	tvetv.Setsel("sel = 1")
	tvetv.Cols("sel").Calc("0")   'убираем выделение ветвей
	tvetv.Setsel("ip.na = 510 & tip = 1 & sta = 0 & n_anc != 0 & ip.uhom > 110 & iq.uhom >= 110")
	pos = tvetv.FindNextSel(-1)
	While pos<>-1
		name = tvetv.cols("dname").z(pos)
		a = InStr(1,name,"РПН")
		If a>0 then tvetv.cols("sel").z(pos) = 1
		pos = tvetv.FindNextSel(pos)
	Wend
End Sub

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'Подпрограмма сортировки методом пузырька по убыванию модуля
Sub BubbleSortAbsDown(Arr, n)
	dim i,j,tmp
    For i = n-1 to 0 step (-1)
        For j = 0 to i
            If Abs(Arr(3,j)) <= Abs(Arr(3,j+1)) then
                Tmp = Arr(0,j)
                Arr(0,j) = Arr(0,j+1)
                Arr(0,j+1) = Tmp
                Tmp = Arr(1,j)
                Arr(1,j) = Arr(1,j+1)
                Arr(1,j+1) = Tmp
                Tmp = Arr(2,j)
                Arr(2,j) = Arr(2,j+1)
                Arr(2,j+1) = Tmp
                Tmp = Arr(3,j)
                Arr(3,j) = Arr(3,j+1)
                Arr(3,j+1) = Tmp
                Tmp = Arr(4,j)
                Arr(4,j) = Arr(4,j+1)
                Arr(4,j+1) = Tmp
            End If
        next
    next
End sub

'/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'функция, выполянющая один шаг разутяжеления с генератором N_agr, на выходе дает код успешности произведенного шага
Function shag_razut(N_agr, kod_d, dP)'kod_d - код действия с генератором: 11-включить, 20-разгрузить на величину dP, 21-отключить
	'dP - величина, на которую требуется разгрузить генератор
	Set tnode = Rastr.Tables("node")
	Set gen = Rastr.Tables("Generator")
	Set Num_gen = gen.Cols("Num")
	Set Node_gen = gen.Cols("Node")
	Set P_gen = gen.Cols("P")
	Set sta_gen = gen.Cols("sta")
	Set Pmax_gen = gen.Cols("Pmax")
	Set Pmin_gen = gen.Cols("Pmin")
	gen.Setsel("Num = " & N_agr)
	gen_pos = gen.FindNextSel(-1)
	P_gen0 = P_gen.Z(gen_pos)      'исходная генерация до осуществления шага утяжеления
	sta_gen0 = sta_gen.Z(gen_pos)  'исходное состояние генераторного узла до осуществления шага разутяжеления
	Select Case kod_d
		Case 11
			sta_gen.Z(gen_pos) = 0
			'P_gen.Z(gen_pos) = Pmax_gen.Z(gen_pos)
			uzel_gen = Node_gen.Z(gen_pos)
			tnode.Setsel("ny = " & uzel_gen)
			uzel_pos = tnode.FindNextSel(-1)
			sta_uzla0 = tnode.Cols("sta").Z(uzel_pos) 'исходное состояние узла в таблице УЗЛЫ до шага утяжеления
			If tnode.Cols("sta").Z(uzel_pos)<>0 then HitGen uzel_gen
			rastr.printp "Включение генератора №" & Num_gen.Z(gen_pos) & " с мощностью " & P_gen.Z(gen_pos) & " МВт"
		Case 20
			P_gen.Z(gen_pos) = Pmax_gen.Z(gen_pos)-dP
			rastr.printp "Разгрузка генератора №" & Num_gen.Z(gen_pos) & " до " & P_gen.Z(gen_pos) & " МВт"
		Case 21
			sta_gen.Z(gen_pos) = 1
			rastr.printp "Отключение генератора №" & Num_gen.Z(gen_pos)
	End Select
	'расчет режима с учетом шага разутяжеления
	shag_razut = rastr.rgm("p")  'код расчета режима
	If shag_razut<>0 then 'если режим разошелся возвращаемся к предыдущему состоянию
		rastr.printp "Режим на данном шаге разутяжеления не сошелся - возврат к предыдущему шагу!"
		P_gen.Z(gen_pos) = P_gen0
		sta_gen.Z(gen_pos) = sta_gen0
		If sta_gen0<>0 then tnode.Cols("sta").Z(uzel_pos) = sta_uzla0
		ppp = rastr.rgm("p")
		'If ppp<>0 then ppp = rastr.rgm("p")
		If ppp<>0 then rastr.printp "Режим не сошелся при откате назад"
	End If
End Function
'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

Sub Poisk_P(branch,Pzad,k_reverse)
	Set tvetv = Rastr.Tables("vetv")
	tvetv.Setsel(branch)
	vetv_pos = tvetv.FindNextSel(-1)
	Set trut = Rastr.Tables("Traektory_ut")
	Set tGen = Rastr.Tables("Generator")
	'perehod = false   'флаг перехода через Pzad в процессе разутяжеления
	'определим количество пройденных шагов при утяжелении
	shag_max = 0
	trut.Setsel("Uchastie = 1 & rashojdenie = 0")   'выборка пройденных шагов утяжеления
	i = trut.findnextsel(-1)
	While i<>-1
		If shag_max<trut.cols("n_shaga").Z(i) then shag_max = trut.cols("n_shaga").Z(i)
		i = trut.findnextsel(i)
	Wend
	shag = shag_max
	Do While (shag >= 0 and Flow_Pip(vetv_pos)*k_reverse>Pzad)
		'rastr.printp "Выполнен шаг №" & shag & " - переток P = " & Flow_Pip(vetv_pos)*(-1)
		trut.Setsel("n_shaga = "& shag)   'выборка пройденных шагов утяжеления
		pos_shaga = trut.findnextsel(-1)
		kod_utyagelenia = 0
		If trut.cols("Uchastie").Z(pos_shaga) = true then
			If trut.cols("rashojdenie").Z(pos_shaga) = false then
				kod_utyagelenia = trut.cols("kod_ut").Z(pos_shaga)
			End If
		End If
		Select Case kod_utyagelenia
			Case 0
				shag = shag-1
			Case 1
				result = shag_razut(trut.cols("Num").Z(pos_shaga), 20, trut.cols("dPgen").Z(pos_shaga))
				If result<>0 then
					rastr.printp "Режим не сходится!!! Пропускаем этот генератор"
					trut.cols("rashojdenie").Z(pos_shaga) = 1
				End If
				trut.cols("Uchastie").Z(pos_shaga) = 0
				shag = shag-1
			Case 2
				result = shag_razut(trut.cols("Num").Z(pos_shaga), 21, trut.cols("dPgen").Z(pos_shaga))
				If result<>0 then
					rastr.printp "Режим не сходится!!! Пропускаем этот генератор"
					trut.cols("rashojdenie").Z(pos_shaga) = 1
				End If
				trut.cols("Uchastie").Z(pos_shaga) = 0
				shag = shag-1
			Case 3
				result = shag_razut(trut.cols("Num").Z(pos_shaga), 11, trut.cols("dPgen").Z(pos_shaga))
				If result<>0 then
					rastr.printp "Режим не сходится!!! Пропускаем этот генератор"
					trut.cols("rashojdenie").Z(pos_shaga) = 1
				End If
				trut.cols("Uchastie").Z(pos_shaga) = 0
				shag = shag-1
		End Select
	Loop

	' как только перескочили через Pзад смотрим dP = Pзад-P и если dP>1 МВт то откатываемся на один шаг назад, проверяем dP еще раз, и если dP>-1 МВт,
	' то откатившийся шаг выполняем постепенно до |dP|< = 1 методом половинного деления
	dP = Pzad-Flow_Pip(vetv_pos)*k_reverse

	If dP>1 then
		shag = shag + 1
		trut.Setsel("n_shaga = " & shag)   'выборка пройденных шагов утяжеления
		pos_shaga = trut.findnextsel(-1)
		trut.cols("Uchastie").Z(pos_shaga) = 1
		If trut.cols("kod_ut").Z(pos_shaga) = 1 then kod_d = 10
		If trut.cols("kod_ut").Z(pos_shaga) = 2 then kod_d = 11
		If trut.cols("kod_ut").Z(pos_shaga) = 3 then kod_d = 21
		result = shag_ut(trut.cols("Num").Z(pos_shaga), kod_d, 0)
		If result<>0 then msgbox "Режим не сошелся при откате на один шаг при поиске заданного перетока мощности по элементу!"
		dP = Pzad-Flow_Pip(vetv_pos)*k_reverse
		If dP > (-1) then
			kod_utyagelenia = trut.cols("kod_ut").Z(pos_shaga)
			tGen.SetSel("Num = " & trut.cols("Num").Z(pos_shaga))
			gen_pos = tGen.FindNextSel(-1)
			Select Case kod_utyagelenia
				Case 1
					rastr.printp "алгоритм 1"
					P_gen0 = tGen.Cols("Pmax").Z(gen_pos)-trut.cols("dPgen").Z(pos_shaga)
					P_gen1 = tGen.Cols("Pmax").Z(gen_pos)
					Do While (Abs(dP)>1 or Abs(P_gen1-P_gen0)>10)
						tGen.Cols("P").Z(gen_pos) = (P_gen1+P_gen0)/2
						rastr.rgm "p"
						dP = Pzad-Flow_Pip(vetv_pos)*k_reverse
						If dP<0 then
							P_gen1 = (P_gen1+P_gen0)/2
						else
							P_gen0 = (P_gen1+P_gen0)/2
						End If
					Loop
				Case 2
					rastr.printp "алгоритм 2"
					tGen.Cols("P").Z(gen_pos) = tGen.Cols("Pmin").Z(gen_pos)
					rastr.rgm "p"
					dP = Pzad-Flow_Pip(vetv_pos)*k_reverse
					If dP >(-1) then
						P_gen0 = tGen.Cols("Pmin").Z(gen_pos)
						P_gen1 = tGen.Cols("Pmax").Z(gen_pos)
						Do While (Abs(dP) > 1 or Abs(P_gen1-P_gen0) > 10)
							tGen.Cols("P").Z(gen_pos) = (P_gen1+P_gen0)/2
							rastr.rgm "p"
							dP = Pzad-Flow_Pip(vetv_pos)*k_reverse
							If dP<0 then
								P_gen1 = (P_gen1+P_gen0)/2
							else
								P_gen0 = (P_gen1+P_gen0)/2
							End If
						Loop
					End If
				Case 3
					rastr.printp "алгоритм 3"
					tGen.Cols("P").Z(gen_pos) = tGen.Cols("Pmin").Z(gen_pos)
					tGen.Cols("sta").Z(gen_pos) = 0
					If tGen.Cols("NodeState").Z(gen_pos)<>0 then HitGen tGen.Cols("Node").Z(gen_pos)
					rastr.rgm "p"
					dP = Pzad-Flow_Pip(vetv_pos)*k_reverse
					If dP > (-1) then
						P_gen0 = tGen.Cols("Pmin").Z(gen_pos)
						P_gen1 = trut.cols("dPgen").Z(pos_shaga)
						Do While (Abs(dP) > 1 or Abs(P_gen1-P_gen0) > 10)
							tGen.Cols("P").Z(gen_pos) = (P_gen1+P_gen0)/2
							rastr.rgm "p"
							dP = Pzad-Flow_Pip(vetv_pos)*k_reverse
							If dP < 0 then
								P_gen1 = (P_gen1+P_gen0)/2
							else
								P_gen0 = (P_gen1+P_gen0)/2
							End If
						Loop
					End If
			End Select
	    End If
	End If
End Sub

'///////////////////////////////////////////////////////////////////////////////////////////////
'Поиск предельного по току режима
'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
Sub Poisk_I(branch,Izad)
	Set tvetv = Rastr.Tables("vetv")
	tvetv.Setsel(branch)
	vetv_pos = tvetv.FindNextSel(-1)
	Set trut = Rastr.Tables("Traektory_ut")
	Set tGen = Rastr.Tables("Generator")
	'определим количество пройденных шагов при утяжелении
	shag_max = 0
	trut.Setsel("Uchastie = 1&rashojdenie = 0")   'выборка пройденных шагов утяжеления
	i = trut.findnextsel(-1)
	While i<>-1
		If shag_max<trut.cols("n_shaga").Z(i) then shag_max = trut.cols("n_shaga").Z(i)
		i = trut.findnextsel(i)
	Wend
	shag = shag_max
	'msgbox Flow_I(vetv_pos)
	Do While (shag >= 0 and Flow_I(vetv_pos) > Izad)
		'rastr.printp "Выполнен шаг №" & shag & " - переток P = " & Flow_Pip(vetv_pos)*(-1)
		trut.Setsel("n_shaga = "& shag)   'выборка пройденных шагов утяжеления
		pos_shaga = trut.findnextsel(-1)
		kod_utyagelenia = 0
		If trut.cols("Uchastie").Z(pos_shaga) = true then
			If trut.cols("rashojdenie").Z(pos_shaga) = false then
				kod_utyagelenia = trut.cols("kod_ut").Z(pos_shaga)
			End If
		End If
		Select Case kod_utyagelenia
			Case 0
				shag = shag-1
			Case 1
				result = shag_razut(trut.cols("Num").Z(pos_shaga), 20, trut.cols("dPgen").Z(pos_shaga))
				If result<>0 then
					rastr.printp "Режим не сходится!!! Пропускаем этот генератор"
					trut.cols("rashojdenie").Z(pos_shaga) = 1
				End If
				trut.cols("Uchastie").Z(pos_shaga) = 0
				shag = shag-1
			Case 2
				result = shag_razut(trut.cols("Num").Z(pos_shaga), 21, trut.cols("dPgen").Z(pos_shaga))
				If result<>0 then
					rastr.printp "Режим не сходится!!! Пропускаем этот генератор"
					trut.cols("rashojdenie").Z(pos_shaga) = 1
				End If
				trut.cols("Uchastie").Z(pos_shaga) = 0
				shag = shag-1
			Case 3
				result = shag_razut(trut.cols("Num").Z(pos_shaga), 11, trut.cols("dPgen").Z(pos_shaga))
				If result<>0 then
					rastr.printp "Режим не сходится!!! Пропускаем этот генератор"
					trut.cols("rashojdenie").Z(pos_shaga) = 1
				End If
			   trut.cols("Uchastie").Z(pos_shaga) = 0
			   shag = shag-1
		End Select
	Loop
	 ' как только перескочили через Iзад смотрим dI = Iзад-I и если |dI|>0.5 А то откатываемся на один шаг назад, проверяем dI еще раз, и если |dI|>1 А снова,
	 ' то откатившийся шаг выполняем постепенно до |dI|< = 1 методом половинного деления
	dI = Izad-Flow_I(vetv_pos)
	If dI < (-0.5) then
	shag = shag+1
    trut.Setsel("n_shaga = " & shag)   'выборка пройденных шагов утяжеления
    pos_shaga = trut.findnextsel(-1)
    trut.cols("Uchastie").Z(pos_shaga) = true
	If trut.cols("kod_ut").Z(pos_shaga) = 1 then kod_d = 10
	If trut.cols("kod_ut").Z(pos_shaga) = 2 then kod_d = 11
	If trut.cols("kod_ut").Z(pos_shaga) = 3 then kod_d = 21
	result = shag_ut(trut.cols("Num").Z(pos_shaga), kod_d, 0)
	If result<>0 then msgbox "Режим не сошелся при откате на один шаг при поиске заданного перетока мощности по элементу!"
		dI = Izad-Flow_I(vetv_pos)
		If dI > 0.5 then
			kod_utyagelenia = trut.cols("kod_ut").Z(pos_shaga)
			tGen.SetSel("Num = " & trut.cols("Num").Z(pos_shaga))
			gen_pos = tGen.FindNextSel(-1)
			Select Case kod_utyagelenia
				Case 1
					msgbox "алгоритм 1"
					P_gen0 = tGen.Cols("Pmax").Z(gen_pos)-trut.cols("dPgen").Z(pos_shaga)
					P_gen1 = tGen.Cols("Pmax").Z(gen_pos)
					dI = Izad-Flow_I(vetv_pos)
					Do While (dI>0.5 or Abs(P_gen1-P_gen0)>1)
						If dI < 0 then
							P_gen1 = (P_gen1+P_gen0)/2
							tGen.Cols("P").Z(gen_pos) = P_gen1
							rastr.rgm "p"
							dI = Izad-Flow_I(vetv_pos)
						End If
						If dI>0 then
							P_gen0 = (P_gen1+P_gen0)/2
							tGen.Cols("P").Z(gen_pos) = P_gen0
							rastr.rgm "p"
							dI = Izad-Flow_I(vetv_pos)
						End If
					Loop
				Case 2
					msgbox "алгоритм 2"
					tGen.Cols("P").Z(gen_pos) = tGen.Cols("Pmin").Z(gen_pos)
					rastr.rgm "p"
					dI = Izad-Flow_I(vetv_pos)
					If dI < 0 then
						P_gen0 = tGen.Cols("Pmin").Z(gen_pos)
						P_gen1 = tGen.Cols("Pmax").Z(gen_pos)
						Do While (dI>0.5 or Abs(P_gen1-P_gen0)>1)
							If dI<0 then
								P_gen1 = (P_gen1+P_gen0)/2
								tGen.Cols("P").Z(gen_pos) = P_gen1
								rastr.rgm "p"
								dI = Izad-Flow_I(vetv_pos)
							End If
							If dI>0 then
								P_gen0 = (P_gen1+P_gen0)/2
								tGen.Cols("P").Z(gen_pos) = P_gen0
								rastr.rgm "p"
								dI = Izad-Flow_I(vetv_pos)
							End If
						Loop
					End If
				Case 3
					msgbox "алгоритм 3"
					tGen.Cols("P").Z(gen_pos) = tGen.Cols("Pmin").Z(gen_pos)
					tGen.Cols("sta").Z(gen_pos) = 0
					If tGen.Cols("NodeState").Z(gen_pos)<>0 then HitGen tGen.Cols("Node").Z(gen_pos)
					rastr.rgm "p"
					dI = Izad-Flow_I(vetv_pos)
					If dI<0 then
						P_gen0 = tGen.Cols("Pmin").Z(gen_pos)
						P_gen1 = trut.cols("dPgen").Z(pos_shaga)
						Do While (dI>0.5 or Abs(P_gen1-P_gen0)>1)
							If dI<0 then
								P_gen1 = (P_gen1+P_gen0)/2
								tGen.Cols("P").Z(gen_pos) = P_gen1
								rastr.rgm "p"
								dI = Izad-Flow_I(vetv_pos)
							End If
							If dI>0 then
								P_gen0 = (P_gen1+P_gen0)/2
								tGen.Cols("P").Z(gen_pos) = P_gen0
								rastr.rgm "p"
								dI = Izad-Flow_I(vetv_pos)
							End If
						Loop
					End If
			End Select
		End If
	End If
End Sub

'////////////////////////////////////////////////////////////////////////////////////////////////
'Поиск предельного по току режима
'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
Sub Poisk_I1(branch,Izad)
	Set tvetv = Rastr.Tables("vetv")
	tvetv.Setsel(branch)
	vetv_pos = tvetv.FindNextSel(-1)
	Set trut = Rastr.Tables("Traektory_ut")
	Set tGen = Rastr.Tables("Generator")
	Rastr.printp "Текущий ток по элементу " & Flow_I(vetv_pos)
	ut_End = 0
	Do While (Flow_I(vetv_pos) > Izad And ut_End <> 2)
		rastr.printp "Ток I = " & Flow_I(vetv_pos)
		Pbal = Balance_P()
		If ut_End = 1 then
			flag = 2
		else
			If Pbal <= (-1) then flag = 1
			If Pbal >= 1 then flag = 0
		End If

		Select Case flag
			Case 0
				trut.SetSel("Uchastie = 1&rashojdenie = 0&kod_ut = 3")
				ut_pos = trut.FindNextSel(-1)
				If ut_pos = (-1) then
					ut_End = 1
				else
					result = shag_razut(trut.cols("Num").Z(ut_pos), 11, trut.cols("dPgen").Z(ut_pos))
					If result<>0 then
						rastr.printp "Режим не сходится!!! Пропускаем этот генератор"
						trut.cols("rashojdenie").Z(ut_pos) = true
					End If
					trut.cols("Uchastie").Z(ut_pos) = false
				End If
			Case 1
				trut.SetSel("Uchastie = 1&rashojdenie = 0&kod_ut<3")
				ut_pos = trut.FindNextSel(-1)
				If ut_pos = -1 then
					ut_End = 1
				else
					If trut.cols("kod_ut").Z(ut_pos) = 1 then kod_d = 20
					If trut.cols("kod_ut").Z(ut_pos) = 2 then kod_d = 21
					result = shag_razut(trut.cols("Num").Z(ut_pos), kod_d, trut.cols("dPgen").Z(ut_pos))
					If result<>0 then
						rastr.printp "Режим не сходится!!! Пропускаем этот генератор"
						trut.cols("rashojdenie").Z(ut_pos) = true
					End If
					trut.cols("Uchastie").Z(ut_pos) = false
				End If

			Case 2      'когда кончились генераторы одного направления утяжеления
				trut.SetSel("Uchastie = 1&rashojdenie = 0")
				ut_pos = trut.FindNextSel(-1)
				If ut_pos<>-1 then
					If trut.cols("kod_ut").Z(ut_pos) = 1 then kod_d = 20
					If trut.cols("kod_ut").Z(ut_pos) = 2 then kod_d = 21
					If trut.cols("kod_ut").Z(ut_pos) = 3 then kod_d = 11
					result = shag_razut(trut.cols("Num").Z(ut_pos), kod_d, trut.cols("dPgen").Z(ut_pos))
					If result<>0 then
						rastr.printp "Режим не сходится при несбалансированном разутяжелении"
						trut.cols("rashojdenie").Z(ut_pos) = true
					End If
					trut.cols("Uchastie").Z(ut_pos) = false
				else
					ut_End = 2
					Msgbox "Возврат к режиму до утяжеления по активной мощности",48,"Внимание..."
				End If

		End Select
	Loop
	' как только перескочили через Iзад смотрим dI = Iзад-I и если |dI|>0.5 А то откатываемся на один шаг назад, проверяем dI еще раз, и если |dI|>1 А снова,
	' то откатившийся шаг выполняем постепенно до |dI|< = 1 методом половинного деления
	dI = Izad-Flow_I(vetv_pos)
	If dI > 0.5 then
		rastr.printp "обратно утяжеляем генератором №" & trut.cols("Num").Z(ut_pos)
		If trut.cols("kod_ut").Z(ut_pos) = 1 then kod_d = 10
		If trut.cols("kod_ut").Z(ut_pos) = 2 then kod_d = 11
		If trut.cols("kod_ut").Z(ut_pos) = 3 then kod_d = 21
		result = shag_ut(trut.cols("Num").Z(ut_pos), kod_d, 0)
		trut.cols("Uchastie").Z(ut_pos) = true
		If result<>0 then msgbox "Режим не сошелся при откате на один шаг при поиске заданного перетока мощности по элементу!"
		dI = Izad-Flow_I(vetv_pos)
		If dI<-0.5 then
			kod_utyagelenia = trut.cols("kod_ut").Z(ut_pos)
			tGen.SetSel("Num = " & trut.cols("Num").Z(ut_pos))
			gen_pos = tGen.FindNextSel(-1)
			Select Case kod_utyagelenia
				Case 1
					rastr.Printp "алгоритм 1"
					P_gen0 = tGen.Cols("Pmax").Z(gen_pos)-trut.cols("dPgen").Z(ut_pos)
					P_gen1 = tGen.Cols("Pmax").Z(gen_pos)
					dI = Izad-Flow_I(vetv_pos)
					Do While (abs(dI)>0.5 and (P_gen1-P_gen0)>10)
						tGen.Cols("P").Z(gen_pos) = (P_gen1+P_gen0)/2
						rastr.rgm "p"
						dI = Izad-Flow_I(vetv_pos)
						If dI<0 then
							P_gen1 = (P_gen1+P_gen0)/2
						else
							P_gen0 = (P_gen1+P_gen0)/2
						End If
					Loop
				Case 2
					rastr.printp "алгоритм 2"
					tGen.Cols("P").Z(gen_pos) = tGen.Cols("Pmin").Z(gen_pos)
					rastr.rgm "p"
					dI = Izad-Flow_I(vetv_pos)
					If dI>1 then
						P_gen0 = tGen.Cols("Pmin").Z(gen_pos)
						P_gen1 = tGen.Cols("Pmax").Z(gen_pos)
						Do While (abs(dI)>0.5 and (P_gen1-P_gen0)>10)
							tGen.Cols("P").Z(gen_pos) = (P_gen1+P_gen0)/2
							rastr.rgm "p"
							dI = Izad-Flow_I(vetv_pos)
							If dI<0 then
								P_gen1 = (P_gen1+P_gen0)/2
							else
								P_gen0 = (P_gen1+P_gen0)/2
							End If
						Loop
					else
						msgbox "Дальше разгружать вручную"
					End If
				Case 3
					rastr.printp "алгоритм 3"
					tGen.Cols("P").Z(gen_pos) = tGen.Cols("Pmin").Z(gen_pos)
					tGen.Cols("sta").Z(gen_pos) = 0
					If tGen.Cols("NodeState").Z(gen_pos)<>0 then HitGen tGen.Cols("Node").Z(gen_pos)
					rastr.rgm "p"
					dI = Izad-Flow_I(vetv_pos)
					If dI <= 0.5 then
						P_gen0 = tGen.Cols("Pmin").Z(gen_pos)
						P_gen1 = trut.cols("dPgen").Z(ut_pos)
						Do While (abs(dI)>0.5 and (P_gen1-P_gen0)>10)
							tGen.Cols("P").Z(gen_pos) = (P_gen1+P_gen0)/2
							rastr.rgm "p"
							dI = Izad-Flow_I(vetv_pos)
							If dI<0 then
								P_gen1 = (P_gen1+P_gen0)/2
							else
								P_gen0 = (P_gen1+P_gen0)/2
							End If
						Loop
					End If
			End Select
		End If
	End If
End Sub

'////////////////////////////////////////////////////////////////////////////////////////////////
'Поиск заданного P по элементу
'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
Sub Poisk_P1(branch,Pzad,K_reverse,control_P)
	Set tvetv = Rastr.Tables("vetv")
	tvetv.Setsel(branch)
	vetv_pos = tvetv.FindNextSel(-1)
	Set trut = Rastr.Tables("Traektory_ut")
	Set tGen = Rastr.Tables("Generator")
	ut_End = 0
	'msgbox Flow_P(vetv_pos,control_P)*K_reverse
	Do While (Flow_P(vetv_pos,control_P)*K_reverse>Pzad)
		rastr.printp "P = " & Flow_P(vetv_pos,control_P)*k_reverse
		Pbal = Balance_P()
		If ut_End = 1 then
			flag = 2
		else
			If Pbal <= -100 then flag = 1
			If Pbal >= 100 then flag = 0
		End If
		Select Case flag
			Case 0
				trut.SetSel("Uchastie = 1&rashojdenie = 0&kod_ut = 3")
				ut_pos = trut.FindNextSel(-1)
				If ut_pos = -1 then
					ut_End = 1
				else
					result = shag_razut(trut.cols("Num").Z(ut_pos), 11, trut.cols("dPgen").Z(ut_pos))
					If result<>0 then
						rastr.printp "Режим не сходится!!! Пропускаем этот генератор"
						trut.cols("rashojdenie").Z(ut_pos) = true
					End If
					trut.cols("Uchastie").Z(ut_pos) = false
				End If
			Case 1
				trut.SetSel("Uchastie = 1&rashojdenie = 0&kod_ut<3")
				ut_pos = trut.FindNextSel(-1)
				If ut_pos = -1 then
					ut_End = 1
				else
					If trut.cols("kod_ut").Z(ut_pos) = 1 then kod_d = 20
					If trut.cols("kod_ut").Z(ut_pos) = 2 then kod_d = 21
					result = shag_razut(trut.cols("Num").Z(ut_pos), kod_d, trut.cols("dPgen").Z(ut_pos))
					If result<>0 then
						rastr.printp "Режим не сходится!!! Пропускаем этот генератор"
						trut.cols("rashojdenie").Z(ut_pos) = true
					End If
					trut.cols("Uchastie").Z(ut_pos) = false
				End If

			Case 2       'когда кончились генераторы одного направления утяжеления
				trut.SetSel("Uchastie = 1&rashojdenie = 0")
				ut_pos = trut.FindNextSel(-1)
				If trut.cols("kod_ut").Z(ut_pos) = 1 then kod_d = 20
				If trut.cols("kod_ut").Z(ut_pos) = 2 then kod_d = 21
				If trut.cols("kod_ut").Z(ut_pos) = 3 then kod_d = 11
				result = shag_razut(trut.cols("Num").Z(ut_pos), kod_d, trut.cols("dPgen").Z(ut_pos))
				If result<>0 then
					rastr.printp "Режим не сходится при несбалансированном разутяжелении"
					trut.cols("rashojdenie").Z(ut_pos) = true
				End If
				trut.cols("Uchastie").Z(ut_pos) = false
		End Select
	Loop
	' как только перескочили через Pзад смотрим dP = Pзад-P и если |dP|>1 МВт то откатываемся на один шаг назад, проверяем dP еще раз, и если |dP|>1 МВт снова,
	' то откатившийся шаг выполняем постепенно до |dP|< = 1 методом половинного деления
	dP = Pzad-Flow_P(vetv_pos,control_P)*k_reverse
	If dP>1 then
		rastr.printp "обратно утяжеляем генератором №" & trut.cols("Num").Z(ut_pos)
		If trut.cols("kod_ut").Z(ut_pos) = 1 then kod_d = 10
		If trut.cols("kod_ut").Z(ut_pos) = 2 then kod_d = 11
		If trut.cols("kod_ut").Z(ut_pos) = 3 then kod_d = 21
		result = shag_ut(trut.cols("Num").Z(ut_pos), kod_d, 0)
		trut.cols("Uchastie").Z(ut_pos) = true
		If result<>0 then msgbox "Режим не сошелся при откате на один шаг при поиске заданного перетока мощности по элементу!"
		dP = Pzad-Flow_P(vetv_pos,control_P)*k_reverse
		If abs(dP)>1 then
			kod_utyagelenia = trut.cols("kod_ut").Z(ut_pos)
			tGen.SetSel("Num = " & trut.cols("Num").Z(ut_pos))
			gen_pos = tGen.FindNextSel(-1)
			Select Case kod_utyagelenia
				Case 1
					rastr.Printp "алгоритм 1"
					P_gen0 = tGen.Cols("Pmax").Z(gen_pos)-trut.cols("dPgen").Z(ut_pos)
					P_gen1 = tGen.Cols("Pmax").Z(gen_pos)
					dP = Pzad-Flow_P(vetv_pos,control_P)*k_reverse
					Do While (abs(dP)>1 and (P_gen1-P_gen0)>10)
						tGen.Cols("P").Z(gen_pos) = (P_gen1+P_gen0)/2
						rastr.rgm "p"
						dP = Pzad-Flow_P(vetv_pos,control_P)*k_reverse
						If dP < 0 then
							P_gen1 = (P_gen1+P_gen0)/2
						else
							P_gen0 = (P_gen1+P_gen0)/2
						End If
					Loop

				Case 2
					rastr.printp "алгоритм 2"
					tGen.Cols("P").Z(gen_pos) = tGen.Cols("Pmin").Z(gen_pos)
					rastr.rgm "p"
					dP = Pzad-Flow_P(vetv_pos,control_P)*k_reverse
					If dP >= (-1) then
						P_gen0 = tGen.Cols("Pmin").Z(gen_pos)
						P_gen1 = tGen.Cols("Pmax").Z(gen_pos)
						Do While (abs(dP)>1 and (P_gen1-P_gen0)>10)
							tGen.Cols("P").Z(gen_pos) = (P_gen1+P_gen0)/2
							rastr.rgm "p"
							dP = Pzad-Flow_P(vetv_pos,control_P)*k_reverse
							If dP<0 then
								P_gen1 = (P_gen1+P_gen0)/2
							else
								P_gen0 = (P_gen1+P_gen0)/2
							End If
						Loop
					else
						'здесь добавить алгоритм для случая когда при  включении генератора на минимум до достижения Pzad>1
						msgbox "Дальше доразгрузиться вручную"
					End If

				Case 3
					rastr.printp "алгоритм 3"
					tGen.Cols("P").Z(gen_pos) = tGen.Cols("Pmin").Z(gen_pos)
					tGen.Cols("sta").Z(gen_pos) = 0
					If tGen.Cols("NodeState").Z(gen_pos)<>0 then HitGen tGen.Cols("Node").Z(gen_pos)
					rastr.rgm "p"
					dP = Pzad-Flow_P(vetv_pos,control_P)*k_reverse
					If dP >= (-1) then
						P_gen0 = tGen.Cols("Pmin").Z(gen_pos)
						P_gen1 = trut.cols("dPgen").Z(ut_pos)
						Do While (abs(dP)>0.5 and (P_gen1-P_gen0)>10)
							tGen.Cols("P").Z(gen_pos) = (P_gen1+P_gen0)/2
							rastr.rgm "p"
							dP = Pzad-Flow_P(vetv_pos,control_P)*k_reverse
							If dP<0 then
								P_gen1 = (P_gen1+P_gen0)/2
							else
								P_gen0 = (P_gen1+P_gen0)/2
							End If
						Loop
					End If
			End Select
		End If
	End If
End Sub

Sub Shkura()
	htmlDialog = "" + vbCrLf+_
	"<html>"+vbCrLf+_
		"<head>"+vbCrLf+_
			"<title>Расчет нагрузочных режимов</title>"+vbCrLf+_
			"<style> INPUT[type = ""text""] {background-color:  #D3D3CA;}"+vbCrLf+_
				"TABLE {width: 100%; border-collapse: collapse; border-radius: 5px;}"+vbCrLf+_
			"</style>"+vbCrLf+_
			""+vbCrLf+_
			"<script type = ""text/javascript"">"+vbCrLf+_
					"var wbp = 0;"+vbCrLf+_
					"document.getElementById(""my"").value = wbp;"+vbCrLf+_
				"Function onBtnOk(){"+vbCrLf+_
					"var wbp = 1;"+vbCrLf+_
					"document.getElementById(""my"").value = wbp;"+vbCrLf+_
				"}"+vbCrLf+_
				"Function onBtnCancel(){"+vbCrLf+_
					"var wbp = 2;"+vbCrLf+_
					"document.getElementById(""my"").value = wbp;"+vbCrLf+_
				"}"+vbCrLf+_
				"Function onBtnLoad(){"+vbCrLf+_
					"var wbp = 3;"+vbCrLf+_
					"document.getElementById(""my"").value = wbp;"+vbCrLf+_
				"}"+vbCrLf+_
				"Function onBtnSave(){"+vbCrLf+_
					"var wbp = 4;"+vbCrLf+_
					"document.getElementById(""my"").value = wbp;"+vbCrLf+_
				"}"+vbCrLf+_
				"Function tiput(ut){"+vbCrLf+_
					"If (document.getElementsByName(""ut"")(1).checked =  = true)"+vbCrLf+_
						"{"+vbCrLf+_
							"document.getElementById(""KVES_ID"").disabled = true;"+vbCrLf+_
							"document.getElementById(""PPRED_ID"").disabled = true;"+vbCrLf+_
							"document.getElementById(""P092_ID"").disabled = true;"+vbCrLf+_
							"document.getElementById(""P08_ID"").disabled = true;"+vbCrLf+_
							"document.getElementById(""PIZAD_ID"").disabled = true;"+vbCrLf+_
							"document.getElementById(""CONTR_PIP"").disabled = true;"+vbCrLf+_
							"document.getElementById(""CONTR_PIQ"").disabled = true;"+vbCrLf+_
							"document.getElementById(""UTQMIN_ID"").disabled = true;"+vbCrLf+_
							"document.getElementById(""KVESMIN_ID"").disabled = true;"+vbCrLf+_
							"document.getElementById(""PMIN_ID"").disabled = true;"+vbCrLf+_
							"document.getElementById(""KVESQ_ID"").disabled = false;"+vbCrLf+_
							"document.getElementById(""UTONLYQ_ID"").disabled = false;"+vbCrLf+_
						"}"+vbCrLf+_
					"If (document.getElementsByName(""ut"")(0).checked =  = true)"+vbCrLf+_
						"{"+vbCrLf+_
							"document.getElementById(""KVES_ID"").disabled = false;"+vbCrLf+_
							"document.getElementById(""PPRED_ID"").disabled = false;"+vbCrLf+_
							"document.getElementById(""P092_ID"").disabled = false;"+vbCrLf+_
							"document.getElementById(""P08_ID"").disabled = false;"+vbCrLf+_
							"document.getElementById(""PIZAD_ID"").disabled = false;"+vbCrLf+_
							"document.getElementById(""CONTR_PIP"").disabled = false;"+vbCrLf+_
							"document.getElementById(""CONTR_PIQ"").disabled = false;"+vbCrLf+_
							"document.getElementById(""UTQMIN_ID"").disabled = true;"+vbCrLf+_
							"document.getElementById(""KVESMIN_ID"").disabled = true;"+vbCrLf+_
							"document.getElementById(""PMIN_ID"").disabled = true;"+vbCrLf+_
							"document.getElementById(""KVESQ_ID"").disabled = true;"+vbCrLf+_
							"document.getElementById(""UTONLYQ_ID"").disabled = true;"+vbCrLf+_
						"}"+vbCrLf+_
					"If (document.getElementsByName(""ut"")(2).checked =  = true)"+vbCrLf+_
						"{"+vbCrLf+_
							"document.getElementById(""KVES_ID"").disabled = true;"+vbCrLf+_
							"document.getElementById(""PPRED_ID"").disabled = true;"+vbCrLf+_
							"document.getElementById(""P092_ID"").disabled = true;"+vbCrLf+_
							"document.getElementById(""P08_ID"").disabled = true;"+vbCrLf+_
							"document.getElementById(""PIZAD_ID"").disabled = true;"+vbCrLf+_
							"document.getElementById(""CONTR_PIP"").disabled = true;"+vbCrLf+_
							"document.getElementById(""CONTR_PIQ"").disabled = true;"+vbCrLf+_
							"document.getElementById(""UTQMIN_ID"").disabled = false;"+vbCrLf+_
							"document.getElementById(""KVESMIN_ID"").disabled = false;"+vbCrLf+_
							"document.getElementById(""PMIN_ID"").disabled = false;"+vbCrLf+_
							"document.getElementById(""KVESQ_ID"").disabled = true;"+vbCrLf+_
							"document.getElementById(""UTONLYQ_ID"").disabled = true;"+vbCrLf+_
						"}"+vbCrLf+_
				"}"+vbCrLf+_
			"</script>"+vbCrLf+_
		"</head>"+vbCrLf+_
		"<body BGCOLOR = ""#с6c3c0"">"+vbCrLf+_
			"<P ALIGN = ""left""><b>Программа для расчета нагрузочных режимов (v2.6)</b><BR>"+vbCrLf+_
			"<ForM name = ""MyForm"" action = """" method = ""post""  onsubmit = ""return false;"">"+vbCrLf+_
				"<LABEL STYLE = ""text-align: Center"">Общие данные:</LABEL><BR>"+vbCrLf+_
				"<input name = ""ButtonPressed"" type = ""hidden"" id = ""my"">"+vbCrLf+_
				"<LABEL>&nbsp&nbspip = &nbsp&nbsp</LABEL>"+vbCrLf+_
				"<INPUT TYPE = ""text"" id = ""IP_ID"" NAME = ""IP"" STYLE = ""text-align: Left; font-weight:bold"" VALUE = ""0"" SIZE = ""8""><BR>"+vbCrLf+_
				"<LABEL>&nbsp&nbspiq = &nbsp&nbsp</LABEL>"+vbCrLf+_
				"<INPUT TYPE = ""text"" id = ""IQ_ID"" NAME = ""IQ"" STYLE = ""text-align: Left; font-weight:bold"" VALUE = ""0"" SIZE = ""8""><BR>"+vbCrLf+_
				"<LABEL>&nbsp&nbspnp = &nbsp</LABEL>"+vbCrLf+_
				"<INPUT TYPE = ""text"" id = ""NP_ID"" NAME = ""NP"" STYLE = ""text-align: Left; font-weight:bold"" VALUE = ""0"" SIZE = ""1""><BR>"+vbCrLf+_
				"<LABEL>Iзад = </LABEL>"+vbCrLf+_
				"<INPUT TYPE = ""text"" id = ""Izad_ID"" NAME = ""Izad"" STYLE = ""text-align: Left; font-weight:bold"" VALUE = ""0"" SIZE = ""4""><BR>"+vbCrLf+_
				"<LABEL STYLE = ""text-align: Left"">Направление утяжеления:</LABEL>"+vbCrLf+_
				"<BR>"+vbCrLf+_
				"<LABEL>ip&#10144iq</LABEL>"+vbCrLf+_
				"<INPUT TYPE = ""radio"" id = ""DIR_ID1"" NAME = ""ddd"" VALUE = ""-1"" CHECKED>"+vbCrLf+_
				"<LABEL>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp iq&#10144ip</LABEL>"+vbCrLf+_
				"<INPUT TYPE = ""radio"" id = ""DIR_ID2"" NAME = ""ddd"" VALUE = ""1"">"+vbCrLf+_
				"<BR>"+vbCrLf+_
				"<LABEL>Зона нечувств. АТ</LABEL>"+vbCrLf+_
				"<INPUT TYPE = ""text"" id = ""ZNCH_ID"" NAME = ""ZNCH"" STYLE = ""text-align: Left"" VALUE = ""0,2"" SIZE = ""3""><BR>"+vbCrLf+_
				"<HR>"+vbCrLf+_
				"<INPUT TYPE = ""radio"" id = ""UTPQ_ID"" NAME = ""ut"" onClick = ""tiput(this);"" VALUE = ""1"" CHECKED>"+vbCrLf+_
				"<LABEL STYLE = ""text-align: Left; font-weight:bold"">Комплексное утяжеление(P,Q)</LABEL>"+vbCrLf+_
				"<BR>"+vbCrLf+_
				"<LABEL STYLE = ""text-align: Left"">Настройки утяжеления:</LABEL>"+vbCrLf+_
				"<BR>"+vbCrLf+_
				"<TABLE>"+vbCrLf+_
				"<TR><TD colspan = ""3"">"+vbCrLf+_
					"<INPUT TYPE = ""CHECKBOX"" id = ""KVES_ID"" NAME = ""KVES"" CHECKED>&nbsp Расчет Kвес.<BR>"+vbCrLf+_
					"<INPUT TYPE = ""CHECKBOX"" id = ""PPRED_ID"" NAME = ""PPRED"" CHECKED>&nbsp Расчет Pпред.<BR>"+vbCrLf+_
				"</TD></TR></TABLE>"+vbCrLf+_
					"<TABLE BGCOLOR = ""#a1c6c0""><TR><TD colspan = ""3"">"+vbCrLf+_
					"<INPUT TYPE = ""CHECKBOX"" id = ""P092_ID"" NAME = ""P092"" CHECKED>&nbsp Расчет 0,92Pпред.<BR>"+vbCrLf+_
					"<INPUT TYPE = ""CHECKBOX"" id = ""P08_ID"" NAME = ""P08"" CHECKED>&nbsp Расчет 0,8Pпред.<BR>"+vbCrLf+_
				"</TD></TR>"+vbCrLf+_
				"<TR><TD>Контроль P в узле:</TD>"+vbCrLf+_
					"<TD>ip"+vbCrLf+_
					"<INPUT TYPE = ""radio"" id = ""CONTR_PIP"" NAME = ""controlP"" VALUE = ""ip"" CHECKED></TD>"+vbCrLf+_
					"<TD>&nbsp iq"+vbCrLf+_
					"<INPUT TYPE = ""radio"" id = ""CONTR_PIQ"" NAME = ""controlP"" VALUE = ""iq""></TD>"+vbCrLf+_
				"</TR>"+vbCrLf+_
				"</TABLE>"+vbCrLf+_
				"<INPUT TYPE = ""CHECKBOX"" id = ""PIZAD_ID"" NAME = ""PIZAD"" CHECKED>&nbsp Расчет P(Iзад.)<BR>"+vbCrLf+_
				"<HR>"+vbCrLf+_
				"<INPUT TYPE = ""radio"" id = ""UTQ_ID"" NAME = ""ut"" onClick = ""tiput(this);"" VALUE = ""2"">"+vbCrLf+_
				"<LABEL STYLE = ""text-align: Left; font-weight:bold"">Утяжеление по Q</LABEL>"+vbCrLf+_
				"<BR>"+vbCrLf+_
				"<LABEL STYLE = ""text-align: Left"">Настройки расчета:</LABEL>"+vbCrLf+_
				"<BR>"+vbCrLf+_
				"<LABEL><INPUT TYPE = ""CHECKBOX"" id = ""KVESQ_ID"" NAME = ""KVESQ"" CHECKED DISABLED>&nbsp Расчет Kвес по Q</LABEL><BR>"+vbCrLf+_
				"<LABEL><INPUT TYPE = ""CHECKBOX"" id = ""UTONLYQ_ID"" NAME = ""UTONLYQ"" CHECKED DISABLED>&nbsp Утяжелить по Q</LABEL><BR>"+vbCrLf+_
				"<HR>"+vbCrLf+_
				"<INPUT TYPE = ""radio"" id = ""UTPMIN_ID"" NAME = ""ut"" onClick = ""tiput(this);"" VALUE = ""3"">"+vbCrLf+_
				"<LABEL STYLE = ""text-align: Left; font-weight:bold"">Минимальный по P</LABEL>"+vbCrLf+_
				"<BR>"+vbCrLf+_
				"<LABEL STYLE = ""text-align: Left"">Настройки расчета:</LABEL>"+vbCrLf+_
				"<BR>"+vbCrLf+_
				"<LABEL><INPUT TYPE = ""CHECKBOX"" id = ""UTQMIN_ID"" NAME = ""UTQMIN"" CHECKED DISABLED>&nbsp Утяжеление по Q</LABEL><BR>"+vbCrLf+_
				"<LABEL><INPUT TYPE = ""CHECKBOX"" id = ""KVESMIN_ID"" NAME = ""KVESMIN"" CHECKED DISABLED>&nbsp Расчет Kвес по P</LABEL><BR>"+vbCrLf+_
				"<LABEL><INPUT TYPE = ""CHECKBOX"" id = ""PMIN_ID"" NAME = ""PMIN"" CHECKED DISABLED>&nbsp Расчет Pmin</LABEL><BR>"+vbCrLf+_
				"<HR>"+vbCrLf+_
				"<LABEL STYLE = ""text-align: Center"">Действия с данными:</LABEL><BR>"+vbCrLf+_
				"<button id = ""butt_load_ID"" NAME = ""butt_load"" onClick = ""onBtnLoad()"">Загрузить</button><LABEL>&nbsp</LABEL>"+vbCrLf+_
				"<button id = ""butt_save_ID"" NAME = ""butt_save"" onClick = ""onBtnSave()"">Сохранить</button>"+vbCrLf+_
				"<br>"+vbCrLf+_
				"<LABEL><INPUT TYPE = ""CHECKBOX"" id = ""SAVE_ID"" NAME = ""SAVE_RESULT"" CHECKED>&nbsp Сохранять результаты</LABEL><BR>"+vbCrLf+_
				"<HR>"+vbCrLf+_
				"<P ALIGN = ""left"">"+vbCrLf+_
					"<button id = ""butt_start_ID"" NAME = ""butt_start"" onClick = ""onBtnOk()"">НАЧАТЬ</button><LABEL>&nbsp&nbsp&nbsp&nbsp</LABEL>"+vbCrLf+_
					"<button id = ""butt_exit_ID"" NAME = ""butt_exit"" onClick = ""onBtnCancel()"">ВЫЙТИ</button>"+vbCrLf+_
				"</P>"+vbCrLf+_
				"<P ALIGN = ""center"">"+vbCrLf+_
					"<LABEL ID = ""ISX""></LABEL>"+vbCrLf+_
				"</P>"+vbCrLf+_
			"</ForM>"+vbCrLf+_
		"</body>"+vbCrLf+_
	"</html>"

	Set obj_IE = CreateObjectEx("InternetExplorer.Application","g_IE_")

	obj_IE.TheaterMode = FALSE
	obj_IE.Left      = 250   'коррдината верхнего левого угла окна IEx
	obj_IE.Top       = 0   'координата верха окна IE
	obj_IE.Height    = 970   'высота окна IE
	obj_IE.Width     = 310 'ширина окна IE
	obj_IE.MenuBar   = FALSE 'без меню IE
	obj_IE.ToolBar   = FALSE 'без тулбара IE
	obj_IE.StatusBar = FALSE 'без строки состояния IE
	obj_IE.Resizable = FALSE
	obj_IE.Navigate  "about:blank"

	'выжидаем пока IE не освободится
	DO While ( obj_IE.Busy )
		SLEEP 100
	LOOP
	obj_IE.Document.Write (htmlDialog)
	obj_IE.Visible = True
	g_Quit = FALSE

	For k = 1 TO 2 STEP 0        ' ожидание нажатия кноки на форме Internet Explorer
		If g_Quit =  TRUE  THEN
			EXIT For
		End If

		If(obj_IE.document.MyForm.ButtonPressed.Value  = "2") THEN 'Если нажата кнопка ВЫЙТИ, то закрывается форма
			g_Quit =  TRUE
			EXIT For
		End If

		If(obj_IE.document.MyForm.ButtonPressed.Value  = "1") THEN 'Если нажата кнопка НАЧАТЬ, то считываются заданые установки и запускается расчет
			ip = obj_IE.document.MyForm.IP.value     'номер узла начала ветви
			iq = obj_IE.document.MyForm.IQ.value     'номер узла конца ветви
			np = obj_IE.document.MyForm.NP.value     'номер параллельности ветви
			Izad = cInt(obj_IE.document.MyForm.Izad.value) 'аварийно допустимый ток контролируемой ветви

			Setlocale("ru-RU")
			on error resume next
			znch = cDbl(obj_IE.document.MyForm.ZNCH.value) 'зона нечуствительности для АТ при утяжелении по Q (Мвар на анцапфу)
			If err.number = 13 then
				msgbox err.Description
				exit sub
			End If

			 'определяем направление утяжеления
			For i = 0 to obj_IE.document.getElementsByName("ddd").length-1
				If obj_IE.document.getElementsByName("ddd")(i).checked then
					directP = cInt(obj_IE.document.getElementsByName("ddd")(i).value)
				End If
			next

			'определяем место контроля P при разутяжелении
			For i = 0 to obj_IE.document.getElementsByName("controlP").length - 1
				If obj_IE.document.getElementsByName("controlP")(i).checked then
					control_P = obj_IE.document.getElementsByName("controlP")(i).value
				End If
			next

			'определяем выбранный блок для расчета
			For i = 0 to obj_IE.document.getElementsByName("ut").length - 1
				If obj_IE.document.getElementsByName("ut")(i).checked then
					Block_R = obj_IE.document.getElementsByName("ut")(i).value
				End If
			next

			'Расчетный блок №1
			If obj_IE.document.getElementById("KVES_ID").checked then
				Raschet_k_ves = true
			else
				Raschet_k_ves = false
			End If

			If obj_IE.document.getElementById("PPRED_ID").checked then
				Raschet_P_pred = true
			else
				Raschet_P_pred = false
			End If

			If obj_IE.document.getElementById("P092_ID").checked then
				Raschet_P092 = true
			else
				Raschet_P092 = false
			End If

			If obj_IE.document.getElementById("P08_ID").checked then
				Raschet_P08 = true
			else
				Raschet_P08 = false
			End If

			If obj_IE.document.getElementById("PIZAD_ID").checked then
				Raschet_I = true
			else
				Raschet_I = false
			End If

			'Расчетный блок №2
			'проведение расчета весовых коэффициентов по Q при утяжелении по Q
			If obj_IE.document.getElementById("KVESQ_ID").checked then
				Raschet_KVESQ = true
			else
				Raschet_KVESQ = false
			End If

			'проведение расчета весовых коэффициентов по Q при утяжелении по Q
			If obj_IE.document.getElementById("UTONLYQ_ID").checked then
				Raschet_UTONLYQ = true
			else
				Raschet_UTONLYQ = false
			End If

			'Расчетный блок №3
			'проведение утяжеления по Q при расчете минимального режима
			If obj_IE.document.getElementById("UTQMIN_ID").checked then
				Raschet_QMIN = true
			else
				Raschet_QMIN = false
			End If

			'расчет весовых коэффициентов по P при расчете минимального режима
			If obj_IE.document.getElementById("KVESMIN_ID").checked then
				Raschet_KVESMIN = true
			else
				Raschet_KVESMIN = false
			End If

			'проведение утяжеления по P в минимальном режиме
			If obj_IE.document.getElementById("PMIN_ID").checked then
				Raschet_PMIN = true
			else
				Raschet_PMIN = false
			End If

			'Блок загрузки и сохранения данных и результатов
			If obj_IE.document.getElementById("SAVE_ID").checked then
				file_save = true
			else
				file_save = false
			End If
			g_Quit =  TRUE

			'/////   ИСХОДНЫЕ ДАННЫЕ   ////////////
			kod_regima = "p"
			Rastr.LogEnable = false
			Rastr.LockEvent = true
			sha_rg2 = "режим.rg2"
			sha_ut2 = "траектория утяжеления.ut2"
			sha_Ktves = "весовые коэффициенты трансформаторов.ves"
			kPut = directP 'коэффициент,определяющий направление утяжеления по P: прямой переток ip----->iq.....kPut = -1, ip<-----iq.....kPut = 1
			kQut = directP 'коэффициент,определяющий направление утяжеления по Q: прямой переток ip----->iq.....kQut = -1, ip<-----iq.....kQut = 1
			branch = "ip = " & ip & "& iq = " & iq & "& np = " & np 'контролируемая ветвь

			'НАСТРОЙКА ОПЦИЙ:
			'***************************************************************************************
			'***************************************************************************************
			'***************************************************************************************
			'Raschet_k_ves = true   'расчет весовых коэффициентов для выбора траектории утяжеления
			'Raschet_P_pred = true      'определение предельного перетока мощности
			'Raschet_P092 = false   'расчет режима с P = 0.92*Pпред
			'Raschet_P08 = false         'расчет режима с P = 0.8*Pпред
			'Raschet_I = false           'расчет режима с перетоком, соответсвующем Izad
			'***************************************************************************************
			'***************************************************************************************
			'***************************************************************************************
			'устанавливаем максимальное число итераций при расчете УР равным 100

			Set Regim_Set = rastr.tables("com_regim")
			Regim_Set.cols("it_max").Z(0) = 100

			If file_save then
				dir_1 = Rastr.SEndCommandMain(13,"Укажите каталог для сохранения файлов:","",0)  'директория, куда сохранять режимы
				prdir = Rastr.SEndCommandMain(3,"","",0) ' директория с Rastr
				shabl_rg2 = prdir & "SHABLON\" & sha_rg2
				shabl_ut2 = prdir & "SHABLON\" & sha_ut2
				shabl_ves = prdir & "SHABLON\" & sha_Ktves
			End If

			If dir_1 = "" then
				rastr.printp "Каталог для сохранения не выбран, расчеты выполняются без автоматического сохранения"
				file_save = false
			End If

			StartTime = Timer
			dopname = day(Now) & month(Now)& hour(Now)& minute(Now)

			Select Case Block_R
				Case 1
					If Raschet_k_ves then
						obj_IE.Document.getElementById("ISX").innerHTML = "Расчет Kves"

						Call Raschet_Kves(branch,kPut)

						If file_save then
							Rastr.Save dir_1 & "\Траектория утяжеления_" & dopname & ".ut2",shabl_ut2
						End If
					else
						If Raschet_P_pred then
							Set trut = Rastr.Tables("Traektory_ut")
							trut.Cols("Uchastie").Calc("0")
							trut.Cols("rashojdenie").Calc("0")
							trut.Cols("n_shaga").Calc("0")
						End If
					End If

					If Raschet_P_pred then
						 'выбор трансформаторов с возможностью изменять положения РПН
						Call Trans_RPN()

						obj_IE.Document.getElementById("ISX").innerHTML = "Расчет Pпред"

						Call Poisk_Ppred(branch,kQut,znch)

						If file_save then
							Rastr.Save dir_1 & "\Предельный режим_" & dopname & ".rg2",shabl_rg2
							Rastr.Save dir_1 & "\Траектория утяжеления_" & dopname & ".ut2",shabl_ut2
							Rastr.Save dir_1 & "\Траектория утяжеления_" & dopname & ".ves",shabl_ves
						End If
					End If

					file_zagr_rg2 = Rastr.SEndCommandMain(6,sha_rg2,"",0)  'путь к загруженному файлу *.rg2
					file_zagr_ut2 = Rastr.SEndCommandMain(6,sha_ut2,"",0)  'путь к загруженному файлу *.ut2

					Set tvetv = Rastr.Tables("vetv")

					Call tvetv.Setsel(branch)

					vetv_pos = tvetv.FindNextSel(-1)

					Raschet_I0 = true 'анализ тока по элементу в предельном (исходном) режиме
					 'если в предельном(исходном) режиме ток по контролируемому элементу меньше Izad, то расчет режима с током по элементу, равным по величине Iав.доп. не осуществляется
					If Flow_I(vetv_pos) < Izad then
						Raschet_I0 = false
					End If

					If control_P = "ip" then
						P092 = 0.92 * Flow_Pip(vetv_pos) * kPut
						P08 = 0.8 * Flow_Pip(vetv_pos) * kPut
					End If

					If control_P = "iq" then
						P092 = 0.92 * Flow_Piq(vetv_pos)*kPut
						P08 = 0.8 * Flow_Piq(vetv_pos)*kPut
					End If

					If Raschet_P092 then
						obj_IE.Document.getElementById("ISX").innerHTML = "Расчет 0,92Pпред"
						Rastr.printp "Расчет режима с перетоком по элементу 0,92*Pпред."
						Rastr.printp "Стремимся получить величину " & P092 & "+/- 1 МВт"

						Call Poisk_P1(branch, P092, kPut, control_P)

						If file_save then Rastr.Save dir_1 & "\Режим 092Pпред_" & dopname & ".rg2",shabl_rg2
					End If

					If Raschet_P08 then
						obj_IE.Document.getElementById("ISX").innerHTML = "Расчет 0,8Pпред"
						Rastr.printp("Расчет режима с перетоком по элементу 0,8*Pпред.")
						Rastr.printp("Стремимся получить величину " & P08 & "+/- 1 МВт")

						Call Poisk_P1(branch,P08,kPut,control_P)

						If file_save then Rastr.Save dir_1 & "\Режим 08Pпред_" & dopname & ".rg2",shabl_rg2
					End If

					If Raschet_I Then
						If not Raschet_I0 then
							msgbox "В предельном(исходном) режиме ток по элементу меньше заданного."
						Else
							obj_IE.Document.getElementById("ISX").innerHTML = "Расчет P(Iзад.)"
							If Flow_I(vetv_pos) > Izad then
								Rastr.printp "Расчет режима с током по элементу, равным по величине Iав.доп."
								Call Poisk_I1(branch,Izad)
							Else
								Rastr.Load 1, file_zagr_rg2, shabl_rg2
								Rastr.Load 1, file_zagr_ut2, shabl_ut2

								Rastr.printp "Загружен режим: " & file_zagr_rg2
								Rastr.printp "Загружена траектория утяжеления: " & file_zagr_ut2
								Rastr.printp "Расчет режима с током по элементу, равным по величине Iав.доп."

								Call Poisk_I1(branch,Izad)

							End If
						End If

						If file_save then Rastr.Save  dir_1 & "\Режим I_" & dopname & ".rg2", shabl_rg2
					End If

				Case 2
					Call Trans_RPN()

					Call Trans_Ut(branch,kQut,znch,Raschet_KVESQ,Raschet_UTONLYQ)

					If file_save then
						Rastr.Save dir_1 & "\Q_режим_" & dopname & ".rg2",shabl_rg2
						Rastr.Save dir_1 & "\Весовые коэффициенты АТ_" & dopname & ".ves",shabl_ves
					End If

				Case 3
					Call MinRegim(branch, kPut, kQut, znch, Raschet_QMIN, Raschet_KVESMIN, Raschet_PMIN, obj_IE)

					If file_save then
						Rastr.Save dir_1 & "\Pmin_режим_" & dopname & ".rg2",shabl_rg2
						Rastr.Save dir_1 & "\Весовые коэффициенты АТ_" & dopname & ".ves", shabl_ves
						Rastr.Save dir_1 & "\Траектория утяжеления_" & dopname & ".ut2", shabl_ut2
					End If
			End Select

			EndTime = Timer
			MsgBox "Затраченное на расчет время: " & (EndTime-StartTime)/60 & " минут"
			Rastr.LogEnable = true
			Rastr.LockEvent = false
			Rastr.SEndChangeData 0,"","",0
		End If

		 '\\\\\\\\\\\\\\\\\\\\\ НАЖАТА КНОПКА ЗАГРУЗИТЬ //////////////////
		If(obj_IE.document.MyForm.ButtonPressed.Value  = "3") THEN    'Если нажата кнопка Загрузить, то выбираем файл загрузки
			File_Set = Rastr.SEndCommandMain(1,"Выберите файл с настройками","",0)
			If File_Set <> "" then
				Set fso = CreateObject("Scripting.FileSystemObject")
				'Чтение из файла
				Set file = fso.OpenTextFile(File_Set, 1, false)
				ip = file.ReadLine()
				iq = file.ReadLine()
				np = file.ReadLine()
				i_zad = file.ReadLine()
				directP = file.ReadLine()
				raschet_k_ves = file.ReadLine()
				raschet_P_pred = file.ReadLine()
				raschet_P_092 = file.ReadLine()
				raschet_P_08 = file.ReadLine()
				raschet_P_Izad = file.ReadLine()
				save = file.ReadLine()

				Set fso = Nothing
				Set file = Nothing

				obj_IE.document.MyForm.IP.value = ip
				obj_IE.document.MyForm.IQ.value = iq
				obj_IE.document.MyForm.NP.value = np
				obj_IE.document.MyForm.Izad.value = i_zad

				'определяем направление утяжеления и применяем в форме
				For i = 0 to obj_IE.document.getElementsByName("ddd").length - 1
					If obj_IE.document.getElementsByName("ddd")(i).value = directP then
						obj_IE.document.getElementsByName("ddd")(i).checked = true
					End If
				next

				If raschet_k_ves then obj_IE.document.getElementById("KVES_ID").checked = true
				If Not raschet_k_ves then obj_IE.document.getElementById("KVES_ID").checked = false
				If raschet_P_pred then obj_IE.document.getElementById("PPRED_ID").checked = true
				If Not raschet_P_pred then obj_IE.document.getElementById("PPRED_ID").checked = false
				If raschet_P_092 then obj_IE.document.getElementById("P092_ID").checked = true
				If Not raschet_P_092 then obj_IE.document.getElementById("P092_ID").checked = false
				If raschet_P_08 then obj_IE.document.getElementById("P08_ID").checked = true
				If Not raschet_P_08 then obj_IE.document.getElementById("P08_ID").checked = false
				If raschet_P_Izad then obj_IE.document.getElementById("PIZAD_ID").checked = true
				If Not raschet_P_Izad then obj_IE.document.getElementById("PIZAD_ID").checked = false
				If save then obj_IE.document.getElementById("SAVE_ID").checked = true
				If Not save then obj_IE.document.getElementById("SAVE_ID").checked = false
			End If

			g_Quit =  FALSE
			obj_IE.document.MyForm.ButtonPressed.Value = "0"
		End If

		'///// НАЖАТА КНОПКА СОХРАНИТЬ //////////////////////////
		If(obj_IE.document.MyForm.ButtonPressed.Value  = "4") THEN  'Если нажата кнопка Сохранить, то считываем переменные из окон и записываем в файл
			ip = obj_IE.document.MyForm.IP.value
			iq = obj_IE.document.MyForm.IQ.value
			np = obj_IE.document.MyForm.NP.value
			i_zad = obj_IE.document.MyForm.Izad.value

			'определяем направление утяжеления
			For i = 0 to obj_IE.document.getElementsByName("ddd").length-1
				If obj_IE.document.getElementsByName("ddd")(i).checked then
					directP = obj_IE.document.getElementsByName("ddd")(i).value
				End If
			next

			If obj_IE.document.getElementById("KVES_ID").checked then
				raschet_k_ves = true
			else
				raschet_k_ves = false
			End If

			If obj_IE.document.getElementById("PPRED_ID").checked then
				raschet_P_pred = true
			else
				raschet_P_pred = false
			End If

			If obj_IE.document.getElementById("P092_ID").checked then
				raschet_P_092 = true
			else
				raschet_P_092 = false
			End If

			If obj_IE.document.getElementById("P08_ID").checked then
				raschet_P_08 = true
			else
				raschet_P_08 = false
			End If

			If obj_IE.document.getElementById("PIZAD_ID").checked then
				raschet_P_Izad = true
			else
				raschet_P_Izad = false
			End If

			If obj_IE.document.getElementById("SAVE_ID").checked then
				save = true
			else
				save = false
			End If

			File_save = Rastr.SEndCommandMain(2,"","",0)

			If File_save<>"" then
				Set fso = CreateObject("Scripting.FileSystemObject")
				 'Запись в файл
				Set file = fso.OpenTextFile(File_save, 2, true)
				file.WriteLine(ip)
				file.WriteLine(iq)
				file.WriteLine(np)
				file.WriteLine(i_zad)
				file.WriteLine(directP)
				file.WriteLine(raschet_k_ves)
				file.WriteLine(raschet_P_pred)
				file.WriteLine(raschet_P_092)
				file.WriteLine(raschet_P_08)
				file.WriteLine(raschet_P_Izad)
				file.WriteLine(save)
			End If
			Set fso = Nothing
			Set file = Nothing
			g_Quit =  FALSE
			obj_IE.document.MyForm.ButtonPressed.Value = "0"
		End If
	next
	'завершаем работу с IE
	obj_IE.Quit
	Set obj_IE = NOTHING
End Sub

'////////////////////////////////////РЕЖИМ С МИНИМАЛЬНЫМ ПЕРЕТОКОМ/////////////////////////////////////////////////
Sub MinRegim(branch, kPut0, kQut, znch, option1,option2,option3,obj_IE) 'option1-утяжеление по Q,option2-расчет весовых коэффициентов по P,option3- утяжеление по P
	Pzad = 1 * kPut0 'требуемый переток P по ветви в минимальном режиме
	If option1 then
		'сначала производим утяжеление по Q путем изменения анцапф на автотрансформаторах
		Trans_RPN
		obj_IE.Document.getElementById("ISX").innerHTML = "Утяжеление по Q"
		Trans_Ut branch,kQut,znch,true,true
	End If

	Set tvetv = Rastr.Tables("vetv")
	tvetv.Setsel(branch)
	vetv_pos = tvetv.FindNextSel(-1)

	'определяем исходный переток P по ветви: в зависимости от требуемого направления перетока P по элементу будем брать значение перетока либо в начале ветви, либо в конце
	If kPut0 = 1 then P0 = Flow_Piq(vetv_pos)  'переток P в конце ветви
	If kPut0 = -1 then P0 = Flow_Pip(vetv_pos) ' переток P в начале ветви
		'проводим расчет весовых коэффициентов по P исходя из фактического перетока по ветви и требуемого направления утяжеления
	If (kPut0 = -1 And P0<Pzad) then kPut = 1
	If (kPut0 = -1 And P0>Pzad And sgn(Pzad)<>sgn(P0)) then kPut = -1
	If (kPut0 = -1 And P0>Pzad And sgn(Pzad) = sgn(P0)) then kPut = 0
	If (kPut0 = 1 And P0>Pzad) then kPut = -1
	If (kPut0 = 1 And P0<Pzad And sgn(Pzad)<>sgn(P0)) then kPut = 1
	If (kPut0 = 1 And P0<Pzad And sgn(Pzad) = sgn(P0)) then kPut = 0

	If option2 then
		'расчет весовых коэффицинтов исходя из фактического и требуемого направления перетока P
		obj_IE.Document.getElementById("ISX").innerHTML = "Расчет Kвес по P"
		Raschet_Kves branch,kPut
	End If
	If option3 then
	'проводим утяжеление для достижения минимального перетока по элементу
	obj_IE.Document.getElementById("ISX").innerHTML = "Расчет Pmin"
	Set trut = Rastr.Tables("Traektory_ut")
	trut.Cols("Uchastie").Calc("0")
	trut.Cols("rashojdenie").Calc("0")
	trut.Cols("n_shaga").Calc("0")
	shag = 0
	'Цикл утяжеления по условию
	FLAG_ut = true 'TRUE разрешает произвести шаг утяжеления, FALSE-выход из цикла утяжеления

	If kPut = 0 then FLAG_ut = false

		Do While (shag < trut.Size and FLAG_ut and Abs(Balance_P()) <= 2000)
			rastr.printp FLAG_ut
			Pbal = Balance_P()
			If ut_End = 1 then
				flag = 2
			else
				If Pbal <= (-100) then flag = 1
				If Pbal >= 100 then flag = 0
			End If

			Select Case flag
				Case 0
					trut.SetSel("Uchastie = 0 & kod_ut < 3")
					ut_pos = trut.FindNextSel(-1)
					If ut_pos = (-1) then
						ut_End = 1
					else
						If trut.cols("kod_ut").Z(ut_pos) = 1 then kod_d = 10
						If trut.cols("kod_ut").Z(ut_pos) = 2 then kod_d = 11
						result = shag_ut(trut.cols("Num").Z(ut_pos), kod_d, 0)
						If result<>0 then
							rastr.printp "Режим не сходится!!! Пропускаем этот генератор"
							trut.cols("rashojdenie").Z(ut_pos) = 1
						End If
						trut.cols("Uchastie").Z(ut_pos) = 1
						trut.cols("n_shaga").Z(ut_pos) = shag
						shag = shag + 1
					End If

				Case 1
					trut.SetSel("Uchastie = 0&kod_ut = 3")
					ut_pos = trut.FindNextSel(-1)
					If ut_pos = (-1) then
						ut_End = 1
					else
						If trut.cols("kod_ut").Z(ut_pos) = 3 then kod_d = 21
						result = shag_ut(trut.cols("Num").Z(ut_pos), kod_d, 0)
						If result<>0 then
							rastr.printp "Режим не сходится!!! Пропускаем этот генератор"
							trut.cols("rashojdenie").Z(ut_pos) = 1
						End If
						trut.cols("Uchastie").Z(ut_pos) = 1
						trut.cols("n_shaga").Z(ut_pos) = shag
						shag = shag + 1
					End If

				Case 2 'когда кончились генераторы одного направления утяжеления
					on Error Resume Next
					trut.SetSel("Uchastie = 0")
					ut_pos = trut.FindNextSel(-1)
					If trut.cols("kod_ut").Z(ut_pos) = 1 then kod_d = 10
					If trut.cols("kod_ut").Z(ut_pos) = 2 then kod_d = 11
					If trut.cols("kod_ut").Z(ut_pos) = 3 then kod_d = 21
					result = shag_ut(trut.cols("Num").Z(ut_pos), kod_d, 0)
					If result<>0 then
						rastr.printp "Режим не сходится при несбалансированном утяжелении"
						trut.cols("rashojdenie").Z(ut_pos) = 1
					End If
					trut.cols("Uchastie").Z(ut_pos) = 1
					trut.cols("n_shaga").Z(ut_pos) = shag
					shag = shag + 1

			End Select
			P_ip = Flow_Pip(vetv_pos)
			P_iq = Flow_Piq(vetv_pos)
			If (kPut0 = (-1) and kPut = 1 and P_ip > Pzad) then FLAG_ut = false
			If (kPut0 = (-1) and kPut = (-1) and P_ip < Pzad) then FLAG_ut = false
			If (kPut0 = 1 and kPut = (-1) and P_iq < Pzad) then FLAG_ut = false
			If (kPut0 = 1 and kPut = 1 and P_iq > Pzad) then FLAG_ut = false
		Loop
	End If
End Sub