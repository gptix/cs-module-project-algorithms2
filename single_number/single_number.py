'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Have to iterate to check each element.
    
    dictionaree = {}
    
    for item in arr:
        # if it is occurring for a second time, trash it.
        if item in dictionaree:
            del dictionaree[item]
        # If this is the first time we've seen it, record it.
        else:
            dictionaree[item] = True
            
    # Per the spec, exactly one element occurs once.  
    # A list will have only one element.
    return list(dictionaree)[0]
       

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 9, 1300, 0, 0]
    

    print(f"The odd-number-out is {single_number(arr)}")