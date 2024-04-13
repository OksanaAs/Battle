from random import randint

from AI import AI
from Board import Board
from Dot import Dot
from Exception import BoardWrongShipException
from Ship import Ship
from User import User


class Game:
    def __init__(self, size=6):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hide = True

        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def try_board(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempt = 0
        for l in lens:
            while True:
                attempt += 1
                if attempt > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), l, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def greet(self):
        print(" Игра морскои бой")
        print("                  ")
        print("формат ввода: x y")
        print("x - номер строки")
        print("y - номер столбца")

    def print_boards(self):
        print("Доска игрока:")
        print(self.us.board)
        print("Доска компьютера:")
        print(self.ai.board)

    def loop(self):
        num = 0
        while True:
            self.print_boards()
            print("Доска игрока:")
            print(self.us.board)
            print("Доска компьютера:")
            print(self.ai.board)
            if num % 2 == 0:
                print("Ход игрока")
                repeat = self.us.move()
            else:
                print(" Ход компьютерф")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.defeat():
                self.print_boards()
                print("Игрок выиграл")
                break

            if self.us.board.defeat():
                self.print_boards()
                print("Компьютер выиграл")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()


g = Game()
g.start()