'''
Main progam module Lotto
Program show how lotto is not profitable
'''

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
    '''
        Main game class to start draws after collected numbers
        from user and show stats
    '''

    def __init__(self, numbers: set):
        self.numbers = numbers
        self.wins = {}

    def draws(self):
        '''Making Lotto class until 6 is hit'''
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
        '''Function to show chosen number by user in nice way'''
        show = ''
        for i in self.numbers:
            show += f'[{str(i)}] '
        return show

    @staticmethod
    def consumed_time():
        '''Time statistic'''
        number_of_game = Lotto.NUMBER_OF_DRAWS
        return int(number_of_game / 52)

    @staticmethod
    def consumed_money():
        '''Money lost'''
        number_of_game = Lotto.NUMBER_OF_DRAWS
        return number_of_game * 3

    def show_summary(self):
        '''Showing all statistic'''
        time = Game.consumed_time()
        money = Game.consumed_money()
        for key, value in sorted(self.wins.items())[1:]:
            print(f'You get hits {key}: {value} times')
        print(f'6 was hit after {time:,} years')
        print(f'You spend for this {money:,} PLN')


class App:
    '''Main App class to draw menu manage user inputs'''

    def __init__(self):
        self.options = {
            1: 'Play lotto',
            0: 'End of game'
        }

    @staticmethod
    def pick_numbers():
        '''Take numbers from user'''
        numbers = set()
        while len(numbers) < 6:
            number = input('Pick number from 1 to1 49: ')
            try:
                number = int(number)
                if number in range(1, 49):
                    numbers.add(number)
            except ValueError:
                print('Try number')
        return numbers

    @staticmethod
    def game():
        '''Game procedure'''
        chosen_numbers = App.pick_numbers()
        game = Game(chosen_numbers)
        print(game.show_numbers())
        game.draws()
        game.show_summary()

    def run(self):
        '''Run method'''
        while True:
            print('_'*50)
            for key, value in self.options.items():
                print(f'[{key}] - {value}')
            option = input('Pick one: ').lower()
            if option == 0:
                sys.exit()
            elif option == 1:
                App.game()
            else:
                print('Not correct choice')


if __name__ == '__main__':

    app = App()
    app.run()
