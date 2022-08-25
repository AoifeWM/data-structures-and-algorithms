import re
from operator import itemgetter

from data_structures.hashtable import Hashtable


def first_repeated_word(str):
    ht = Hashtable()
    text = clean_str(str)
    for word in text.split():
        if ht.contains(word):
            return word
        ht.set(word, ' ')
    return None


def word_count(str):
    ht = Hashtable()
    text = clean_str(str)
    for word in text.split():
        # when the hashtable reaches a collision, get its value, increment by 1, and overwrite it to the new value
        count = 1
        if ht.contains(word):
            count += ht.get(word)
        ht.set(word, count)
    # clean up the hashtable into a useable dictionary
    return hash_table_to_dict(ht)


def hash_table_to_dict(ht):
    # the hashtable has all words with their appearance count. they still need to be sorted from most to least frequent
    # get all keys into a list
    all_words = ht.keys()
    # modify the list in place to replace each key with a corresponding dict in this format:
    # {'name': 'Example', 'number':3}
    all_words = [{'name': word, 'number': ht.get(word)} for word in all_words]
    # Sort this list by the number value. reverse so the highest frequency words appear first.
    all_words = sorted(all_words, key=itemgetter('number'), reverse=True)
    # reformat the list into a dict in the format: {'example': 3, 'words':2, 'etc': 2, ... }
    all_words = {word['name']: word['number'] for word in all_words}
    return all_words


def clean_str(str):
    text = str.lower()
    # remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    return text
