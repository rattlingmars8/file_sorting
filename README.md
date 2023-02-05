# FILE SORTER SCRIPT / СКРІПТ ДЛЯ СОРУВАННЯ ФАЙЛІВ

## What does it do? / Що він виконує?

The script goes through the folder specified during the call and sorts all files into groups:

images ('JPEG', 'PNG', 'JPG', 'SVG');
video files ('AVI', 'MP4', 'MOV', 'MKV');
documents ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
music ('MP3', 'OGG', 'WAV', 'AMR');
archives ('ZIP', 'GZ', 'TAR');
unknown extensions

Performs transliteration of the Cyrillic alphabet into Latin. Replaces all characters except Latin letters, numbers and '.' with '_'.


Скрипт переглядає папку, вказану під час виклику, і сортує всі файли за групами:

зображення ('JPEG', 'PNG', 'JPG', 'SVG');
відеофайли ('AVI', 'MP4', 'MOV', 'MKV');
документи ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
музика ('MP3', 'OGG', 'WAV', 'AMR');
архіви ('ZIP', 'GZ', 'TAR');
невідомі розширення

Здійснює транслітерацію кирилиці в латиницю.Замінює всі символи, крім латинських літер, цифр і "." на '_'.


## Usage / Використання 

Open the folder where you saved this script and from this folder run the command line in a comma and run the following command `py file_sorting.py {}`. 
`{}` -  is the path to the folder where the script should run 


Відкрийте папку, куди ви зберегли цей скріпт  і з цієї папки запустіть командний рядок у кому викличте таку команду `py file_sorting.py {}`.
`{}` - це хлях до теки у якій повинен працювати скріпт.

**NOTE!!! / ПРИМІТКА!!!** 
DO NOT USE IT ON FOLDERS LIKE THIS: `['windows', 'program files', 'bin', 'lib', 'etc', 'applications']`.

НЕ ВИКОРИСТОВУЙТЕ ЙОГО ДЛЯ ПАПОК ПО ТИПУ ТАКИХ ЯК: `['windows', 'program files', 'bin', 'lib', 'etc', 'applications']`.


