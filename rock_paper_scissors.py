import random  
# hello guys a made a strong hashing system so you can play rock paper scissors xD
#let's discover this code
#first we have the input 

password = input('enter your password: ')
#then the computer options 
options = ["&", "é", "(","-","è","ç","^","ù","*",":",",","?","$","£","%","<",">","²","..","§","!","°","#"]
#then here is where the magic happens 

random_number = random.randint(0,22)
#the computer will generate 18 options from 23 symbols

computer_pick1 = options[random_number]
random_number = random.randint(0,22)
computer_pick2 = options[random_number]
random_number = random.randint(0,22)
computer_pick3 = options[random_number]
random_number = random.randint(0,22)
computer_pick4 = options[random_number]
random_number = random.randint(0,22)
computer_pick5 = options[random_number]
random_number = random.randint(0,22)
computer_pick6 = options[random_number]
random_number = random.randint(0,22)
computer_pick7 = options[random_number] 
random_number = random.randint(0,22)
computer_pick8 = options[random_number] 
random_number = random.randint(0,22)
computer_pick9 = options[random_number] 
random_number = random.randint(0,22)
computer_pick10 = options[random_number] 
random_number = random.randint(0,22)
computer_pick11= options[random_number]
random_number = random.randint(0,22)
computer_pick12 = options[random_number] 
random_number = random.randint(0,22)
computer_pick13 = options[random_number] 
random_number = random.randint(0,22)
computer_pick14 = options[random_number] 
random_number = random.randint(0,22)
computer_pick15 = options[random_number]
random_number = random.randint(0,22)
computer_pick16 = options[random_number] 
random_number = random.randint(0,22)
computer_pick17 = options[random_number]
random_number = random.randint(0,22)
computer_pick18 = options[random_number] 
#after that he will combine them to one string
hashing = computer_pick1+computer_pick2 +computer_pick3+computer_pick4+computer_pick5+computer_pick6+computer_pick7+computer_pick8+computer_pick9+computer_pick10+computer_pick11+computer_pick12+computer_pick13+computer_pick14+computer_pick15+computer_pick16+computer_pick17+computer_pick18
#the computer will give us a second input to enter the hash that he generated 

print('your hash is /// ' + hashing)
#now the game will start but in order to play you must put the correct hashing to reveal your password and to play 
get_your_password = input('please enter your hash: ')
# let's try this OUT  
while True:
    if get_your_password != hashing:
        wrong=input('try again or Q to quit: ')
        if wrong=='q':
            break
        if wrong != hashing:
            continue
        if get_your_password == hashing : 
            print('your password is:'+ password)
            
        while True:
            print('welcome to the game')
            options_game = ["rock", "paper", "scissors"]
            user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
            if user_input == "q":
                print("Goodbye!")
            break

        if user_input not in options:
            continue

        random_number = random.randint(0, 2)
        # rock: 0, paper: 1, scissors: 2
        computer_game = options_game[random_number]
        print("Computer picked", computer_game + ".")

        if user_input == "rock" and computer_game == "scissors":
            print("You won!")

        elif user_input == "paper" and computer_game == "rock":
            print("You won!")
        elif user_input == "scissors" and computer_game == "paper":
            print("You won!")
        else:
         print("You lost!")
        print("Goodbye!")
        break

