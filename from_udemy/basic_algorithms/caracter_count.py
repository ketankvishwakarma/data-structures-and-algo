"""
Write a program to count the number of occurrences of each character in the given text.
You can skip special characters like space, !, ? etc
"""

class CharCount:
    skip_list = ['!',' ','?','.','1','2','3','4','5','6','7','8','9','0']
    def __init__(self,char_string):
        self.char_string = char_string

    def compute_char_count(self):
        lower_case = self.char_string.lower()
        char_count_map ={}
        for char in lower_case:
            if char in self.skip_list:
                continue
            if char in char_count_map.keys():
                current_count = char_count_map.get(char)
                char_count_map.update({char:current_count+1})
            else:
                char_count_map.update({char:1})    
        return char_count_map


x = CharCount("Hello Sweety! This is test string")
print(x.compute_char_count())






