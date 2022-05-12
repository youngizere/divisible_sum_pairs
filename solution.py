def divisible_sum_pairs(input_int_array, k):
    count = 0
    for i in input_int_array:
        for j in input_int_array:
            if i < j:
                pair_sum = i+j
                if pair_sum%k == 0:
                    count = count+1
    return count

if __name__=="__main__":
    input_int_array = [1, 2, 3, 4, 5, 6]
    k = 5
    print(divisible_sum_pairs(input_int_array, k))