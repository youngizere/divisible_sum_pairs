def divisible_sum_pairs(input_int_array, k):
    count = 0
    # Each element in the array is paired with each other element in the array in order 
    # to computer the pair_sum as below implemented
    for i in input_int_array:
        for j in input_int_array:
            if input_int_array.index(i) < input_int_array.index(j):
                pair_sum = i+j
                # if the remainder of pair_sum/k is zero then pair_sum is divisible by k
                if pair_sum%k == 0:
                    count = count+1
    return count

if __name__=="__main__":
    input_int_array = [1, 2, 3, 4, 5, 6]
    k = 5
    print(divisible_sum_pairs(input_int_array, k))