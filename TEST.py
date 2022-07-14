import os
import re
import numpy as np
import _pickle as pickle
START = '*'
OTHER = 'O'
VOWEL_SYMBOLS = {'ٌ', 'ً', 'ٍ', 'ُ', 'َ', 'ِ', 'ْ', 'ٌّ', 'ّ'}
VOWEL_REGEX = re.compile('|'.join(VOWEL_SYMBOLS))
def word_iterator(word):
    output = []
    prev_char = word[0]
    for idx, char in enumerate(word[1:]):
        try:
            # first 1 because we skipped the first character
            # second 1 because it's the next character
            next_char = word[idx + 1 + 1]
        except IndexError:  # will happen with the last character only
            next_char = ''
        if char in VOWEL_SYMBOLS:
            if next_char == '' and prev_char not in VOWEL_SYMBOLS:
                output.append((prev_char, char))
            elif prev_char not in VOWEL_SYMBOLS and next_char not in VOWEL_SYMBOLS:
                output.append((prev_char, char))
            elif prev_char not in VOWEL_SYMBOLS and next_char in VOWEL_SYMBOLS:
                output.append((prev_char, char + next_char))
        else:
            # if a character wasn't diacritized
            if prev_char not in VOWEL_SYMBOLS:
                output.append((prev_char, OTHER))
            if next_char == '':
                output.append((char, OTHER))
        prev_char = char
    return output

def create_dir(name):
    if not name:
        return
    name = str(name)
    if not os.path.isdir(name):
        os.makedirs(name)

def clean_word(word):
    return re.sub(VOWEL_REGEX, '', word)

def evaluate_word(gold_word, predicted_word, analysis=False):
    correct = 0.  # number of correct tags
    total_num = 0.  # total count of tags
    gold_tags = [tag for _, tag in word_iterator(gold_word)]
    predicted_tags = [tag for _, tag in word_iterator(predicted_word)]
    assert len(gold_tags) == len(predicted_tags)
    for gold_tag, predicted_tag in zip(gold_tags, predicted_tags):
        total_num += 1
        if gold_tag == predicted_tag:
            # print(gold_tag, predicted_tag)
            correct += 1.
    if analysis:
        return correct, total_num
    else:
        return correct / total_num

