from services.base import BaseFileService
from services.file import FileService
from services.binary import BinaryFileService
from services.serialization import SerializationService


def display_file_info(file_path):
    with open(file_path, "r", encoding="UTF-8") as f:
        print("-" * 80)
        print(f"ИНФОРМАЦИЯ О ФАЙЛЕ:")
        print(f"Имя: {f.name}")
        print(f"режим: {f.mode}")
        print(f"кодировка: {f.encoding}")
        print(f"состояние: {f.closed}")
        print(f"класс: {f.__class__}")
        print(f"буфер: {f.buffer}")
        print(f"ошибки: {f.errors}")
        print(f.line_buffering)
        print(f.newlines)
        print("-" * 80)

#Создание пустого файла
file1 = FileService("data\\empty_file.txt")
file1.create_file()


#Вывод размер файла в байтах
file_bytes = BinaryFileService("data\\example_data.txt")

print(f"Размер файла в байтах = {file_bytes.size()}")

#Альтернативный способ (размер записи в файл в байтах)
with open("data\\empty_file.txt", "w+", encoding="UTF-8") as f:
    bytes = f.write("BPMN")
    print(f"Размер файла в байтах = {bytes}")

#Запись списка в файл
programming_languages = ['Python', 'Rust', 'C++', 'C#', 'Go', 'Ruby', 'F#', 'Java', 'JavaScript']

file2 = FileService("data\\languages.txt")
file2.write_text(programming_languages)

#Запись чисел 
file3 = FileService("data\\numbers_file.txt")

numbers = [i for i in range(1, 100)] 


method = input("как записать числа в файл? l - list comprehension, j - join: ")

# через list comprehension
if method.lower() == "l":
    str_numbers = [str(x) for x in numbers]
    file3.write_text(str_numbers)

    print("Готово")

#через join
elif method.lower() == "j":
    str_of_numbers = "\n".join(map(str, numbers))

    file3.write_text(str_of_numbers)

    print("Готово")

else:
    print("Неверный ввод.")


#Атрибуты файла
display_file_info("data\\example_data.txt")

#Чтение файла
file4 = FileService("data\\example_data.txt")
result = file4.read_file()

print(result)

#Получения списка строк из файла
with open("data\\example_data.txt", "r", encoding="UTF-8") as f:
    result_list = f.readlines()

print(result_list, ": ", result_list.__class__, "\n")

#Получение строки из файла до n-го символа
n = 10

with open("data\\example_data.txt", "r", encoding="UTF-8") as f:
    result_lines = f.readline(10)

print(result_lines, ": ", result_lines.__class__, "\n")

#Функции chr() и ord()

# ord: символ -> число (Unicode код)
print(ord('A'))   
print(ord('a'))   
print(ord('1'))   

# chr: число -> символ
print(chr(65))    
print(chr(97))    
print(chr(49))    

# мини-цикл (кодировка алфавита)
for i in range(65, 71):
    print(i, "->", chr(i))

#Создание бинарных файлов
with open("data\\bin_file.bin", "wb") as f:
    f.close()

#Запись байтов в файл
file_bin = BinaryFileService("data\\bin_file.bin")

data = b"BPMN"

file_bin.write_bytes(data)

#Положение указателя в бинарном файле
with open("data\\bin_file.bin", "rb") as f:
    f.read()
    print(f"Положение указателя: {f.tell()}")


#Чтение бинарного файла
print(file_bin.read_bytes())


#pickle сериализация

file_pickle = SerializationService("data\\user.pkl")

data = {
    "name": "Max",
    "age": 20,
    "languages": ["Python", "C++", "SQL"]
}

file_pickle.serialize(data)


#pickle десериализация
loaded_data = file_pickle.deserialize()

print("Восстановленные данные:")
print(loaded_data)
print(type(loaded_data))