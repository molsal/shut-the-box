import random

class Box(object):

    def __init__(self):
        self.board = [False] * 9

    def situation(self):
        return self.board

    def flip(self, tiles):
        for tile in tiles:
            self.board[tile - 1] = True

    def check(self, tile):
        return self.board[tile - 1]

    def is_over(self):
        return all(elem for elem in self.board)

    def get_unflipped(self):
        list = []
        for i in range(0,9):
            if not self.board[i]:
                list.append(i + 1)
        return list


class Die(object):

    def __init__(self):
        self.sides = range(1,7)

    def roll(self):
        return random.choice(self.sides)


class Game(object):

    def __init__(self):
        self.die1 = Die()

        self.die2 = Die()

        self.box = Box()

    def situation(self):
        ret = ""
        for i in range (0,9):
            if self.box.situation()[i]:
                ret += "*"
            else:
                ret += str(i + 1)
        return ret

    def choose(self, options):
        ret = options[-1]
        #if len(self.box.getUnflipped()) < 5:

        for option in options:
            if len(option) == 1:
                ret = option
        return ret

    def subsets_with_sum(self, lst, target):
        def _a(idx, l, r, t):
            if t == sum(l):
                r.append(l)
            elif t < sum(l):
                return
            for u in range(idx, len(lst)):
                _a(u + 1, l + [lst[u]], r, t)
            return r

        return _a(0, [], [], target)

    def get_options(self, val):
        tiles = self.box.get_unflipped()
        options = self.subsets_with_sum(tiles, val)
        return options


    def turn(self):
        val1 = self.die1.roll()
        val2 = self.die2.roll()
        val = val1 + val2
        print(val1)
        print(val2)
        options = self.get_options(val)
        print(options)

        success = False

        if len(options) > 0:
            option = self.choose(options)
            print(option)
            self.box.flip(option)
            success = True
        '''
        for n in range(9, 0, -1):
            if (not self.box.check(n) and not success):
                if val == n:
                    self.box.flip(n)
                    success = True
                    break
                else:
                    for m in range(9, 0, -1):
                        if (not self.box.check(m)):
                            if n != m and n + m == val:
                                self.box.flip(n,m)
                                success = True
                                break
        '''
        return success

    def play(self):
        print(self.situation())
        is_over = False
        while not self.is_finished() and not is_over:
            ret = self.turn()
            print(self.situation())
            if not ret:
                is_over = True
        return is_over

    def is_finished(self):
        return self.box.is_over()


class Multigame(object):

    def __init__(self, times):
        self.times = times

    def play(self):
        counter = 0

        for i in range(0, self.times):
            game = Game()
            is_over = game.play()

            if not is_over:
                counter += 1

        return counter
