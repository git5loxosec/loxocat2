import os

class FileHandler:
    @staticmethod
    def file_exists(file_path):
        return os.path.exists(file_path)

    @staticmethod
    def read_file(file_path):
        if FileHandler.file_exists(file_path):
            with open(file_path, 'r') as file:
                return file.read().strip()
        else:
            return ""

    @staticmethod
    def write_file(file_path, content):
        with open(file_path, 'w') as file:
            file.write(content)
