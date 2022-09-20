#!/usr/bin/env python3
'''
9. Let's duck type an iterable object
'''

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Annotate this function’s parameters and return values with
    the appropriate types
    '''
    return [(i, len(i)) for i in lst]
