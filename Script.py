import random

computer = random.choice([0, 1, 2])
user_str=input("Enter the input: ")
user_dict={
    "rock":0,
    "paper":1,
    "scissors":2    
}
computer_dict={
    0:"rock",
    1:"paper",
    2:"scissors"
}
if user_str not in user_dict:
    print("Invalid input! Please enter rock, paper, or scissors.")
    exit()
user_num=user_dict[user_str]
if(computer==0 and user_num==1):
    print("You win:!!")
elif(computer==0 and user_num==2):
    print("You lose!!")
elif(computer==1 and user_num==0):
    print("You lose!!")
elif(computer==1 and user_num==2):
    print("You win:!!")
elif(computer==2 and user_num==0):
    print("You win:!!")
elif(computer==2 and user_num==1):
    print("You lose!!")
else:
    print("It's a tie!!")
