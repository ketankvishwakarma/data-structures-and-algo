"""
Given two integers, find out if the two numbers have same frequency of digits

182,281          -> True
34,14            -> False
22,222           -> False
3589578,5879385  -> True
"""

def same_frequency(first,second):

    first_str = str(first)
    second_str = str(second)
    if len(first_str)!=len(second_str):
        return False
    
    first_str_dict = {}
    for index, value in enumerate(first_str):
        if value in first_str_dict.keys():
            first_str_dict.update({value:(first_str_dict.get(value)+1)})
        else:
            first_str_dict.update({value:1})

    second_str_dict = {}
    for index, value in enumerate(second_str):
        if value in second_str_dict.keys():
            second_str_dict.update({value:(second_str_dict.get(value)+1)})
        else:
            second_str_dict.update({value:1})

    for key in first_str_dict.keys():
        if key not in second_str_dict.keys():
            return False
        if first_str_dict.get(key)!= second_str_dict.get(key):
            return False

    return True


if __name__ =="__main__":
    print("182,281 ({})".format(same_frequency(182,281)))
    print("34,14 -> ({})".format(same_frequency(34,14)))
    print("22,222 -> ({})".format(same_frequency(22,222)))
    print("3589578,5879385 -> ({})".format(same_frequency(3589578,5879385)))