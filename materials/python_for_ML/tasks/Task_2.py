Encoded_Message="###!!@mocleW EPGTQ!!!6789"
core = Encoded_Message.split('@')[1].split('!')[0]
print(core)
word1=core[-7::-1]
word2=core[7::1]
words=[word1,word2]
Message=" ".join(words)
print(Message)
#Good job
