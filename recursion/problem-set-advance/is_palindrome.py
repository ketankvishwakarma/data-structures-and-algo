"""
Write a function called is_palindrome which returns true if the string passed to it is a
palindrome. Otherwise it returns false
"""

def is_palindrome(word):
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    print(word[1:-1])
    return is_palindrome(word[1:-1])


if __name__ == "__main__":
    print(is_palindrome("awesomea"))
