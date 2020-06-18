'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache = None):
    
    if n < 0:
        return 0
    
    if not cache:
        cache = {0: 1, 1: 1, 2: 2}

    if n in cache:
        return cache[n]
    
    # a NEW one!
    foo = eating_cookies(n-3, cache) + eating_cookies(n-2, cache) + eating_cookies(n-1, cache)
    cache[n] = foo
    return foo

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    for i in range (7):
        print(f"There are {eating_cookies(i)} ways for Cookie Monster to each {i} cookies")