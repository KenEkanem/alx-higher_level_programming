#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if lenght > 0:
        first_char = (lenght, sentence[0])
    else:
        first_char = (lenght, None)
    return (first_char)
