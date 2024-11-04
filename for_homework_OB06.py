import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} на {self.attack_power} урона!")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player_turn()
            if not self.computer.is_alive():
                break

            # Ход компьютера
            self.computer_turn()
            if not self.player.is_alive():
                break

        self.declare_winner()

    def player_turn(self):
        self.player.attack(self.computer)
        print(f"{self.computer.name} осталось здоровья: {self.computer.health}\n")

    def computer_turn(self):
        self.computer.attack(self.player)
        print(f"{self.player.name} осталось здоровья: {self.player.health}\n")

    def declare_winner(self):
        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")

if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()