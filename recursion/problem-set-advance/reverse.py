"""
Write a recursive function called reverse that accepts a string and return a new string that is reversed.
"""
def reverse(str):
    if len(str)==1:
        return str[0]
    return str[len(str)-1] + reverse(str[0:len(str)-1])

if __name__ == "__main__":
    print(reverse("abc"))
    print(reverse("awesome"))
    print(reverse("rithmschool"))