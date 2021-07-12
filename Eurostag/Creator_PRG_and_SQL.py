# -*- coding: utf-8 -*-
import os
import shutil


def ReplaceLineInFile(fileName, sourceText, replaceText):
    # Открываем файл только для чтения
    f = open(fileName, 'r')
    text = f.read()
    f.close()
    file = open(fileName, 'w')
    file.write(text.replace(sourceText, replaceText))
    file.close()


def File_SEQ(dir_file_1, dir_file_2, number_regime, regime, Unom, PSS):
    dir_file_1 = dir_file_1 + '/' + 'SEQ.seq'
    for num in range(1, int(number_regime) + 1):
        file_2 = dir_file_2 + '/' + str(regime) + '_' + str(num) + '_' + str(PSS) + '_' + str(Unom) + 'kV' + '.seq'
        shutil.copyfile(dir_file_1, file_2)


def File_PRG(dir_file_1, dir_file_2, number_regime, regime, Unom, PSS):
    dir_file_1 = dir_file_1 + '/' + 'PRG.prg'
    for num in range(1, int(number_regime) + 1):
        file_2 = dir_file_2 + '/' + str(regime) + '_' + str(num) + '_' + str(PSS) + '_' + str(Unom) + 'kV' + '.prg'
        shutil.copyfile(dir_file_1, file_2)


dialog_1 = int(input("Вы хотите вывести файлы *.seq или *.prg (1-*.seq или 2-*.prg): "))

if dialog_1 == 1:
    print('Создайте файл (сценарий КЗ(3)) в Eurostag-e с названием файла "SEQ.seq".')
    print(
        'Данный файл будет использоваться для создания копий с названиями файлов в соответствии с рассматриваемыми режимами.')
    print(
        'Пример: 1_2_N_750kV.seq - 1 - Зима макс; 2 - откл ВЛ(в соответствии со списком режмов; N (No) или Y (Yes) - без PSS и с PSS.')
    print(
        '==============================================================================================================================')

    dir_file_1 = input("Ссылка на файл 1 *.seq (Пример: C:\\Users\\Александр\\Desktop\\77\\seq): ")
    dir_file_2 = input("Ссылка куда сохранить файлы *.seq (Пример: C:\\Users\\Александр\\Desktop\\77\\seq2): ")
    number_regime = int(input("Число режимов: "))
    regime = input("Номер режимов (Пример: Зима_макс=1;Зима_мин=2;Лето_макс=3;Лето_мин=4): ")
    PSS = input("с PSS или без PSS (Пример: Y или N, 0 - создаст все режимы с Y и N): ")
    Unom = input("Номинальное напряжение в точке КЗ(3) (Например: 750): ")

    dir_file_1 = dir_file_1.replace('\\', '/')
    dir_file_2 = dir_file_2.replace('\\', '/')

    if PSS == 0:
        for flag in range(1, 3):
            if flag == 1:
                PSS = 'Y'
                File_SEQ(dir_file_1, dir_file_2, number_regime, regime, Unom, PSS)
            if flag == 2:
                PSS = 'N'
                File_SEQ(dir_file_1, dir_file_2, number_regime, regime, Unom, PSS)
    elif PSS == 'Y':
        PSS = 'Y'
        File_SEQ(dir_file_1, dir_file_2, number_regime, regime, Unom, PSS)
    elif PSS == 'N':
        PSS = 'N'
        File_SEQ(dir_file_1, dir_file_2, number_regime, regime, Unom, PSS)
    print('Файлы сохранены в папке: ' + dir_file_2)

#########################################################################################################
elif dialog_1 == 2:
    print('Создайте файл (макрос вывода дынных по сетевым элементам) '
          'в Eurostag-e с названием файла "PRG.prg".')
    print(
        'Данный файл будет использоваться для создания копий с названиями файлов '
        'в соответствии с рассматриваемыми режимами.')
    print(
        'Пример: 1_2_N_750kV.prg - 1 - Зима макс; 2 - откл ВЛ(в соответствии со списком режмов; '
        'N (No) или Y (Yes) - без PSS и с PSS.')
    print('Открываем файл "PRG.prg" с помощью "Блокнота" и задаем следующие колонки: ')
    print('CASE_1_NAME=C:/03_LetoMaxKalinaNPP/PRG.red    => остается без изменений')
    print('CASE_1_IMPORT_ASCII=0     => остается без изменений')
    print(
        'CASE_1_EXPORT_ASCII=C:/03_LetoMaxKalinaNPP/PRG.exp  => '
        'копируем ссылку из CASE_1_NAME (выше) и выставляем с расширением *.exp')
    print('CASE_1_EXPORT_ASCII_START_TIME=45.000000')
    print('CASE_1_EXPORT_ASCII_END_TIME=80.000000 ')
    print('Далее - необходимо сохранить все изменения.')
    print('==============================================================='
          '===============================================================')

    dir_file_1_prg = input("Ссылка дир. файла (Пример:C:\\Users\\Александр\\Desktop\\77\\prg): ")
    regime_prg = input("Номер режима (Пример: Зима_макс=1; Зима_мин=2; Лето_макс=3; Лето_мин=4): ")
    number_regime_prg = input("Количество файлов (режимов): ")
    dir_file_2_prg = input("Ссылка куда сохранить файлы (Пример:C:\\Users\\Александр\\Desktop\\77\\prg2): ")
    Unom = input("Номинальное напряжение в точке КЗ(3) (Например: 750): ")

    link_One = input("Заменяема ССЫЛКА в *.prg (Что изменяем?): ")
    link_Two = input("ССЫЛКА расположения *.res файлов (На что?): ")

    dir_file_1_prg = dir_file_1_prg.replace('\\', '/')
    dir_file_2_prg = dir_file_2_prg.replace('\\', '/')
    link_One = link_One.replace('\\', '/')
    link_Two = link_Two.replace('\\', '/')

    dir_file_1 = dir_file_1_prg
    dir_file_2 = dir_file_2_prg
    regime = regime_prg
    number_regime = number_regime_prg
    for flag in range(1, 3):
        if flag == 1:
            PSS = str('Y')
            File_PRG(dir_file_1, dir_file_2, number_regime, regime, Unom, PSS)
        if flag == 2:
            PSS = str('N')
            File_PRG(dir_file_1, dir_file_2, number_regime, regime, Unom, PSS)

    print('Файлы сохранены в папке: ' + dir_file_2)

    for num in range(1, int(number_regime) + 1):
        for num_pss in range(1, 3):
            if num_pss == 1:
                PSS = str('Y')
                fileName = dir_file_2_prg + '/' + str(regime_prg) + '_' + str(num) + '_' + str(PSS) + '_' + str(
                    Unom) + 'kV' + '.prg'

                sourceText = link_One + '/' + 'PRG'
                replaceText = link_Two + '/' + str(regime_prg) + '_' + str(num) + '_' + str(PSS) + '_' + str(
                    Unom) + 'kV'

                ReplaceLineInFile(fileName, sourceText, replaceText)

            elif num_pss == 2:
                PSS = str('N')
                fileName = dir_file_2_prg + '/' + str(regime_prg) + '_' + str(num) + '_' + str(PSS) + '_' + str(
                    Unom) + 'kV' + '.prg'

                sourceText = link_One + '/' + 'PRG'
                replaceText = link_Two + '/' + str(regime_prg) + '_' + str(num) + '_' + str(PSS) + '_' + str(
                    Unom) + 'kV'

                ReplaceLineInFile(fileName, sourceText, replaceText)

print('================================================'
      '========================================================================')
print('Исследование завершено!')
