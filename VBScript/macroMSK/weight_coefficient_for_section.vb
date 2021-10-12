
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

	sha_ut2 = "���������� ����������.ut2"
	prdir = Rastr.SEndCommandMain(3,"","",0) ' ���������� � Rastr
	shabl_ut2 = prdir & "SHABLON\" & sha_ut2

	'k_reverse - ����������� ��������� �������� ��� �����, ��������� ����������� ����������
	dPgen = 10   '������ ��������� ��� ����������� ������� �������������
	'������ ������������ ������� ��� �������� ���������� ���������� ����������
	'� �������� ��������:
	'0 ������� - N ���
	'1 ������� - K_ves
	'2 ������� - dP ����������
	'3 ������� - ��� ��������: 0 - �� ���������, 1- ��������� �� ���������, 2 - ��������, 3 - ���������
	redim traektory(3,1)
	'***********************************************
	'***********************************************
	tvetv.Setsel(branch)
	vetv_pos = tvetv.FindNextSel(-1)
	Pl_ip1 = Flow_Pip(vetv_pos)*k_reverse    '������� �� �������������� ����� � �������� ������ (� ������ ��� ���� ip ������� ��������� ������������� ��� ����������� � iq)

	'/////////////////////////////////////////////////////////////////////////////
	'���� �� ������� ����������
	gen.Setsel("Num != 40100173 & ((Node.na = 510 & Pmax>9) | (Node.na >= 511 & Node.na <= 531 & Pmax >= 50) | (Node.na >= 201 & Node.na <= 409 & Pmax >= 145))")
	'gen.Setsel("(Node.na = 510&Pmax> = 10)|(Node.na> = 511&Node.na<531&Pmax> = 30)|(Node.na = 531&Pmax> = 10)|(Node.na> = 200&Node.na<500&Pmax> = 250)")
	str_traektory = 0 ' ��������� ������ � ������� ����������
	gen_pos = gen.FindNextSel(-1)
	While gen_pos<>(-1)
		K_ves_gen = 0
		kod_ut = 0   '��� ���������� � ������������ � ��������� ����
		redim preserve traektory(3, str_traektory)
		'���� ��������� �������, ��������� � ���� ��������� dPgen � ������������ ��������� �������� (Pl_ip2-Pl_ip1)
		If sta_gen.Z(gen_pos) = 0 then
			dPgen_plus = Pmax_gen.Z(gen_pos) - P_gen.Z(gen_pos)         '��������, �� ������� ����� ��������� ���������
			'dPgen_minus = P_gen.Z(gen_pos)-Pmin_gen.Z(gen_pos)         '��������, �� ������� ����� ������� ��������� �� �������� ��� ���������
			P_gen.Z(gen_pos) = P_gen.Z(gen_pos) + dPgen
			kod = rastr.rgm(kod_regima)
			If kod<>0 then '���� ����� �� ��������
				K_ves_gen = 0   '��������� �� ����� ����������� � ���������� ����������
			else
				Pl_ip2 = Flow_Pip(vetv_pos) * k_reverse
				K_ves_gen = (Pl_ip2 - Pl_ip1)/dPgen
				'� ������������ � K_ves ��������� ������� ���������� ��� ����������
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
						traektory(2,str_traektory) =  P_gen.Z(gen_pos)-dPgen            'P_gen.Z(gen_pos) - ���� ��������� ���������, dPgen_minus - ���� ���������� �� ��������
					End If
			End If
			traektory(0,str_traektory) =  Num_gen.Z(gen_pos)
			traektory(1,str_traektory) =  K_ves_gen
			P_gen.Z(gen_pos) = P_gen.Z(gen_pos)-dPgen             '���������� �������� ���������
		End If
		'���� ��������� ��������, �������� ��� � ���������� Pmin � ������������ ��������� �������� (Pl_ip2-Pl_ip1)
		If sta_gen.Z(gen_pos)<>0 then
			sta_uzla_0 = 0
			Pgen0 = P_gen.Z(gen_pos)   '�������� ���������, ������������� ��� ������������ ����������
			uzel_gen = 0
			dPgen_plus = Pmax_gen.Z(gen_pos)-P_gen.Z(gen_pos)         '��������, �� ������� ����� ��������� ���������
			'dPgen_minus = P_gen.Z(gen_pos)-Pmin_gen.Z(gen_pos)       '��������, �� ������� ����� ������� ��������� �� �������� ��� ���������
			sta_gen.Z(gen_pos) = 0
			uzel_gen = Node_gen.Z(gen_pos)                    		'����, � ������� ������� ���������
			'���� ���� ���������� ��������, ���������� ��� ���������, �������� ��� ������ � �������

			If Node_sta.Z(gen_pos)<>0 then
			   sta_uzla_0 = 1
			   HitGen uzel_gen '���� ���� ���������� ��������, �������� ��� � �������
			End If

			P_gen.Z(gen_pos) = Pmin_gen.Z(gen_pos)+dPgen
			kod = rastr.rgm(kod_regima)

			If kod<>0 then
				K_ves_gen = 0   '���� ����� ��� ��������� ���������� �� Pg_min �� �������, �� �� ����� ����������� � ���������� ����������
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
			P_gen.Z(gen_pos) = Pgen0  							'���������� �������� ��������� ���������� � ������� ����������
			sta_gen.Z(gen_pos) = 1
			'���� �������� ��������� ���� ���� �����������, �� ���������� ��� � ���� �� ���������
			If sta_uzla_0 = 1 then
			   tnode.Setsel("ny = " & uzel_gen)      '����� ������������� ���� � ������� ����
			   uzel_pos = tnode.FindNextSel(-1)      '����������� ��� ������� � �������
			   sta_uzla.Z(uzel_pos) = 1              '���������� �������� ��������� ����, � �������� ��������� ���������
			End If
		 End If
		traektory(3,str_traektory) =  kod_ut
		gen_pos = gen.FindNextSel(gen_pos)
		str_traektory = str_traektory + 1
	Wend
	rastr.rgm kod_regima
	'��������� �� �������� ������ ������� �������������
	Call BubbleSortKvesAbsDown(traektory, str_traektory-1)
	'��������� ������� ���������� ���������� ������
	Rastr.NewFile(shabl_ut2)
	Set trut = Rastr.Tables("Traektory_ut")
	' trut.SetSel("1")
	' trut.DelRows
	str_num = 0   '����� ������ � ������� ��������� ������
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
	'��������� ���� "Name" � ��������� �������
	For i = 0 to trut.size-1
		num_G = trut.Cols("Num").Z(i)
		gen.SetSel("Num = " & num_G)
		gen_pos = gen.FindNextSel(-1)
		If gen_pos<>-1 then trut.Cols("Name").Z(i) = gen.cols("Name").Z(gen_pos)
	next
	'������� ������ traektory
	Erase traektory
End Sub

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'������� ����������� �������� �������� � ������ �����
Function Flow_Pip(position)    '������� ����� � ������� VETV
	Set tvetv = Rastr.Tables("vetv")
	Flow_Pip = tvetv.Cols("pl_ip").Z(position)'�� ������������� ����������� ������� ����������� �� ��� � �������
End Function

Function Flow_Piq(position)    '������� ����� � ������� VETV
	Set tvetv = Rastr.Tables("vetv")
	Flow_Piq = tvetv.Cols("pl_iq").Z(position)      '�� ������������� ����������� ������� ����������� �� ��� � �������
End Function

Function Flow_P(position,control_P)    '������� ����� � ������� VETV, ����� ������ P
	If control_P = "ip" then Flow_P =  Flow_Pip(position)
	If control_P = "iq" then Flow_P =  Flow_Piq(position)
End Function

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'������� ����������� ������������� ���� �� �����
Function Flow_I(position)    '������� ����� � ������� VETV
	Set tvetv = Rastr.Tables("vetv")
	Flow_I = max(tvetv.Cols("ib").Z(position),tvetv.Cols("ie").Z(position))*1000
End Function

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'������������ ��������� ���� � �������
Sub HitGen(uzel)
	Set tvetv = Rastr.Tables("vetv")
	Set tnode = Rastr.Tables("node")
	tnode.SetSel("ny = " & uzel)
	tnode.Cols("sta").calc("0")
	rastr.printp "��������� ���� �" & uzel
	tvetv.SetSel("ip = " & uzel & "|iq = " & uzel)
	tvetv.Cols("sta").Calc("0")
