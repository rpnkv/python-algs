import pytest

from algs.binary_search import search_while

small_test_len = 20
testing_arr = [i for i in range(small_test_len)]


@pytest.mark.parametrize(
    argnames=["arr", "target"],
    argvalues=[(testing_arr, i) for i in range(small_test_len)],
)
def test_search(arr: list[int], target: int) -> None:
    assert search_while(arr, target) == arr.index(target)


def _gen_test_data(limit: int):
    limits = [*range(5)]
    income_collections = [[*range(limit + 1)] for limit in limits]
    collections_with_indices = [[(income_collection, index) for index in income_collection] for income_collection in
                                income_collections]
    flattened = [inner_list_element for outer_list in collections_with_indices for inner_list_element in outer_list]
    return flattened


@pytest.mark.parametrize(
    argnames=["arr", "target"],
    argvalues=_gen_test_data(5),
)
def test_search_2(arr: list[int], target: int) -> None:
    assert search_while(arr, target) == arr.index(target)


""" ok, i'm stuck. Decomposing the concept.
    1. What I want, not definition, but raw data?
    Input args to be like:
    collection, value->index
    
    [1],        1->1
    
    [1,2],      1->1 
    [1,2],      2->2
    
    [1,2,3],    1->1 
    [1,2,3],    2->2 
    [1,2,3],    3->3 
    
    [1,2,3,4],  1->1 
    [1,2,3,4],  2->2 
    [1,2,3,4],  3->3 
    [1,2,3,4],  4->4 
    
    So, for each value in [1,2,3,4] I need to explode it into: 
    [
        [1 to n], 1->1],
        ...
        [1 to n], n->n]
    ]
    
    How?
    Step 1: explode each value into new collection, so it will look like:
    [0,1,2] ->
    [
        [0],
        [0,1],
        [0,1,2]
    ]        
    Implementation of step 1:
    n = 3
    initial_seq = [total_elements for total_elements in range(total_elements + 1)]
    
    exploded_initial_seq = [[i for i in range(total_elements + 1)] for total_elements in initial_seq]
    
    Step 2: Explode exploded seq so each "exploded" seq is appended with indices, iterating over each element.
    Income data:
    [ [0], [0,1], [0,1,2] ]
    Outcome data:
    [ (([0], 0)), ([0,1], (0)), ([0,1], (1)) ... ([0,1,2], (2) ]
    
    Implementation if step 2:
    income_data = [[0], [0, 1], [0, 1, 2]]
    
    outcome_data = [
        
    ]
    
"""
