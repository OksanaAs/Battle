class BoardException(Exception):
    pass


class BoardOutException(BoardException):
    def __str__(self):
        return "Выстрел за пределы поля"


class BoardUsedException(BoardException):
    def __str__(self):
        return "Повторыи выстрел в ту же точку"


class BoardWrongShipException(BoardException):
    pass