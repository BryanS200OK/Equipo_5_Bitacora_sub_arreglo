import pytest
from audrithm.algorithms import kadane, brute_force, max_sum, kadane_trace

CASES = [([1,2,3], (6,0,2)), ([-5,-1,-3],(-1,1,1)),
         ([-2,1,-3,4,-1,2,1,-5,4],(6,3,6)), ([0,0,0],(0,0,0)),
         ([7],(7,0,0)), ([-7],(-7,0,0)), ([2,2,-9,2],(4,0,1)),
         ([4,3,-10],(7,0,1)), ([-10,3,4],(7,1,2)), ([-9,2,3,-9],(5,1,2)),
         ([1,-1,1],(1,0,0)), ([0,1],(1,0,1))]

@pytest.mark.parametrize("fn", [kadane, brute_force])
@pytest.mark.parametrize("arr,expected", CASES)
def test_cases(fn, arr, expected):
    original = arr.copy()
    answer = fn(arr)
    assert (answer.total, answer.start, answer.end) == expected
    assert answer.subarray == tuple(arr[answer.start:answer.end+1])
    assert sum(answer.subarray) == answer.total
    assert arr == original

@pytest.mark.parametrize("fn", [kadane, brute_force])
def test_empty(fn):
    with pytest.raises(ValueError):
        fn([])

@pytest.mark.parametrize("arr", [[True], [1.5], ["1"], "123", None])
@pytest.mark.parametrize("fn", [kadane, brute_force])
def test_invalid(fn, arr):
    with pytest.raises(TypeError):
        fn(arr)

def test_sum_and_trace():
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    assert max_sum(arr) == 6
    for i, row in enumerate(kadane_trace(arr)):
        assert row["Mejor global"] == brute_force(arr[:i+1]).total
        assert row["Mejor terminado"] == max(sum(arr[j:i+1]) for j in range(i+1))
