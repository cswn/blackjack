import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
user_wallet = 100
user_total = 0
house_total = 0
house_card_1 = 0
house_card_2 = 0

print("Welcome to the casino!")

def game_over():
    choice = input("Would you like to play again? Press 'y' for yes and 'n' for no. ")
    if choice == "y":
        pass
    else:
        break

def house_turn_to_draw():
    global user_total
    global house_total
    #card_1 and card_2 references here are local to another function, how to make them global?
    print("The house had " + str(house_card_1) + " and the hole card, which was...")
    print(str(house_card_2) + "!")
    print("This means the house total was " + str(house_total) + ".")
    print("\n")
    if house_total == 21:
        print("House wins with a Blackjack!")
        game_over()
    elif house_total > user_total:
        print("House wins!")
        game_over()
    else:
        while house_total < 17:
            card = random.choice(deck)
            print("House's next card is... " + str(card))
            house_total += card
            print("New house total = " + str(house_total))
            if house_total > 21:
                print("House busts, you won!")
                game_over()
            elif house_total < user_total:
                print("User wins!")
                game_over()
            else:
                print("House wins!")
                game_over()


def first_hand():
    global user_total
    card_1 = random.choice(deck)
    card_2 = random.choice(deck)
    user_total += card_1
    user_total += card_2
    hand = str(card_1) + " and " + str(card_2)
    return hand

def house_initial():
    global house_total
    global house_card_1
    global house_card_2
    card_1 = random.choice(deck)
    card_2 = random.choice(deck)
    house_card_1 += card_1
    house_card_2 += card_2
    house_total += card_1
    house_total += card_2
    hand = str(card_1) + " and the hole card."
    return hand

def hit():
    global user_total
    card = random.choice(deck)
    user_total += card
    print(card)
    print("\n")
    if user_total > 21:
        print("Bust! House wins.")
        game_over()
    elif user_total == 21:
        print("Blackjack! You win!")
        game_over()
    else:
        choice()

def stand():
    global user_total
    print("Okay, your total stands at " + str(user_total) + ".")
    print("\n")
    house_turn_to_draw()

def double():
    print("This feature will be available soon. Bye.")

def choice():
    options_choice = input("Hit 'h' for hit, 's' for stand, and 'd' for double. ")
    if options_choice == "h":
        hit()
    elif options_choice == "s":
        stand()
    elif options_choice == "d":
        double()
    else:
        print("I didn't understand your choice.")
        choice()

def start_sequence():
    print("You currently have " + str(user_wallet) + " dollars in your wallet.")
    print("Let's begin.")
    print("\n")
    initial_hand = first_hand()
    print("Your hand is: ")
    print(initial_hand)
    print("\n")
    print("Here is the dealer's hand: ")
    dealer_hand = house_initial()
    print(dealer_hand)
    print("Note that the hole card has been drawn but will only be revealed after you stop.")
    print("\n")
    print("Alright, time to play!")
    choice()




start_sequence()


