import os 
import pickle

class BaseFileService:
    """Базовый класс с общими операциями для работы с файлами"""

    def __init__(self, file_path):
        self.path = file_path

    def __str__(self):
        return f"BaseFileService (path={self.path})"
    
    def exists(self):
        """Возвращает True если путь к файлу существует, False в противном случае"""
        return os.path.exists(self.path)
    
    def delete(self):
        """Удаляет файл"""
        if self.exists():
            os.remove(self.path)


class FileService(BaseFileService):
    """Класс, работающий с файлами"""
    def __init__(self, file_path):
        super().__init__(file_path)

    
    def read_file(self):
        """Чтение файла"""
        try:
            with open(self.path, 'r', encoding='UTF-8') as f:
                return f.read()
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found: {self.path}") from e


    def write_text(self, text, mode="w"):
        """Записывает текст в файл"""
        with open(self.path, mode, encoding="UTF-8") as f:
        
            if isinstance(text, str):
                f.write(text)
            
            elif isinstance(text, list):
                f.write("\n".join(map(str, text)))

            else:
                raise TypeError("Unsupported type")
            

class BinaryFileService(BaseFileService):
    """Класс работающий с бинарной информацией файла"""
    def __init__(self, file_path):
        super().__init__(file_path)

    def read_bytes(self) -> bytes:
        """Читает бинарный файл"""
        with open(self.path, "rb") as f:
            return f.read()
        
    def write_bytes(self, data : bytes, mode="wb"):
        """Записывает байты"""
        with open(self.path, mode) as f:
            f.write(data)

    def size(self) -> int:
        """Возвращает размер файла"""
        return os.path.getsize(self.path)
    
    def read_chunks(self, chunk_size=4096):
        """Читает файл кусками"""
        with open(self.path, "rb") as f:
            while chunk := f.read(chunk_size):
                yield chunk

class SerializationService(BaseFileService):
    """Класс для сериализации файла"""
    def __init__(self, file_path):
        super().__init__(file_path)

    def serialize(self, obj):
        with open(self.path, "wb") as f:
            pickle.dump(obj, f)
    
    def deserialize(self):
        with open(self.path, "rb") as f:
            return pickle.load(f)
            
        
    

                









