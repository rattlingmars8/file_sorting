import os 
import shutil
import sys
from normalize import normalize # Імпорт функції нормалізації імені з іншого файлу
import settings #Імпорт налаштувань користувача для сортування файлів

settings._init() #Ініціалізація налаштувань

unknown_types = set()
known_types = set()
RESULT = []
    
SKIPDIRS = list(settings.folder_name_file_ext.keys())

#Нормалізація імен папок та файлів
def _normalize_items(FOLDER):
    for root, dirs, files in os.walk(FOLDER):
        dirs[:] = [dir for dir in dirs if dir not in SKIPDIRS]
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            new_name_dir = normalize(dir)
            new_path_dir = os.path.join(root, new_name_dir)
            os.rename(dir_path, new_path_dir)
            if os.path.isdir(new_path_dir):
                _normalize_items(new_path_dir)
        for file in files:
            for folder_name, extention in settings.folder_name_file_ext.items():
                file_ext = os.path.splitext(file)[-1]
                if file_ext in extention:
                    file_path = os.path.join(root, file)
                    new_name_file = normalize(file)
                    new_path_file = os.path.join(root, new_name_file)
                    os.rename(file_path, new_path_file)
                    known_types.add(file_ext)
                if file_ext not in extention:
                    unknown_types.add(file_ext)

#Видаляємо пусті папки. Запуск останнім!!!
def _del_empty_folder():
    for root, dirs, files in os.walk(FOLDER, topdown=False):
        dirs[:] = [dir for dir in dirs if dir not in SKIPDIRS]
        if not dirs and not files:
            print("Видаляю пусті папки....")
            os.rmdir(root)

#Основна функція сортування
def _sort_by_type(FOLDER):
    for root, dirs, files in os.walk(FOLDER):
        dirs[:] = [dir for dir in dirs if dir not in SKIPDIRS]
        for file in files:
            file_ext = os.path.splitext(file)[-1]
            path = next((folder_name for folder_name, extention in settings.folder_name_file_ext.items() if file_ext in extention), None)#Отримуєм ім'я папки зі словника з розширеннями файлів, відповідно до розширення
            ext = next((extention for folder_name, extention in settings.folder_name_file_ext.items() if file_ext in extention), None)#Отримуєм можливі розширення файлів зі словника з розширеннями файлів
            if ext is not None and file_ext in ext:
                print(f'Файл {file}, було переміщено у {os.path.join(FOLDER, path)}\n')
                RESULT.append(file)
            if path:
                if not os.path.exists(FOLDER+'/'+path):
                    os.mkdir(FOLDER +'/'+path)
                    shutil.move(os.path.join(root, file), FOLDER+'/'+path)
                else:
                    shutil.move(os.path.join(root, file), FOLDER+'/'+path)


#Розпаковка архівів
def _unpack_archive():
    for root_dir, sub_dir, files in os.walk(FOLDER+'/archives'):
        for archive in files:
            archive_ext = os.path.splitext(archive)[-1]
            if archive_ext in settings.folder_name_file_ext['archives']:
                filename = os.path.basename(archive)
                archive_file = FOLDER+'/archives/'+filename
                if not os.path.exists(FOLDER+'/archives'+'/'+filename.split('.')[0]):
                    os.mkdir(FOLDER+'/archives'+'/'+filename.split('.')[0])
                    dest_dir = FOLDER+'/archives'+'/'+filename.split('.')[0]
                    shutil.unpack_archive(archive_file, dest_dir)
                    print(f'Архів {archive}, було розпаковано в {dest_dir}\n')
                else:
                    pass


if __name__ == "__main__":
    FOLDER = sys.argv[1]
    if os.path.exists(FOLDER):
        try: 
            _normalize_items(FOLDER)
        except PermissionError:
            print(f"Закрийте головну папку - {FOLDER} для корректної роботи скрипта!!")
            pass
        else:
            _sort_by_type(FOLDER)
            _unpack_archive()
            if RESULT == []:
                print(f"Не було знайдено жодного підходящого файлу для сортування!\nПерелік НЕВІДОМИХ програмі розширень файлів: {unknown_types}")
            else:
                print(f"Перелік ВІДОМИХ програмі розширень файлів: {known_types}\nПерелік НЕВІДОМИХ програмі розширень файлів: {unknown_types.difference(known_types)}\n")
            _del_empty_folder()