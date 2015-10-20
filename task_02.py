#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Optional and required things."""

def  prepare_email(appointments):
    """Prepares an email when user provides names and times.

    There'd be paragraphs of text here should they be needed.

    Returns: 
        string: a completed, formatted email

    Examples:

        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')]
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max,\nI look forward to meeting you on March 3.\nBest\nMe']
    
    """
    somevar = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    formatted = []
    for content in appointments:
        formattedString = somevar.format(content[0], content[1])
        formatted.append(formattedString)
    return formatted
