a=100 # Startin limit of first number
b=100 # Startin limit of Second number
print("Palindrom numbers are,")
def  panlindrom(int):
    b=100
    while b<1000: # Ending limit of second number
        product=a*b  # Product of both numbers
     
        String=str(product) # Converting Product to String
        length=len(String) # Getting length of String
        alf=length//2      #Half length
    
        x=0 
        y=length-1
        answer=True
        while alf>0:
           if String[x]!=String[y]: #if numbers are not same then Answer==False
               answer=False
               break
           x+=1
           y-=1
           alf-=1
        if answer:
            print(String)
        b+=1
    
while a<1000:# Ending limit of first number
     panlindrom(a) 
     a+=1

print("END")
