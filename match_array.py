class MatchArray:
    def __init__(self,array1,array2):
        self.array1=array1
        self.array2=array2
    
    def does_array_match(self):
        if len(self.array1) !=len(self.array2):
            return False
        array1_dict ={}
        array2_dict = {}
        for item in self.array1:
            squared_item = item**2
            if squared_item in array1_dict.keys():
                item_val = array1_dict.get(squared_item)
                array1_dict.update({squared_item:item_val+1})
            else:
                array1_dict.update({squared_item:1})

        for item in self.array2:
            if item in array2_dict.keys():
                item_val = array2_dict.get(item)
                array2_dict.update({item:item_val+1})
            else:
                array2_dict.update({item:1})
        
        for item in array1_dict.keys():
            if item not in array2_dict.keys():
                return False
            array_2_value = array2_dict.get(item)
            if array_2_value != array1_dict.get(item):
                return False
        return True

x = MatchArray([1,2,3,2,9], [1,4,9,4,25])
print(x.does_array_match())