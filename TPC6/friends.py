#!/usr/bin/env python3
'''
NAME
    friends - Calculates the frequency of name combinations occurring within a sentence.

SYNOPSIS
    friends [FILE]...
    
DESCRIPTION
    Calculate the frequency of two names appearing together within a single sentence.

    With no FILE, read standard input.
'''
from jjcli import *
import spacy

cl = clfilter("", doc=__doc__)

nlp = spacy.load("pt_core_news_lg")
nlp.add_pipe("merge_entities")

for txt in cl.text():
    doc = nlp(txt)

    friends = {}

    for sentence in doc.sents:
        names = []

        for token in sentence:
            if not token.is_space and token.ent_type_ == 'PER' and token.pos_ == 'PROPN':
                current_name = str(token)
                names = list(filter(lambda x: x != current_name, names))

                if current_name not in friends:
                    friends[current_name] = {}
                    
                for name in names:
                    if name in friends[current_name]:
                        friends[current_name][name] += 1
                    elif current_name in friends[name]:
                        friends[name][current_name] += 1
                    else:
                        friends[current_name][name] = 1
                names.append(current_name)

    friends = {key: value for key, value in friends.items() if any(value.values())}

    for person in sorted(friends.keys()):
        print(f"{person}")
        connections = friends[person]
        for friend, occurrences in connections.items():
            print(f"    {friend}: {occurrences} ")
        print("-"*40)