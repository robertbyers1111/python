
###
# FROM: https://stackoverflow.com/questions/15302386/advanced-for-loops

###
# [Question]

# I have a list of lists of lists(that last list doesn't really matter)

#[code] data = [[[['f', 0], 'C'], [['X', 0], 'X']], [[['s', 1], 'X'], [['X', 0], 'X']]]

# It is essentially a map with 4 quadrants. Currently I am iterating
# through it and updating it with

#[code] for i in data:
#[code]     for x in i:
#[code]         if x[0][0] == 'f':
#[code]             x[0][1] += 1

# but I want to check a cell's neighbors. Is there a way to do it, when
# iterating by this or will i have to resolve to move through the list
# with integer keys?

###
# [Answer]

# Yes, unless you write something more complex that allows you to iterate
# over the elements that also gives you their neighbors, you will have to
# use absolute addressing of the elements.

# If you are certain to always use a lists of lists (i.e. not just some
# other iterable), you can certainly make use of enumerate to get both
# the index and the element itself quickly:

#[code] for i, row in enumerate(data):
#[code]     for j, cell in enumerate(row):
#[code]         # now you can access data[i][j-1], data[i+1][j] etc

# So, I mentioned the “more complex” thing first and what you could do is
# make a generator which iterates over the cells automatically and also
# returns additional data like for example the left neighbor or
# something.

#[code] def myLeftNeighborGenerator(data):
#[code]     for i, row in enumerate(data):
#[code]         for j, cell in enumerate(row):
#[code]             leftNeighbor = data[i][j-1] if j > 0 else None
#[code]             yield cell, leftNeighbor

# Then you could just use that generator to magically get your data:

#[code] for x, left in myLeftNeighborGenerator(data):
#[code]     if x[0][0] == 'f':
#[code]         x[0][1] += 1
#[code]     if left is not None:
#[code]         # whatever


def myLeftNeighborGenerator(data):
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            leftNeighbor = data[i][j-1] if j > 0 else None
            yield cell, leftNeighbor

data = [
  [ [['f', 0], 'C' ], [['X', 0], 'X' ] ], 
  [ [['s', 1], 'X' ], [['X', 0], 'X' ] ],
  [ [['f', 1], 'z' ], [['f', 9], 'f' ] ],
  [ [['z', 1], 'z' ], [['z', 0], 'z' ] ],

]

for x, left in myLeftNeighborGenerator(data):
    print()
    print('left:',left)
    print('   x:',x)
    if x[0][0] == 'f':
        x[0][1] += 1
    if left is not None:
        a=7
