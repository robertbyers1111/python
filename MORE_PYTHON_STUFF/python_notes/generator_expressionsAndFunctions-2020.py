
# From: https://www.dataquest.io/blog/python-generators-tutorial/
# 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# !!! This is worth rereading !!!
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
# Python generators are a powerful, but misunderstood tool. They?re often treated as too difficult a concept for beginning programmers to learn
# - creating the illusion that beginners should hold off on learning generators until they are ready. I think this assessment is unfair, and
# that you can use generators sooner than you think. In this tutorial, we?ll cover:
# 
#     The basic terminology needed to understand generators
#     What a generator is
#     How to create your own generators
#     How to use a generator and generator methods
#     When to use a generator
# 
# Prereqs
# 
# To get the most out of this tutorial, you should be familiar with the following concepts:
# 
#     Basic Python data structures
#         What a list is
#         What a dictionary is
# 
#     Functions
#         What a function is
#         How to create and use functions
# 
#     List Comprehensions
#         What a list comprehension is
#         How to create a simple list comprehension
# 
# Basic terms to know
# 
# Iteration and iterables
# 
# Iteration is the repetition of some kind of process over and over again. Python?s
# 
# for loop gives us an easy way to iterate over various objects. Often, you?ll iterate over a list, but we can also iterate over other Python
# objects such as strings and dictionaries.
# 
# # Iterating over a list
# ez_list = [1, 2, 3]
# for i in ez_list:
#     print(i)
# >>> 1
# >>> 2
# >>> 3
# 
# # Iterating over a string
# ez_string = "Generators"
# for s in ez_string:
#     print(s)
# >>> "G"
# >>> "e"
# ...
# >>> "r"
# >>> "s"
# 
# # Iterating over a dictionary
# ez_dict = {1 : "First, 2 : "Second"}
# for key, value in ez_dict.items():
#     print(k, v)
# >>> 1 "First"
# >>> 2 "Second"
# 
# In each of the above examples, the for loop iterates over the sequence we give it. The code above used a list, string, and dictionary, but
# you can iterate over tuples and sets as well. In each loop above, we print each of the items in the sequence in the order they appear. For
# example, you can confirm that the order of the ez_list is replicated in the order that its items are printed out. For Loop Anatomy We refer
# to any object that can support iteration as an iterable.
# 
# 
# What defines an iterable?
# 
# Iterables support something called the Iterator Protocol. The technical definition for the Iterator Protocol is out of the scope of this
# article, but it can be thought of as a set of requirements to be used for a for loop. That is to say: lists, strings and dictionaries all
# follow the Iterator Protocol, therefore we can use them in for loops. Conversely, objects that do not follow the protocol cannot be used in a
# for loop. One example of an object that does not follow the protocol is an integer. If we try to give an integer to a for loop, Python will
# throw an error.
# 
# number = 12345
# for n in number:
#     print(n)
# >>> TypeError: 'int' object is not iterable
# 
# An integer is just a singular number, not a sequence. You may argue that the ?first? number in number is 1, but it is not the same as the
# first item in a sequence. It doesn?t make sense to ask ?What?s after 1?? from number since Python only understands integers as a single
# entities. Therefore, one of the requirements to be an iterable is to be able to describe to the for loop what the next item to perform the
# operation on is. For example, lists tell the for loop that the next item to iterate on is in the index+1 from the current one (1 comes after
# 0). Consequently, an iterable must also signal to a for loop when to stop iterating. This signal usually comes when we arrive at the end of a
# sequence (i.e. the end of a list or string). We will explore the specific functions that make something iterable later in this article, the
# important thing to know is that iterables describe how a for loop should traverse its contents.  Generators are iterables themselves. As
# you?ll see later, for loops are one of the main ways we use a generator, so they must be able to support iteration. We?ll delve into how we
# can create our own generators in the next secton.
# 
# Key takeaways: basic terms to know
# 
#     Iteration is the idea of repeating some process over a sequence of items. In Python, iteration is usually related to the for loop.
#     An iterable is an object that supports iteration.
#     To be an iterable, it must describe to a for loop two things:
# 
#         What item comes next in the iteration.
#         When should the loop stop iteration.
#         Generators are iterables.
# 
# A data-based approach
# 
# To truly explore generators, we?ll use the Brewer?s Friend Beer Recipes data set from Kaggle. You can find the data set here, if you?d like
# to follow along on your own computer. The data contains important beer characteristics from brewers around the world, including style of
# beer, alcohol by volume (ABV), and amount of beer produced. For the purposes of this article, let?s say that we are interested in brewing our
# own beer. Perhaps we want to sell our beer, so we would like to see what others have done to inform our brewing choices and produce more
# popular beer styles. Author?s Note: The ?Name? column in the original data set contains some messy values that interfere with our analysis.
# You can find a cleaned version that will serve our purposes here.
# 
# Generators and you
# 
# If you?ve never encountered a generator before, the most common real-life example of a generator is a backup generator, which creates -
# generates - electricity for your house or office. Conceptually, Python generators generate values one at a time from a given sequence,
# instead of giving the entirety of the sequence at once. This one-at-a-time fashion of generators is what makes them so compatible with for
# loops. If this sounds confusing, don?t worry too much. As we explain how to create generators, it will become more clear. There are two ways
# to create a generator. They differ in their syntax, but the end result is still a generator. We?ll teach these concepts by covering their
# syntax and comparing them to a similar, but non-generator equivalent.
# 
#     A generator function versus a regular function
#     A generator expression versus a list comprehension
# 
# The generator function
# 
# A generator function is just like a regular function but with a key difference: the yield keyword replaces return.
# 
# # Regular function
# def function_a():
#     return "a"
# 
# # Generator function
# def generator_a():
#     yield "a"
# 
# The two functions above perform exactly same action (returning/yielding the same string). However, if you try to inspect the generator
# function, it won?t match what the regular function shows.
# 
# function_a()
# >>> "a"
# 
# generator_a()
# 
# >>> <generator object a at 0x000001565469DA98>
# 
# Calling a regular function tells Python to go back to where the function is located in our code, perform the code within the block, and
# return the result. In order to get the generator function to yield its values, you need to pass it into the next() function. next() is a
# special function that asks, ?What?s the next item in the iteration?? In fact, next() is the precise function that is called when you run a
# for loop! Lists, dictionaries, strings, and the like all implement next(), so this is why you can incorporate them into loops in the first
# place.
# 
# # Asking the generator what the next item is
# 
# next(a())
# >>> "a"
# 
# # Do not do this
# 
# next(a)
# 
# Notice that we have to pass in generator function with the parentheses since the function itself is the generator. Providing only the
# function name will throw an error since you?re trying to give next() a function name. As expected, the generator function will yield ?a? once
# we invoke the next() function. This example is not fully representative of what a generator is useful for. Remember that generators produce a
# stream of values, so yielding a single value doesn?t really qualify as a stream. To do this, we can actually put in multiple yield statements
# into a generator function. These yield statements form the sequence that the generator will output. We?ll create a generator and bind it to a
# varible mg. Then, if we keep passing mg into next(), we?ll get to the next yield. If we keep going past, we?ll be given a StopIteration error
# to tell us that the generator has no more values to give. The StopIteration error is actually how a for loop knows when to stop iterating.
# 
# def multi_generate():
#     yield "a"
#     yield "b"
#     yield "c"
# 
# mg = multi_generate()
# next(mg)
# >>> "a"
# 
# next(mg)
# >>> "b"
# 
# next(mg)
# >>> "c"
# 
# next(mg)
# >>> StopIteration:
# 
# Assigning
# 
# multi_generate to mg is a crucial step in using a generator function. Binding a generator to mg allows us to create a single instance of a
# generator we can refer back to. We can continue passing mg into next() and get those other yield statements. Observe what happens if we just
# keep trying to pass in multi_generate itself.
# 
# next(multi_generate())
# >>> "a"
# next(multi_generate())
# >>> "a"
# 
# It?s easy to think of generators as a machine that waits for one command and one command only: next().
# 
# Once you call next() on the generator, it will dispense the next value in the sequence it is holding. Otherwise, you can?t do much else with
# a generator. The image below represents our generator as a simple machine. Generators 1 We continue to get the result of the first yield
# statement. The reason behind this is subtle. When we pass the generator function itself into next(), Python assumes you are passing a new
# instance of multi_generate into it, so it will always give you the first yield result. By binding the generator to a variable, Python knows
# you are trying to act on the same thing when you pass it into next(). We?ve noted that as we keep passing in mg into next, we get the other
# yield results. This is possible only if the generator somehow remembers what it last did. This memory is what distinguishes generator
# functions from regular functions! Once you use a function, it?s a one-and-done deal. Once you return the value from the function. A generator
# will keep yielding values until its out. This brings us to another important property of generators. Once we?ve finished iterating through
# them, we can?t use them anymore. Once we got through all three yield values in mg, it can?t provide anything to us anymore. We?d have to
# store another instance of the multi_generate generator to begin asking next() statements of it again. Our data still hasn?t been read in yet,
# so let?s do that with a generator function. The data is called recipeData.csv, and its contained in a CSV file. We?ll use the open() function
# to enable us to read it, and we?ll start using next() function to read what the first few lines of the CSV are.
# 
# # Creating a generator that will generate the data row by row
# def beerDataGenerator():
#     file = "recipeData.csv"
#     for row in open(file, encoding="ISO-8859-1"):
#         yield row
# 
# We?ll slowly dissect the above code:
# 
#     We?ve designated dataGenerator as our generator function that will dispense our CSV file row by row. The function includes the name of
#     the file in file, and this enables us to use the open() function to be able to read it.
# 
#     While we?ve discussed that Python objects like lists and dictionaries can be iterated over, we can also iterate over files that we open()
#     as well.
# 
#     The encoding tells Python what kinds of characters it should expect to see; ISO-8859-1 specifically refers to Latin-1.
# 
#     The for loop will start with the first row in the CSV file, yield that row, and then save its current place in reading the file until the
#     generator function is called again.
# 
# If you?re following along with the data on your own computer, you?ll need to replace file with the exact path on your computer to where the
# file is located. This will enable Python to find it when you want to open() it.
# 
# # Remember to store an instance of the generator so we can refer back to it
# beer = beerDataGenerator()
# next(beer)
# >>> 'BeerID,Name,URL,Style,StyleID,Size(L),OG,FG,ABV,IBU,Color,BoilSize,BoilTime,BoilGravity,Efficiency,MashThickness,SugarScale,BrewMethod,PitchRate,PrimaryTemp,PrimingMethod,PrimingAmount,UserId\n'next(beer)
# >>> '1,Vanilla Cream Ale,/homebrew/recipe/view/1633/vanilla-cream-ale,Cream Ale,45,21.77,1.055,1.013,5.48,17.65,4.83,28.39,75,1.038,70,N/A,Specific Gravity,All Grain,N/A,17.78,corn sugar,4.5 oz,116\n'
# 
# Once we?ve created a beerDataGenerator in beer, we can start passing it into next() to look at the data itself. As the CSV file suggests, the
# columns are separated by commas. Furthermore, each row ends with an \n, which indicates a line break. We found that the first item in
# recipeData.csv to is a list of column names and the first row to describe a delicious Vanilla Cream Ale.
# 
# A self-imposed restriction
# 
# You may be asking, ?We can store the data in a list comprehension! Why jump through an extra hoop and use a generator?? As a programmer, you
# may encounter Big Data. This is a somewhat nebulous term, and so we won?t delve into the various Big Data definitions here. Suffice to say
# that any Big Data file is too big to assign to a variable. Our data file doesn?t qualify as Big Data, but we can still learn a lot by
# imposing a restriction on ourselves to recreate this conundrum. We?ll assume for now that our beer data is so large in size that we are
# incapable of storing all of the data in a list of lists. With the normal route of reading in data blocked off, we are forced to reconsider
# our options. This is where generators come in. We?ll explain later precisely why generators work here, but until then we can rest assured
# that our generator function will enable us to read the data in the first place, albeit not all at once. Along with generator functions, we
# can also create generators using generator expressions.
# 
# The generator expression
# 
# Early, we compared our generator function to a regular function since they have many similar aspects. For generation expressions, we?ll use
# list comprehensions.
# 
# lc_example = [n**2 for n in [1, 2, 3, 4, 5]]
# 
# genex_example = (n**2 for n in [1, 2, 3, 4, 5])
# 
# lc_example is our list comprehension, while genex_example is our generator expression that performs almost the same task. Take note that the
# only difference between the two is that the generator expression is surrounded by parentheses, rather than brackets. If we either of these
# iterators in a for loop, they will produce the same result and will be indistinguishable. However, if we try to inspect these variables in
# our interpreter, they produce different results.
# 
# lc_example
# >>> [1, 4, 9, 16, 25]
# 
# genex_example
# >>> <generator object <genexpr> at 0x00000156547B4FC0>
# 
# This result is similar to what we saw when we tried to look at a regular function and a generator function. Python also recognizes that
# genex_example is a generator in generator expression form (). As lc_example is a list, we can perform all of the operations that they
# support: indexing, slicing, mutation, etc. We cannot do this with the generator expression. Generators are specialized as an easy to produce
# an output one-at-a-time, so they do not support these operations. However, like list comprehensions we can implement logic within generator
# expressions to form a filter if we needed it.
# 
# genex_example2 = (n**2 for n in [1, 2, 3, 4, 5] if n >= 3)
# next(genex_example2)
# >>> 9
# 
# Effectively, there is no difference in how we will use a generator function or generator expression. Once we have our generator expression,
# we can call next() on it to start getting the values it will produce. Once we go through all of the values that the generator expression can
# produce, we cannot use it anymore. This contrasts against a list comprehension, which we can reuse as much as we want.
# 
# next(genex_example)
# >>> 1
# 
# # Repeat until we reach the end...
# 
# next(genex_example)
# >>> 25
# next(genex_example)
# >>> StopIteration:
# 
# The idea that we can only use generators once is tied to the idea of their consumption. Recall that when we iterate over some iterator, we
# perform some operation on each of the values within. We then move on with our analysis using these processed values, meaning that typically
# we may not need the original iterator. Generators fit perfectly into this need, allowing us to form an iterator that we can use once and then
# not have to worry about it taking up space after we use it (in a for loop, for example). We talked about next() as the way to get the values
# from the generators, but its often better to use generators in for loops. Using next() forces us to have to deal with the StopIteration
# ourselves, but the for loop uses this to know when to stop!
# 
# # Using a for loop to consume a generator is better than using next()
# for ge in genex_example:
#     print(ge)
# >>> 1
# >>> 4
# >>> 9
# >>> 16
# >>> 25
# 
# One distinction that generator expressions have over functions is their succinctness. Generator functions take up multiple lines, whereas we
# can fit generator expressions in one line. Multiple lines are not bad in and of itself, but it opens up functions to greater complexity that
# may introduce bugs later on. We?ll rewrite our generator function as a one-line expression that read in our beer data. This conciseness that
# will come in handy later in the article.
# 
# beer_data = "recipeData.csv"
# 
# # This one line perfoms the same action as beerDataGenerator()!
# 
# lines =  (line for line in open(beer_data, encoding="ISO-8859-1"))
# 
# Key takeaways: generators and you
# 
#     Generators produce values one-at-a-time as opposed to giving them all at once.
#     There are two ways to create generators: generator functions and generator expressions.
#     Generator functions yield, regular functions return.
#     Generator expressions need (), list comprehensions use [].
#     You can only use a generator once.
#     There are two ways to get values from generators: the next() function and a for loop. The for loop is often the preferred method.
#     We can use generators to read files and give us one line at a time.
# 
# Generators: motivation and uses
# 
# Earlier, we discussed imposing a restriction on ourselves that forced us to use a generator to read our data instead of reading it into a
# list of lists. We cited the problem of Big Data and an our inability to store it all in one variable. While calling it a Big Data problem is
# still correct, you may also call it a memory problem. Let?s say that you have an older laptop with about 4GB of RAM, random access memory.
# The true size of our beer data set is only about 3MB, but suppose that we asked everyone around the globe to give us their recipes, resulting
# in a data set around 3GB. If we were to read the entirety of our data set into a variable, it would take up a bit more than 3GB of RAM! This
# would leave us with little room for other operations, much less other variables of similar size. Storing our data in a list of lists would
# take up so much memory that any analyses we do would take excruciatingly long to do.
# 
# Laziness and generators
# 
# We know now that generators produce a single value from a defined sequence, but only when we ask next() or within a for loop. We call this
# lazy evaluation. Generators are lazy because they only give us a value when we ask for it. The flipside here is that only that single value
# takes up memory. The ultimate result is that generators are incredibly memory efficient, which makes it a perfect candidate for reading and
# using Big Data files. Once we ask for the next value of a generator, the old value is discarded. Once we go through the entire generator, it
# is also discarded from memory as well.
# 
# Generators feeding generators
# 
# We currently haven?t learned anything from the beer data. All we?ve done so far is to take the original CSV file and create a generator that
# will yield each line in the CSV, one at a time in the form of a string. Unless we?d like to do some crazy string manipulation, we?ll need to
# think of a way to get our data into a readable, useable form. Below is a representation of what our code currently does: a simple read from
# file and output of a single line from the file.
# 
# Generators 2
# 
# Generators come to the rescue again here! So far in the article, we?ve been passing in other structures, specifically iterators, to the
# generators to indicate what sequence we?d like to generate from. However, generators are iterators themselves too - why don?t we create
# another generator that takes the output another generator? Our lines generator outputs the line in its entirety, so we?ll make a second
# generator that does some formatting for us.
# 
# beer_data = "recipeData.csv"
# lines = (line for line in open(beer_data, encoding="ISO-8859-1"))
# lists = (l.split(",") for l in lines)
# 
# The end result of our generators is a stream of lists, each containing the data within a row of the CSV. If we iterate through lists, we?ll
# be able to easily access the data elements within and perform the analyses we need! We?ve effectively made a pipeline for our data set,
# starting from the raw data set and sending it through 2 generators to get it into a familiar form. Remember that generators aren?t lists
# themselves, they merely generate a single element of a sequence and only take up the amount that element needs. By piping generators
# together, we?ve created a quick, easy-to-read way for us to read data that would be inaccessible through normal means. There?s some real
# power to this approach, and its significance can?t be understated. We didn?t need to create any temporary lists to hold intermediate values
# as we processed them. With the additional generator in the pipeline, our code might look like this: Generators 3 In this pipeline, each
# generator is put in charge of a single operation that will eventually be applied to all rows of the data set. Although having each list is
# good, there?s still some small issues that need to be addressed before we can do any meaningul analyses. First, we?d like to take the column
# names since they aren?t data and then turn them into a dictionary that would make any further code easier to read. Note: if you?re running
# this code on your own machine, you must remember that you can only use generators once. If you use the generator in a for loop to view the
# output, you?ll need to run the data and the whole pipeline again. Thankfully, the generators run fast here.
# 
# beer_data = "recipeData.csv"
# lines = (line for line in open(beer_data, encoding="ISO-8859-1"))
# lists = (l.split(",") for l in lines)
# 
# # Take the column names out of the generator and store them, leaving only data
# columns = next(lists)
# 
# # Take these columns and use them to create an informative dictionary
# beerdicts = (dict(zip(columns, data)) for data in lists)
# 
# The beerdicts does some simple formatting, which gives our pipeline even more power! Generators 4 This is a great place to start inquiring
# our data about our future beer brewing choices. Now that we have our generator pipeline in place, we can start consuming the data produced by
# the generators and create some insights. We usually consume generators using for loops, so we?ll use one to figure out what the most popular
# type of homebrewed beer is.
# 
# beer_counts = {}
# for bd in beerdicts:
#     if bd["Style"] not in beer_counts:
#         beer_counts[bd["Style"]] = 1
#     else:
#         beer_counts[bd["Style"]] += 1
# 
# most_popular = 0
# most_popular_type = None
# for beer, count in beer_counts.items():
#     if count > most_popular:
#         most_popular = count
#         most_popular_type = beer
# 
# most_popular_type
# >>> "American IPA"
# 
# This operation is ubiquitous in data wrangling and processing, and you?ve probably seen it before. The only new thing here is that instead of
# referring back to a list of lists containing our data, we rely on dictionaries that are produced by our generators. With generators, we are
# able to make the same inquires we?d want from any Big Data set as we would a regular-sized one. We now know that American IPAs are the most
# popular homebrewed beer in the data set, and we know how many entries they have in the data. We can try figuring out how strong our beer
# should be. This data is contained in the ?ABV? (Alcohol By Volume) key. Since we are working with dictionaries as the output of our generator
# stream, why don?t we add another generator to hone in on the exact values we want to output.
# 
# abv = (float(bd["ABV"]) for bd in beerdicts if bd["Style"] == "American IPA")
# 
# # Get the average ABV for an American IPAsum(abv)/most_popular
# >>> 6.44429396984925
# 
# This last generator forms the last of our pipeline, as visualized below:
# 
# Generators 5 We should take special note of our use of sum() with the abv generator. It is not immediately intuitive that sum() will sum up
# all of the ABV values that it receives. You may think of sum() as reducing the whole output of the generator into one value. By dividing this
# sum by the number of American IPA entires there are, we got the average. Our data suggests that your average American IPA is about 6.4%
# alcohol by volume! Our last generator abv takes the dictionaries that are output by beerdicts and outputs the ABV key, but only if the beer
# is an American IPA. Filters on our generator expression form a powerful tool in our pipeline. If we think of each successive generator as a
# modular component, we can then swap out generators for others that may have a more desirable functionality. If we wanted to change what kind
# of beer we wanted to investigate or look at another beer characteristic, the only thing we need to change is the generator operation. The
# picture below expresses the different parts of the generator pipeline approach. It consists of some raw data you want to process, the
# pipeline that does the actual processing, and the final consumption of the output of this pipeline. Following this pattern will enable you to
# reenact what we?ve done with the beer data. Generator Pipeline If you?re used to the workflow of using a list of lists and leveraging all the
# list methods to do your analyses, this new approach to data wrangling might be strange. However, the data pipeline is a powerful concept that
# can be immediately incorporated into your code and you should try it.
# 
# Infinite generation
# 
# Let?s say that it?s been a few years since you first made that analysis on the beer data set. You used the insights from your analyses to
# create a successful American IPA, and you only have generators to thank. You produce thousands of bottles of your beer each day, and you need
# a way to analyze the quality of each batch. You go back to your old laptop to fire up the Python interpreter. You begin to write up a
# function to calculate and check the various qualities of your beer batches as you make them, but then you stop. You don?t know how much beer
# you?re going to make in advance. Analyzing the batches by day could offer discrete points for us to look at, but what if we want continuous
# data? Regular functions would not work here! They expect some arguments and will always return a discrete object. You can?t conceivably give
# a regular function a stream of data and return a continuous stream of values. But you can with generators! Generators are well suited to this
# type of task. We?ve discussed how generators will yield values one-at-a-time until it?s told to stop. If we never give a generator a stopping
# signal, it will happily generate these values ad infinitum. Take the example below.
# 
# function alwaysBeer():
#     while True:
#         yield "Beer"
# 
# The while loop will always be true, so the generator function will always be yielding beer. We haven?t done anything wrong, this is
# completely valid code (although not one you?d actually want to implement)! How would this ?infinite? stream of beer fit into our timeline? In
# our original look at the beer data set, the CSV was originally a set amount of lines. If you could automate your brewing process to output
# this data to a similar CSV and continuously update it, all you need to do to run your analyses would be to run the data through the
# generators again! You could conceivably create a generator in your pipeline to catch any batches that don?t meet your expectations and flag
# them in real time! Unfortunately, we don?t have said data, but this thought experiment should offer another compelling use case for the
# Python generator. With generators, you could even tackle infinity (in some cases).
# 
# Key takeaways: motivation and uses behind generators
# 
#     Generators are memory efficient since they only require memory for the one value they yield.
#     Generators are lazy: they only yield values when explicitly asked.
#     You can feed the output of a generator to the input of another generator to form data pipelines.
#     Data pipelines can be modularized and customized to your needs.
#     Generators are useful for generating values ad infinitum.
# 
# Conclusion
# 
# Generators don?t have to be complicated topics, they have a place in any Python programmer?s repertoire if given the time to be understood.
# Even in Big Data situations where simpler methods fall short, generator-based analyses still stand tall. There?s a lot about generators that
# we didn?t discuss here, but it should still give you a good foundation to start using them in your own analytic life.
# 
# Further Resources:
# 
#     Python Tutorials - Our ever-expanding list of Python tutorials for data science.
#     Data Science Courses - Take your studies to the next level with fully interactive programming, data science, and stats courses, right in your browser.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MY DEMO

#   +----------------------+
#---| Expression generator |---
#   +----------------------+

squares_under_10 = (number*number for number in range(10) if number*number < 10)

for x in squares_under_10:
    print("{}".format(x),end=' ')

# Second time nothing - generators are a one time thing (!)

for x in squares_under_10:
    print("{}".format(x),end=' ')

#   +--------------------+
#---| Function generator |---
#   +--------------------+

def sq_un_10():
    for number in range(10):
        if number*number < 10:
            yield number*number

gen = sq_un_10()

print("")
for x in gen:
    print("{}".format(x),end=' ')

# Second time works IFF we create a new instance for the variable (!)

gen = sq_un_10()

print("")
for x in gen:
    print("{}".format(x),end=' ')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From: https://www.dataquest.io/blog/python-generators-tutorial/
