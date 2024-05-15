def is_subset_sum(set, n, sum):
    
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False

   
    if set[n-1] > sum:
        return is_subset_sum(set, n-1, sum)

  
    return is_subset_sum(set, n-1, sum) or is_subset_sum(set, n-1, sum-set[n-1])


set = [3, 34, 4, 12, 5, 2]
sum = 9
n = len(set)

if is_subset_sum(set, n, sum):
    print("Found a subset with given sum")
else:
    print("No subset with given sum")