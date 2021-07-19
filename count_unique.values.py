"""
Question: Write a function which takes in a sorted array, and returns the count of unique elements in it. 

"""

class CountUnique:
    pass
    
    def count(self,input_array):
        if len(input_array) ==0:
            return 0
        unique_count = 1
        for index,value in enumerate(input_array):
            if index == (len(input_array)-1):
                break
            if value == input_array[index+1]:
                continue
            if value !=input_array[index+1]:
                unique_count=unique_count+1
        return unique_count

unique_counter = CountUnique()
print(unique_counter.count([1,1,1]))
print(unique_counter.count([1,1,1,2,2,3,4,5,5]))
print(unique_counter.count([1,1,1,2,3,3,4,4,4,4,5,9,11,12]))





