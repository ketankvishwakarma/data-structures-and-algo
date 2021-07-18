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

    str1_char_count_dict = {}
    for char in str1:
        if char in str1_char_count_dict.keys():
            str1_char_count_dict.update({char:str1_char_count_dict.get(char)+1})
        else:
            str1_char_count_dict.update({char:1})

    str2_char_count_dict = {}
    for char in str2:
        if char in str2_char_count_dict.keys():
            str2_char_count_dict.update({char:str2_char_count_dict.get(char)+1})
        else:
            str2_char_count_dict.update({char:1})
    
    for char in str1_char_count_dict.keys():
        if char not in str2_char_count_dict.keys():
            return False
        if str1_char_count_dict.get(char) != str2_char_count_dict.get(char):
            return False
    return True

if __name__ == "__main__":
    str1 = "anagram"
    str2 = "nagaram"
    is_anagram = valid_anagram(str1,str2)
    print("{} and {} are anagrams : {}".format(str1,str2,is_anagram))
