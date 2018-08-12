'''
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8

'''


def row_sum_odd_numbers(n):
    return reduce(lambda x, y: x+y, range((n**2-n)+1, (n**2+n)+1, 2))
