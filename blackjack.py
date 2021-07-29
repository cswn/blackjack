import random

deck = ['1', '2','3', '4', '5', '6', '7', '8', '9', '10', '11']
user_wallet = 100

print("Welcome to the casino!")
username = input("What is your name? ")

def first_hand():
    shuffled_deck = random.shuffle(deck_of_cards)
    hand = random.sample(shuffled_deck, 2)
    return hand
    #return two cards to the user, their initial hand. These cards should be drawn randomly from the deck list, after shuffling the deck list.

def start_sequence():
    print("You currently have " + str(user_wallet) + " dollars in your wallet.")
    print("Let's begin, " + username + ".")
    initial_hand = first_hand()
    print("Your hand is: ")
    print(initial_hand)



start_sequence()


