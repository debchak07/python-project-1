import random

def game(comp,you):
    if(comp==you):
        return None

    elif(comp=='R'):   
        if(you=='S'):
           return False
        elif (you=='P'):
            return True

    elif(comp=='P'):   
        if(you=='R'):
           return False
        elif (you=='S'):
            return True  

    elif(comp=='S'):   
        if(you=='P'):
           return False
        elif (you=='R'):
            return True                           

print("Let's play the rock paper scissor game")
print()
print()
print()
print("Computer's turn: Enter rock(R), paper(P), scisssor(S)? -computer chose")
random=random.randint(1,3)
if(random==1):
    comp='R'
if(random==2):
    comp='P'
if(random==3):
    comp='S' 
you=input("Your's turn: Enter rock(R), paper(P), scisssor(S)?")    
if(you != 'R')&(you != 'S')&(you != 'P'):
    print("Wrong Input")
    exit()
print("The computer chose:", comp)
print("You chose:",you)
b=game(comp,you)
if(b==None):
    print("It's a tie")
elif b==True:
    print("You Win")
elif b==False:
    print("You Lose")




    
