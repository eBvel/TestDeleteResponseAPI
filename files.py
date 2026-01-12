

class FileManager:
    @staticmethod
    def write(file_path, data, encoding = "UTF-8"):
        try:
            with open(file_path, 'w', encoding=encoding) as file:
                file.write(data)
        except FileNotFoundError as e:
            print(f"ERROR: File not found. \n{e}")

    @staticmethod
    def write_list(file_path, data, encoding = "UTF-8"):
        try:
            # Перед записью, отчищаем содержимое файла.
            FileManager.write(file_path, "")
            with open(file_path, 'a', encoding=encoding) as file:
                for line in data:
                    file.write(f"{line}\n")
        except FileNotFoundError as e:
            print(f"ERROR: File not found. \n{e}")

    @staticmethod
    def read_line_by_line(file_path, encoding = "UTF-8"):
        try:
            result = []
            with open(file_path, 'r', encoding=encoding) as file:
                for line in file:
                    result.append(line.strip())
            return result
        except FileNotFoundError as e:
            print(f"ERROR: File not found. \n{e}")
            return None