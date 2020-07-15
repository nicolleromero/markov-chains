"""Generate Markov text from text files."""
import re
import sys
import random
from pprint import pprint


def open_and_read_file():
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(str(sys.argv[1])).read()

    return contents


def make_chains():
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # Open the file and turn it into one long string
    contents = open_and_read_file()


    # List of individual words
    words_list = re.split('\s+', contents)

    if '' in words_list:
        words_list.remove('')
    
    # new_list is a list of tuples (that correspond to keys)
    new_list = []
    for i, word in enumerate(words_list[:-1]):
        new_list.append((words_list[i], words_list[i + 1]))

    for idx, tup in enumerate(new_list[:-1]):
        next_word = new_list[idx + 1][1]
        values = chains.setdefault(tup, [])
        
        values.append(next_word)

    return chains



def make_text():
    """Return text from chains."""

    # Get a Markov chain
    chains = make_chains()
    chain_keys = list(chains.keys())

    # Must start with a a capital
    while True:
        try:
            max = len(chains.keys()) - 1
            phrase = chain_keys[random.randint(0, max)] 
            phrase_list = chains[phrase]
            random_word = phrase_list[random.randint(0, (len(phrase_list)) - 1)]

            if random_word and random_word[0].isupper():
                break

        except:
            break

    words = [random_word]
    phrase = (phrase[1], random_word)

    while True:
        try:
            max = len(chains[phrase]) - 1
            random_word = chains[phrase][random.randint(0, max)]
            words.append(random_word)
            phrase = (phrase[1], random_word)


        except:
            break


    return " ".join(words)


# Produce random text
pprint(make_text())