End sub

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'������������ ���������� ������� �������� �� �������� ������
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
'������������ ���������� ������� �������� �� �����������
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
'������������ ���������� ������� �������� �� ��������
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
'������� ������� ����� ������� ��������� �������
Function Column_Sum(Arr, n, num) 'Arr - ������, n - ����� ����� � �������, num - �������, � ������� ������������ ����� ���������
	dim i
	Column_Sum = 0
	For i = 0 to n
		Column_Sum = Column_Sum+Arr(num,i)
	next
End Function

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'������� ������ �������� ����� ���� ��������
Function min(a,b)
	'dim a,b
	If a<= b then
		min = a
	else
		min = b
	End If
End Function

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'������� ������ ��������� ����� ���� ��������
Function max(a,b)
	'dim a,b
	If a >= b then
		max = a
	else
		max = b
	End If
End Function

'////////////////////////////////////////////////////
'������� ����������� �������� � ������������� ����
Function Balance_P()
	'ny_bal = 10291049 '����� �������������� ���� (����� ���������� ��� ��������� ������ - ������� ���� �� �����)
	Set tnode = Rastr.Tables("node")
	tnode.SetSel("na = 102&tip = 0")
	'tnode.SetSel("ny = " & ny_bal)
	node_bal_pos = tnode.FindNextSel(-1)
	Balance_P = 0    '��������� � ������������� ����
	Balance_P = tnode.Cols("pg").Z(node_bal_pos)
End Function

'/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'�������, ����������� ���� ��� ���������� � ����������� N_agr, �� ������ ���� ��� ���������� �������������� ����
Function shag_ut(N_agr, kod_d, U_control) 'kod_d - ��� �������� � �����������: 10-��������� �� Pmax, 11-��������, 20-���������� �� Pmin, 21-���������
	If U_control = 1 then
		Call Control_U_500_750()  '������ �������� ���������� � ����� 500-750 �� ���� ��� ������
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
		P_gen0 = P_gen.Z(gen_pos)      '�������� ��������� �� ������������� ���� ����������
		sta_gen0 = sta_gen.Z(gen_pos)  '�������� ��������� ������������� ���� �� ������������� ���� ����������
		Select Case kod_d
			Case 10
			   P_gen.Z(gen_pos) = Pmax_gen.Z(gen_pos)
			   rastr.printp "�������� �� Pmax ���������� �" & Num_gen.Z(gen_pos)
			Case 11
			   sta_gen.Z(gen_pos) = 0
			   P_gen.Z(gen_pos) = Pmax_gen.Z(gen_pos)
			   uzel_gen = Node_gen.Z(gen_pos)
			   tnode.Setsel("ny = " & uzel_gen)
			   uzel_pos = tnode.FindNextSel(-1)
			   sta_uzla0 = tnode.Cols("sta").Z(uzel_pos)   '�������� ��������� ���� � ������� ���� �� ���� ����������
			   If tnode.Cols("sta").Z(uzel_pos)<>0 then HitGen uzel_gen
			   rastr.printp "��������� � ��������� Pmax ���������� �" & Num_gen.Z(gen_pos)
			Case 20
			   P_gen.Z(gen_pos) = Pmin_gen.Z(gen_pos)
			Case 21
			sta_gen.Z(gen_pos) = 1
			rastr.printp "���������� ���������� �" & Num_gen.Z(gen_pos)
		End Select
		'������ ������ � ������ ���� ����������
		shag_ut = rastr.rgm(kod_regima)  '��� ������� ������
		If shag_ut<>0 then '���� ����� ��������� ������������ � ����������� ���������
			rastr.printp "����� �� ������ ���� ���������� �� ������� - ������� � ����������� ����!"
			P_gen.Z(gen_pos) = P_gen0
			sta_gen.Z(gen_pos) = sta_gen0
			If sta_gen0<>0 then tnode.Cols("sta").Z(uzel_pos) = sta_uzla0
			ppp = rastr.rgm(kod_regima)
			If ppp<>0 then ppp = rastr.rgm("p")
			If ppp<>0 then rastr.printp "����� �� ������� ��� ������ �����"
		End If
        End If
End Function

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'********������������ ������ ����������� ������*************************************************************************
'///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Sub Poisk_Ppred(branch,kQut,znch)  '�������������� �����, ����������� ���������� �� Q, ���� ����������������� �� Q ��� ��
	Set tvetv = Rastr.Tables("vetv")
	tvetv.Setsel(branch)
	vetv_pos = tvetv.FindNextSel(-1)
	Set trut = Rastr.Tables("Traektory_ut")
	shag = 0
	ut_End = 0     '� ���������� ��������� ���������� ��� �� ���������, ��� � �� �������� - ut_End = 1 ����� � ���������� ���������� ������ ���������� ����� ������
	zapusk_Q = false   '���� �� ������ ���������� �� Q ��� ������ ���
	'���������� ����������� ���������� �� ��������� � ������������� ����
	'���� ���������� �� �������
	Do While (shag < trut.Size and Abs(Balance_P()) <= 3000)
		rastr.printp "������� P = " & Flow_Pip(vetv_pos)*(-1)
		Pbal = Balance_P()
		If ut_End = 1 then
			flag = 2
		else
			If Pbal <= (-100) then flag = 1
			If Pbal >= 100 then flag = 0
		End If
		'rastr.printp "��� �" & shag & ": ������ " & Balance_P(node_bal_pos)
		Select Case flag
			Case 0
				trut.SetSel("Uchastie = 0&kod_ut<3")
				ut_pos = trut.FindNextSel(-1)
				If ut_pos = (-1) then
					ut_End = 1
					Trans_Ut branch,kQut,znch,true,true    '������ �� ���������� �� Q ����� ��������� ��������� ��� ���������������
				else
					If trut.cols("kod_ut").Z(ut_pos) = 1 then kod_d = 10
					If trut.cols("kod_ut").Z(ut_pos) = 2 then kod_d = 11
					result = shag_ut(trut.cols("Num").Z(ut_pos), kod_d, 1)
					If result<>0 then
						rastr.printp "����� �� ��������!!! ���������� ���� ���������"
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
					Trans_Ut branch,kQut,znch,true,true  '������ �� ���������� �� Q ����� ��������� ��������� ��� ���������������
				else
					If trut.cols("kod_ut").Z(ut_pos) = 3 then kod_d = 21
					result = shag_ut(trut.cols("Num").Z(ut_pos), kod_d, 1)
					If result<>0 then
						rastr.printp "����� �� ��������!!! ���������� ���� ���������"
						trut.cols("rashojdenie").Z(ut_pos) = 1
					End If
					trut.cols("Uchastie").Z(ut_pos) = 1
					trut.cols("n_shaga").Z(ut_pos) = shag
					shag = shag + 1
				End If
			Case 2    '����� ��������� ���������� ������ ����������� ����������
				on Error Resume Next
				trut.SetSel("Uchastie = 0")
				ut_pos = trut.FindNextSel(-1)
				If trut.cols("kod_ut").Z(ut_pos) = 1 then kod_d = 10
				If trut.cols("kod_ut").Z(ut_pos) = 2 then kod_d = 11
				If trut.cols("kod_ut").Z(ut_pos) = 3 then kod_d = 21
				result = shag_ut(trut.cols("Num").Z(ut_pos), kod_d, 1)
				If result<>0 then
					rastr.printp "����� �� �������� ��� ������������������ ����������"
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
	tnode.SetSel("na >= 510 & na <= 532 & uhom >= 500 & bsh > 0 & vras < 0.8*uhom&sta = 0") '������� ��  ��� ������
	tnode.Cols("sta").Calc("1")
End Sub

