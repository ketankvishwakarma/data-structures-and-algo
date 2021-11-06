"""
Wirte a function called is_subsequence which takes two string and check whether the 
characters in the first string form a subsequence of the character in the second string.
in other words the function should check whether the charecters in the first string
appers somewere in the second string without changing there order.

is_subsecuence('hello','hello world') --> true
is_subsecuence('sing','string') --> true
is_subsecuence('abc','abracadabra') --> true
is_subsecuence('abc','acb') --> false //(order matters)
"""

def is_subsecuence(sub_string,main_string):
    sub_string_index = 0
    for index, value in enumerate(main_string):
        if sub_string[sub_string_index] == main_string[index]:
            sub_string_index = sub_string_index + 1
        if sub_string_index == len(sub_string):
            return True
    return False
    


if __name__ =="__main__":
    print("'abc','acb' --> {}".format(is_subsecuence('sing','string')))
    print("'abc','abracadabra' --> {}".format(is_subsecuence('abc','abracadabra')))
    print("'abc','acb' --> {}".format(is_subsecuence('abc','acb')))


