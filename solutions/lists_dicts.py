# TODO: Implement a function that returns a list of numbers from 1 to n
def generate_numbers(n):
    list=[]
    for i in range(1,n+1):
        list.append(i)
    return list

# TODO: Implement a function that returns a dictionary where keys are numbers from 1 to n and values are their squares
def generate_squares(n):
    dict={}
    for i in range(1,n+1):
        dict[i]=i*i
    return dict

# TODO: Implement a function that merges two lists in an alternating fashion
def merge_lists(list1, list2):
    list = []
    max_len = max(len(list1), len(list2))

    for i in range(max_len):
        if i < len(list1):
            list.append(list1[i])
        if i < len(list2):
            list.append(list2[i])

    return list

# TODO: Implement a function that returns a list and replicates the dictionary keys based on their respective values
def multiply_keys(data):
    list=[]
    for key, value in data.items():
        list.extend([key] * value)
    return list

# TODO: Implement a function that converts a list of strings to a dictionary with the string as the key and its length as the value
def list_to_dict(items):
    dict={}
    for i in items:
        dict[i]=len(i)
    return dict
# TODO: Implement a function to find the majority element in a list
def majority_element(nums):
    majority=""
    a=0
    for i in nums:
        if a == 0:
            majority=i
        if i == majority:
            a+=1
        else:
            a-=1
    return majority

# TODO: Implement a function that filters a dictionary based on a threshold value. If the value of any key in the dictionary is greater than the threshold, that key-value pair should be retained in the output dictionary. Otherwise, it should be excluded.
def filter_dictionary(data, threshold):
    dict = {}
    for key, value in data.items():
        if value > threshold:
            dict[key] = value
    return dict
