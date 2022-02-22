"""
Write a function called power which accepts base and an exponent. The function should return the
power of  the base to the exponent. This function should mimic the functionality of `Math.pow()`
do not worry about negative abse and exponents.
"""

class Custom:
    def power(self,base,expoenet):
        if expoenet < 0 or base < 0:
            return "negative values not supported"
        if expoenet == 0:
            return 1
        return base * self.power(base,expoenet-1)

print(Custom().power(10,-2))
print(Custom().power(2,0))
print(Custom().power(2,2))
print(Custom().power(2,4))
