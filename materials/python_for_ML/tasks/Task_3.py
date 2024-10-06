Encoded_Message="&&&**$gnirtS PLIO!!@1234"
core = Encoded_Message.split('$')[1].split('!')[0]
print(core)
word1=core[-6::-1]
word2=core[7::1]
word2=word2.replace("I","E")
word2=word2.replace("O","U")
words=[word1,word2]
Message=" ".join(words)
print(Message)