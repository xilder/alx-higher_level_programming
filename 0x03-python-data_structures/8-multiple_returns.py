#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_length = 0
    first_char = None
    if sentence:
        first_char = sentence[0]
        sentence_length = len(sentence)
    return (sentence_length, first_char)
