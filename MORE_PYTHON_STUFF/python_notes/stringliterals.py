
what is this?

	r'ab\n'

.. it means the backslash is just a normal character.

From docs.python.org ...

When an 'r' or 'R' prefix is present, a character following a backslash
is included in the string without change, and all backslashes are left
in the string. For example, the string literal r"\n" consists of two
characters: a backslash and a lowercase 'n'. String quotes can be
escaped with a backslash, but the backslash remains in the string; for
example, r"\"" is a valid string literal consisting of two characters: a
backslash and a double quote; r"\" is not a valid string literal (even a
raw string cannot end in an odd number of backslashes). Specifically, a
raw string cannot end in a single backslash (since the backslash would
escape the following quote character). Note also that a single backslash
followed by a newline is interpreted as those two characters as part of
the string, not as a line continuation.

When an 'r' or 'R' prefix is used in conjunction with a 'u' or 'U'
prefix, then the \uXXXX and \UXXXXXXXX escape sequences are processed
while all other backslashes are left in the string. For example, the
string literal ur"\u0062\n" consists of three Unicode characters: 'LATIN
SMALL LETTER B', 'REVERSE SOLIDUS', and 'LATIN SMALL LETTER N'.
Backslashes can be escaped with a preceding backslash; however, both
remain in the string. As a result, \uXXXX escape sequences are only
recognized when there are an odd number of backslashes.
