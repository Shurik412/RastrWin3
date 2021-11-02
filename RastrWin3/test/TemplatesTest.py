from RastrWin3.Templates import ROOT_DIR_SHABLON


dir = ROOT_DIR_SHABLON()

print(dir.directory_shabl(russian_name_shabl='динамика',
                          location_of_files=dir.LOCATION_FOLDER_DOCUMENTS))

print(dir.directory_shabl(russian_name_shabl='режим',
                          location_of_files=dir.LOCATION_FOLDER_DOCUMENTS))

print(dir.directory_shabl(russian_name_shabl='',
                          location_of_files=dir.LOCATION_FOLDER_DOCUMENTS))

print(dir.directory_shabl(russian_name_shabl='динамика',
                          location_of_files=dir.LOCATION_SCRIPT))

print(dir.directory_shabl(russian_name_shabl='режим',
                          location_of_files=dir.LOCATION_SCRIPT))

print(dir.directory_shabl(russian_name_shabl='',
                          location_of_files=dir.LOCATION_SCRIPT))

print(dir.directory_shabl(russian_name_shabl='динамика',
                          location_of_files=dir.LOCATION_ROOT_FOLDER_RASTR))

print(dir.directory_shabl(russian_name_shabl='режим',
                          location_of_files=dir.LOCATION_ROOT_FOLDER_RASTR))

print(dir.directory_shabl(russian_name_shabl='',
                          location_of_files=dir.LOCATION_ROOT_FOLDER_RASTR))