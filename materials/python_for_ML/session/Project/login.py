import random
u="Dimes"
p="1111"
class LOGIN():
 def __init__(self,x,y):
     self.x=x
     self.y=y   
 def login (self):
  while True:
    
    if self.x==u:
        
        if self.y==p:
            s=random.randrange(10000,1000000)
            print("Verification code ise: ",s)
            
            while True:
                l=int(input("Enter Verification code: "))
                
                if l==s:
                    print("Welcome")
                    break
                else:
                    print("Incorrect Verification code. Try again.")
            break 
        else:
            print("Incorrect password")
    else:
        print("Incorrect username")   
        
