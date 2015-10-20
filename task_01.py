#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Optional and required things."""

def get_party_stats(families, table_size=6):
    """Returns the number of guests and tables required in a tuple.

    There'd be paragraphs of text here if they were needed.

    Args:
        families (mixed): arg that gets computed
        table_size (interger): default table size

    Returns:
        tuple: of how many guests and tables

    Examples:

        >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']])
        (6, 3)

        >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']], 2)
        (6, 4)
    
    """
    total = [0, 0]
    for family in families:
        total[0] = total[0] + len(family)
        total[1] = total[1] + (-(-len(family) // table_size))
    return tuple(total)
