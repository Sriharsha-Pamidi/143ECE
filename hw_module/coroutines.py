from time import sleep
import random
from datetime import datetime

from hw_module.coroutines_tracker import tracker


def producer():
    'produce timestamps'
    starttime = datetime.now()
    while True:
        sleep(random.uniform(0, 0.2))
        yield datetime.now() - starttime


if __name__ == '__main__':
    pr = tracker(producer(), 2)
    next(pr)
    # pr.send(7)
    print(list(pr))
    # pr.send(7)
    # print(list(pr))
