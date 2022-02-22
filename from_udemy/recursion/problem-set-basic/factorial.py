class MyClass:
    def factorial(self,num):
        if num == 1:
            return 1
        return num * self.factorial(num-1)

print(MyClass().factorial(3))