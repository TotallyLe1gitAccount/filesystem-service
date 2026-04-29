import os

class BaseFileService:
    """Базовый класс с общими операциями для работы с файлами"""

    def __init__(self, file_path): 
        self.path = os.fspath(file_path)
        self._validate_path() 

    def __str__(self):
        return f"BaseFileService (path={self.path})"
    
    def exists(self):
        """Возвращает True если путь к файлу существует, False в противном случае"""
        return os.path.exists(self.path)
    
    def delete(self):
        """Удаляет файл"""
        if not self.exists():
            raise FileNotFoundError(f"File not found: {self.path}")
        os.remove(self.path)

    def _validate_path(self):
        """Проверяет путь на правильность"""
        if not isinstance(self.path, (str, os.PathLike)):
            raise TypeError("Path must be a str or path")
        
    def _ensure_exists(self):
        """Проверяет путь на существование"""
        if not self.exists():
            raise FileNotFoundError (f"file not found: {self.path}")
