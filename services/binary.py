import os
from .base import BaseFileService
from .constraints import VALID_BINARY_MODES

class BinaryFileService(BaseFileService):
    """Класс работающий с бинарной информацией файла"""
    def __init__(self, file_path):
        super().__init__(file_path)

    def read_bytes(self) -> bytes:
        """Читает бинарный файл"""
        self._ensure_exists()
        with open(self.path, "rb") as f:
            return f.read()
        
    def write_bytes(self, data : bytes, mode="wb"):
        """Записывает байты"""
        if mode not in VALID_BINARY_MODES:
            raise ValueError(f"Invalid mode: {mode}")
        
        if not isinstance(data, (bytes, bytearray)):
            raise TypeError("data must be bytes or bytearray")
        with open(self.path, mode) as f:
            f.write(data)

    def size(self) -> int:
        """Возвращает размер файла"""
        self._ensure_exists()
        return os.path.getsize(self.path)
    
    def read_chunks(self, chunk_size=4096):
        """Читает файл кусками"""
        if not isinstance(chunk_size, int) or chunk_size <= 0:
            raise ValueError("chunk_size must be positive integer")
        with open(self.path, "rb") as f:
            while chunk := f.read(chunk_size):
                yield chunk
