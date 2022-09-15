import random
target=input("please creat a 5digit number from 0 to 4")

while True:
 options = ["1", "2", "3", "0" , "4"]
 random_number = random.randint(0,4)
 computer_pick1 = options[random_number]

 options = ["1", "2", "3", "0", "4"]
 random_number = random.randint (0,4)
 computer_pick2 = options[random_number]

 options = ["1", "2", "3", "0" , "4"]
 random_number = random.randint(0,4)
 computer_pick3 = options[random_number]
 
 options = ["1", "2", "3","0", "4"]
 random_number = random.randint(0,4)
 computer_pick4 = options[random_number]

 options = ["1", "2", "3","0", "4"]
 random_number = random.randint(0,4)
 computer_pick5 = options[random_number]

 password = computer_pick1+computer_pick2 +computer_pick3+computer_pick4+computer_pick5
 print(password)
 if password == target :
    print("it's a match")
    print('the number that you picked is')
    print(password)
    break
 
