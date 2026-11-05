import itertools
import random
from audrithm.algorithms import kadane, brute_force

def oracle(arr):
    candidates = [(sum(arr[i:j+1]), i, j) for i in range(len(arr)) for j in range(i,len(arr))]
    return min(candidates, key=lambda v: (-v[0],v[1],v[2]))

def test_exhaustive_independent_oracle():
    for n in range(1,7):
        for values in itertools.product((-1,0,1), repeat=n):
            a, b = kadane(values), brute_force(values)
            assert a == b
            assert (a.total,a.start,a.end) == oracle(values)

def test_seeded_differential():
    rng = random.Random(20261105)
    for _ in range(500):
        values = [rng.randint(-1000,1000) for _ in range(rng.randint(1,80))]
        assert kadane(values) == brute_force(values)
