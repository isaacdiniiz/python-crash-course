from random import randint

class Die:

    def __init__(self, times_rolled=1, sides=6):
        self.sides = sides
        self.times_rolled = times_rolled

    def roll_die(self):
        return randint(1, self.sides)

    def print_die_results(self):
        print('\n')
        for _ in range(self.times_rolled):
            print(self.roll_die(), end=' ')


dice_6 = Die(10)
dice_6.print_die_results()

dice_10 = Die(10, 10)
dice_10.print_die_results()

dice_20 = Die(10, 20)
dice_20.print_die_results()