def combine_dicts_remove_duplicates(*dicts):
    combined_dict = {}
    
    for d in dicts:
        for key, value_list in d.items():
            if key not in combined_dict:
                combined_dict[key] = []
                
            for value in value_list:
                if value not in combined_dict[key]:
                    combined_dict[key].append(value)
    
    return combined_dict

# Define your dictionaries here
dict1 = {
    "key1": [1, 2, 3],
    "key2": [4, 5, 6]
}

dict2 = {
    "key1": [2, 3, 4],
    "key3": [7, 8, 9]
}

# Add more dictionaries if needed
# dict3 = {...}
# dict4 = {...}

# Call the function with your dictionaries as arguments
result = combine_dicts_remove_duplicates(dict1, dict2)  # Add more dictionaries as needed

# Print the combined dictionary with duplicates removed
print(result)