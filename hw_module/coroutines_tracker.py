def tracker(coroutine, limit):
    """The limit keyword argument is the number of odd-numbered seconds to track until completion"""
    from types import GeneratorType
    assert isinstance(coroutine, GeneratorType) and isinstance(limit, int)

    count = 0
    while limit >= count:
        new_value = (yield count)  # If a new value got sent in, reset limit with it
        if new_value is not None:
            limit = new_value

        next_value = next(coroutine)
        if next_value.seconds % 2 == 1:
            count += 1
