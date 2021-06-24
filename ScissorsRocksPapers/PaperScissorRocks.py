# Paper Scissors stone
# Needs at least two players.
import enum
import random as rand

class Player:
    __name: str = ""
    __throw: enum.Enum = ""
    __points: int = 3

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def getThrow(self) -> enum.Enum:
        return self.__throw

    def setThrow(self, throw: enum.Enum):
        self.__throw = throw

    def getLive(self) -> int:
        return self.__points

    def setLife(self, points: int):
        self.__points = points

    def __str__(self):
        return f"Player: {self.__name}, Lives: {self.__points}"

class Rules:
    __player_numbers: int = 0
    __players: dict[int, Player] = {}
    __hands: list[enum.Enum] = ['Rock', 'Scissors', 'Paper']
    __rounds: int = 1

    def withPcOrFriend(self) -> bool:
        """
        checks if the player wants to play alone with an npc or with a friend
        :return:
        """
        print("Hi, do you want to play with a Computer or with a friend?")
        print("1. pc, 2. with a friend")
        choice: str = input()
        assert choice.isnumeric() and 0 < int(choice) < 3, "please only enter 1 or 2"
        if choice == "1":
            print("You choose to play with the pc")
            return True
        else:
            print("you choose to play with a friend")
            return False

    def anybodyDead(self) -> bool:
        for k, v in self.__players:
            player = v
            if player.getLive() == 0:
                print(player.getName() + "is  O   U     T!\nGame Over")
                return True
        print("And the game rages on!")
        return False

    def showAllPlayers(self):
        for k, v in self.__players:
            player: Player = v
            print(player.__str__())

    def chooseRandomPoison(self) -> enum.Enum:
        poison: int = rand.randint(0,2)
        return self.__hands[poison]

    def gameStart(self):
        choice: bool = self.withPcOrFriend()
        print("it's time to play!")
        self.createPlayers(choice)

    def createPlayers(self, pcOrPlayer: bool):
        if pcOrPlayer:
            print('computer opponent is being created...')
            pc = Player()
            pc.setName('pc')
            self.__players.__setitem__(1, pc)
            print("What's your name?")
            name: str = input()
            player = Player()
            player.setName(name)
            self.__players.__setitem__(2, player)
        else:
            print("Enter first player's name: ")
            name: str = input()
            player1 = Player()
            player1.setName(name)
            self.__players.__setitem__(1, player1)
            print("Enter second player's name: ")
            name: str = input()
            player2 = Player()
            player2.setName(name)
            self.__players.__setitem__(2, player2)

    def dealWithHands(self):
        player1 = self.__players.get(1)
        player2 = self.__players.get(2)
        player1S = "player 1 loses a life"
        player2S = "player 2 loses a life"

        # Rock and Scissors
        if player1.getThrow() == "Rock" and player2.getThrow() == "Scissors":
            player1.setLife(player1.getLive() - 1)
            print(player2S)
        elif player1.getThrow() == "Scissor" and player2.getThrow() == "Rock":
            player2.setLife(player2.getLive() - 1)
            print(player1S)
        # Paper and Rock
        elif player1.getThrow() == "Paper" and player2.getThrow() == "Rock":
            player2.setLife(player2.getLive() - 1)
            print(player2S)
        elif player1.getThrow() == "Rock" and player2.getThrow() == "Paper":
            player1.setLife(player1.getLive() - 1)
            print(player1S)
        # paper and scissor
        elif player1.getThrow() == "Paper" and player2.getThrow() == "Scissor":
            player1.setLife(player1.getLive() - 1)
            print(player2S)
        elif player1.getThrow() == "Scissor" and player2.getThrow() == "Paper":
            player2.setLife(player2.getLive() - 1)
            print(player2S)
        else:
            print("draw!")
        if self.anybodyDead():
            SystemExit(0)



game = Rules()
game.gameStart()
