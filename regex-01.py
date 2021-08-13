#!/usr/bin/python

import re

"""
#   +------------------+
#---| Group Extraction |-------------------------------------------------------
#   +------------------+

The "group" feature of a regular expression allows you to pick out parts
of the matching text. Suppose for the emails problem that we want to
extract the username and host separately. To do this, add parenthesis (
) around the username and host in the pattern, like this:
r'([\w.-]+)@([\w.-]+)'. In this case, the parenthesis do not change what
the pattern will match, instead they establish logical "groups" inside
of the match text. On a successful search, match.group(1) is the match
text corresponding to the 1st left parenthesis, and match.group(2) is
the text corresponding to the 2nd left parenthesis. The plain
match.group() is still the whole match text as usual.

  str = 'purple alice-b@google.com monkey dishwasher'

  match = re.search('([\w.-]+)@([\w.-]+)', str)

  if match:
    print match.group()   ## 'alice-b@google.com' (the whole match)
    print match.group(1)  ## 'alice-b' (the username, group 1)
    print match.group(2)  ## 'google.com' (the host, group 2)

A common workflow with regular expressions is that you write a pattern
for the thing you are looking for, adding parenthesis groups to extract
the parts you want.

#   +---------+
#---| findall |----------------------------------------------------------------
#   +---------+

findall() is probably the single most powerful function in the re
module. Above we used re.search() to find the first match for a pattern.
findall() finds *all* the matches and returns them as a list of strings,
with each string representing one match.

  ## Suppose we have a text with many email addresses
  str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

  ## Use findall() to return a list of all email strings

  emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']

  for email in emails:
    print email

#   +--------------------+
#---| findall With Files |-----------------------------------------------------
#   +--------------------+

For files, you may be in the habit of writing a loop to iterate over the
lines of the file, and you could then call findall() on each line.
Instead, let findall() do the iteration for you -- much better! Just
feed the whole file text into findall() and let it return a list of all
the matches in a single step (recall that f.read() returns the whole
text of a file in a single string):

  f = open('test.txt', 'r')

  # Feed the file text into findall(); it returns a list of all the found strings

  strings = re.findall(r'some pattern', f.read())

#   +--------------------+
#---| findall and Groups |-----------------------------------------------------
#   +--------------------+

The parenthesis ( ) group mechanism can be combined with findall(). If
the pattern includes 2 or more parenthesis groups, then instead of
returning a list of strings, findall() returns a list of *tuples*. Each
tuple represents one match of the pattern, and inside the tuple is the
group(1), group(2) .. data. So if 2 parenthesis groups are added to the
email pattern, then findall() returns a list of tuples, each length 2
containing the username and host, e.g. ('alice', 'google.com').

  str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

  tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)

  for tuple in tuples:
    print tuple[0]  ## username
    print tuple[1]  ## host

Once you have the list of tuples, you can loop over it to do some
computation for each tuple. If the pattern includes no parenthesis, then
findall() returns a list of found strings as in earlier examples. If the
pattern includes a single set of parenthesis, then findall() returns a
list of strings corresponding to that single group. (Obscure optional
feature: Sometimes you have paren ( ) groupings in the pattern, but
which you do not want to extract. In that case, write the parens with a
?: at the start, e.g. (?: ) and that left paren will not count as a
group result.)

#   +-----------------------+
#---| RE Workflow and Debug |--------------------------------------------------
#   +-----------------------+

Regular expression patterns pack a lot of meaning into just a few
characters , but they are so dense, you can spend a lot of time
debugging your patterns. Set up your runtime so you can run a pattern
and print what it matches easily, for example by running it on a small
test text and printing the result of findall(). If the pattern matches
nothing, try weakening the pattern, removing parts of it so you get too
many matches. When it's matching nothing, you can't make any progress
since there's nothing concrete to look at. Once it's matching too much,
then you can work on tightening it up incrementally to hit just what you
want.

Options

The re functions take options to modify the behavior of the pattern
match. The option flag is added as an extra argument to the search() or
findall() etc., e.g. re.search(pat, str, re.IGNORECASE).

    IGNORECASE -- ignore upper/lowercase differences for matching, so
                  'a' matches both 'a' and 'A'.

    DOTALL -- allow dot (.) to match newline -- normally it matches
	      anything but newline. This can trip you up -- you think .*
	      matches everything, but by default it does not go past the
	      end of a line. Note that \s (whitespace) includes
	      newlines, so if you want to match a run of whitespace that
              may include a newline, you can just use \s*

    MULTILINE -- Within a string made of many lines, allow ^ and $ to
		 match the start and end of each line. Normally ^/$
		 would just match the start and end of the whole string. 

#   +----------------------------------+
#---| Greedy vs. Non-Greedy (optional) |---
#   +----------------------------------+

This is optional section which shows a more advanced regular expression
technique not needed for the exercises.

Suppose you have text with tags in it: <b>foo</b> and <i>so on</i>

Suppose you are trying to match each tag with the pattern '(<.*>)' --
what does it match first?

The result is a little surprising, but the greedy aspect of the .*
causes it to match the whole '<b>foo</b> and <i>so on</i>' as one big
match. The problem is that the .* goes as far as is it can, instead of
stopping at the first > (aka it is "greedy").

There is an extension to regular expression where you add a ? at the
end, such as .*? or .+?, changing them to be non-greedy. Now they stop
as soon as they can. So the pattern '(<.*?>)' will get just '<b>' as the
first match, and '</b>' as the second match, and so on getting each <..>
pair in turn. The style is typically that you use a .*?, and then
immediately its right look for some concrete marker (> in this case)
that forces the end of the .*? run.

The *? extension originated in Perl, and regular expressions that
include Perl's extensions are known as Perl Compatible Regular
Expressions -- pcre. Python includes pcre support. Many command line
utils etc. have a flag where they accept pcre patterns.

An older but widely used technique to code this idea of "all of these
chars except stopping at X" uses the square-bracket style. For the above
you could write the pattern, but instead of .* to get all the chars, use
[^>]* which skips over all characters which are not > (the leading ^
"inverts" the square bracket set, so it matches any char not in the
brackets).

#   +--------------+
#---| Substitution |---
#   +--------------+

The re.sub(pat, replacement, str) function searches for all the
instances of pattern in the given string, and replaces them. The
replacement string can include '\1', '\2' which refer to the text from
group(1), group(2), and so on from the original matching text.

Here's an example which searches for all the email addresses, and
changes them to keep the user (\1) but have yo-yo-dyne.com as the host.

  str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
  ## re.sub(pat, replacement, str) -- returns new string with all replacements,
  ## \1 is group(1), \2 group(2) in the replacement

  print re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str)

  ## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher

"""


