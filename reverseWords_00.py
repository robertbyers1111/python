#!/usr/bin/python

#   +------------------+
#---| class 'Sentence' |----------------------------------------
#   +------------------+

class Sentence:

    def __init__(self, sentence):
        self.orig = sentence

        self.words = []
        for word in self.orig.split():
            self.words.append(word)

    def reverse(self):

        length = len(self.orig.split())

        self.reversed = []

        for i in range(length-1, -1, -1):
            self.reversed.append(self.words[i])

    def showReversed(self):
        for word in self.reversed:
            print(word)

#-- TESTING ----------------------------------------------------

if __name__ == "__main__":
    sentence = Sentence('a man a plan a canal, panama')
    sentence.reverse()
    sentence.showReversed()

