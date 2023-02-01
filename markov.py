"""Generate Markov text from text files."""

from random import choice



def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()
    # print(contents)
    return contents
    # words = contents.split()
    # # print(words)
    # return words



    return 'Contents of your file as one long string'
# open_and_read_file('green-eggs.txt')

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

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

    words_list = text_string.split()
    # print(words_list)
    
    
    for i in range(len(words_list) - 1):
        word_key = (words_list[i], words_list[i + 1])
        word_value = chains.get(word_key, [])
        # word_value.append(words_list[i + 2])
        if i < len(words_list) - 2:
            # if word_key in chains:
            #     # existing_words = chains[word_key]
            #     # chains[word_key].append(words_list[i + 2])
            #     # chains[word_key] = word_value 
            # else: 
            #     word_value.append(words_list[i + 2])
            #     chains[word_key] = word_value
            word_value.append(words_list[i +2])
        else:
            # # continue
            # if word_key in chains:
            #     chains[word_key].append(None)
            # else: 
            word_value.append(None)
            #     chains[word_key] = word_value
        chains[word_key] = word_value
            

    return chains    


def make_text(chains):
    """Return text from chains."""
    words = []
    first_words = choice(list(chains.keys()))
    next_word = choice(chains[first_words])
    words.extend(first_words)
    words.append(next_word)
    # print(words)

    while next_word != None:
        find_key = (words[-2], words[-1])
        next_word = choice(chains[find_key])
        words.append(next_word)
        # print(f"{find_key}, {next_word}")

    # words.remove(words[-1])
    words.pop()
    # print(words)
        

    return ' '.join(words)



input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
 