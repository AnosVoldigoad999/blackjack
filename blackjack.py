import random
import time

print("---WELCOME TO BLACKJACK---")
starteroptions = ["1. Start Game", "2. Exit"]
gameoptions = ["1. Deposit", "2. End game"]
playerbalance = 0
players_cards = []
dealers_cards = []
player_total = 0
dealer_total = 0
bet_amount = 0
first_deal = True
player_stands = False
endgame = False



blackjack_deck= [
{'card': '2 S', 'value': 2}, {'card': '3 S', 'value': 3}, {'card': '4 S', 'value': 4},
{'card': '5 S', 'value': 5}, {'card': '6 S', 'value': 6}, {'card': '7 S', 'value': 7},
{'card': '8 S', 'value': 8}, {'card': '9 S', 'value': 9}, {'card': '10 S', 'value': 10},
{'card': 'J S', 'value': 10}, {'card': 'Q S', 'value': 10}, {'card': 'K S', 'value': 10},
{'card': 'A S', 'value': 11}, 

{'card': '2 H', 'value': 2}, {'card': '3 H', 'value': 3}, {'card': '4 H', 'value': 4},
{'card': '5 H', 'value': 5}, {'card': '6 H', 'value': 6}, {'card': '7 H', 'value': 7},
{'card': '8 H', 'value': 8}, {'card': '9 H', 'value': 9}, {'card': '10 H', 'value': 10},
{'card': 'J H', 'value': 10}, {'card': 'Q H', 'value': 10}, {'card': 'K H', 'value': 10},
{'card': 'A H', 'value': 11},

{'card': '2 D', 'value': 2}, {'card': '3 D', 'value': 3}, {'card': '4 D', 'value': 4},
{'card': '5 D', 'value': 5}, {'card': '6 D', 'value': 6}, {'card': '7 D', 'value': 7},
{'card': '8 D', 'value': 8}, {'card': '9 D', 'value': 9}, {'card': '10 D', 'value': 10},
{'card': 'J D', 'value': 10}, {'card': 'Q D', 'value': 10}, {'card': 'K D', 'value': 10},
{'card': 'A D', 'value': 11},

{'card': '2 C', 'value': 2}, {'card': '3 C', 'value': 3}, {'card': '4 C', 'value': 4},
{'card': '5 C', 'value': 5}, {'card': '6 C', 'value': 6}, {'card': '7 C', 'value': 7},
{'card': '8 C', 'value': 8}, {'card': '9 C', 'value': 9}, {'card': '10 C', 'value': 10},
{'card': 'J C', 'value': 10}, {'card': 'Q C', 'value': 10}, {'card': 'K C', 'value': 10},
{'card': 'A C', 'value': 11}
]



def welcome():
    for option in starteroptions:
        print(option)
    choice = input(">> ")
    if(choice == "1"):
        start()
    elif (choice == "2"):
        pass
    else:
        print("Please input 1 or 2")
        welcome()
        


def deposit():
    global playerbalance
    print("How much would you like to deposit?")
    amount = int(input(">> "))
    playerbalance += amount
    print(f"{amount} deposited!, new balance: {playerbalance}")

def bet():
    global playerbalance
    global bet_amount
    
    bet_amount= int(input("Enter bet: "))  
    if(bet_amount > 0):
        if(bet_amount <= playerbalance):
            playerbalance -= bet_amount
            print("Bet taken, dealing cards...")
        else:
            print(f"Bet greater than current balance, please input a value less than or equal to {playerbalance}")
            bet()
    else:
        print("Bet cannot be 0")
        bet()
    
    
