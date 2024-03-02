#!/usr/bin/env python3
import re
import sys

def main():
    counter=0
    words={}
    
    db_file = open(sys.argv[1],"r", encoding="ISO-8859-1")
    pattern = re.compile('(\d+)\s+(\S+)')

    for line in db_file:
        match = pattern.match(line)
        if match:
            words[match.group(2)]=int(match.group(1))
            counter+=int(match.group(1))

    for w in words.keys():
        words[w] = (1000000 * words[w]) / counter
        print(f"{w}   {words[w]}")
            

if __name__ == "__main__":
    main()