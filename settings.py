def _init():
    global folder_name_file_ext
    # Сортування за замовчуванням. 
    #Якщо хочете додати якийсь тип для сортування файлів додайте його у folder_name_file_ext у вигляді --- "ІМ'Я ПАПКИ КУДИ ПЕРЕМІЩАТИМУТЬСЯ ФАЙЛИ":('.РОЗШИРЕННЯ ЯКЕ ПОТРІБНО ПЕРЕМІСТИТИ')
    #НАПРИКЛАД: 'video': ('.avi', '.mp4', '.mov', '.mkv')
    folder_name_file_ext = {
    'audio': ('.mp3', '.ogg', '.wav', '.amr'),
    'video': ('.avi', '.mp4', '.mov', '.mkv'),
    'images': ('.jpeg', '.png', '.jpg', '.svg'),
    'documents': ('.doc', '.docs', '.txt', '.pdf', '.xlsx', '.pptx'),
    'archives': ('.zip', '.gz', '.tar')
}