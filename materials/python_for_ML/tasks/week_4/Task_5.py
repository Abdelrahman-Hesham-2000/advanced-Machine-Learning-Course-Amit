words = ["Welcome", "Ali", "Hi", "Ali", "No", "Hi", "No", "Ali", "No", "Ali"]
def words_count(words):
 unique_words = set(words)
 counts = {word: 0 for word in unique_words}
 for i in unique_words:
    for j in words:
        if i == j:
            counts[i] += 1
 print(counts)
 
words_count(words)