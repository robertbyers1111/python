#!/usr/bin/python

import re

address = re.compile(
    '''

    # A name is made up of letters, and may include "." for title
    # abbreviations and middle initials.
    ((?P<name>
       ([\w.,]+\s+)*[\w.,]+)
       \s*
       # Email addresses are wrapped in angle brackets: < >
       # but we only want one if we found a name, so keep
       # the start bracket in this group.
       <
    )? # the entire name is optional

    # The address itself: username@domain.tld
    (?P<email>
      [\w\d.+-]+       # username
      @
      ([\w\d.]+\.)+    # domain name prefix
      (com|org|edu)    # limit the allowed top-level domains
    )

    >? # optional closing angle bracket
    ''',
    re.UNICODE | re.VERBOSE)

candidates = [
    u'first.last@example.com',
    u'first.last+category@gmail.com',
    u'valid-address@mail.example.com',
    u'not-valid@example.foo',
    u'First Last <first.last@example.com>',
    u'No Brackets first.last@example.com',
    u'First Last',
    u'First Middle Last <first.last@example.com>',
    u'First M. Last <first.last@example.com>',
    u'<first.last@example.com>',
    ]

for candidate in candidates:
    print()
    print ('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print( '  Match name :', match.groupdict()['name'])
        print( '  Match email:', match.groupdict()['email'])
    else:
        print( '  No match')

