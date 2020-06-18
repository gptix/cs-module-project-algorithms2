#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    plays = [['rock'], ['paper'], ['scissors']]
    
    if n == 0:
        return []
    
    if n == 1:
        return [p for p in plays]
    
    shorter = rock_paper_scissors(n-1)
    
    out = []
    for s in shorter:
        for p in plays:
            out.append(s + p)
            
    return out

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')