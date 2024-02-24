# tasks 5         
# [1, 2, 3]
# [[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]]

def data_preparation(data):
    result = []
    
    for sublist in data:
        if len(sublist) > 2:
            
            sublist.remove(max(sublist))
            sublist.remove(min(sublist))
        
        
        result.extend(sublist)
    
    
    return sorted(result, reverse=True)


input_data = [[1, 2, 3], [3, 4], [5, 6]]
output_result = data_preparation(input_data)
print(output_result)