#   +-------------+
#---| Basic usage |------------------------------------------------------------
#   +-------------+

line = "abc 300 xyz"
pattern = "^.*\s+(\d+)\s+.*$"
searched = re.search(pattern, line)

if searched:
  print
  print '     MATCHED PATTERN:', searched.re.pattern
  print '        COLUMN RANGE:', searched.start(),'-',searched.end()
  print '      MATCHED STRING:', searched.string
  print '   EXTRACTED INTEGER:', searched.group(1)

  value = searched.group(1)
  print
  print '               value:',value
  print '    type of value is:',type(value)

  ivalue = int(value)
  print
  print '              ivalue:',ivalue
  print '   type of ivalue is:',type(ivalue)

  fvalue = float(value)
  print
  print '              fvalue:',fvalue
  print '   type of fvalue is:',type(fvalue)




#   +--------------+
#---| Substitution |---
#   +--------------+

s = re.sub(r'bc|fg', ' ZZ ', 'abcdefgabcdefg')

print
print 's after substitution:', s




#   +---------------+
#---| Remove quotes |----------------------------------------------------------
#   +---------------+

searched = re.match("(\S+):(\S+)", line)

if searched:

  key = searched.group(1)
  if key.startswith('"') and key.endswith('"'):
      key = key[1:-1]
  
  value = searched.group(2)
  if value.startswith('"') and value.endswith('"'):
      value = value[1:-1]
  
  print '   found data line'
  print '   key:',key
  print ' value:',value




#   +------------+
#---| BARE BONES |-------------------------------------------------------------
#   +------------+

line = "SIP Session Status -- Period -- Lifetime --"

print
print 'Searching for \'sip session status\' (ignoring case)'

if re.search("session status", line, re.IGNORECASE):
  print 'OK'
else:
  print 'ERROR'

if re.search("sip session status", line):
  print 'ERROR'
else:
  print 'OK'

