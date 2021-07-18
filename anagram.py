"""
Check if two string are valid anagrams.

NOTE: All inputs will be in lower cases

EXAMPLE: 
1. " " & " "             -> True
2. "aaz" & "zza"         -> False
3. "anagram" & "nagram"  -> True
4. "rat" & "car"         -> False
"""


def valid_anagram(str1, str2):

    if len(str1) != len(str2):
        return False

    return True




if __name__ == "__main__":
    str1 = "anagram"
    str2 = "nagaram "
    is_anagram = valid_anagram(str1,str2)
    print("{} and {} are anagrams : {}".format(str1,str2,is_anagram))
