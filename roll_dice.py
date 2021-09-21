#rolling n number sided dice, 1 millon times.
# We try with 2 six-sided dice: roll_dice(6,6)
# or 1, four-sided dice and 2 six-sided dice: roll_dice(4,6,6)

from random import randint
from collections import Counter


def roll_dice(*dice, num_trials=1_000_000):
    counts = Counter()
    for roll in range(num_trials):
        counts[sum((randint(1,sides) for sides in dice))] += 1

    print('\nOUTCOME\tPROBABILITY')
    for outcome in range(len(dice), sum(dice)+1):
        print('{}\t{:0.2f}%'.format(outcome,counts[outcome]*100/num_trials))

roll_dice(6,6)
