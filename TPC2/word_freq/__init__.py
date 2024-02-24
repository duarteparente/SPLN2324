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
    print(len(tokens))
    return tokens

def add_relative_freq(ocorr):
    total_ocorr = sum(item[1] for item in ocorr)
    return {(word, n_ocorr, (n_ocorr/total_ocorr)*100) for word, n_ocorr in ocorr}


def sort(ocorr, option):
    ocorr = add_relative_freq(ocorr)
    if option == 1:
        ocorr = sorted(ocorr, key=lambda x: x[0])                     # Sorted by Ascending Alphabetical Order
    elif option == 2:
        ocorr = sorted(ocorr, key=lambda x: x[0], reverse=True)       # Sorted by Descending Alphabetical Order
    elif option == 3:  
        ocorr = sorted(ocorr, key=lambda x: x[1], reverse=True)       # Sorted by Number of Ocorrences
    return ocorr


def printf(ocorr, option):
    ocorr = sort(ocorr, option)
    for word, n_ocorr, relative_freq in ocorr:
        print(f'{word:<{23}}  {n_ocorr:<{7}}  {relative_freq:.3f} %')


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


def generate_table(ocorr):
    ocorr = sort(ocorr, 3)
    
    table = """
<html>
    <head>
        <style>
            table {
                width: 30%;
                margin: 20px auto;
                border: #cacaca solid;
            }
            th, td {
                padding: 6px;
                text-align: center;
                border-bottom: 1.5px solid #ddd;
            }
            th {
                background-color: #cacaca;
            }
        </style>
    </head>
    <body>
    <table>
        <tr>
            <th>Palavra</th><th>Número de Ocorrências</th><th>Frequência Relativa</th>
        </tr>
"""
    for word, n_ocorr, relative_freq in ocorr:
        table += f"     <tr><td>{word}</td><td>{n_ocorr}</td><td>{relative_freq:.3f} %</td></tr>"

    table += """
    </table>
    </body>
</html>"""
    
    #out_path = os.path.join(os.path.dirname(__file__), "output.html")
    #print(os.path.dirname(__file__))
    with open("output.html", 'w') as file:
        file.write(table)



def main():
    cl = clfilter("adm:is:t", doc=__doc__)

    for txt in cl.text():
        print(cl.args)
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
        elif "-t" in cl.opt:
            generate_table(ocorr.items())
        else:
            printf(ocorr.items(), 3)
            

## Arranjar uma tabela padrão de ocorrências do portugues - linguateca

## Limpeza da tabela - cortar as palavras que ocorrem poucas vezes, tirar numeros 
            
## Comparar racios de palavras entre dois textos (através da frequencia relativa)
            
## Localização do output da tabela (caminho relativo), usar __file__