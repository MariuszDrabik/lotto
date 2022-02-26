from lotto import Lotto, Game


def test_lotto():
    # given
    lotto = Lotto()
    # when
    lotto.draw()
    lotto.draw()
    # then
    assert Lotto.NUMBER_OF_DRAWS == 2
    assert len(lotto.get_numbers()) == 6


def test_game():
    game = Game({12, 34, 14, 23, 43, 33})

    game.draws()
    time = Game.consumed_time()
    money = Game.consumed_money()

    assert [i for i in game.wins.keys()][-1] == 6
    assert type(game.show_numbers()) == str
    assert type(time) == int
    assert type(money) == int
