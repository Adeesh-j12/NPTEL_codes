def rock_paper_scissore(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    if(player_one[p1]==player_two[p2]):
        print("Draw")
    elif(player_one[p1]=="Rock" and player_two[p2]=="Scissor"):
        print("Player one wins")
    elif(player_one[p1]=="Rock" and player_two[p2]=="Paper"):
        print("Player two wins")
    elif(player_one[p1]=="Paper" and player_two[p2]=="Scissor"):
        print("Player two wins")
    elif(player_one[p1]=="Paper" and player_two[p2]=="Rock"):
        print("Player one wins")
    elif(player_one[p1]=="Scissor" and player_two[p2]=="Rock"):
        print("Player two wins")
    elif(player_one[p1]=="Scissor" and player_two[p2]=="Paper"):
        print("Player one wins!!")

player_one={0:'paper',1:'rock',3:'scissor'}
player_two={0:'rock',1:'paper',2:'scissor'}
while(1):
    num1=input("Player one enter your choice")
    num2=input("Player two enter your choice")
    bit1=int(input("Player one enter the secret bit position"))
    bit2=int(input("Player two enter the secret bit position"))
    ch=input("Do you want to continue? y/n")
    if(ch=='n'):
        break


