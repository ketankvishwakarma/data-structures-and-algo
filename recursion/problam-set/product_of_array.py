"""
Write a function called product_of_array which takes in an array of numbers and returns the 
product of them all.
"""

class MyClass:
    def procuct(self,items):
        if (len(items)==1):
            return items[0]
        return items[len(items)-1] * self.procuct(items[0:len(items)-1])

print(MyClass().procuct([1,2,3]))
print(MyClass().procuct([1,2,3,10]))
        