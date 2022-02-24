from random import randint


class Lotto:
    NUMBER_OF_DRAWS = 0

    def __init__(self):
        self._numbers = set()

    def __str__(self):
        return str(self._numbers)

    def draw(self):
        Lotto.NUMBER_OF_DRAWS += 1
        self._numbers = set()
        while len(self._numbers) < 6:
            number = randint(1, 49)
            self._numbers.add(number)

    def get_numbers(self):
        return self._numbers


class Game:
    SHORTCUT = '1'
    LABEL = 'Gramy w totka?'

    def __init__(self, numbers: set):
        self.numbers = numbers
        self.wins = {}

    @classmethod
    def pick_numbers(cls):
        numbers = set()
        while len(numbers) < 6:
            number = input('Podaj liczbę od 1 do 49: ')
            try:
                number = int(number)
                numbers.add(number)
            except ValueError:
                print('Spróbuj jeszcze raz')
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

    def consumed_time(self):
        number_of_game = Lotto.NUMBER_OF_DRAWS
        print(f'Years: {number_of_game/52:,}')

    def consumed_money(self):
        number_of_game = Lotto.NUMBER_OF_DRAWS
        print(f'Money: {number_of_game*3:,}')

    def show_summary(self):
        for key, value in sorted(self.wins.items()):
            print(f'{key}: {value}')
        self.consumed_time()
        self.consumed_money()


class App:

    def menu(self):
        self.options = {
            1: 'Gramy w totka',
            'z': 'Kończymy'
        }
        return self.options

    def run(self):
        while True:
            print('_'*50)
            for key, value in self.options.items():
                print(f'[{key}] - {value}')
            option = input('Wybierz jedną: ').lower()
            if option == 'z':
                exit()
            game = Game.pick_numbers()
            game.draws()
            game.show_summary()


if __name__ == '__main__':

    while True:
        app = App()
        app.menu()
        app.run()
