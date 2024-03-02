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

    -t          Output in Frequency Table
'''
import os
from jjcli import *
from collections import Counter


__version__ = "0.0.1"

def tokenizer(content):
    tokens = re.findall(r'\w+(?:\-\w+)?|[.,!_?;:—]+',content)
    return tokens


def printf(ocorr):
    for word, n_ocorr in ocorr:
        print(f'{word:<{23}}  {n_ocorr:<{7}}')


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
    return {word: total_ocorr for _,(word,_,total_ocorr) in holder.items()}


def check_substring(ocorr, substring):
    filtered_words = filter(lambda item: substring in item[0], ocorr.items())
    return {word: n_ocorr for word, n_ocorr in filtered_words}


def import_table(ocorr):
    total_ocorr = ocorr.total()
    with open(os.path.join(os.path.split(__file__)[0],"out.txt")) as file:
        stdvals = {}
        for line in file:
            value,expectedPerM = line.strip().split("   ")
            if ocorr[value]!=0:
                stdvals[value]=(total_ocorr*float(expectedPerM)) / 1000000
    return stdvals


def compare_ratios(ocorr):
    expected = Counter(import_table(ocorr))
    holder = {}
    for word, n_ocorr in ocorr.items():
        if expected[word]!=0:
            holder[word] = ((n_ocorr-expected[word])/expected[word])*100
        else:
            holder[word] = ((n_ocorr-0.0397)/0.0397)*100
    return holder


def main():
    cl = clfilter("adm:is:tr", doc=__doc__)

    for txt in cl.text():
        words = tokenizer(txt)
        ocorr = Counter(words)

        if "-i" in cl.opt:
            ocorr = ignore_case(ocorr)
        if "-s" in cl.opt:
            ocorr = check_substring(ocorr,cl.opt.get("-s"))
        if "-t" in cl.opt:
            ocorr = compare_ratios(ocorr)
        ocorr = sorted(ocorr.items(), key=lambda x: x[1], reverse=True)       # Sorted by Number of Ocorrences
        if "-m" in cl.opt:
            ocorr = ocorr[:(int(cl.opt.get("-m")))]
        if "-a" in cl.opt:
            ocorr = sorted(ocorr, key=lambda x: x[0])                         # Sorted by Ascending Alphabetical Order
        if "-d" in cl.opt:
            ocorr = sorted(ocorr, key=lambda x: x[0], reverse=True)           # Sorted by Descending Alphabetical Order
        printf(ocorr)