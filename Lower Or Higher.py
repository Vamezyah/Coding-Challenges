import random


score = 0
flag = 1

logo = """
    __                               
   / /   ____ _      _____  _____    
  / /   / __ \ | /| / / _ \/ ___/    
 / /___/ /_/ / |/ |/ /  __/ /        
/_____/\____/|__/|__/\___/_/         
  / __ \_____                        
 / / / / ___/                        
/ /_/ / /                            
\____/_/___       __                 
   / / / (_)___ _/ /_  ___  _____    
  / /_/ / / __ `/ __ \/ _ \/ ___/    
 / __  / / /_/ / / / /  __/ /        
/_/ /_/_/\__, /_/ /_/\___/_/         
        /____/                       """
print(logo)
list = {
        
        1: {'name': 'Luka Modric',
        1: [1 ,"Ballon d'Ors"],
        2: [6,"Champions Leagues"]}, 

        2: {'name': 'Ronaldo Nazario',
        1: [2,"Ballon d'Ors"], 
        2: [0,"Champions Leagues"]},

        3: {'name': 'Johan Cruyff',
        1: [3,"Ballon d'Ors"],
        2: [3,"Champions Leagues"] },

        4: {'name': 'Cristiano Ronaldo',
        1: [5,"Ballon d'Ors"],
        2: [5,"Champions Leagues"] },

       5: {'name': 'Lionel Messi',
        1: [8,"Ballon d'Ors"],
        2: [4,"Champions Leagues"] },

        6: {'name': 'Lionel Messi',
        1: [10,"Spanish Leagues"],
        2: [7,"Copas del rey"] },

}

while True:
        option1 = random.randint(1,2)
        option2 = random.randint(1,2)

        while True:
                player1 = random.randint(1,6)
                player2 = random.randint(1,6)
                if player1 != player2:
                        break

        while True:
                option = input(f"Who has more: {list[player1]['name']}'s {list[player1][option1][1]} (option A) or {list[player2]['name']}'s {list[player2][option2][1]} (option B)? Type A or B ").upper()
                if option == "A" or option == "B":
                        break

        if list[player1][option1][0] > list[player2][option2][0]:
                if option == "A":
                        print("You win")
                        score += 1
                else:
                        print("You lose")
                        flag = 0
                        

        if list[player1][option1][0] < list[player2][option2][0]:
                if option == "B":
                        print("You win")
                        score += 1
                else:
                        print("You lose")   
                        flag = 0           
                
        print(f"Score {score} \n")
        if flag == 0:
                break
