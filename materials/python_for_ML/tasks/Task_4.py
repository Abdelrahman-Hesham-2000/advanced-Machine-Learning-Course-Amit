Encoded_Message="##$$$@!yalpstcejorp EPUVT****9887"
core = Encoded_Message.split('!')[1].split('*')[0]
print(core)
word1=core[-7::-1]
word2=core[13::1]
word2=word2.replace("E","A")
word2=word2.replace("U","O")
words=[word1,word2]
Message=" ".join(words)
print(Message)