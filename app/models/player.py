class Player:
    def __init__(self, name, move):
        self.name = name
        self.move = move

    # Need this to assertEqual on objects - http://www.igeorgiev.eu/python/tdd/python-unittest-assert-custom-objects-are-equal/
    # def __eq__(self, other):
    #     return self.name == other.name and self.move == other.move