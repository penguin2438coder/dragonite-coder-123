import random


def catch():
    choice = input("what do you do \n1 run away or \n2 use arceus and pikatchu to fight")
    if choice == "1":
        print("the zombies catch you and you die")
    elif choice == "2":
        print(" pikatchu and arceus defeat the zombie alpha and the zombie apocolypse ends THE END")


def check_sound():
    print("you follow the sound to see a zombie")
    choice = input("what do you do ?\n1use a bb bat to fight or \n2 catch the arceus you see")
    if choice == "1":
        print("the bb bat slips out of your hand and the zombies kill you")
    elif choice == "2":
        print("you catch arceus and he protects you")
        catch()

def ignore_sound():
    luck = random.randint(1,3)
    if luck == 1:
        print("you get engrossed in the game just as you caught the croocedile you see a zombie in front of you it ends your life by biting you")
        print(" the game finishes without you THE END")
    elif luck == 2:
        print("your house gets broken by the zombie pokemon and you die THE END.")
    elif luck == 3:
        print("you hear another sound and see a zombie")
        check_sound()
              

def start():
    print("I'm so tired from work today I can't wait to play pokemon go")
    print("as you catch a mew you think you hear a scream from your backyard")
    choice = input("what do you do? \nl. pause the game and check it out or\n2. think it was the video game and keep playing ")
    if choice == "1":
        print("you steel you're nerves and head toward the sound with pikatchu")
        check_sound()
    elif choice == "2":
        print ("you shrug off the disturbance and keep playing")
        ignore_sound()
    else:
        print(" that's not an option so stop doing it or die")
        start()

def main():
    print("welcome to the night of the living dead \npress enter to continue")
    input()
    start()

main()
