from .base import BaseFileService
from .constraints import VALID_TEXT_MODES

class FileService(BaseFileService):
    """Класс, работающий с файлами"""
    def __init__(self, file_path):
        super().__init__(file_path)

    
    def read_file(self):
        """Чтение файла"""
        self._ensure_exists()

        with open(self.path, "r", encoding="UTF-8") as f:
            return f.read()
        
    def create_file(self):
        """Создание файла"""
        try:
            with open(self.path, "x", encoding="UTF-8") as f:
                f.write("")
        except FileExistsError:
            print("File already exists")



    def write_text(self, text, mode="w"):
        """Записывает текст в файл"""
        if mode not in VALID_TEXT_MODES:
            raise ValueError(f"Invalid mode: {mode}")
        
        with open(self.path, mode, encoding="UTF-8") as f:
        
            if isinstance(text, str):
                f.write(text)
            
            elif isinstance(text, list):
                f.write("\n".join(map(str, text)))

            else:
                raise TypeError("Unsupported type")