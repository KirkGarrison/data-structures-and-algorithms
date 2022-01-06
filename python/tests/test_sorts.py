from code_challenges.sorts.sorts import insertion_sort

def test_example_arr():
    arr = [8,4,23,42,16,15]
    insertion_sort(arr)
    assert arr == [4,8,15,16,23,42]


def test_other_arr():
    arr = [5,3,20,40,66]
    insertion_sort(arr)
    assert arr == [3,5,20,40,66]


def test_duplicate_arr():
    arr = [5,5,20,20,66]
    insertion_sort(arr)
    assert arr == [5,5,20,20,66]

def test_reverse_arr():
    arr = [97,80,61,57,25,10,2]
    insertion_sort(arr)
    assert arr == [2,10,25,57,61,80,97]
