import math
def most_digit(arr):
    max_len = 0
    for digit in arr:
        if digit==0:
            digit_len =1
        else:
            digit_len = int(math.log10(abs(digit)))+1
        if digit_len > max_len:
            max_len = digit_len
    return max_len


def get_digit(num,position):
    return int((abs(num) / math.pow(10,position))%10)


def radix_sort(arr):
    max_len = most_digit(arr)
    results = []
    for i in range(max_len):
        
        digit_bucket = [[] for j in range(10)]
        for k in arr:
           digit_bucket[get_digit(k,i)].append(k) 
        for buckets in digit_bucket:
            for items in buckets:
                results.append(items)
        arr = results
        results = [] 
    return arr



#print(get_digit(7,3))
print(radix_sort([23,567,89,12231,90]))
print(radix_sort([23,23,23,23,23]))
print(radix_sort([]))