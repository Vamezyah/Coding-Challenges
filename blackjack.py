import random
import os
import math
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] #In blackjack there are plenty of decks so the cards can repeat (there are 4 10's because of the cards 10,J,Q and K)
player_cards = []
dealer_cards = []
flag = 0

# Deal of cards

for i in range(2):
    player_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))

# #player_cards.append(10)
# dealer_cards.append(10)
# #player_cards.append(11)
# dealer_cards.append(11)


if(sum(dealer_cards) > 21): #Dealer has two 11 cards
    dealer_cards[0] = 1
print(f'Dealer visible card: {dealer_cards[0]}')



for i in range(len(player_cards)):
    if (player_cards[i] == 11):
        print(f'Your cards: {player_cards}')
        option = input("Do you want to transform your 11 into a 1? (Y/N) ")
        option = option.upper()
        if(option == "Y"):
            player_cards[i] = 1
            print("Your card is now a 1")
            print(f'Your cards: {player_cards}')
        else:
            print("Your card will stay as 11")

if(sum(player_cards) > 21): #Player has two 11 cards
    print("You lose")
    print(f'Your cards: {player_cards} sum: {sum(player_cards)}')
    print(f'Dealer cards: {dealer_cards} sum: {sum(dealer_cards)}')
    flag = 1

if(sum(player_cards) == 21):
        if(sum(dealer_cards) == 21):
            os.system('cls')
            print("It's a tie!!!")
            print(f'Your cards: {player_cards} sum: {sum(player_cards)}')
            print(f'Dealer cards: {dealer_cards} sum: {sum(dealer_cards)}')
            flag = 1
        else:
            os.system('cls')
            print("You win!!!")
            print(f'Your cards: {player_cards} sum: {sum(player_cards)}')
            print(f'Dealer cards: {dealer_cards} sum: {sum(dealer_cards)}')
            flag = 1

elif(sum(dealer_cards) == 21):
    os.system('cls')
    print("You lose!!!")
    print(f'Your cards: {player_cards} sum: {sum(player_cards)}')
    print(f'Dealer cards: {dealer_cards} sum: {sum(dealer_cards)}')
    flag = 1
 
# Player turn
while (sum(player_cards) < 21 and flag == 0):
    print(f'Your cards: {player_cards}')
    option = " "
    option = input("Do you want yo hit or stand? H/S ")
    option = option.upper()
    if (option == "H"):
        player_cards.append(random.choice(cards))
        #player_cards.append(11)
        if(player_cards[-1] == 11):
            option = input("Do you want to transform your 11 into a 1? (Y/N) ")
            option = option.upper()
            if(option == "Y"):
                player_cards[-1] = 1
                print("Your card is now a 1")
            else:
                print("Your card will stay as 11")
    elif(option == "S"):
        print("You decided to stand")
        print("\nDealer's turn")
        break

    if(sum(player_cards) > 21):
        os.system('cls')
        print("You lose!!!")
        print(f'Your cards: {player_cards} sum: {sum(player_cards)}')
        print(f'Dealer cards: {dealer_cards} sum: {sum(dealer_cards)}')
        flag = 1
        break
    if(sum(player_cards) == 21):
        os.system('cls')
        print(f'Your cards: {player_cards} sum: {sum(player_cards)}')
        print("You reach 21, let's wait the dealer")
        print("\nDealer's turn")

# Dealers turn
while (sum(dealer_cards) < 21 and flag == 0):
    print(f'Dealer cards: {dealer_cards} sum: {sum(dealer_cards)}')
    if(sum(dealer_cards) < 18):
        dealer_cards.append(random.choice(cards))
        print("Dealer decided to hit")
    else:
        print("Dealer decided to stand")
        break

#Final result
print("\nFINAL RESULTS")
if(sum(player_cards) == 21 and flag == 0):
        if(sum(dealer_cards) == 21):
            print("It's a tie!!!")
            print(f'Your cards: {player_cards} sum: {sum(player_cards)}')
            print(f'Dealer cards: {dealer_cards} sum: {sum(dealer_cards)}')
            flag = 1
        else:
            print("You win!!!")
            print(f'Your cards: {player_cards} sum: {sum(player_cards)}')
            print(f'Dealer cards: {dealer_cards} sum: {sum(dealer_cards)}')
            flag = 1



if ((abs(sum(player_cards)-21) <= abs(sum(dealer_cards)-21) and flag == 0) or (sum(player_cards) == 21 and flag == 0)):
    if(sum(dealer_cards) == sum(player_cards)):
            print("It's a tie!!!")
            print(f'Your cards: {player_cards} sum: {sum(player_cards)}')
            print(f'Dealer cards: {dealer_cards} sum: {sum(dealer_cards)}')
            flag = 1
    else:
        print("You win!!!")
        print(f'Your cards: {player_cards} sum: {sum(player_cards)}')
        print(f'Dealer cards: {dealer_cards} sum: {sum(dealer_cards)}')


elif ((abs(sum(player_cards)-21) > abs(sum(dealer_cards)-21) and flag == 0) or (sum(dealer_cards) == 21 and flag == 0) and sum(player_cards) != 21 and flag == 0):
    print("You lose!!!")
    print(f'Your cards: {player_cards} sum: {sum(player_cards)}')
    print(f'Dealer cards: {dealer_cards} sum: {sum(dealer_cards)}')
