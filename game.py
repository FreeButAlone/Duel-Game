import random
from time import sleep


class Gamer:
    def __init__(self, name):  # creating a new gamer
        self.name = name
        self.health = 100

    def light_attack(self, vict: "Gamer"):  # attack with small range of damage
        dmg = random.randint(18, 25)
        vict.health -= dmg
        print("{} performed a light attack on {}. {} damage dealt.".format(self.name, vict.name, dmg))
        if vict.health <= 0:
            print("{} died.\nWINNER: {}\n".format(vict.name, self.name))

    def heavy_attack(self, vict: "Gamer"):  # attack with big range of damage
        dmg = random.randint(10, 35)
        vict.health -= dmg
        print("{} performed a heavy attack on {}. {} damage dealt.".format(self.name, vict.name, dmg))
        if vict.health <= 0:
            print("{} died.\nWINNER: {}\n".format(vict.name, self.name))

    def heal(self):  # healing
        hp = random.randint(18, 25)
        self.health += hp
        if self.health > 100:  # checking that health points don't exceed 100
            hp -= self.health - 100
            self.health = 100
        print("{} performed a heal. {} HP gained.".format(self.name, hp))


play = True
while play:  # loop for starting games in a row
    turn = 0
    print("Let's get the battle started!\n")
    sleep(1)
    Computer = Gamer("Computer")
    Player = Gamer("Player")  # creating new gamers
    while Computer.health >= 0 and Player.health >= 0:  # main loop for one game
        turn += 1
        print("Turn " + str(turn))  # displaying number of turns played
        if random.randint(0, 1) == 0:  # determining whose turn is it now, 0 for computer, 1 for player
            action = random.randint(1, 4) % 3 if Computer.health <= 35 else random.randint(1, 3)
            # determining action, 50% chance to heal if health is low
            if action == 1:
                Computer.heal()
            elif action == 2:
                Computer.light_attack(Player)
            else:
                Computer.heavy_attack(Player)
        else:
            action = random.randint(1, 3)  # determining action
            if action == 1:
                Player.heal()
            elif action == 2:
                Player.light_attack(Computer)
            else:
                Player.heavy_attack(Computer)
        print("Computer: {} HP\nPlayer: {} HP\n".format(Computer.health, Player.health))
        # printing results of each turn
        sleep(2)  # little pause between turns
    ans = input("Do you want to start a new game? yes/no\n")
    # starting a new game if needed
    while True:
        if ans == 'yes':
            play = True
            break
        elif ans == 'no':
            play = False
            break
        else:
            ans = input("Please, answer in format y/n\n")
