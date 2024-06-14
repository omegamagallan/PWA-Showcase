from dataclasses import dataclass
import os


@dataclass
class Data:
    def __init__(self, static_folder):
        self.static_folder = static_folder
        self.key = "secret_key_224jlsdf924fhasf823"
        self.plotly_default_code = self.get_txt_file('default_code.txt')

    def get_txt_file(self, file_path: str):
        absolute_file_path = os.path.join(self.static_folder, file_path)
        if os.path.exists(absolute_file_path):
            with open(absolute_file_path, 'r') as file:
                return file.read()
