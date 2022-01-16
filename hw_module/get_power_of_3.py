import itertools


def get_power_of3(number):
    'this function will construct any number between 1 and 40 using given a set of weights {1,3,9,27}'
    assert type(number) == int
    assert number >= 1
    assert number <= 40

    weights = [1, 3, 9, 27]
    possibs = list(itertools.product([-1, 0, 1], repeat=4))
    result_dict = {sum(i[0] * i[1] for i in zip(possib, weights)): possib for possib in possibs}
    result = list(result_dict[number])
    assert len(result) == 4
    return result
