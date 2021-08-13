#!/usr/bin/python

class Sentence:

    def __init__(self, sentence):
        self.sentence = sentence
        self.reversed_words = None

    def reverse_words(self):
        wordList = self.sentence.split()
        wordList.reverse()
        self.reversed_words = ' '.join(wordList)

    def show(self):
        print()
        print(self.sentence, '(original)')
        if self.reversed_words:
            print(self.reversed_words, '(reversed by words)')
        else:
            print('(not yet reversed)')

if __name__ == "__main__":
    w = Sentence('A man, a plan, a canal, Panama')
    w.reverse_words()
    w.show();
