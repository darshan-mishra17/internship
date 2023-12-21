def unique_values_in_ascending_order(input_dict):
    unique_values = list(set(input_dict.values()))
    unique_values.sort()
    return unique_values


my_dict = {
    'a': [1,2,8,8],
    'b': [10,11,12,5],
    'c': [7,12,10,11],
    'd': 2,
    'e': 7,
    'f': 3
}

unique_values = unique_values_in_ascending_order(my_dict)
print("Unique values in ascending order:", unique_values)
