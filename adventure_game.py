import time
import random
items = []


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def evil_character():
    enemy = (["Zombie!", "Mommy!", "Pirate!"])
    noun = random.choice(enemy)
    print_pause(noun)


def intro():
    print_pause("In the midst of a zombie apocolypse.")
    print_pause("You find yourself outside of an abandond warehouse.")
    print_pause("You are faced with a few of options:")


def main_door(items):
    print_pause("You carefully approach the main door.")
    print_pause("As you edge nearer to the entrance you start to hear eery\n"
                "noises.")
    print_pause("The door handle starts to rattle and out pops a.....")
    evil_character()
    if "sword" in items:
        print_pause("The shiny sword of Argandale gives the enemy a fright.")
        print_pause("You strike the enemy with your sword and are victorious.")
        print_pause("You are on the path to saving the world and restoring\n"
                    "mankind.")
        print_pause("However.....")
        print_pause("That's all for tonight's episode.")
        print_pause("Tune in tomorrow for part 2 to find out your heros\n"
                    "destiny.")
        play_again()
    else:
        print_pause("You realise that this is too risky without a weapon.")
        print_pause("So you retreat back away from the doors of the abandond\n"
                    "warehouse.")
        print_pause("You are faced with the same options.")


def boxes(items):
    print_pause("You cautiosuly check behind the boxes.")
    if "sword" in items:
        print_pause("You've been here before warrior!")
        print_pause("There is nothing left behind the boxes.")
        print_pause("You go back to where you came.")
    else:
        print_pause("You find food rashens!")
        print_pause("Medical supplies and the sword of Argandale! WAHOO!")
        items.append("sword")


def barrels(items):
    print_pause("You wearily creep up to peer behind the barrels.")
    if "discount card" in items:
        print_pause("Unfortunately nothing has changed!")
        print_pause("You've collected all the goods.")
        print_pause("You go back to where you came.")
    else:
        print_pause("You find a 40% discount card for Udacity's nanodegree!")
        print_pause("This is INCREDIBLE, how fortunate!")
        items.append("discount card")


def multiple_choices(items):
    print_pause("Please indicate which route you would like to take by\n"
                "selecting a letter: ")
    choice = input("A. To go through the main front door\n"
                   "B. To check the barrels to your right\n"
                   "C. To check behind the boxes to your left\n")
    if choice == "A".lower():
        main_door(items)
    elif choice == "B".lower():
        barrels(items)
    elif choice == "C".lower():
        boxes(items)
    else:
        print_pause("I'm sorry, I didn't understand your answer")
    multiple_choices(items)


def play_again():
    print_pause("Would you like to play again?")
    again = input("'Yes' or 'no'")
    if again == "Yes".lower():
        play_game()
    elif again == "No".lower():
        print_pause("Very well, goodbye brave warrior, until next time!")
        exit()
    else:
        print_pause("I'm sorry, I didn't understand your answer")
    play_again()


def play_game():
    items = []
    intro()
    multiple_choices(items)
    evil_character()
    play_again()


play_game()
