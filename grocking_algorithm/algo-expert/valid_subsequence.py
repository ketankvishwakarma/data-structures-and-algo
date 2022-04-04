def is_valid_subsequence(array, sequence):
    match_left = len(sequence)
    start = sequence[len(sequence)-match_left]
    #print("start with {} total match to be found {}".format(start,match_left))
    for val in array:
     #   print("matching {} with {} | match remaining {}".format(val,start,match_left))
        if val == start:
            match_left -=1
            if match_left==0:
                return True
            start = sequence[len(sequence)-match_left]
    return False



def is_valid_subsequence(array, sequence):
    match_left = len(sequence)
    start = sequence[len(sequence)-match_left]
    for val in array:
        if val == start:
            match_left -=1
            if match_left==0:
                return True
            start = sequence[len(sequence)-match_left]
    return False

def is_valid_subsequence_ax(array,seq):
    seq_idx = 0
    for value in array:
        if seq_idx == len(seq):
            break
        if seq[seq_idx] == value:
            seq_idx+=1
    return seq_idx == len(seq)

print(is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10],[1, 6, -1, 10]))
print(is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10],[5, 1, 22, 25, 6, -1, 8, 10]))

print(is_valid_subsequence_ax([5, 1, 22, 25, 6, -1, 8, 10],[1, 6, -1, 10]))
print(is_valid_subsequence_ax([5, 1, 22, 25, 6, -1, 8, 10],[5, 1, 22, 25, 6, -1, 8, 10]))