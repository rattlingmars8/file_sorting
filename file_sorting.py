import os 
import shutil
import sys
from normalize import normalize # Імпорт функції нормалізації імені з іншого файлу

folder_name_file_ext = {
    'audio': ('.mp3', '.ogg', '.wav', '.amr'),
    'video': ('.avi', '.mp4', '.mov', '.mkv'),
    'images':('.jpeg', '.png', '.jpg', '.svg'),
    'documents':('.doc', '.docs', '.txt', '.pdf', '.xlsx', '.pptx'),
    'archives':('.zip', '.gz', '.tar')
}

unknown_types = set()
known_types = set()

image_files = []
video_files = []
doc_files = []
audio_files = []
archive_files = []
    
skipdirs = ['audio', 'video', 'archives', 'documents', 'images']        

#Нормалізація імен папок та файлів
def _normalize_items(FOLDER):
    for root, dirs, files in os.walk(FOLDER):
        dirs[:] = [dir for dir in dirs if dir not in skipdirs]
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            new_name_dir = normalize(dir)
            new_path_dir = os.path.join(root, new_name_dir)
            os.rename(dir_path, new_path_dir)
            if os.path.isdir(new_path_dir):
                _normalize_items(new_path_dir)
        for file in files:
            for folder_name, extention in folder_name_file_ext.items():
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
        dirs[:] = [dir for dir in dirs if dir not in skipdirs]
        if not dirs and not files:
            print("Видаляю пусті папки....")
            os.rmdir(root)

#Основна функція сортування
def _sort_by_type(FOLDER):
    for root, dirs, files in os.walk(FOLDER):
        dirs[:] = [dir for dir in dirs if dir not in skipdirs]
        for file in files:
            file_ext = os.path.splitext(file)[-1]
            if file_ext in folder_name_file_ext['video']:
                video_files.append(file)
            if file_ext in folder_name_file_ext['images']:
                image_files.append(file)
            if file_ext in folder_name_file_ext['documents']:
                doc_files.append(file)
            if file_ext in folder_name_file_ext['audio']:
                audio_files.append(file)
            if file_ext in folder_name_file_ext['archives']:
                archive_files.append(file)
            path = next((folder_name for folder_name, extention in folder_name_file_ext.items() if file_ext in extention), None)#Отримуєм ім'я папки зі словника з розширеннями файлів, відповідно до розширення
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
            if archive_ext in folder_name_file_ext['archives']:
                filename = os.path.basename(archive)
                archive_file = FOLDER+'/archives/'+filename
                if not os.path.exists(FOLDER+'/archives'+'/'+filename.split('.')[0]):
                    os.mkdir(FOLDER+'/archives'+'/'+filename.split('.')[0])
                    dest_dir = FOLDER+'/archives'+'/'+filename.split('.')[0]
                    shutil.unpack_archive(archive_file, dest_dir)
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
            result = []
            if image_files != []:
                result.append(f"Зображення: {image_files}\n")
            if video_files != []:
                result.append(f"Відеофайли: {video_files}\n")
            if doc_files != []:
                result.append(f"Документи: {doc_files}\n")
            if archive_files != []:
                result.append(f"Архіви: {archive_files}\n")
            if audio_files != []:
                result.append(f"Аудіо: {audio_files}\n")
            if result != []:
                print("Переміщую файли у відповідні папки...")
                print(f"Було переміщено:\n{''.join(result)}")
                print(f"Перелік ВІДОМИХ програмі розширень файлів: {known_types}\nПерелік НЕВІДОМИХ програмі розширень файлів: {unknown_types.difference(known_types)}")
            else:
                print(f"Не було знайдено жодного підходящого файлу для сортування!\nПерелік НЕВІДОМИХ програмі розширень файлів: {unknown_types}")
            _del_empty_folder()