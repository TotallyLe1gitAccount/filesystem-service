import pickle
from .base import BaseFileService

class SerializationService(BaseFileService):
    """Класс для сериализации файла"""
    def __init__(self, file_path):
        super().__init__(file_path)

    def serialize(self, obj):
        try:
            with open(self.path, "wb") as f:
                pickle.dump(obj, f)
        except pickle.PickleError as e:
            raise ValueError("Object is not serializable") from e
        
    def deserialize(self):
        self._ensure_exists()
        try:
            with open(self.path, "rb") as f:
                return pickle.load(f)
        except pickle.PickleError as e:
            raise ValueError("Failed to deserialize object") from e
        
    