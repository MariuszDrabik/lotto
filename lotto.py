from random import randint
import sys


class Lotto:
    '''Draw class to get 6 random numbers'''
    NUMBER_OF_DRAWS = 0

    def __init__(self):
        self._numbers = set()

    def __str__(self):
        return str(self._numbers)

    def draw(self):
        '''6 random numbers draw'''
        Lotto.NUMBER_OF_DRAWS += 1
        self._numbers = set()
        while len(self._numbers) < 6:
            number = randint(1, 49)
            self._numbers.add(number)

    def get_numbers(self):
        '''6 random getter'''
        return self._numbers


class Game:

    def __init__(self, numbers: set):
        self.numbers = numbers
        self.wins = {}

    @classmethod
    def pick_numbers(cls):
        numbers = set()
        while len(numbers) < 6:
            number = input('Pick number from 1 to1 49: ')
            try:
                number = int(number)
                if number in range(1, 49):
                    numbers.add(number)
            except ValueError:
                print('Try number')
        return cls(numbers)

    def draws(self):
        while True:
            lotto = Lotto()
            lotto.draw()
            wins = 0
            for i in lotto.get_numbers():
                if i in self.numbers:
                    wins += 1
            if self.wins.get(wins):
                self.wins[wins] += 1
            else:
                self.wins[wins] = 1

            if self.wins.get(6):
                break

    def show_numbers(self):
        return self.numbers

    @staticmethod
    def consumed_time():
        number_of_game = Lotto.NUMBER_OF_DRAWS
        return int(number_of_game / 52)

    @staticmethod
    def consumed_money():
        number_of_game = Lotto.NUMBER_OF_DRAWS
        return number_of_game * 3

    def show_summary(self):
        time = Game.consumed_time()
        money = Game.consumed_money()
        for key, value in sorted(self.wins.items())[1:]:
            print(f'You get 0 hits:{key}: {value} times')
        print(f'6 was hit after: {time:,}')
        print(f'You spend for this: {money:,} PLN')


class App:

    def __init__(self):
        self.options = {
            1: 'Play lotto',
            'z': 'End of game'
        }

    @staticmethod
    def exit_game():
        sys.exit()

    def run(self):
        while True:
            print('_'*50)
            for key, value in self.options.items():
                print(f'[{key}] - {value}')
            option = input('Pick one: ').lower()
            if option == 'z':
                App.exit_game()
            game = Game.pick_numbers()
            print(game.show_numbers())
            game.draws()
            game.show_summary()


if __name__ == '__main__':

    app = App()
    app.run()
