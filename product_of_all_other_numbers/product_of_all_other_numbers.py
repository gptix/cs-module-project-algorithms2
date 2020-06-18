'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    from functools import reduce
    import operator

    input_length = len(arr)

    zero_count = 0 # we will find if one, or more than one, zeroes are present.
    zero_index = 0 # this will be used only if we find exactly one.
    idx = 0
    # once we find more than one zero, all values in the return list must be zero.
    while zero_count < 2 and idx < input_length:
        if arr[idx] == 0:
            zero_index = idx # we will only care if there is exactly one zero.
            zero_count += 1
        idx += 1

    # In this case, every product will have at least one zero as operand, so all are zero.
    if zero_count == 2:
        return [0]*input_length

    # If the array contains exactly one zero, only that index will have a value.
    if zero_count == 1:
        # get non-zero elements
        non_zeroes = [el for el in arr if el is not 0]
        product = reduce(operator.mul, non_zeroes)
        output = [0]*input_length # all but one will be zero.
        output[zero_index] = product # this is the one that is not zero.
        return output

    # else (no zeroes)
    total_product = reduce(operator.mul, arr)
    return [int(total_product / element) for element in arr]





        





if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
