import math
class Math():
    def __init__(self):
     pass 
       
    def factorial(self,num):
     if num == 0:
        return 0
     if num == 1:
        return 1
     return num * self.factorial(num-1)
 
    def isPrime(self,num):
      for i in range(2, num):
        if num % i == 0:
            return False
      return True
  
    def dividors(self,num1,num2):
     mn = min(num1, num2)
     common_dividors = []
     for i in range(1, mn+1):
        if num1 % i == 0 and num2 % i ==0:
            common_dividors.append(i)
     return common_dividors
 
    def add(self,num1,num2):
     result=num1+num2
     return result
 
    def subtract(self,num1,num2):
     result=num1-num2
     return result
 
    def multiply(self,num1,num2):
     result=num1*num2
     return result
 
    def divide(self,num1,num2):
     result=num1/num2
     return result
 
    def mod(self,num1,num2):
        return num1 % num2

    def power(self, base, exponent):
        return base ** exponent
    
    def sqrt(self, num):
        return math.sqrt(num)
    
    def absolute(self, num):
        return abs(num)
    
if __name__=="__main__":
    result=Math()
    print(result.dividors(10,30))    