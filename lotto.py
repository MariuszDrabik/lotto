"""
Main progam module Lotto
Program show how lotto is not profitable
"""

import glob
from json import dump, load
from random import randint
import sys


class Lotto:
    """Class to get 6 random numbers and count number of draws"""
    NUMBER_OF_DRAWS = 0

    def __init__(self):
        self._numbers = set()

    def __str__(self):
        show = ''
        for i in self._numbers:
            show += f'({str(i)}) '
        return show

    def draw(self):
        """6 random numbers draw and add number to draws counter"""
        Lotto.NUMBER_OF_DRAWS += 1
        self._numbers = set()
        while len(self._numbers) < 6:
            number = randint(1, 50)
            self._numbers.add(number)

    def get_numbers(self) -> set:
        """6 random getter"""
        return self._numbers


class Game:
    """
        Main game class to start draws after collected numbers
        from user and show stats
    """
    NUMBER_STATS = {}

    def __init__(self, numbers: set, lotto: Lotto):
        self.lotto = lotto
        self.numbers = numbers
        self.wins = {}

    def play_to_win(self):
        """Making Lotto class until 6 is hit"""
        while True:
            wins = 0
            self.lotto.draw()
            lotto_numbers = self.lotto.get_numbers()
            Game.save_number_of_numbers(lotto_numbers)
            for i in lotto_numbers:
                if i in self.numbers:
                    wins += 1
            if self.wins.get(str(wins)):
                self.wins[str(wins)] += 1
            else:
                self.wins[str(wins)] = 1

            if self.wins.get("6"):
                break

    def show_numbers(self) -> str:
        """Function to show chosen number by user in nice way"""
        show = ''
        for i in self.numbers:
            show += f'[{str(i)}] '
        return show

    def show_summary(self):
        """Showing all statistic"""
        time = Game.consumed_time()
        money = Game.consumed_money()
        for key, value in sorted(self.wins.items())[1:]:
            print(f'You get hits {key}: {value} times')
        print(f'6 was hit after {time}: years')
        print(f'You spend for this {money}: PLN')

    @staticmethod
    def save_number_of_numbers(numbers: set):
        """Getting number form draw and save to dict

        Args:
            numbers (set): get number from draw
        """
        for number in numbers:
            if Game.NUMBER_STATS.get(str(number)):
                Game.NUMBER_STATS[str(number)] += 1
            else:
                Game.NUMBER_STATS[str(number)] = 1

    @staticmethod
    def consumed_time() -> int:
        """Time statistic"""
        number_of_game = Lotto.NUMBER_OF_DRAWS
        return int(number_of_game / 3 / 52)

    @staticmethod
    def consumed_money() -> int:
        """Money lost"""
        number_of_game = Lotto.NUMBER_OF_DRAWS
        return number_of_game * 3

    @staticmethod
    def save_json():
        """Saving JSON file with stats"""
        file_name = 'stats.json'
        data = {}
        data.update({"Number of draws": Lotto.NUMBER_OF_DRAWS})
        data.update(Game.NUMBER_STATS)
        if glob.glob(file_name):
            with open(file_name, 'r+', encoding='utf-8') as file:
                data_f = load(file)
                print(data)
                file.truncate(0)
                file.seek(0)
                for key, value in data.items():
                    if data_f.get(key):
                        data_f[key] += value
                    else:
                        data_f[key] = value

                dump(data_f, file, indent=3)
        else:
            with open(file_name, 'w', encoding='utf-8') as save:
                dump(data, save, indent=3)


class App:
    """Main App class to draw menu and manage user inputs"""

    def __init__(self):
        self.options = {
            1: 'Play lotto',
            2: 'Save stats',
            0: 'End of game'
        }

    @staticmethod
    def pick_numbers():
        """Take numbers from user"""
        numbers = set()
        while len(numbers) < 6:
            number = input('Pick number from 1 to 49: ')
            try:
                number = int(number)
                if number not in range(1, 50):
                    print('Number should be between 1 and 49')
                else:
                    numbers.add(number)
            except ValueError:
                print('Try number')
        return numbers

    @staticmethod
    def game():
        """Game procedure"""
        chosen_numbers = App.pick_numbers()
        game = Game(chosen_numbers, Lotto())
        print(game.show_numbers())
        game.play_to_win()
        game.show_summary()

    def run(self):
        """Run method"""
        while True:
            print('_'*50)
            for key, value in self.options.items():
                print(f'[{key}] - {value}')
            option = input('Pick one: ').lower()
            if option == '0':
                sys.exit()
            elif option == '1':
                App.game()
            elif option == '2':
                Game.save_json()
            else:
                print('Not correct choice')


if __name__ == '__main__':
    app = App()
    app.run()
