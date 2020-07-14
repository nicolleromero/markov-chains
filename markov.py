"""Generate Markov text from text files."""
import re
import sys
import random


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

    words_list = re.split('\s|\n', contents)

    words_list.remove('')

    new_list = []

    i = len(words_list)
    for i, word in enumerate(words_list):
        new_list.append((words_list[i - 1], words_list[i]))

    for tup in new_list:
        chains[tup] = []

    temp = []
    idx = 0

    while idx < len(new_list) - 1:
        for k,v in chains.items():
            if k == new_list[idx]:
                v.append(new_list[idx + 1][1])
        idx += 1

    for k,v in chains.items():
        if v == []:
            to_delete = k

    del chains[to_delete]

    for k,v in chains.items():
        if k[0] == words_list[-1] and k[1] == words_list[0]:
            to_delete = k

    del chains[to_delete]

    # del chains[('I', 'am?')]
    # del chains[('am?', 'Would')]

    # print(chains)
    # print(len(chains))

    return chains



def make_text():
    """Return text from chains."""

    words = []

    # Get a Markov chain
    chains = make_chains()
    max = len(chains.keys()) - 1

    chain_keys = list(chains.keys())
    phrase = chain_keys[random.randint(0, max)] 
    start_phrase_list = chains[phrase]

    end = ''
    end = list(chains.items())[-1]
    stop = end[0][1] + " " + end[1][0]

    random_word = start_phrase_list[random.randint(0, (len(start_phrase_list)) - 1)]
    
    words.append(phrase[0] + " " + phrase[1] + " " + random_word)

    phrase = (phrase[1], random_word)

    while True:
        try:
            random_word = chains[phrase][random.randint(0, (len(chains[phrase])) - 1)]
            words.append(random_word)
            phrase = (phrase[1], random_word)
        except:
            break

    final_text = " ".join(words)

    final_text = final_text[0:1].upper() + final_text[1:]

    return final_text




# Produce random text
random_text = make_text()

print(random_text)
