# find summation of n integers, memoization technique
def n_sum(n):
    # memoized/cached results
    summation = [0]
    for i in range(1, n + 1):
        summation.append(summation[i - 1] + i)
    return summation[-1]


print(n_sum(0))
