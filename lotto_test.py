from lotto import Lotto, Game


def test_lotto():
    # given
    lotto = Lotto()
    # when
    lotto.draw()
    lotto.draw()
    in_range_1_49 = False
    for n in lotto.get_numbers():
        if n in range(1, 50):
            in_range_1_49 = True
            continue
        in_range_1_49 = False

    # then
    assert Lotto.NUMBER_OF_DRAWS == 2
    assert len(lotto.get_numbers()) == 6
    assert in_range_1_49 is True


def test_game():
    game = Game({12, 34, 14, 23, 43, 33}, Lotto())

    game.play_to_win()
    time = Game.consumed_time()
    money = Game.consumed_money()

    assert [i for i in game.wins.keys()][-1] == '6'
    assert type(game.show_numbers()) == str
    assert type(time) == int
    assert type(money) == int
