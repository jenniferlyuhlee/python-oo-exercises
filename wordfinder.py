from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary.
    
    >>> test = WordFinder("words.txt")
    235886 words read

    >>> test.random() in test.words
    True

    >>> test.random() in test.words
    True

    >>> test.random() in test.words
    True
    
    """
    
    def __init__(self, path):
        """Opens file and prints how many words were read """
        self.file = open(path)
        self.words = self.make_list(self.file)
        print (f"{len(self.words)} words read")

    def make_list(self, file):
        "Makes list of words"
        return [word.strip() for word in file]

    def random(self):
        """Returns random word"""
        return choice(self.words)



class SpecialWordFinder (WordFinder):
    """WordFinder that excludes blank lines(empty strings) and category titles (#)
    
    >>> test2 = SpecialWordFinder("complex.txt")
    4 words read
    
    >>> test2.random() in test2.words
    True

    >>> test2.random() in test2.words
    True
    
    """

    def make_list(self, file):
        return [word.strip() for word in file if word.strip() and word.strip()[0] != "#"]