def game():
    global endgame
    global playerbalance
    global player_stands
    gotten_players_cards =""
    gotten_dealers_cards =""
    player_input =""
    #deal first two cards
    
    #conditions for winning or losing
    if(player_total>21 or (dealer_total>player_total and dealer_total <=21) or dealer_total>21 or (dealer_total==player_total and first_deal!=True and player_stands==True) or player_total==21 or dealer_total==21):
        if(player_total>21):
            print("Player bust! Dealer wins!")
            player_stands = True
            gotten_players_cards = getCards(players_cards)
            gotten_dealers_cards = getCards(dealers_cards)
            print(f"Dealer: {gotten_dealers_cards}")
            print(f"Player: {gotten_players_cards}")
            reset()
            return
        elif(player_total==21):
            print("Player wins! (Blackjack)")
            playerbalance += bet_amount*2
            player_stands = True
            gotten_players_cards = getCards(players_cards)
            gotten_dealers_cards = getCards(dealers_cards)
            print(f"Dealer: {gotten_dealers_cards}")
            print(f"Player: {gotten_players_cards}")
            reset()
            return
        elif(dealer_total==21):
            print("Dealer wins! (Blackjack)")
            player_stands = True
            gotten_players_cards = getCards(players_cards)
            gotten_dealers_cards = getCards(dealers_cards)
            print(f"Dealer: {gotten_dealers_cards}")
            print(f"Player: {gotten_players_cards}")
            reset()
            return
        elif(dealer_total>player_total and dealer_total <=21):
            if(player_stands != True):
                pass
            else:
                print("dealer wins!")
                player_stands = True
                gotten_players_cards = getCards(players_cards)
                gotten_dealers_cards = getCards(dealers_cards)
                print(f"Dealer: {gotten_dealers_cards}")
                print(f"Player: {gotten_players_cards}")
                reset()
                return

        elif(dealer_total>21):
            print("Player wins! Dealer bust!")
            playerbalance += bet_amount*2
            player_stands = True
            gotten_players_cards = getCards(players_cards)
            gotten_dealers_cards = getCards(dealers_cards)
            print(f"Dealer: {gotten_dealers_cards}")
            print(f"Player: {gotten_players_cards}")
            reset()
            return
        elif(dealer_total == player_total):
            print("Push!")
            playerbalance += bet_amount
            player_stands = True
            gotten_players_cards = getCards(players_cards)
            gotten_dealers_cards = getCards(dealers_cards)
            print(f"Dealer: {gotten_dealers_cards}")
            print(f"Player: {gotten_players_cards}")
            reset()
            return
        else:
            print("omo me i no sabi o")
            endgame = True
            reset()
            return
    
    if(first_deal):
        dealCards(2, "player") #deal two cards to both the player and the dealer
        dealCards(2, "dealer")
        gotten_players_cards = getCards(players_cards)
        gotten_dealers_cards = getCards(dealers_cards)
    else:
        gotten_players_cards = getCards(players_cards)
        gotten_dealers_cards = getCards(dealers_cards)
        
    print(f"Dealer: {gotten_dealers_cards}")
    print(f"Player: {gotten_players_cards}")
    print("1.Hit 2.Stand")
    player_input = input(">> ")
    if(player_input == "1"):
        dealCards(1, "player")
    else:
        player_stands = True
        while(dealer_total < player_total and player_total!=21 and dealer_total!=21):
            dealCards(1, "dealer")
            gotten_dealers_cards = getCards(dealers_cards)
            print(f"Dealer: {gotten_dealers_cards}")
            print(f"Player: {gotten_players_cards}")
            time.sleep(1)
            print("-----------")

def reset():
    #reset all necessary stuff
    global players_cards
    global dealers_cards
    global player_total
    global dealer_total
    global first_deal
    global player_stands
    global endgame
    global bet_amount
    
    bet_amount = 0
    players_cards = []
    dealers_cards = []
    player_total = 0
    dealer_total = 0
    first_deal = True
    player_stands = False
    
    print("1. End game 2.Play again 3. Deposit 4. Check Balance")
    player_choice = input(">> ")
    if(player_choice == "1"):
        endgame = True
    elif(player_choice == "2"):
        if(playerbalance == 0):
            print("You have no money left, please deposit")
            reset()
        else:
            bet()
    elif(player_choice == "3"):
        deposit()
        reset()
    elif(player_choice == "4"):
        print(f"Player balance: {playerbalance}")
        reset()
    else:
        print("Please input one of the options (e.g 1)")
        reset()
        
def dealCards(numberOfCards, whoTodealTo):
    global player_total
    global dealer_total
    if(whoTodealTo == "player"):
        for i in range(numberOfCards):
            new_card = random.choice(blackjack_deck) #get a random card from the deck list
            player_total += new_card["value"] #add the value of the dealt card to the player's total
            players_cards.append(new_card) #add the card to the player's hand
    else:
        for i in range(numberOfCards):
            new_card = random.choice(blackjack_deck)
            dealer_total += new_card["value"]
            dealers_cards.append(new_card)
    
        
def getCards(whoTogetCardsFrom):
    global first_deal
    cards = ""
    if(player_stands==False and whoTogetCardsFrom == dealers_cards): #only reveal the dealer's first card if the player stands and if its the dealer's cards you're getting
        for card in whoTogetCardsFrom:
            if(len(cards)==0):
                cards += f"[X]" #the first card should be hidden i.e it appears as [X]
            else:
                cards += f" [{card["card"]}]" #second card isnt hidden
        first_deal = False
    else:
        for card in whoTogetCardsFrom:
            if(len(cards)==0):
                cards += f"[{card["card"]}]"
            else:
                cards += f" [{card["card"]}]"
    return cards
        
        
def start():
    print("---TAKE YOUR SEAT PLAYER---")
    if(playerbalance == 0):
        deposit()
        
    bet()
    
    while(endgame!=True):
        game()




def main():
    welcome()

main()