#!/usr/bin/python

import sys

def rock_paper_scissors(n, cache=None):
    
    plays = [['rock'], ['paper'], ['scissors']]
    
    if n == 0:
        return []
    
    if n == 1:
        return [p for p in plays]
    
    if not cache:
        cache = {1: plays}
        
    # a NEW one!
    foo = []
    for play in plays:
        for i in rock_paper_scissors(n-1):
            foo.append(play + i)
    cache[n] = foo
    return foo

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')