'**********************************************************************************************************************
'������������ ���������� �� ���������� �������� ��� ������ ��� ���������������, ������� �������� - �������������� ����� � ����������� ����������
Sub Trans_Ut(branch,k_reverse,zone_nch,option1,option2)  'option1 - ������ K��� �� Q, option2 - ���������� �� Q
	'zone_nch = 0.2      '���� ����������������� - ���������� ����� ���������� ������� �� ������������� ��� �������������� ��� ��������� ��������� ��� �� ���� �������

	sha_Ktves = "������� ������������ ���������������.ves"
	sha_anc = "�������.anc"
	prdir = Rastr.SEndCommandMain(3,"","",0) ' ���������� � Rastr
	shabl_ves = prdir & "SHABLON\" & sha_Ktves
	shabl_anc = prdir & "SHABLON\" & sha_anc
	'�������� �������� ����� � ���������
	proverka = false
	Set Tabs = Rastr.Tables
	For i = 0 to Tabs.Count-1
		If tabs(i).Name = "ancapf" then
			proverka = true
			j = i
		End If
	Next

	If ((not proverka) or (tabs(j).size = 0)) then
		msgbox "�� �������� ���� ������! ������ ���������.",48,"��������!!!"
		file_anc = Rastr.SEndCommandMain(1,"�������� ���� � ���������","",0)
		If file_anc = "" then exit Sub
		Rastr.Load 1,file_anc,shabl_anc
	End If

	Rastr.rgm kod_regima

	redim trans_ves(4,1)                    '������� ������� ������������� ���������������: 0-ip;1-iq;2-np;3-Kt_ves;4-anc0
	Set tvetv = Rastr.tables("vetv")
	Set tancapf = Rastr.tables("ancapf")
	tvetv.Setsel(branch)
	vetv_pos = tvetv.FindNextSel(-1)
	Ql_ip0 = tvetv.Cols("ql_ip").Z(vetv_pos)*k_reverse   '�������� ������� Q � ������ �������������� ���

	If option1 then
		tvetv.Setsel("sel = 1")
		pos = tvetv.FindNextSel(-1)
		stroka_trans = 0
		While pos<>(-1)
			anc0 = tvetv.Cols("n_anc").Z(pos)          '������� ��������� ��� �� ��������������
			ktr0 = tvetv.Cols("ktr").Z(pos)            '������� ����������� ������������� ��������������
			nomer_bd = tvetv.Cols("bd").Z(pos)
			redim preserve trans_ves(4,stroka_trans)
			'��������� � ����� ��������� ����� ���: ���� �� � ������� ������������, ����� ����������� �� ���� ������� �����(� ��������� ��������� ������������ �������������) � ������������ ������ Q �� ����������� �����
			If anc0 < Anc_max(nomer_bd) then              '���� ��� �� � ������� ������������ ���������, �� ��������� ���� �������
				do
					tvetv.Cols("n_anc").Z(pos) = tvetv.Cols("n_anc").Z(pos)+1    '���� ��� ���������� ����� ������� ����������� ������������� �� �������� �� ��������� ��� �� ������ ���������
					'������������ �������������(��������� ��� ����������� ���������)
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
					Kt_ves = 0  '������������� �� ��������� � ���������� �� Q
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

		 '���������� Kt_ves � ������� �������� ������
		BubbleSortAbsDown trans_ves, stroka_trans-1

		 '��������� ������� ���������� �� Q
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
	    '��������� ����� ��������� ��� �������� ������� ������������� �� ������� "���������� �� Q"
	    Set transutQ = Rastr.Tables("TransUt")
		transutQ.Cols("Uchastie").Calc("0")
		For i = 0 to transutQ.size-1
			tvetv.SetSel("ip = " & transutQ.Cols("ip").z(i) & "& iq = " & transutQ.Cols("iq").z(i) & "&  np = " & transutQ.Cols("np").z(i))
			pos_trans = tvetv.FindNextSel(-1)
			anc0 = tvetv.cols("n_anc").Z(pos_trans)   '���������� �������� ��������� ��� ��� ����������� ������ �����
			rastr.printp "������ " & tvetv.cols("dname").Z(pos_trans) & ".....n_anc ��� = " & tvetv.cols("n_anc").Z(pos_trans)
			If transutQ.Cols("kt_ves").z(i)>zone_nch then '���� ������� ����������� >���� ����������������� zone_nch ����� ���������� ������������ ��������� ���
				tvetv.cols("n_anc").Z(pos_trans) = 50
				tvetv.cols("n_anc").calc("1*n_anc")
				kod = Rastr.rgm(kod_regima)
				If kod<>0 then        '���� ����� ���������, ���������� �������� ��������� ���
					tvetv.cols("n_anc").Z(pos_trans) = anc0
					transutQ.Cols("Uchastie").Z(i) = false
				else
					tvetv.cols("groupid").Z(pos_trans) = 50
					transutQ.Cols("Uchastie").Z(i) = true
				End If
			End If
			If transutQ.Cols("kt_ves").z(i) < zone_nch*(-1) then '���� ������� ����������� <0 ����� ���������� ����������� ��������� ���
				tvetv.cols("n_anc").Z(pos_trans) = 1
				tvetv.cols("n_anc").calc("1*n_anc")
				kod = Rastr.rgm(kod_regima)
				If kod<>0 then        '���� ����� ���������, ���������� �������� ��������� ���
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
'������� ����������� �������� ������������� ��������� ��� �������������� � ���� ������ �������
Function Anc_max(nomer_bd)
	On Error Resume Next
	Set tancapf = Rastr.tables("ancapf")
	tancapf.SetSel("nbd = " & nomer_bd)
	pos_bd_anc = tancapf.FindNextSel(-1)
	Anc_max = tancapf.cols("n_anc1").Z(pos_bd_anc)+tancapf.cols("n_anc2").Z(pos_bd_anc)+tancapf.cols("n_anc3").Z(pos_bd_anc)+tancapf.cols("n_anc4").Z(pos_bd_anc)+tancapf.cols("n_anc5").Z(pos_bd_anc)+tancapf.cols("kne").Z(pos_bd_anc)
End Function

'************************************************************************************************************
'������������ ������ ��������������� 220 �� � ���� � ���������� �� � ������������ ������������� ������������ ������������� ��� ���������
Sub Trans_RPN()
	Set tvetv = rastr.tables("vetv")
	tvetv.Setsel("sel = 1")
	tvetv.Cols("sel").Calc("0")   '������� ��������� ������
	tvetv.Setsel("ip.na = 510 & tip = 1 & sta = 0 & n_anc != 0 & ip.uhom > 110 & iq.uhom >= 110")
	pos = tvetv.FindNextSel(-1)
	While pos<>-1
		name = tvetv.cols("dname").z(pos)
		a = InStr(1,name,"���")
		If a>0 then tvetv.cols("sel").z(pos) = 1
		pos = tvetv.FindNextSel(pos)
	Wend
End Sub

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'������������ ���������� ������� �������� �� �������� ������
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
'�������, ����������� ���� ��� ������������� � ����������� N_agr, �� ������ ���� ��� ���������� �������������� ����
Function shag_razut(N_agr, kod_d, dP)'kod_d - ��� �������� � �����������: 11-��������, 20-���������� �� �������� dP, 21-���������
	'dP - ��������, �� ������� ��������� ���������� ���������
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
	P_gen0 = P_gen.Z(gen_pos)      '�������� ��������� �� ������������� ���� ����������
	sta_gen0 = sta_gen.Z(gen_pos)  '�������� ��������� ������������� ���� �� ������������� ���� �������������
	Select Case kod_d
		Case 11
			sta_gen.Z(gen_pos) = 0
			'P_gen.Z(gen_pos) = Pmax_gen.Z(gen_pos)
			uzel_gen = Node_gen.Z(gen_pos)
			tnode.Setsel("ny = " & uzel_gen)
			uzel_pos = tnode.FindNextSel(-1)
			sta_uzla0 = tnode.Cols("sta").Z(uzel_pos) '�������� ��������� ���� � ������� ���� �� ���� ����������
			If tnode.Cols("sta").Z(uzel_pos)<>0 then HitGen uzel_gen
			rastr.printp "��������� ���������� �" & Num_gen.Z(gen_pos) & " � ��������� " & P_gen.Z(gen_pos) & " ���"
		Case 20
			P_gen.Z(gen_pos) = Pmax_gen.Z(gen_pos)-dP
			rastr.printp "��������� ���������� �" & Num_gen.Z(gen_pos) & " �� " & P_gen.Z(gen_pos) & " ���"
		Case 21
			sta_gen.Z(gen_pos) = 1
			rastr.printp "���������� ���������� �" & Num_gen.Z(gen_pos)
	End Select
	'������ ������ � ������ ���� �������������
	shag_razut = rastr.rgm("p")  '��� ������� ������
	If shag_razut<>0 then '���� ����� ��������� ������������ � ����������� ���������
		rastr.printp "����� �� ������ ���� ������������� �� ������� - ������� � ����������� ����!"
		P_gen.Z(gen_pos) = P_gen0
		sta_gen.Z(gen_pos) = sta_gen0
		If sta_gen0<>0 then tnode.Cols("sta").Z(uzel_pos) = sta_uzla0
		ppp = rastr.rgm("p")
		'If ppp<>0 then ppp = rastr.rgm("p")
		If ppp<>0 then rastr.printp "����� �� ������� ��� ������ �����"
	End If
