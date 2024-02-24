#!/usr/bin/env python3
'''
NAME
    word_freq - Calculates word frequency in a text

SYNOPSIS
    word-freq [OPTION]... [FILE]...
    
DESCRIPTION
    Calculates word frequency in FILE and lists the result to standard output.

    With no FILE, read standard input.

    -a          Alphabetical order (Ascending)
    
    -d          Alphabetical order (Descending)
        
    -i          Ignore Case
    
    -m x        Show x most common

    -s x        Show words that contain x
'''

from jjcli import *
from collections import Counter

__version__ = "0.0.1"

def tokenizer(content):
    tokens = re.findall(r'\w+(?:\-\w+)?|[.,!_?;:—]+',content)
    return tokens

def sort(ocorr, option):
    if option == 1:
        ocorr = sorted(ocorr, key=lambda x: x[0])                     # Sorted by Ascending Alphabetical Order
    elif option == 2:
        ocorr = sorted(ocorr, key=lambda x: x[0], reverse=True)       # Sorted by Descending Alphabetical Order
    elif option == 3:  
        ocorr = sorted(ocorr, key=lambda x: x[1], reverse=True)       # Sorted by Number of Ocorrences
    return ocorr


def printf(ocorr, option):
    ocorr = sort(ocorr, option)
    for word, n_ocorr in ocorr:
        print(f'{word:<{23}}  {n_ocorr}')


def ignore_case(ocorr):
    holder = {}

    for word, n_ocorr in ocorr.items():
        lower = word.lower()
        if lower not in holder:
            holder[lower] = (word,n_ocorr,n_ocorr)
        elif n_ocorr > holder[lower][1]:
            holder[lower] = (word,n_ocorr,n_ocorr+holder[lower][2])
        else:
            holder[lower] = (holder[lower][0],holder[lower][1],n_ocorr+holder[lower][2])

    return {word: total_ocorr for _, word, _, total_ocorr in holder.items()}


def check_substring(ocorr, substring):
    return filter(lambda item: substring in item[0], ocorr.items())


def main():
    cl = clfilter("adm:is:", doc=__doc__)

    for txt in cl.text():
        words = tokenizer(txt)
        ocorr = Counter(words)
    
        if "-m" in cl.opt:
            printf(ocorr.most_common(int(cl.opt.get("-m"))), 3)
        elif "-a" in cl.opt:
            printf(ocorr.items(), 1)
        elif "-d" in cl.opt:
            printf(ocorr.items(), 2)
        elif "-i" in cl.opt:
            printf(ignore_case(ocorr).items(), 1)
        elif "-s" in cl.opt:
            printf(check_substring(ocorr,cl.opt.get("-s")), 3)
        else:
            printf(ocorr.items(), 3)