class TextFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.content = ""

    def write_file(self, content):
        with open(self.file_path, 'w') as file:
            file.write(content)
    
    def read_file(self):
        with open(self.file_path, 'r') as file:
            self.content = file.read()  
        return self.content       
     
    def count_lines(self):
        line_count = len(self.content.splitlines())
        return line_count

    def count_words(self):
        word_count = len(self.content.split())
        return word_count

    def count_characters(self):
        character_count = len(self.content)
        return character_count

    def display_statistics(self, line_count, word_count, character_count):
        print(f"Number of Lines: {line_count}")
        print(f"Number of Words: {word_count}")
        print(f"Number of Characters: {character_count}")


# Usage
if __name__ == "__main__":
    file_path = r"C:\Users\Kimo Store\Desktop\Count\Thema.txt"
    content = """As the sun dipped below the horizon, the sky transformed into a canvas of warm hues.
Shades of pink, orange, and violet stretched across the fading daylight, reflecting on the calm surface of the lake.
A gentle breeze stirred the trees along the shoreline, while distant sounds of birds settling for the night filled the air.
The world seemed to pause, enveloped in a quiet beauty that marked the end of another day, leaving a sense of peace and reflection in its wake."""

    # Create an instance of TextFile
    text_file = TextFile(file_path)
    
    # Write content to the file
    text_file.write_file(content)
    
    # Read content from the file
    text_file.read_file()
    
    # Calculate statistics
    line_count = text_file.count_lines()
    word_count = text_file.count_words()
    character_count = text_file.count_characters()
    
    # Display the statistics
    text_file.display_statistics(line_count, word_count, character_count)
    
   