print("I have number between 1 and 1000")
print("Can you guess my number?")
print("please type your first guess")
def guess(num):
    while num>0:
       if x==num:
          return False
         
          
         
          
          num=-1
       elif x>num:
          
          print("Too Low ! Try again")
          return True
       else:
         
          print("Too High ! Try again")
          return True
num=int(input(" ? "))
from random import randint
x=randint(1 , 1000)
guess(num)
a=1
while a>0:
    if guess(num):
      
        
        num=int(input(" ? "))
        guess(num)
    else:
            print("Excellent")
            print("Would you like to play again?")
            num=int(input("please type 1=Yes ,2=No "))
       
    if num==1:
            num=int(input(" ? "))
            from random import randint
            x=randint(1 , 1000)
            guess(num)
    if num==2:
        a=-1

           
