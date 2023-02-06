# (ENG) FILE SORTER SCRIPT 

## What does it do? / Що він виконує?
1. The script goes through the folder specified during the call and sorts all files into groups:

    By default, these are the following groups:

    images ('JPEG', 'PNG', 'JPG', 'SVG');
    video files ('AVI', 'MP4', 'MOV', 'MKV');
    documents ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
    music ('MP3', 'OGG', 'WAV', 'AMR');
    archives ('ZIP', 'GZ', 'TAR');
    unknown extensions

     You can add your own use case here by modifying the **settings.py** file. If you 
     want to add some type for sorting files, add it to **CATEGORIES** in the form --- 
      `"FOLDER NAME WHERE FILES WILL BE MOVED TO":('.EXTENSION TO BE MOVED TO')`.
     FOR EXAMPLE: `'video': ('.avi', '.mp4', '.mov', '.mkv')`

2. Performs transliteration of the Cyrillic alphabet into Latin. Replaces all characters except Latin letters, numbers and '.' with '_'.

3. Deletes folders that are/became empty.

## Usage

    Open the folder where you saved this script and from this folder run the command line in a comma and run the following command `py file_sorting.py {}`. 
`{}` -  is the path to the folder where the script should run. For example: `py file_sorting.py C:\Users\Admin\Desktop\Хлам`

**NOTE!!!** 

    DO NOT USE IT ON FOLDERS LIKE THIS: `['windows', 'program files', 'bin', 'lib', 'etc', 'applications']`.


# (UA) СКРИПТ ДЛЯ СОРУВАННЯ ФАЙЛІВ

1. Скрипт переглядає папку, вказану під час виклику, і сортує всі файли за групами:

    За замовчування це наступні групи:

    зображення ('JPEG', 'PNG', 'JPG', 'SVG');
    відеофайли ('AVI', 'MP4', 'MOV', 'MKV');
    документи ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
    музика ('MP3', 'OGG', 'WAV', 'AMR');
    архіви ('ZIP', 'GZ', 'TAR');
    невідомі розширення

     Ви можете додати сюди свій сценарій використання змінивши файл **settings.py**. Якщо 
     хочете додати якийсь тип для сортування файлів додайте його у **CATEGORIES** у 
     вигляді --- `"ІМ'Я ПАПКИ КУДИ ПЕРЕМІЩАТИМУТЬСЯ ФАЙЛИ":('.РОЗШИРЕННЯ ЯКЕ ПОТРІБНО 
     ПЕРЕМІСТИТИ')`.
     НАПРИКЛАД: `'video': ('.avi', '.mp4', '.mov', '.mkv')`

2. Здійснює транслітерацію кирилиці в латиницю.Замінює всі символи, крім латинських літер, цифр і "." на '_'.

3. Видаляє папки які є/стали порожніми

## Використання 

    Відкрийте папку, куди ви зберегли цей скріпт  і з цієї папки запустіть командний рядок у якому викличте таку команду `py file_sorting.py {}`.
`{}` - це хлях до теки у якій повинен працювати скріпт. Наприклад: `py file_sorting.py C:\Users\Admin\Desktop\Хлам`

**ПРИМІТКА!!!** 
    НЕ ВИКОРИСТОВУЙТЕ ЙОГО ДЛЯ ПАПОК ПО ТИПУ ТАКИХ ЯК: `['windows', 'program files', 'bin', 'lib', 'etc', 'applications']`.


