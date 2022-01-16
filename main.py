import pandas as pd
import numpy as np
from hw_module.Polynomial import Polynomial
from hw_module.add_month_yr import add_month_yr
from hw_module.count_month_yr import count_month_yr
from hw_module.count_paths import count_paths
from hw_module.find_convex_cover2 import find_convex_cover
from hw_module.fix_categorical import fix_categorical
from hw_module.get_trapped_water import get_trapped_water
from hw_module.next_permutation import next_permutation
from hw_module.solvefrob import solvefrob
from hw_module.split_count import split_count


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
    pvertices = np.array([[0.573, 0.797],
                       [0.688, 0.402],
                       [0.747, 0.238],
                       [0.802, 0.426],
                       [0.757, 0.796],
                       [0.589, 0.811]])
    clist = [(0.7490863467660889, 0.4917635308023209),
             (0.6814339441396109, 0.6199470305156477),
             (0.7241617773773865, 0.6982813914515696),
             (0.6600700275207232, 0.7516911829987891),
             (0.6315848053622062, 0.7730550996176769),
             (0.7348437356868305, 0.41342916986639894),
             (0.7597683050755328, 0.31729154508140384)]
    # clist = [(0.703, 0.6),
    #          (0.7, 0.5),
    #          (0.7, 0.55)]
    print(find_convex_cover(pvertices, clist))