End Function
'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

Sub Poisk_P(branch,Pzad,k_reverse)
	Set tvetv = Rastr.Tables("vetv")
	tvetv.Setsel(branch)
	vetv_pos = tvetv.FindNextSel(-1)
	Set trut = Rastr.Tables("Traektory_ut")
	Set tGen = Rastr.Tables("Generator")
	'perehod = false   '���� �������� ����� Pzad � �������� �������������
	'��������� ���������� ���������� ����� ��� ����������
	shag_max = 0
	trut.Setsel("Uchastie = 1 & rashojdenie = 0")   '������� ���������� ����� ����������
	i = trut.findnextsel(-1)
	While i<>-1
		If shag_max<trut.cols("n_shaga").Z(i) then shag_max = trut.cols("n_shaga").Z(i)
		i = trut.findnextsel(i)
	Wend
	shag = shag_max
	Do While (shag >= 0 and Flow_Pip(vetv_pos)*k_reverse>Pzad)
		'rastr.printp "�������� ��� �" & shag & " - ������� P = " & Flow_Pip(vetv_pos)*(-1)
		trut.Setsel("n_shaga = "& shag)   '������� ���������� ����� ����������
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
					rastr.printp "����� �� ��������!!! ���������� ���� ���������"
					trut.cols("rashojdenie").Z(pos_shaga) = 1
				End If
				trut.cols("Uchastie").Z(pos_shaga) = 0
				shag = shag-1
			Case 2
				result = shag_razut(trut.cols("Num").Z(pos_shaga), 21, trut.cols("dPgen").Z(pos_shaga))
				If result<>0 then
					rastr.printp "����� �� ��������!!! ���������� ���� ���������"
					trut.cols("rashojdenie").Z(pos_shaga) = 1
				End If
				trut.cols("Uchastie").Z(pos_shaga) = 0
				shag = shag-1
			Case 3
				result = shag_razut(trut.cols("Num").Z(pos_shaga), 11, trut.cols("dPgen").Z(pos_shaga))
				If result<>0 then
					rastr.printp "����� �� ��������!!! ���������� ���� ���������"
					trut.cols("rashojdenie").Z(pos_shaga) = 1
				End If
				trut.cols("Uchastie").Z(pos_shaga) = 0
				shag = shag-1
		End Select
	Loop

	' ��� ������ ����������� ����� P��� ������� dP = P���-P � ���� dP>1 ��� �� ������������ �� ���� ��� �����, ��������� dP ��� ���, � ���� dP>-1 ���,
	' �� ������������ ��� ��������� ���������� �� |dP|< = 1 ������� ����������� �������
	dP = Pzad-Flow_Pip(vetv_pos)*k_reverse

	If dP>1 then
		shag = shag + 1
		trut.Setsel("n_shaga = " & shag)   '������� ���������� ����� ����������
		pos_shaga = trut.findnextsel(-1)
		trut.cols("Uchastie").Z(pos_shaga) = 1
		If trut.cols("kod_ut").Z(pos_shaga) = 1 then kod_d = 10
		If trut.cols("kod_ut").Z(pos_shaga) = 2 then kod_d = 11
		If trut.cols("kod_ut").Z(pos_shaga) = 3 then kod_d = 21
		result = shag_ut(trut.cols("Num").Z(pos_shaga), kod_d, 0)
		If result<>0 then msgbox "����� �� ������� ��� ������ �� ���� ��� ��� ������ ��������� �������� �������� �� ��������!"
		dP = Pzad-Flow_Pip(vetv_pos)*k_reverse
		If dP > (-1) then
			kod_utyagelenia = trut.cols("kod_ut").Z(pos_shaga)
			tGen.SetSel("Num = " & trut.cols("Num").Z(pos_shaga))
			gen_pos = tGen.FindNextSel(-1)
			Select Case kod_utyagelenia
				Case 1
					rastr.printp "�������� 1"
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
					rastr.printp "�������� 2"
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
					rastr.printp "�������� 3"
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
'����� ����������� �� ���� ������
'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
Sub Poisk_I(branch,Izad)
	Set tvetv = Rastr.Tables("vetv")
	tvetv.Setsel(branch)
	vetv_pos = tvetv.FindNextSel(-1)
	Set trut = Rastr.Tables("Traektory_ut")
	Set tGen = Rastr.Tables("Generator")
	'��������� ���������� ���������� ����� ��� ����������
	shag_max = 0
	trut.Setsel("Uchastie = 1&rashojdenie = 0")   '������� ���������� ����� ����������
	i = trut.findnextsel(-1)
	While i<>-1
		If shag_max<trut.cols("n_shaga").Z(i) then shag_max = trut.cols("n_shaga").Z(i)
		i = trut.findnextsel(i)
	Wend
	shag = shag_max
	'msgbox Flow_I(vetv_pos)
	Do While (shag >= 0 and Flow_I(vetv_pos) > Izad)
		'rastr.printp "�������� ��� �" & shag & " - ������� P = " & Flow_Pip(vetv_pos)*(-1)
		trut.Setsel("n_shaga = "& shag)   '������� ���������� ����� ����������
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
					rastr.printp "����� �� ��������!!! ���������� ���� ���������"
					trut.cols("rashojdenie").Z(pos_shaga) = 1
				End If
				trut.cols("Uchastie").Z(pos_shaga) = 0
				shag = shag-1
			Case 2
				result = shag_razut(trut.cols("Num").Z(pos_shaga), 21, trut.cols("dPgen").Z(pos_shaga))
				If result<>0 then
					rastr.printp "����� �� ��������!!! ���������� ���� ���������"
					trut.cols("rashojdenie").Z(pos_shaga) = 1
				End If
				trut.cols("Uchastie").Z(pos_shaga) = 0
				shag = shag-1
			Case 3
				result = shag_razut(trut.cols("Num").Z(pos_shaga), 11, trut.cols("dPgen").Z(pos_shaga))
				If result<>0 then
					rastr.printp "����� �� ��������!!! ���������� ���� ���������"
					trut.cols("rashojdenie").Z(pos_shaga) = 1
				End If
			   trut.cols("Uchastie").Z(pos_shaga) = 0
			   shag = shag-1
		End Select
	Loop
	 ' ��� ������ ����������� ����� I��� ������� dI = I���-I � ���� |dI|>0.5 � �� ������������ �� ���� ��� �����, ��������� dI ��� ���, � ���� |dI|>1 � �����,
	 ' �� ������������ ��� ��������� ���������� �� |dI|< = 1 ������� ����������� �������
	dI = Izad-Flow_I(vetv_pos)
	If dI < (-0.5) then
	shag = shag+1
    trut.Setsel("n_shaga = " & shag)   '������� ���������� ����� ����������
    pos_shaga = trut.findnextsel(-1)
    trut.cols("Uchastie").Z(pos_shaga) = true
	If trut.cols("kod_ut").Z(pos_shaga) = 1 then kod_d = 10
	If trut.cols("kod_ut").Z(pos_shaga) = 2 then kod_d = 11
	If trut.cols("kod_ut").Z(pos_shaga) = 3 then kod_d = 21
	result = shag_ut(trut.cols("Num").Z(pos_shaga), kod_d, 0)
	If result<>0 then msgbox "����� �� ������� ��� ������ �� ���� ��� ��� ������ ��������� �������� �������� �� ��������!"
		dI = Izad-Flow_I(vetv_pos)
		If dI > 0.5 then
			kod_utyagelenia = trut.cols("kod_ut").Z(pos_shaga)
			tGen.SetSel("Num = " & trut.cols("Num").Z(pos_shaga))
			gen_pos = tGen.FindNextSel(-1)
			Select Case kod_utyagelenia
				Case 1
					msgbox "�������� 1"
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
					msgbox "�������� 2"
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
					msgbox "�������� 3"
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
'����� ����������� �� ���� ������
'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
Sub Poisk_I1(branch,Izad)
	Set tvetv = Rastr.Tables("vetv")
	tvetv.Setsel(branch)
	vetv_pos = tvetv.FindNextSel(-1)
	Set trut = Rastr.Tables("Traektory_ut")
	Set tGen = Rastr.Tables("Generator")
	Rastr.printp "������� ��� �� �������� " & Flow_I(vetv_pos)
	ut_End = 0
	Do While (Flow_I(vetv_pos) > Izad And ut_End <> 2)
		rastr.printp "��� I = " & Flow_I(vetv_pos)
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
						rastr.printp "����� �� ��������!!! ���������� ���� ���������"
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
						rastr.printp "����� �� ��������!!! ���������� ���� ���������"
						trut.cols("rashojdenie").Z(ut_pos) = true
					End If
					trut.cols("Uchastie").Z(ut_pos) = false
				End If

			Case 2      '����� ��������� ���������� ������ ����������� ����������
				trut.SetSel("Uchastie = 1&rashojdenie = 0")
				ut_pos = trut.FindNextSel(-1)
				If ut_pos<>-1 then
					If trut.cols("kod_ut").Z(ut_pos) = 1 then kod_d = 20
					If trut.cols("kod_ut").Z(ut_pos) = 2 then kod_d = 21
					If trut.cols("kod_ut").Z(ut_pos) = 3 then kod_d = 11
					result = shag_razut(trut.cols("Num").Z(ut_pos), kod_d, trut.cols("dPgen").Z(ut_pos))
					If result<>0 then
						rastr.printp "����� �� �������� ��� ������������������ �������������"
						trut.cols("rashojdenie").Z(ut_pos) = true
					End If
					trut.cols("Uchastie").Z(ut_pos) = false
				else
					ut_End = 2
					Msgbox "������� � ������ �� ���������� �� �������� ��������",48,"��������..."
				End If

		End Select
	Loop
	' ��� ������ ����������� ����� I��� ������� dI = I���-I � ���� |dI|>0.5 � �� ������������ �� ���� ��� �����, ��������� dI ��� ���, � ���� |dI|>1 � �����,
	' �� ������������ ��� ��������� ���������� �� |dI|< = 1 ������� ����������� �������
	dI = Izad-Flow_I(vetv_pos)
	If dI > 0.5 then
		rastr.printp "������� ��������� ����������� �" & trut.cols("Num").Z(ut_pos)
		If trut.cols("kod_ut").Z(ut_pos) = 1 then kod_d = 10
		If trut.cols("kod_ut").Z(ut_pos) = 2 then kod_d = 11
		If trut.cols("kod_ut").Z(ut_pos) = 3 then kod_d = 21
		result = shag_ut(trut.cols("Num").Z(ut_pos), kod_d, 0)
		trut.cols("Uchastie").Z(ut_pos) = true
		If result<>0 then msgbox "����� �� ������� ��� ������ �� ���� ��� ��� ������ ��������� �������� �������� �� ��������!"
		dI = Izad-Flow_I(vetv_pos)
		If dI<-0.5 then
			kod_utyagelenia = trut.cols("kod_ut").Z(ut_pos)
			tGen.SetSel("Num = " & trut.cols("Num").Z(ut_pos))
			gen_pos = tGen.FindNextSel(-1)
			Select Case kod_utyagelenia
				Case 1
					rastr.Printp "�������� 1"
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
					rastr.printp "�������� 2"
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
						msgbox "������ ���������� �������"
					End If
				Case 3
					rastr.printp "�������� 3"
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
'����� ��������� P �� ��������
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
						rastr.printp "����� �� ��������!!! ���������� ���� ���������"
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
						rastr.printp "����� �� ��������!!! ���������� ���� ���������"
						trut.cols("rashojdenie").Z(ut_pos) = true
					End If
					trut.cols("Uchastie").Z(ut_pos) = false
				End If

			Case 2       '����� ��������� ���������� ������ ����������� ����������
				trut.SetSel("Uchastie = 1&rashojdenie = 0")
				ut_pos = trut.FindNextSel(-1)
				If trut.cols("kod_ut").Z(ut_pos) = 1 then kod_d = 20
				If trut.cols("kod_ut").Z(ut_pos) = 2 then kod_d = 21
				If trut.cols("kod_ut").Z(ut_pos) = 3 then kod_d = 11
				result = shag_razut(trut.cols("Num").Z(ut_pos), kod_d, trut.cols("dPgen").Z(ut_pos))
				If result<>0 then
					rastr.printp "����� �� �������� ��� ������������������ �������������"
					trut.cols("rashojdenie").Z(ut_pos) = true
				End If
				trut.cols("Uchastie").Z(ut_pos) = false
		End Select
	Loop
	' ��� ������ ����������� ����� P��� ������� dP = P���-P � ���� |dP|>1 ��� �� ������������ �� ���� ��� �����, ��������� dP ��� ���, � ���� |dP|>1 ��� �����,
	' �� ������������ ��� ��������� ���������� �� |dP|< = 1 ������� ����������� �������
	dP = Pzad-Flow_P(vetv_pos,control_P)*k_reverse
	If dP>1 then
		rastr.printp "������� ��������� ����������� �" & trut.cols("Num").Z(ut_pos)
		If trut.cols("kod_ut").Z(ut_pos) = 1 then kod_d = 10
		If trut.cols("kod_ut").Z(ut_pos) = 2 then kod_d = 11
		If trut.cols("kod_ut").Z(ut_pos) = 3 then kod_d = 21
		result = shag_ut(trut.cols("Num").Z(ut_pos), kod_d, 0)
		trut.cols("Uchastie").Z(ut_pos) = true
		If result<>0 then msgbox "����� �� ������� ��� ������ �� ���� ��� ��� ������ ��������� �������� �������� �� ��������!"
		dP = Pzad-Flow_P(vetv_pos,control_P)*k_reverse
		If abs(dP)>1 then
			kod_utyagelenia = trut.cols("kod_ut").Z(ut_pos)
			tGen.SetSel("Num = " & trut.cols("Num").Z(ut_pos))
			gen_pos = tGen.FindNextSel(-1)
			Select Case kod_utyagelenia
				Case 1
					rastr.Printp "�������� 1"
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
					rastr.printp "�������� 2"
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
						'����� �������� �������� ��� ������ ����� ���  ��������� ���������� �� ������� �� ���������� Pzad>1
						msgbox "������ �������������� �������"
					End If

				Case 3
					rastr.printp "�������� 3"
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
			"<title>������ ����������� �������</title>"+vbCrLf+_
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
		"<body BGCOLOR = ""#�6c3c0"">"+vbCrLf+_
			"<P ALIGN = ""left""><b>��������� ��� ������� ����������� ������� (v2.6)</b><BR>"+vbCrLf+_
			"<ForM name = ""MyForm"" action = """" method = ""post""  onsubmit = ""return false;"">"+vbCrLf+_
				"<LABEL STYLE = ""text-align: Center"">����� ������:</LABEL><BR>"+vbCrLf+_
				"<input name = ""ButtonPressed"" type = ""hidden"" id = ""my"">"+vbCrLf+_
				"<LABEL>&nbsp&nbspip = &nbsp&nbsp</LABEL>"+vbCrLf+_
				"<INPUT TYPE = ""text"" id = ""IP_ID"" NAME = ""IP"" STYLE = ""text-align: Left; font-weight:bold"" VALUE = ""0"" SIZE = ""8""><BR>"+vbCrLf+_
				"<LABEL>&nbsp&nbspiq = &nbsp&nbsp</LABEL>"+vbCrLf+_
				"<INPUT TYPE = ""text"" id = ""IQ_ID"" NAME = ""IQ"" STYLE = ""text-align: Left; font-weight:bold"" VALUE = ""0"" SIZE = ""8""><BR>"+vbCrLf+_
				"<LABEL>&nbsp&nbspnp = &nbsp</LABEL>"+vbCrLf+_
				"<INPUT TYPE = ""text"" id = ""NP_ID"" NAME = ""NP"" STYLE = ""text-align: Left; font-weight:bold"" VALUE = ""0"" SIZE = ""1""><BR>"+vbCrLf+_
				"<LABEL>I��� = </LABEL>"+vbCrLf+_
				"<INPUT TYPE = ""text"" id = ""Izad_ID"" NAME = ""Izad"" STYLE = ""text-align: Left; font-weight:bold"" VALUE = ""0"" SIZE = ""4""><BR>"+vbCrLf+_
				"<LABEL STYLE = ""text-align: Left"">����������� ����������:</LABEL>"+vbCrLf+_
				"<BR>"+vbCrLf+_
				"<LABEL>ip&#10144iq</LABEL>"+vbCrLf+_
				"<INPUT TYPE = ""radio"" id = ""DIR_ID1"" NAME = ""ddd"" VALUE = ""-1"" CHECKED>"+vbCrLf+_
				"<LABEL>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp iq&#10144ip</LABEL>"+vbCrLf+_
				"<INPUT TYPE = ""radio"" id = ""DIR_ID2"" NAME = ""ddd"" VALUE = ""1"">"+vbCrLf+_
				"<BR>"+vbCrLf+_
				"<LABEL>���� ��������. ��</LABEL>"+vbCrLf+_
				"<INPUT TYPE = ""text"" id = ""ZNCH_ID"" NAME = ""ZNCH"" STYLE = ""text-align: Left"" VALUE = ""0,2"" SIZE = ""3""><BR>"+vbCrLf+_
				"<HR>"+vbCrLf+_
				"<INPUT TYPE = ""radio"" id = ""UTPQ_ID"" NAME = ""ut"" onClick = ""tiput(this);"" VALUE = ""1"" CHECKED>"+vbCrLf+_
				"<LABEL STYLE = ""text-align: Left; font-weight:bold"">����������� ����������(P,Q)</LABEL>"+vbCrLf+_
				"<BR>"+vbCrLf+_
				"<LABEL STYLE = ""text-align: Left"">��������� ����������:</LABEL>"+vbCrLf+_
				"<BR>"+vbCrLf+_
				"<TABLE>"+vbCrLf+_
				"<TR><TD colspan = ""3"">"+vbCrLf+_
					"<INPUT TYPE = ""CHECKBOX"" id = ""KVES_ID"" NAME = ""KVES"" CHECKED>&nbsp ������ K���.<BR>"+vbCrLf+_
					"<INPUT TYPE = ""CHECKBOX"" id = ""PPRED_ID"" NAME = ""PPRED"" CHECKED>&nbsp ������ P����.<BR>"+vbCrLf+_
				"</TD></TR></TABLE>"+vbCrLf+_
					"<TABLE BGCOLOR = ""#a1c6c0""><TR><TD colspan = ""3"">"+vbCrLf+_
					"<INPUT TYPE = ""CHECKBOX"" id = ""P092_ID"" NAME = ""P092"" CHECKED>&nbsp ������ 0,92P����.<BR>"+vbCrLf+_
					"<INPUT TYPE = ""CHECKBOX"" id = ""P08_ID"" NAME = ""P08"" CHECKED>&nbsp ������ 0,8P����.<BR>"+vbCrLf+_
				"</TD></TR>"+vbCrLf+_
				"<TR><TD>�������� P � ����:</TD>"+vbCrLf+_
					"<TD>ip"+vbCrLf+_
					"<INPUT TYPE = ""radio"" id = ""CONTR_PIP"" NAME = ""controlP"" VALUE = ""ip"" CHECKED></TD>"+vbCrLf+_
					"<TD>&nbsp iq"+vbCrLf+_
					"<INPUT TYPE = ""radio"" id = ""CONTR_PIQ"" NAME = ""controlP"" VALUE = ""iq""></TD>"+vbCrLf+_
				"</TR>"+vbCrLf+_
				"</TABLE>"+vbCrLf+_
				"<INPUT TYPE = ""CHECKBOX"" id = ""PIZAD_ID"" NAME = ""PIZAD"" CHECKED>&nbsp ������ P(I���.)<BR>"+vbCrLf+_
				"<HR>"+vbCrLf+_
				"<INPUT TYPE = ""radio"" id = ""UTQ_ID"" NAME = ""ut"" onClick = ""tiput(this);"" VALUE = ""2"">"+vbCrLf+_
				"<LABEL STYLE = ""text-align: Left; font-weight:bold"">���������� �� Q</LABEL>"+vbCrLf+_
				"<BR>"+vbCrLf+_
				"<LABEL STYLE = ""text-align: Left"">��������� �������:</LABEL>"+vbCrLf+_
				"<BR>"+vbCrLf+_
				"<LABEL><INPUT TYPE = ""CHECKBOX"" id = ""KVESQ_ID"" NAME = ""KVESQ"" CHECKED DISABLED>&nbsp ������ K��� �� Q</LABEL><BR>"+vbCrLf+_
				"<LABEL><INPUT TYPE = ""CHECKBOX"" id = ""UTONLYQ_ID"" NAME = ""UTONLYQ"" CHECKED DISABLED>&nbsp ��������� �� Q</LABEL><BR>"+vbCrLf+_
				"<HR>"+vbCrLf+_
				"<INPUT TYPE = ""radio"" id = ""UTPMIN_ID"" NAME = ""ut"" onClick = ""tiput(this);"" VALUE = ""3"">"+vbCrLf+_
				"<LABEL STYLE = ""text-align: Left; font-weight:bold"">����������� �� P</LABEL>"+vbCrLf+_
				"<BR>"+vbCrLf+_
				"<LABEL STYLE = ""text-align: Left"">��������� �������:</LABEL>"+vbCrLf+_
				"<BR>"+vbCrLf+_
				"<LABEL><INPUT TYPE = ""CHECKBOX"" id = ""UTQMIN_ID"" NAME = ""UTQMIN"" CHECKED DISABLED>&nbsp ���������� �� Q</LABEL><BR>"+vbCrLf+_
				"<LABEL><INPUT TYPE = ""CHECKBOX"" id = ""KVESMIN_ID"" NAME = ""KVESMIN"" CHECKED DISABLED>&nbsp ������ K��� �� P</LABEL><BR>"+vbCrLf+_
				"<LABEL><INPUT TYPE = ""CHECKBOX"" id = ""PMIN_ID"" NAME = ""PMIN"" CHECKED DISABLED>&nbsp ������ Pmin</LABEL><BR>"+vbCrLf+_
				"<HR>"+vbCrLf+_
				"<LABEL STYLE = ""text-align: Center"">�������� � �������:</LABEL><BR>"+vbCrLf+_
				"<button id = ""butt_load_ID"" NAME = ""butt_load"" onClick = ""onBtnLoad()"">���������</button><LABEL>&nbsp</LABEL>"+vbCrLf+_
				"<button id = ""butt_save_ID"" NAME = ""butt_save"" onClick = ""onBtnSave()"">���������</button>"+vbCrLf+_
				"<br>"+vbCrLf+_
				"<LABEL><INPUT TYPE = ""CHECKBOX"" id = ""SAVE_ID"" NAME = ""SAVE_RESULT"" CHECKED>&nbsp ��������� ����������</LABEL><BR>"+vbCrLf+_
				"<HR>"+vbCrLf+_
				"<P ALIGN = ""left"">"+vbCrLf+_
					"<button id = ""butt_start_ID"" NAME = ""butt_start"" onClick = ""onBtnOk()"">������</button><LABEL>&nbsp&nbsp&nbsp&nbsp</LABEL>"+vbCrLf+_
					"<button id = ""butt_exit_ID"" NAME = ""butt_exit"" onClick = ""onBtnCancel()"">�����</button>"+vbCrLf+_
				"</P>"+vbCrLf+_
				"<P ALIGN = ""center"">"+vbCrLf+_
					"<LABEL ID = ""ISX""></LABEL>"+vbCrLf+_
				"</P>"+vbCrLf+_
			"</ForM>"+vbCrLf+_
		"</body>"+vbCrLf+_
	"</html>"

	Set obj_IE = CreateObjectEx("InternetExplorer.Application","g_IE_")

	obj_IE.TheaterMode = FALSE
	obj_IE.Left      = 250   '���������� �������� ������ ���� ���� IEx
	obj_IE.Top       = 0   '���������� ����� ���� IE
	obj_IE.Height    = 970   '������ ���� IE
	obj_IE.Width     = 310 '������ ���� IE
	obj_IE.MenuBar   = FALSE '��� ���� IE
	obj_IE.ToolBar   = FALSE '��� ������� IE
	obj_IE.StatusBar = FALSE '��� ������ ��������� IE
	obj_IE.Resizable = FALSE
	obj_IE.Navigate  "about:blank"

	'�������� ���� IE �� �����������
	DO While ( obj_IE.Busy )
		SLEEP 100
	LOOP
	obj_IE.Document.Write (htmlDialog)
	obj_IE.Visible = True
	g_Quit = FALSE

	For k = 1 TO 2 STEP 0        ' �������� ������� ����� �� ����� Internet Explorer
		If g_Quit =  TRUE  THEN
			EXIT For
		End If

		If(obj_IE.document.MyForm.ButtonPressed.Value  = "2") THEN '���� ������ ������ �����, �� ����������� �����
			g_Quit =  TRUE
			EXIT For
		End If

		If(obj_IE.document.MyForm.ButtonPressed.Value  = "1") THEN '���� ������ ������ ������, �� ����������� ������� ��������� � ����������� ������
			ip = obj_IE.document.MyForm.IP.value     '����� ���� ������ �����
			iq = obj_IE.document.MyForm.IQ.value     '����� ���� ����� �����
			np = obj_IE.document.MyForm.NP.value     '����� �������������� �����
			Izad = cInt(obj_IE.document.MyForm.Izad.value) '�������� ���������� ��� �������������� �����

			Setlocale("ru-RU")
			on error resume next
			znch = cDbl(obj_IE.document.MyForm.ZNCH.value) '���� ����������������� ��� �� ��� ���������� �� Q (���� �� �������)
			If err.number = 13 then
				msgbox err.Description
				exit sub
			End If

			 '���������� ����������� ����������
			For i = 0 to obj_IE.document.getElementsByName("ddd").length-1
				If obj_IE.document.getElementsByName("ddd")(i).checked then
					directP = cInt(obj_IE.document.getElementsByName("ddd")(i).value)
				End If
			next

			'���������� ����� �������� P ��� �������������
			For i = 0 to obj_IE.document.getElementsByName("controlP").length - 1
				If obj_IE.document.getElementsByName("controlP")(i).checked then
					control_P = obj_IE.document.getElementsByName("controlP")(i).value
				End If
			next

			'���������� ��������� ���� ��� �������
			For i = 0 to obj_IE.document.getElementsByName("ut").length - 1
				If obj_IE.document.getElementsByName("ut")(i).checked then
					Block_R = obj_IE.document.getElementsByName("ut")(i).value
				End If
			next

			'��������� ���� �1
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

			'��������� ���� �2
			'���������� ������� ������� ������������� �� Q ��� ���������� �� Q
			If obj_IE.document.getElementById("KVESQ_ID").checked then
				Raschet_KVESQ = true
			else
				Raschet_KVESQ = false
			End If

			'���������� ������� ������� ������������� �� Q ��� ���������� �� Q
			If obj_IE.document.getElementById("UTONLYQ_ID").checked then
				Raschet_UTONLYQ = true
			else
				Raschet_UTONLYQ = false
			End If

			'��������� ���� �3
			'���������� ���������� �� Q ��� ������� ������������ ������
			If obj_IE.document.getElementById("UTQMIN_ID").checked then
				Raschet_QMIN = true
			else
				Raschet_QMIN = false
			End If

			'������ ������� ������������� �� P ��� ������� ������������ ������
			If obj_IE.document.getElementById("KVESMIN_ID").checked then
				Raschet_KVESMIN = true
			else
				Raschet_KVESMIN = false
			End If

			'���������� ���������� �� P � ����������� ������
			If obj_IE.document.getElementById("PMIN_ID").checked then
				Raschet_PMIN = true
			else
				Raschet_PMIN = false
			End If

			'���� �������� � ���������� ������ � �����������
			If obj_IE.document.getElementById("SAVE_ID").checked then
				file_save = true
			else
				file_save = false
			End If
			g_Quit =  TRUE

			'/////   �������� ������   ////////////
			kod_regima = "p"
			Rastr.LogEnable = false
			Rastr.LockEvent = true
			sha_rg2 = "�����.rg2"
			sha_ut2 = "���������� ����������.ut2"
			sha_Ktves = "������� ������������ ���������������.ves"
			kPut = directP '�����������,������������ ����������� ���������� �� P: ������ ������� ip----->iq.....kPut = -1, ip<-----iq.....kPut = 1
			kQut = directP '�����������,������������ ����������� ���������� �� Q: ������ ������� ip----->iq.....kQut = -1, ip<-----iq.....kQut = 1
			branch = "ip = " & ip & "& iq = " & iq & "& np = " & np '�������������� �����

			'��������� �����:
			'***************************************************************************************
			'***************************************************************************************
			'***************************************************************************************
			'Raschet_k_ves = true   '������ ������� ������������� ��� ������ ���������� ����������
			'Raschet_P_pred = true      '����������� ����������� �������� ��������
			'Raschet_P092 = false   '������ ������ � P = 0.92*P����
			'Raschet_P08 = false         '������ ������ � P = 0.8*P����
			'Raschet_I = false           '������ ������ � ���������, �������������� Izad
			'***************************************************************************************
			'***************************************************************************************
			'***************************************************************************************
			'������������� ������������ ����� �������� ��� ������� �� ������ 100

			Set Regim_Set = rastr.tables("com_regim")
			Regim_Set.cols("it_max").Z(0) = 100

			If file_save then
				dir_1 = Rastr.SEndCommandMain(13,"������� ������� ��� ���������� ������:","",0)  '����������, ���� ��������� ������
				prdir = Rastr.SEndCommandMain(3,"","",0) ' ���������� � Rastr
				shabl_rg2 = prdir & "SHABLON\" & sha_rg2
				shabl_ut2 = prdir & "SHABLON\" & sha_ut2
				shabl_ves = prdir & "SHABLON\" & sha_Ktves
			End If

			If dir_1 = "" then
				rastr.printp "������� ��� ���������� �� ������, ������� ����������� ��� ��������������� ����������"
				file_save = false
			End If

			StartTime = Timer
			dopname = day(Now) & month(Now)& hour(Now)& minute(Now)

			Select Case Block_R
				Case 1
					If Raschet_k_ves then
						obj_IE.Document.getElementById("ISX").innerHTML = "������ Kves"

						Call Raschet_Kves(branch,kPut)

						If file_save then
							Rastr.Save dir_1 & "\���������� ����������_" & dopname & ".ut2",shabl_ut2
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
						 '����� ��������������� � ������������ �������� ��������� ���
						Call Trans_RPN()

						obj_IE.Document.getElementById("ISX").innerHTML = "������ P����"

						Call Poisk_Ppred(branch,kQut,znch)

						If file_save then
							Rastr.Save dir_1 & "\���������� �����_" & dopname & ".rg2",shabl_rg2
							Rastr.Save dir_1 & "\���������� ����������_" & dopname & ".ut2",shabl_ut2
							Rastr.Save dir_1 & "\���������� ����������_" & dopname & ".ves",shabl_ves
						End If
					End If

					file_zagr_rg2 = Rastr.SEndCommandMain(6,sha_rg2,"",0)  '���� � ������������ ����� *.rg2
					file_zagr_ut2 = Rastr.SEndCommandMain(6,sha_ut2,"",0)  '���� � ������������ ����� *.ut2

					Set tvetv = Rastr.Tables("vetv")

					Call tvetv.Setsel(branch)

					vetv_pos = tvetv.FindNextSel(-1)

					Raschet_I0 = true '������ ���� �� �������� � ���������� (��������) ������
					 '���� � ����������(��������) ������ ��� �� ��������������� �������� ������ Izad, �� ������ ������ � ����� �� ��������, ������ �� �������� I��.���. �� ��������������
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
						obj_IE.Document.getElementById("ISX").innerHTML = "������ 0,92P����"
						Rastr.printp "������ ������ � ��������� �� �������� 0,92*P����."
						Rastr.printp "��������� �������� �������� " & P092 & "+/- 1 ���"

						Call Poisk_P1(branch, P092, kPut, control_P)

						If file_save then Rastr.Save dir_1 & "\����� 092P����_" & dopname & ".rg2",shabl_rg2
					End If

					If Raschet_P08 then
						obj_IE.Document.getElementById("ISX").innerHTML = "������ 0,8P����"
						Rastr.printp("������ ������ � ��������� �� �������� 0,8*P����.")
						Rastr.printp("��������� �������� �������� " & P08 & "+/- 1 ���")

						Call Poisk_P1(branch,P08,kPut,control_P)

						If file_save then Rastr.Save dir_1 & "\����� 08P����_" & dopname & ".rg2",shabl_rg2
					End If

					If Raschet_I Then
						If not Raschet_I0 then
							msgbox "� ����������(��������) ������ ��� �� �������� ������ ���������."
						Else
							obj_IE.Document.getElementById("ISX").innerHTML = "������ P(I���.)"
							If Flow_I(vetv_pos) > Izad then
								Rastr.printp "������ ������ � ����� �� ��������, ������ �� �������� I��.���."
								Call Poisk_I1(branch,Izad)
							Else
								Rastr.Load 1, file_zagr_rg2, shabl_rg2
								Rastr.Load 1, file_zagr_ut2, shabl_ut2

								Rastr.printp "�������� �����: " & file_zagr_rg2
								Rastr.printp "��������� ���������� ����������: " & file_zagr_ut2
								Rastr.printp "������ ������ � ����� �� ��������, ������ �� �������� I��.���."

								Call Poisk_I1(branch,Izad)

							End If
						End If

						If file_save then Rastr.Save  dir_1 & "\����� I_" & dopname & ".rg2", shabl_rg2
					End If

				Case 2
					Call Trans_RPN()

					Call Trans_Ut(branch,kQut,znch,Raschet_KVESQ,Raschet_UTONLYQ)

					If file_save then
						Rastr.Save dir_1 & "\Q_�����_" & dopname & ".rg2",shabl_rg2
						Rastr.Save dir_1 & "\������� ������������ ��_" & dopname & ".ves",shabl_ves
					End If

				Case 3
					Call MinRegim(branch, kPut, kQut, znch, Raschet_QMIN, Raschet_KVESMIN, Raschet_PMIN, obj_IE)

					If file_save then
						Rastr.Save dir_1 & "\Pmin_�����_" & dopname & ".rg2",shabl_rg2
						Rastr.Save dir_1 & "\������� ������������ ��_" & dopname & ".ves", shabl_ves
						Rastr.Save dir_1 & "\���������� ����������_" & dopname & ".ut2", shabl_ut2
					End If
			End Select

			EndTime = Timer
			MsgBox "����������� �� ������ �����: " & (EndTime-StartTime)/60 & " �����"
			Rastr.LogEnable = true
			Rastr.LockEvent = false
			Rastr.SEndChangeData 0,"","",0
		End If

		 '\\\\\\\\\\\\\\\\\\\\\ ������ ������ ��������� //////////////////
		If(obj_IE.document.MyForm.ButtonPressed.Value  = "3") THEN    '���� ������ ������ ���������, �� �������� ���� ��������
			File_Set = Rastr.SEndCommandMain(1,"�������� ���� � �����������","",0)
			If File_Set <> "" then
				Set fso = CreateObject("Scripting.FileSystemObject")
				'������ �� �����
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

				'���������� ����������� ���������� � ��������� � �����
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

		'///// ������ ������ ��������� //////////////////////////
		If(obj_IE.document.MyForm.ButtonPressed.Value  = "4") THEN  '���� ������ ������ ���������, �� ��������� ���������� �� ���� � ���������� � ����
			ip = obj_IE.document.MyForm.IP.value
			iq = obj_IE.document.MyForm.IQ.value
			np = obj_IE.document.MyForm.NP.value
			i_zad = obj_IE.document.MyForm.Izad.value

			'���������� ����������� ����������
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
				 '������ � ����
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
	'��������� ������ � IE
	obj_IE.Quit
	Set obj_IE = NOTHING
End Sub

'////////////////////////////////////����� � ����������� ���������/////////////////////////////////////////////////
Sub MinRegim(branch, kPut0, kQut, znch, option1,option2,option3,obj_IE) 'option1-���������� �� Q,option2-������ ������� ������������� �� P,option3- ���������� �� P
	Pzad = 1 * kPut0 '��������� ������� P �� ����� � ����������� ������
	If option1 then
		'������� ���������� ���������� �� Q ����� ��������� ������ �� �������������������
		Trans_RPN
		obj_IE.Document.getElementById("ISX").innerHTML = "���������� �� Q"
		Trans_Ut branch,kQut,znch,true,true
	End If

	Set tvetv = Rastr.Tables("vetv")
	tvetv.Setsel(branch)
	vetv_pos = tvetv.FindNextSel(-1)

	'���������� �������� ������� P �� �����: � ����������� �� ���������� ����������� �������� P �� �������� ����� ����� �������� �������� ���� � ������ �����, ���� � �����
	If kPut0 = 1 then P0 = Flow_Piq(vetv_pos)  '������� P � ����� �����
	If kPut0 = -1 then P0 = Flow_Pip(vetv_pos) ' ������� P � ������ �����
		'�������� ������ ������� ������������� �� P ������ �� ������������ �������� �� ����� � ���������� ����������� ����������
	If (kPut0 = -1 And P0<Pzad) then kPut = 1
	If (kPut0 = -1 And P0>Pzad And sgn(Pzad)<>sgn(P0)) then kPut = -1
	If (kPut0 = -1 And P0>Pzad And sgn(Pzad) = sgn(P0)) then kPut = 0
	If (kPut0 = 1 And P0>Pzad) then kPut = -1
	If (kPut0 = 1 And P0<Pzad And sgn(Pzad)<>sgn(P0)) then kPut = 1
	If (kPut0 = 1 And P0<Pzad And sgn(Pzad) = sgn(P0)) then kPut = 0

	If option2 then
		'������ ������� ������������ ������ �� ������������ � ���������� ����������� �������� P
		obj_IE.Document.getElementById("ISX").innerHTML = "������ K��� �� P"
		Raschet_Kves branch,kPut
	End If
	If option3 then
	'�������� ���������� ��� ���������� ������������ �������� �� ��������
	obj_IE.Document.getElementById("ISX").innerHTML = "������ Pmin"
	Set trut = Rastr.Tables("Traektory_ut")
	trut.Cols("Uchastie").Calc("0")
	trut.Cols("rashojdenie").Calc("0")
	trut.Cols("n_shaga").Calc("0")
	shag = 0
	'���� ���������� �� �������
	FLAG_ut = true 'TRUE ��������� ���������� ��� ����������, FALSE-����� �� ����� ����������

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
							rastr.printp "����� �� ��������!!! ���������� ���� ���������"
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
							rastr.printp "����� �� ��������!!! ���������� ���� ���������"
							trut.cols("rashojdenie").Z(ut_pos) = 1
						End If
						trut.cols("Uchastie").Z(ut_pos) = 1
						trut.cols("n_shaga").Z(ut_pos) = shag
						shag = shag + 1
					End If

				Case 2 '����� ��������� ���������� ������ ����������� ����������
					on Error Resume Next
					trut.SetSel("Uchastie = 0")
					ut_pos = trut.FindNextSel(-1)
					If trut.cols("kod_ut").Z(ut_pos) = 1 then kod_d = 10
					If trut.cols("kod_ut").Z(ut_pos) = 2 then kod_d = 11
					If trut.cols("kod_ut").Z(ut_pos) = 3 then kod_d = 21
					result = shag_ut(trut.cols("Num").Z(ut_pos), kod_d, 0)
					If result<>0 then
						rastr.printp "����� �� �������� ��� ������������������ ����������"
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