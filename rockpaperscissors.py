import random
a=int(input("enter number of turns "))
i=0
while(i<a):
    p1=(random.choice(['rock','paper','scissor']))
    p2=str(input("you: "))
    print("bot:",p1)
    if(p1==p2):
        print("tie")
    elif(p1=='rock' and p2=='paper'):
        print('you win')
    elif(p1=='rock' and p2=='scissor'):
        print('bot wins')
    elif(p1=='paper' and p2=='rock'):
        print('bot wins')
    elif(p1=='paper' and p2=='scissor'):
        print('you win')
    elif(p1=='scissor' and p2=='paper'):
        print('bot wins')
    elif(p1=='scissor' and p2=='rock'):
        print('you win')
    i+=1
