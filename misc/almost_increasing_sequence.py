"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].
"""

def almostIncreasingSequence(sequence):
    sequence_disturbed_count = 0
    current_max = sequence[0]
    for idx in range(len(sequence)-1):   
        if sequence[current_max] <= sequence[idx+1]:
            sequence_disturbed_count+=1
        else:
            current_max = idx
        if sequence_disturbed_count > 1:
            return False
    return True

print(almostIncreasingSequence([1,3,2]))

print(almostIncreasingSequence([1,2,1,2]))

print(almostIncreasingSequence([3, 6, 5, 8, 10, 20, 15]))

print(almostIncreasingSequence([1, 1, 2, 3, 4, 4]))

