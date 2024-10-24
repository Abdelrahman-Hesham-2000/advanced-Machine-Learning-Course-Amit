input_file = open(r"C:\Users\Kimo Store\Desktop\AMIT\advanced-Machine-Learning-Course-Amit\materials\python_for_ML\session\test.text", "r")
def frequency(input_file):
 text = input_file.read()
 input_file.close()

 text = text.replace('\n', ' ')
 words = text.split(' ')

 unique_words = set(words)
 word_counts = dict()

 for word in unique_words:
    word_counts[word] = words.count(word)
    
 output_file = open(r"C:\Users\Kimo Store\Desktop\AMIT\advanced-Machine-Learning-Course-Amit\materials\python_for_ML\session\result.text", "w")
 for word in word_counts:
    output_file.write("{}: {}\n".format(word, word_counts[word]))
 output_file.close()  
 
frequency(input_file)   