def read_txt_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().splitlines()
        return content
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."
    except IOError:
        return "Error: An error occurred while reading the file."

class UserExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file=read_txt_file(self.file_path)

    def extract_usernames(self):
        names=[]
        for i in self.file:
            names.append(i.split(":")[0])
        return names
# Usage example
if __name__ == "__main__":
    file_path =r'C:\Users\Kimo Store\Desktop\AMIT\advanced-Machine-Learning-Course-Amit\materials\python_for_ML\tasks\week_4\Test.text'
    u=UserExtractor(file_path)
    print(u.extract_usernames())