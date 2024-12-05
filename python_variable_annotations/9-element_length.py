from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Computes the length of each element in an iterable of sequences.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequence objects.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
        an element from the iterable and its length.
    """
    return [(i, len(i)) for i in lst]
